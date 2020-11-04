# Copyright (c) 2020 LinkD
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import sys
from math import *
from typing import *
from collections import *
from pprint import pprint
import unittest
from unittest import TestCase


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def assertEqual(actual, excepted):
  if actual != excepted:
    raise RuntimeError(f'Excepted {excepted}, got {actual}')


def run_tests():
  unittest.main(argv=[''], verbosity=2, exit=False)
