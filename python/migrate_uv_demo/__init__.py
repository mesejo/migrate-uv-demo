import importlib.metadata

from .migrate_uv_demo import *


__doc__ = migrate_uv_demo.__doc__
if hasattr(migrate_uv_demo, "__all__"):
    __all__ = migrate_uv_demo.__all__

__version__ = importlib.metadata.version(__package__)
