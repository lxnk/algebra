# -*- coding: utf-8 -*-

from .context import *
from firing.interval import Interval, asinterval


@pt.fixture(params=[(3, 4), (1.0, 2.0), (-3, 1)], ids=["34", "12", "-31"])
def iv(request):
    """Create intervals out of the numbers pairs"""
    return Interval(*request.param)


# def test_roots(iv):
#     print()
#     print(iv)
#     print(iv == interval(1, 2))
#     print(type(iv.a))
#
#

def test_print(iv):
    i = Interval(1, 2)
    print()
    print(iv, type(iv.a))


def test_arithmetics(iv):
    i = Interval(1, 2)
    print(iv+i)
