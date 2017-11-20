# BrainIAK Real-time cloud

[![Travis](https://travis-ci.org/brainiak/rtcloud.svg?branch=master)](https://travis-ci.org/brainiak/rtcloud)
[![Appveyor](https://ci.appveyor.com/api/projects/status/dldyb9jmwla03y0e/branch/master?svg=true)](https://ci.appveyor.com/project/danielsuo/rtcloud/branch/master)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## Getting started on client machine
First, install Docker ([Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac), [Linux](https://store.docker.com/editions/community/docker-ce-server-ubuntu), [Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)). Then, run
```bash
# Sudo may be necessary
docker pull brainiak/rtcloud
docker run -it -p 8888:8888 brainiak/rtcloud
```


## Getting started on server machine (Ubuntu 16.04)
```bash
git clone git@github.com:brainiak/rtcloud.git
./bin/server/install
```

## TODO
```
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```
- [HPC on EC2](https://d0.awsstatic.com/Projects/P4114756/deploy-elastic-hpc-cluster_project.pdf)
