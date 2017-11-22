from setuptools import setup

setup(
    name='rtcloud',
    version='0.0.1',
    install_requires=[
        'click',
        'requests',
        'tqdm',
        'watchdog',
        'flask',
        'flask_session',
        'binaryornot',
        'cfncluster',
        'matplotlib',
        'nilearn',
        'numpy',
        'scipy',
        'pybind11',
        'cython',
        'pika'
    ],
    extras_require={
        'demo': [
            'jupyter',
            'brainiak'
        ]
    },
    author='Princeton Neuroscience Institute and Intel Corporation',
    author_email='dsuo@princeton.edu',
    url='https://github.com/brainiak/rtcloud',
    description='Brain Imaging Analysis Kit Cloud',
    license='Apache 2',
    keywords='neuroscience, algorithm, fMRI, distributed, scalable',
    packages=['rtcloud'],
    python_requires='>=3.4',
    entry_points='''
        [console_scripts]
        watch=rtcloud.watcher:watch
        serve=rtcloud.server:serve
    '''
)
