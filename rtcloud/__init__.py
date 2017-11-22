"""
Your brain in the cloud.

A work in progress. More documentation to come.
"""

from .server import Server
from .client import Client
from .launcher import Launcher

from .experiments import (
    Experiment,
    FCMAExperiment,
    SearchlightExperiment
)

from .utils import (
    Config,
    Logger
)

__all__ = [
    'Server',
    'Client',
    'Launcher',

    'Experiment',
    'FCMAExperiment',
    'SearchlightExperiment',

    'Config',
    'Logger'
]
