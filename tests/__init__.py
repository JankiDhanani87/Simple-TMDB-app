import os
import sys
import pytest

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path = [os.path.join(HERE, "../src")] + sys.path
