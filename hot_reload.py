from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp


class HotReload(MDApp):
    KV_FILES = ['app_interface/pid_controller.kv']
    DEBUG = True

    def build_app(self, first=False):
        return Builder.load_file('app_interface/pid_controller.kv')


HotReload().run()
