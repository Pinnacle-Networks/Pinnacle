import os
import sys

from setuptools import setup

if not os.getenv("IGNORE_ERROR"):
    error_message = """
    ERROR: This package has been renamed to 'pinnacle'. Please install the new package using:
    
    pip install pinnacle

    Github: https://github.com/pinnacle-io/pinnacle
    """
    print(error_message)
    sys.exit(1)

setup(
    name="pinnacledb",
    version="0.2.2",
    description="This package has been deprecated. Use pinnacle instead.",
    packages=[],
)