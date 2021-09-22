# -*- coding: utf-8 -*-

from .context import *
from firing.interval import Interval, interval_


# @pt.fixture(params=[(3, 4), (1.0, 2.0), (-3, 1)], ids=["34", "12", "-31"])
# def iv(request):
#     """Create intervals out of the numbers pairs"""
#     return interval(request.param[0], request.param[1])


def test_datatype():

    # x = np.empty((2,3), dtype=dt)

    x = np.array([(1,2),(3,4)], dtype=interval_)

    print()
    print(type(x))
    print(x, x[0], x['l'][0])


# def test_roots(iv):
#     print()
#     print(iv)
#     print(iv == interval(1, 2))
#     print(type(iv.a))
#
#
# def test_arithmetics(iv):
#     c = 0.7
#     iv = c*iv
