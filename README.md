# BrainIAK Real-time cloud

[![Travis](https://travis-ci.org/brainiak/rtcloud.svg?branch=master)](https://travis-ci.org/brainiak/rtcloud)
[![Appveyor](https://ci.appveyor.com/api/projects/status/dldyb9jmwla03y0e/branch/master?svg=true)](https://ci.appveyor.com/project/danielsuo/rtcloud/branch/master)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## Getting started on client machine (MacOS only)
```bash
git clone --recursive git@github.com:brainiak/rtcloud.git
./bin/client/install
```

## Getting started on server machine (Ubuntu 16.04)
```bash
git clone --recursive git@github.com:brainiak/rtcloud.git
./bin/server/install
```

## TODO
```
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```
