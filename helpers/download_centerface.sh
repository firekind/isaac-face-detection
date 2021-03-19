#!/bin/bash

# taken from https://github.com/NVIDIA-AI-IOT/deepstream_triton_model_deploy
# full credits goes to original authors

echo "Downloading centernet.onnx model"
wget https://github.com/Star-Clouds/CenterFace/raw/master/models/onnx/centerface.onnx

echo "Changing input and output node dimensions"
python3 change_dim.py

# Remove the original onnx model *
rm -r centerface.onnx

# moving the updated model to ../model/centerface/1
mkdir -p ../model/centerface/1
mv model.onnx ../model/centerface/1/
