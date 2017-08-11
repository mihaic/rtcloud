from setuptools import setup

setup(
        name='brainiak-cloud',
        version='0.0.1',
        install_requires=[
            'brainiak',
            'watchdog',
            'requests'
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
