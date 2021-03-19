load("@com_nvidia_isaac_sdk//bzl:module.bzl", "isaac_app", "isaac_pkg")

filegroup(
    name = "configs",
    srcs = glob(["configs/*"]),
)

filegroup(
    name = "libs",
    srcs = glob(["lib/*"])
)

isaac_app(
    name = "centerface",
    app_json_file = "graphs/graph-centerface.app.json",
    data = [
        ":configs",
        ":libs",
        "//:centerface"
    ],
    modules = [
        "@com_nvidia_isaac_sdk//packages/sight",
        "@com_nvidia_isaac_sdk//packages/viewers",
        "@com_nvidia_isaac_sdk//packages/sensors:v4l2_camera",
        "@com_nvidia_isaac_sdk//packages/deepstream"
    ],
)

isaac_app(
    name = "facedetectir",
    app_json_file = "graphs/graph-facedetectir.app.json",
    data = [
        ":configs",
        ":libs",
        "//:facedetectir"
    ],
    modules = [
        "@com_nvidia_isaac_sdk//packages/sight",
        "@com_nvidia_isaac_sdk//packages/viewers",
        "@com_nvidia_isaac_sdk//packages/sensors:v4l2_camera",
        "@com_nvidia_isaac_sdk//packages/deepstream"
    ],
)

isaac_pkg(
    name = "face_detection_facedetectir_pkg",
    srcs = [ ":facedetectir" ]
)
