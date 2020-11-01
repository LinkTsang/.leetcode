# Copyright (c) 2020 LinkD
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import sys
from math import *
from typing import *
from collections import *


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def assertEqual(actual, excepted):
  if actual != excepted:
    raise RuntimeError(f'Excepted {excepted}, got {actual}')
