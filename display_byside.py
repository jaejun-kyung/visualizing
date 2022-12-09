import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from ipywidgets import widgets, Layout
from IPython import display

#Displaying 함수

def display_byside(*args,display_type = 1):
    widget_list = list()
    for obj in args:
        widget_temp = widgets.Output()
        with widget_temp:
            display.display(obj)
            widget_list.append(widget_temp)
    if display_type == 1:
        return widgets.HBox(widget_list)
    else:
        box_layout = Layout(display='flex',
                    flex_flow='column',
                    align_items='stretch',
                    width='100%')
        return widgets.VBox(widget_list, layout=box_layout)
