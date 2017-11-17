# BrainIAK Real-time cloud

[![Build Status](https://travis-ci.org/brainiak/rtcloud.svg?branch=master)](https://travis-ci.org/brainiak/rtcloud)
[![Build status](https://ci.appveyor.com/api/projects/status/dldyb9jmwla03y0e/branch/master?svg=true)](https://ci.appveyor.com/project/danielsuo/rtcloud/branch/master)

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
