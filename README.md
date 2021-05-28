# ODModel
The object detection model for ARMAPS. This model is used to create a model for the objects in the sorounding that will be used to validate the AR output. 


## Getting Started

**Tutorial** -  https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85

**TensorFlow**
1. Download tensorflow 
```
git clone https://github.com/tensorflow/models.git
```

2. Install tensorflow
First modify the dockerfile at research/object_detection/dockerfiles/tf1/, by adding  below at line 15 
```
libgl1-mesa-dev
```
and add below at line 41
```
RUN pip install jupyterlab
RUN pip install opencv-python
```

```
cd models
docker build -f research/object_detection/dockerfiles/tf1/Dockerfile -t od .
```
3. Run tensorflow
```
cd armaps-od
docker-compose up -d
```
4. Enter into the tensorflow environment
```
docker exec -it armaps-od_tensorflow_1 /bin/bash
```
5. Test tensorflow to ensure its working correctly
```
python object_detection/builders/model_builder_tf1_test.py
```

**Label Img**

1. Download labelImg
```
git clone https://github.com/tzutalin/labelImg.git
```
2. Install on linux. To install on another os follow the instructions https://github.com/tzutalin/labelImg#installation
```
cd labelImg
sudo apt-get install pyqt5-dev-tools
sudo pip3 install -r requirements/requirements-linux-python3.txt
make qt5py3
```
3. Run label img
```
python3 labelImg.py
```

**Python environemnt locally**
1. Setup virtual environment
```
cd armaps-od
python -m venv venv
```
2. Activate virtual environment
```
source venv/bin/activate (linux)

venv\Scripts\activate (Windows)
```
3. Intsall Requirments
```
pip install -r requirements.txt 
```

If a new python package is added refresh the requirments filr with
```
pip freeze > requirements.txt
```
**Run Jupyter**
```
jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root
```

## Steps to train and test model (Perform all these comands in the tensorflow docker container)

1. Transforming image sizes**
```
python transform_image_resolution.py -d images/ -s 800 600
```
2. Label the images using  labelImg 
   
3. Transform xml to csv 
```
python xml_to_csv.py
```

4. Generate Tensor flow record**
```
python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=records/train.record
python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=records/test.record
```
5. Train the model
```
python model_main.py --logtostderr --model_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
```
6. In another terminal start enter the comands to view the tensorflow logs
```
docker exec -it armaps-od_tensorflow_1 /bin/bash
cd object_detection
tensorboard --logdir=training
```

7. Export the inference graph for the results (change XXX to the highest number in the training fodler)
```
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```
8. Test the model
9. Convert to Js compatible format 
Run below inside of the container
```
pip install tensorflowjs[wizard]
cd object_detection/inference_graph
tensorflowjs_wizard

```

tensorflowjs_converter \
    --input_format=tf_saved_model \
    --output_node_names='MobilenetV1/Predictions/Reshape_1' \
    --saved_model_tags=serve \
    saved_model \
    web_model2