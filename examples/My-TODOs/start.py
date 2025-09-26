import sys
from ui import MySiliconApp


if __name__ == "__main__":
    from siui.qt_utils import render_ui
    with render_ui():
        window = MySiliconApp()
        window.show()

