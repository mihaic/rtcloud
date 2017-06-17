# RtFCMA classifier
Watch a directory for newly coming NIfTI files, and accumulate them to compute correlation and run classification
on top of it. The correlation computation and classification is done 
by calling FCMA in [BrainIAK](https://github.com/IntelPNI/brainiak).

```
usage: nifti_file_watcher.py [-h] [-w WINDOW] [-t TOTAL]
                             directory epoch mask model

positional arguments:
  directory             path to the monitored directory
  epoch                 path to the numpy file of epoch info in 1D array
  mask                  path to the mask file which specifies the top voxels
  model                 path to the model's pickle file, usually *.pkl

optional arguments:
  -h, --help            show this help message and exit
  -w WINDOW, --window WINDOW
                        correlation window size [8]
  -t TOTAL, --total TOTAL
                        total number of TRs generated in real-time [1500]
```
