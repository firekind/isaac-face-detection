# Face detection using Isaac and Deepstream

Face detection using Centerface and FaceDetectIR, built using Isaac 2020.2 and Deepstream 5.0

## Setup

Start a container using the `firekind/isaac:2020.2-deepstream-5.0.1-triton` image (for centerface) or `firekind/isaac:2020.2-deepstream-5.0.1-base` (for facedetectir):

```
$ docker run \
    --gpus=all \
    --net=host \
    --mount source=isaac-sdk-build-cache,target=/root \
    -v `pwd`:/workspaces \
    -w /workspaces \
    -it \
    <image tag>
```

Take a note of the device id of the v4l2 camera. Update the `device_id` in the `config` section of the graph (in `app/graphs`) which you will use.

### Centerface

Download the centerface model using

```
$ cd helpers && ./download_centerface.sh
```

This will download the centerface model, and updates the dimension of the input and output nodes. (In Triton Inference Server, if you want the input and output nodes to have variable size then relevant dimensions should be specified as -1. `helpers/change_dim.py` reads the input ONNX model, updates the height and width dimensions to -1, and saves the resulting model.)

Then, run the application using

```
$ bazel run //app:centerface
```

### FaceDetectIR

Download the model using

```
$ cd helpers && ./download_facedetectir.sh
```

This will download the facedetectir model from NGC, and extract the contents to `model/facedetectir`. Run the application using

```
$ bazel run //app:facedetectir
```

This model can be deployed on jetson as well, using the `deploy.sh` script.

```
$ ./deploy.sh --remote_user <username_on_jetson> -p //app:face_detection_facedetectir_pkg -d jetpack44 -h <jetson_ip>
```

And on jetson, execute:

```
$ cd ~/deploy/face_detection_facedetectir_pkg 
$ ./app/run_facedetectir
```

## Credits

Most of the deepstream related code taken from [NVIDIA-AI-IOT](https://github.com/NVIDIA-AI-IOT/deepstream_triton_model_deploy).
