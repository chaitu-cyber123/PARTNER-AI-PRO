import importlib
import os

PLUGIN_FOLDER = "plugins"


def load_plugins():

    plugins = {}

    for name in os.listdir(PLUGIN_FOLDER):

        path = os.path.join(PLUGIN_FOLDER, name)

        if os.path.isdir(path):

            try:

                module = importlib.import_module(
                    f"plugins.{name}"
                )

                plugins[name] = module

            except Exception:
                pass

    return plugins
