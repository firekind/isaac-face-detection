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
    name = "face_detection",
    app_json_file = "graphs/graph.app.json",
    data = [
        ":configs",
        ":libs",
        "//:model"
    ],
    modules = [
        "@com_nvidia_isaac_sdk//packages/sight",
        "@com_nvidia_isaac_sdk//packages/viewers",
        "@com_nvidia_isaac_sdk//packages/sensors:v4l2_camera",
        "@com_nvidia_isaac_sdk//packages/deepstream"
    ],
)

isaac_app(
    name = "face_detection_jetson",
    app_json_file = "graphs/graph-jetson.app.json",
    data = [
        ":configs",
        ":libs",
        "//:model"
    ],
    modules = [
        "@com_nvidia_isaac_sdk//packages/sight",
        "@com_nvidia_isaac_sdk//packages/viewers",
        "@com_nvidia_isaac_sdk//packages/sensors:v4l2_camera",
        "@com_nvidia_isaac_sdk//packages/deepstream"
    ],
)

isaac_pkg(
    name = "face_detection_pkg",
    srcs = [ ":face_detection_jetson" ]
)
