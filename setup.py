from setuptools import setup

setup(
    name='brainiak-rtcloud',
    version='0.0.1',
    install_requires=[
            'brainiak',
            'flask',
            'flask-session',
            'watchdog',
            'requests',
            'cython',
            'mpi4py',
            'nitime',
            'numpy',
            'scikit-learn',
            'scipy',
            'pymanopt',
            'theano',
            'pybind11',
            'nibabel',
            'typing'
    ],
    author='Princeton Neuroscience Institute and Intel Corporation',
    author_email='dsuo@princeton.edu',
    url='https://github.com/IntelPNI/rtfcma-prisma',
    description='Brain Imaging Analysis Kit Cloud',
    license='Apache 2',
    keywords='neuroscience, algorithm, fMRI, distributed, scalable',
    packages=['rtcloud'],
    python_requires='>=3.4'
)
