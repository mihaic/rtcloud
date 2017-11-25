import matplotlib.pylab as plt
from nilearn import plotting
import numpy as np
import pandas as pd
import time
from IPython import display


def display_input(nifti, i):
    plotting.plot_img(nifti, title=i, figure=plt.gcf())
    display.clear_output(wait=True)
    display.display(plt.gcf())

def display_output(ndarray, i):
    pass
