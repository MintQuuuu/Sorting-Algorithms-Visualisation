import algorithms
from threading import Thread
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot



class VisualisationLayout(BoxLayout):
    def __init__(self):
        super(VisualisationLayout, self).__init__()
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.data = []
        self.step_time = 0.4

    def start_bubble(self, how_much, step_time):
        self.ids.graph.xmax = int(how_much)
        self.ids.graph.add_plot(self.plot)
        self.data = algorithms.generate_random_list(int(how_much))
        self.step_time = float(step_time)
        bubble_thread = Thread(target=algorithms.bubble, args=(self.data, self.plot, self.step_time))
        bubble_thread.daemon = True
        bubble_thread.start()

    def start_selection(self, how_much, step_time):
        self.ids.graph.xmax = int(how_much)
        self.ids.graph.add_plot(self.plot)
        self.data = algorithms.generate_random_list(int(how_much))
        self.step_time = float(step_time)
        selection_thread = Thread(target=algorithms.selection, args=(self.data, self.plot, self.step_time))
        selection_thread.daemon = True
        selection_thread.start()

    def start_quick(self, how_much, step_time):
        self.ids.graph.xmax = int(how_much)
        self.ids.graph.add_plot(self.plot)
        self.data = algorithms.generate_random_list(int(how_much))
        self.step_time = float(step_time)
        quick_thread = Thread(target=algorithms.quick, args=(self.data, 0, len(self.data)-1, self.plot, self.step_time))
        quick_thread.daemon = True
        quick_thread.start()


class VisualisationApp(App):
    def build(self):
        return VisualisationLayout()


VisualisationApp().run()


