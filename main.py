from jlcipher.views import main_view
from jlcipher import configs


if __name__ == '__main__':
    main_view = main_view.MainApp(configs.MODE["COMPACT"])
    main_view.MainLoop()  # WXPython built-in function
