import random

# Define the __all__ variable
__all__ = ["c01", "c02", "c03", "c04", "c05"]
random.shuffle(__all__)

#print(__all__)
# Import the submodules
from . import c01
from . import c02
from . import c03
from . import c04
from . import c05