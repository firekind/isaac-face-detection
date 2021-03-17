load("@com_nvidia_isaac_sdk//bzl:module.bzl", "isaac_app")

filegroup(
    name = "configs",
    srcs = glob(["configs/*"]),
)

filegroup(
    name = "graphs",
    srcs = glob(["graphs/*"]),
)

isaac_app(
    name = "face_detection",
    app_json_file = "graphs/graph.app.json",
    data = [
        ":configs",
    ],
    modules = [
        "@com_nvidia_isaac_sdk//packages/sight",
        "@com_nvidia_isaac_sdk//packages/viewers",
        "@com_nvidia_isaac_sdk//packages/sensors:v4l2_camera",
        "@com_nvidia_isaac_sdk//packages/deepstream"
    ],
)
