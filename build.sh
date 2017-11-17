#!/usr/bin/env bash

CIBW_SKIP="cp27-* cp33-*"
CIBW_BEFORE_BUILD_MACOS="brew install llvm cmake mpich python3 cmake pkg-config automake autoconf libtool boost wget && {pip} install jupyter cython numpy pybind11"
CIBW_BEFORE_BUILD_LINUX="sudo yum update && sudo apt yum install -y libgomp1 gcc-gfortran mpich mpich-devel"
