from itertools import cycle
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout


class Cycle:
    def __init__(self):
        self.cycle = cycle([
            Timer(25), Timer(5),
            Timer(25), Timer(5),
            Timer(25), Timer(15),
        ])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cycle)


class Timer:
    def __init__(self, time):
        self.time = time * 60

    def decrementar(self):
        self.time -= 1
        return self.time

    def __str__(self):
        return '{:02d}:{:02d}'.format(*divmod(self.time, 60))


class PID_Controller(MDFloatLayout):  # Alterar para nome do componente.
    pid_controller = StringProperty('xpto')
    button_string = StringProperty('SIMULAR')
    running = BooleanProperty(False)
    cycle = Cycle()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._time = next(self.cycle)
        self.pid_controller = str(self._time)

    def start(self):
        self.button_string = 'Simulando...'
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        time = self._time.decrementar()
        if time == 0:
            self.stop()
            self._time = next(self.cycle)
        self.pid_controller = str(self._time)

    def stop(self):
        self.button_string = 'SIMULAR'
        if self.running:
            self.running = False

    def click(self):
        if self.running:
            self.stop()
        else:
            self.start()


class PIDController(MDApp):
    def build(self):
        return Builder.load_file('app_interface/pid_controller.kv')
