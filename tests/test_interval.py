# -*- coding: utf-8 -*-

from .context import *
from firing.interval import Interval, asfinterval


def function_interval_check(func, *args):
    def linsp(x,n):
        y = np.linspace(x.a, x.b)
        return y[(..., *([np.newaxis] * n))]

    vargs = tuple(map(linsp, args, range(len(args))))
    res = func(*vargs)
    return float(np.min(res)), float(np.max(res))


@pt.fixture(params=[(3, 4), (1.0, 2.0), (-3, 1)], ids=["34", "12", "-31"])
def iv(request):
    """Create intervals out of the numbers pairs"""
    return Interval(*request.param)


@pt.fixture(params=[(3, 4), (1.0, 2.0), (-3, 1)], ids=["f34", "f12", "f-31"])
def fiv(request):
    """Create intervals out of the numbers pairs"""
    return asfinterval(request.param)

# def test_roots(iv):
#     print()
#     print(iv)
#     print(iv == interval(1, 2))
#     print(type(iv.a))
#


def test_print(iv):
    print()
    print(iv, type(iv.a))


def test_print_f(fiv):
    print()
    print(fiv, type(fiv.c))


def test_arithmetics(iv):
    i = Interval(1, 2)
    for f in (lambda x, y: x + y,
              lambda x, y: x - y,
              lambda x, y: x * y):
        fmin, fmax = function_interval_check(f, i, iv)
        j = f(i, iv)
        assert fmin == j.a
        assert fmax == j.b


def test_square(iv):
    f = lambda x: x * x
    fmin, fmax = function_interval_check(f, iv)
    j = f(iv)
    if iv.a < 0 < iv.b:
        assert fmin >= j.a
        assert fmax <= j.b
    else:
        assert fmin == j.a
        assert fmax == j.b

    f = lambda x, y: x * y
    fmin, fmax = function_interval_check(f, iv, iv)
    j = f(iv, iv)
    assert fmin == j.a
    assert fmax == j.b


def test_square_f(fiv):
    f = lambda x: x * x
    fmin, fmax = function_interval_check(f, fiv)
    j = f(fiv)
    print()
    print(fiv, Interval(fmin, fmax), j)
    # if iv.a < 0 < iv.b:
    #     assert fmin >= j.a
    #     assert fmax <= j.b
    # else:
    #     assert fmin == j.a
    #     assert fmax == j.b
    #
    # f = lambda x, y: x * y
    # fmin, fmax = function_interval_check(f, iv, iv)
    # j = f(iv, iv)
    # assert fmin == j.a
    # assert fmax == j.b

