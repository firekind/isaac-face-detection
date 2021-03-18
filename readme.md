# Face detection using Isaac and Deepstream

Face detection using Centerface, built using Isaac 2020.2 and Deepstream 5.0

## Setup

Start a container using the `firekind/isaac:2020.2-deepstream-5.0.1-triton` image:

```
$ docker run \
    --gpus=all \
    --net=host \
    --mount source=isaac-sdk-build-cache,target=/root \
    -v `pwd`:/workspaces \
    -w /workspaces \
    -it \
    firekind/isaac:2020.2-deepstream-5.0.1-triton
```

Then, download the centerface model using

```
$ cd helpers && ./run.sh
```

This will download the centerface model, and updates the dimension of the input and output nodes. (In Triton Inference Server, if you want the input and output nodes to have variable size then relevant dimensions should be specified as -1. `helpers/change_dim.py` reads the input ONNX model, updates the height and width dimensions to -1, and saves the resulting model.)

If needed, edit the `device_id` under the `config` section of [`app/graphs/graph.app.json`](https://github.com/firekind/isaac_deepstream_yolo/blob/master/app/graphs/graph.app.json#L74)

Then, run the application using

```
$ bazel run //app:face_detection
```

## Credits

Most of the deepstream related code taken from [NVIDIA-AI-IOT](https://github.com/NVIDIA-AI-IOT/deepstream_triton_model_deploy).
