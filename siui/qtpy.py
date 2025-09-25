import Qt
import importlib

QGuiApplication = importlib.import_module("%s.QtGui" % Qt.__binding__).QGuiApplication
