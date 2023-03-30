import logging
import os
import pathlib

import pytest


here = pathlib.Path(__file__).parent


@pytest.fixture
def banana_preparer():
    if os.path.exists("banana.log"):
        os.remove("banana.log")
    yield
    if os.path.exists("banana.log"):
        os.remove("banana.log")
