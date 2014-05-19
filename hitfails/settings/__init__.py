"""
Settings used by hitfails project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from hitfails.settings.production import *

# Import optional local settings.
try:
    from hitfails.settings.local import *
except ImportError:
    pass