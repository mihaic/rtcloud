import matplotlib.pyplot as plt
from nilearn import plotting

def display_input(nifti, i):
    plotting.plot_img(nifti, title=i)

def display_output(ndarray, i):
    pass
