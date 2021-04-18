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
```
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


## Steps to train model (Perform all these comands in the tensorflow docker container)

1. Transforming image sizes**
```
python transform_image_resolution.py -d process-images/ -s 800 600
```
1. Label the images using  labelImg 
   
2. Transform xml to csv 
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


python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record