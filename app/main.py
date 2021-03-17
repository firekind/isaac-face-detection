from isaac import Application

from codelets import HelloWorld
from utils import configure_websight_root, patch_capnp_paths


def main():
    # patching capnp paths. Needed if using isaac python API.
    patch_capnp_paths()

    # creating app
    app = Application(app_filename="app/graphs/graph.app.json")

    # adding python codelet to the hello_node in graph
    app.nodes["hello_node"].add(HelloWorld, "print")

    # configuring Websight webroot and assetroot. Needed if using isaac python API.
    configure_websight_root(app)

    # running the application
    app.run()


if __name__ == "__main__":
    main()
