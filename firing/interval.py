# -*- coding: utf-8 -*-
"""
Interval arithmetic
https://en.wikipedia.org/wiki/Interval_arithmetic

https://tel.archives-ouvertes.fr/tel-00680352/document

https://pyinterval.readthedocs.io/en/latest/guide.html

https://conference.scipy.org/proceedings/scipy2008/paper_3/full_text.pdf
"""

import numpy as np


interval_ = np.dtype({'names': ['l','u'], 'formats': [np.float_, np.float_]})

# def asinterval(c):
#     if isinstance(type(c), Interval):
#         return c
#     else:
#         return Interval(c, c)


def interval(a: float = 0, b: float = 0):
    return Interval(np.min((a,b)), np.max((a,b)))


class AssignmentError(ArithmeticError):
    """Base class for exceptions in this module."""
    pass


class Interval(np.ndarray):
    """A numeric class that represent the interval [a..b] if a<=b and union [-inf..b]U[a..inf] if a>b
    """
    pass
    # def __repr__(self):
    #     return f"Interval({self.a}, {self.b})"
    #
    # def __format__(self, format_spec):
    #     if format_spec == '':
    #         return f"❪{self.a}⠤{self.b}❫"
    #     elif format_spec == 'ascii':
    #         return f"({self.a}..{self.b})"
    #     elif format_spec == 'unicode':
    #         return f"〖{self.a}⠤{self.b}〗"
    #
    # def __str__(self):
    #     return f"【{self.a}⠤{self.b}】"
    #
    # def __eq__(self, other):
    #     return self.a == other.a and self.b == other.b

    # def __add__(self, other):
    #     # other = asinterval(other)
    #     return Interval(self['l'] + other['l'], self['u'] + other['u'])
    #
    # def __sub__(self, other):
    #     other = asinterval(other)
    #     return Interval(self.a - other.b, self.b - other.a)
    #
    # def __neg__(self):
    #     return Interval(-self.b, -self.a)

    # def __pos__(self):
    #     return NotImplemented
    #
    # def _products(self, other):
    #     products = [self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b]
    #     return min(products), max(products)
    #
    # def __mul__(self, other):
    #     a, b = self._products(asinterval(other))
    #     return Interval(a, b)


# def asfinterval(c):
#     if issubclass(type(c), Finterval):
#         return c
#     else:
#         return Finterval(c, c)
#
#
# def finterval(a: float = 0, b: float = 0):
#     if 0 <= a <= b:
#         return Finterval(0, 0, np.float_(a), np.float_(b))
#     elif a <= b <= 0:
#         return Finterval(np.float_(a), np.float_(b), 0, 0)
#     elif a <= 0 <= b:
#         return Finterval(np.float_(a), 0, 0, np.float_(b))
#
#
# class Finterval:
#     """New numeric class that represent the doupled interval <[a..b], [c..d]>
#     """
#     a: np.float_ = 0
#     b: np.float_ = 0
#     c: np.float_ = 0
#     d: np.float_ = 0
#
#     def __init__(self, a: np.float_ = 0, b: np.float_ = 0, c: np.float_ = 0, d: np.float_ = 0):
#         self.a, self.b, self.c, self.d = a, b, c, d
#
#     def __repr__(self):
#         return f"Fint({self.a}, {self.b}, {self.c}, {self.d})"
#
#     def __format__(self, format_spec):
#         if format_spec == '':
#             return f"⟨({self.a}⠤{self.b}),({self.c}⠤{self.d})⟩"
#         elif format_spec == 'ascii':
#             return f"<({self.a}..{self.b}),({self.c}..{self.d})>"
#         elif format_spec == 'unicode':
#             return f"⟨({self.a}⠤{self.b}),({self.c}⠤{self.d})⟩"
#
#     def __str__(self):
#         return f"⟨[{self.a}⠤{self.b}],[{self.c}⠤{self.d}]⟩"
#
#     def __add__(self, other):
#         # other = asinterval(other)
#         return Finterval(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
#
#     def __sub__(self, other):
#         other = asinterval(other)
#         return Finterval(self.a - other.b, self.b - other.a)
#
#     def __isub__(self, other):
#         other = asinterval(other)
#         self.a -= other.b
#         self.b -= other.a
#         return self
#
#     def __rsub__(self, other):
#         other = asinterval(other)
#         return Interval(other.a - self.b, other.b - self.a)
#
#     def __neg__(self):
#         return Interval(-self.b, -self.a)
#
#     # def __pos__(self):
#     #     return NotImplemented
#
#     def _products(self, other):
#         products = [self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b]
#         return min(products), max(products)
#
#     def __mul__(self, other):
#         a, b = self._products(asinterval(other))
#         return Interval(a, b)
#
#     def __imul__(self, other):
#         self.a, self.b = self._products(asinterval(other))
#         return self
#
#     def __rmul__(self, other):
#         return self.__mul__(other)

