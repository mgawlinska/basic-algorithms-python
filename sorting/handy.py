#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Collection of handy functions
"""

# authorship information; metadata
__author__ = "Magdalena Gawlinska"
__copyright__ = ""
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Magdalena Gawlinska"
__email__ = ""
__status__ = "Prototype"

from timeit import repeat


def time_your_sort(algorithm, data, repeat_count):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({data})"
    executions = repeat(stmt=stmt, setup=setup_code, repeat=repeat_count, number=1)

    print(f"Algorithm: {algorithm}: Execution times: {executions}. "
          f"Minimum execution time: {min(executions)}")


