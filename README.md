# ODModel
The object detection model for ARMAPS. This model is used to create a model for the objects in the sorounding that will be used to validate the AR output. 


## Getting Started in 5 steps

**Tutorial** -  https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85

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
