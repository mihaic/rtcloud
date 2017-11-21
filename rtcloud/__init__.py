"""
Your brain in the cloud.

A work in progress. More documentation to come.
"""

from .client import (
    Client
)

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
    'Client',

    'Experiment',
    'FCMAExperiment',
    'SearchlightExperiment',

    'Config',
    'Logger'
]
