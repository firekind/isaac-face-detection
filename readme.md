
# Isaac Application Template

This is a template for developing isaac applications.

## Run
## Run without docker
Download Nvidia Isaac 2020.2, and extract it in a local folder. Update the [`WORKSPACE`](https://github.com/firekind/isaac-template/blob/master/WORKSPACE#L4) by specifying the Isaac SDK folder for `ISAAC_SDK_RELEASE`

You may need to build the Isaac SDK using

```
$ bazel build ...
```

Although I have no idea when this should be done. Sometimes things work without doing it.

To run the hello world application in this template, execute the command:

```
$ bazel run //app:hello_world
```

## Run with docker

Make sure docker and nvidia-docker is installed. The docker image `firekind/isaac:2020.2` can be used to run the application. Pull the image using:

```
$ docker pull firekind/isaac:2020.2
```

and create a container using

```
$ docker run --mount source=isaac-sdk-build-cache,target=/root -v <path to workspace directory>:/workspace -w /workspace --runtime=nvidia -it isaacbuild:latest /bin/bash
```

And then run the application using

```
$ bazel run //app:hello_world
```

VSCode users can use the [remote containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) along with the `.devcontainer/devcontainer.json` to develop inside a container.

> **Note:** If you are using the Python API, take a look at [`main.py`](https://github.com/firekind/isaac-template/blob/master/app/main.py). There are a few lines of code that needs to be executed for everything to work.

> **Also another Note:** The workspace doesn't include ros, zed, sensor certification, cartographer or prometheus. If they are needed, uncomment the corresponding lines in [`WORKSPACE`](https://github.com/firekind/isaac-template/blob/master/WORKSPACE)
