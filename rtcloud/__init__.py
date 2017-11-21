"""
Your brain in the cloud.

A work in progress. More documentation to come.
"""

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
    'Experiment',
    'FCMAExperiment',
    'SearchlightExperiment',

    'Config',
    'Logger'
]
