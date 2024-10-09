import os
import threading
from time import time

import webview
import sys


class Api:
    def fullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def save_content(self, content):
        filename = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        if not filename:
            return

        with open(filename, "w") as f:
            f.write(content)

    def ls(self):
        return os.listdir(".")


def get_entrypoint(debug_mode):
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if debug_mode:
        return "http://localhost:5173"

    if exists("../dist/index.html"):  # unfrozen development
        return "../dist/index.html"

    # if exists("../Resources/gui/index.html"):  # frozen py2app
    #     return "../Resources/gui/index.html"

    if exists("./dist/index.html"):
        return "./dist/index.html"

    raise Exception("No index.html found")


def set_interval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop():  # executed in another thread
                while not stopped.wait(interval):  # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True  # stop if the program exits
            t.start()
            return stopped

        return wrapper

    return decorator


@set_interval(1)
def update_ticker():
    if len(webview.windows) > 0:
        webview.windows[0].evaluate_js(
            'window.pywebview.state.setTicker("%d")' % time()
        )


if __name__ == "__main__":
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # running in a PyInstaller bundle
        debug_mode = False
    else:
        if len(sys.argv) > 1 and sys.argv[1] == 'DEBUG':
            debug_mode = True
        else:
            debug_mode = False

    entry = get_entrypoint(debug_mode)

    window = webview.create_window("pywebview-react boilerplate", entry, js_api=Api())

    webview.start(update_ticker, debug=debug_mode)
