"""
Your brain in the cloud.

A work in progress. More documentation to come.
"""

from .server import Server
from .client import Client
from .launcher import Launcher

from .ui import (
    display_input,
    display_output
)

from .experiments import (
    Experiment,
    # FCMAExperiment,
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

    'display_input',
    'display_output',

    'Experiment',
    'FCMAExperiment',
    'SearchlightExperiment',

    'Config',
    'Logger'
]
