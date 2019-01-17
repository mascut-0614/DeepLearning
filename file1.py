import numpy as np
import matplotlib.pyplot as plt
class Graph:
    def __init__(self,title):
        self.title=title
        print("Initialized!")
    def show_graph(self):
        x=np.arange(0,5,0.1)
        y_sin=np.sin(x)
        y_cos=np.cos(x)
        plt.plot(x,y_sin,label="sin")
        plt.plot(x,y_cos,linestyle="--",label="cos")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(self.title)
        plt.legend()
        plt.show()
    def hello(self):
        print("Hello!\nThis is "+self.title+" graph!")
g=Graph("sin & cos")
g.hello()
g.show_graph()
