#! /bin/bash

# Downloading the pruned model from ngc
wget --content-disposition https://api.ngc.nvidia.com/v2/models/nvidia/tlt_facedetectir/versions/pruned_v1.0/zip -O tlt_facedetectir_pruned_v1.0.zip

# extracting the model
unzip tlt_facedetectir_pruned_v1.0.zip -d model/facedetectir

# deleting the zip file
rm tlt_facedetectir_pruned_v1.0.zip
