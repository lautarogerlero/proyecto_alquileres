import io
import base64

import matplotlib
matplotlib.use('Agg')   
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg


def graficar(x):
    fig = plt.figure()
    fig.suptitle("Comparacion de las propiedades", fontsize=16)
    ax = fig.add_subplot()
    
    ax.pie(x.values(), labels=x.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    
    image_html = io.BytesIO()
    FigureCanvas(fig).print_png(image_html)
    plt.close(fig)  
    return image_html