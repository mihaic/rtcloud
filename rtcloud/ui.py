from nilearn import plotting
import numpy as np
import pandas as pd
import time
from IPython import display


def display_input(nifti, i, fig, ax):
    plotting.plot_img(nifti, title=i, axes=ax)
    display.clear_output(wait=True)
    display.display(fig)

def display_output(ndarray, i, fig, ax):
    i = pd.date_range('2013-1-1',periods=100,freq='s')
    ax.clear()
    ax.plot(pd.Series(data=np.random.randn(100), index=i))
