# -*- coding: utf-8 -*-
"""
Interval arithmetic
https://en.wikipedia.org/wiki/Interval_arithmetic

https://tel.archives-ouvertes.fr/tel-00680352/document

https://pyinterval.readthedocs.io/en/latest/guide.html

https://conference.scipy.org/proceedings/scipy2008/paper_3/full_text.pdf
"""

from math import inf


class AssignmentError(ArithmeticError):
    """Base class for exceptions in this module."""
    pass


def asinterval(c):
    if isinstance(c, Interval):
        return c
    elif isinstance(c, tuple):
        return Interval(*c)
    elif isinstance(c, (float, int)):
        return Interval(c, c)
    else:
        return AssignmentError


class Interval:
    """A numeric class that represent the interval [a..b] if a<=b and union [-inf..b]U[a..inf] if a>b
    """
    a: float = 0
    b: float = 0

    def __init__(self, a: float = 0, b: float = inf):
        self.a, self.b = a, b

    def __repr__(self):
        return f"Interval({self.a}, {self.b})"

    def __format__(self, format_spec):
        if format_spec == '':
            return f"❪{self.a}⠤{self.b}❫"
        elif format_spec == 'ascii':
            return f"({self.a}..{self.b})"
        elif format_spec == 'unicode':
            return f"〖{self.a}⠤{self.b}〗"

    def __str__(self):
        return f"【{self.a}⠤{self.b}】"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    @staticmethod
    def _values(other):
        if isinstance(other, Interval):
            return other.a, other.b
        elif isinstance(other, (int, float)):
            return other, other
        else:
            return ArithmeticError

    def _products(self, other):
        a, b = self._values(other)
        products = (self.a * a, self.a * b, self.b * a, self.b * b)
        return min(products), max(products)

    def __add__(self, other):
        a, b = self._values(other)
        return Interval(self.a + a, self.b + b)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        a, b = self._values(other)
        return Interval(self.a - b, self.b - a)

    def __rsub__(self, other):
        a, b = self._values(other)
        return Interval(a - self.b, b - self.a)

    def __neg__(self):
        return Interval(-self.b, -self.a)

    # def __pos__(self):
    #     return NotImplemented
    #

    def __mul__(self, other):
        a, b = self._products(other)
        return Interval(a, b)

    def __rmul__(self, other):
        return self.__mul__(other)


def asfinterval(c):
    if isinstance(c, Finterval):
        return c
    else:
        if isinstance(c, Interval):
            a, d = c.a, c.b
        elif isinstance(c, tuple):
            a, d = c
        elif isinstance(c, (float, int)):
            a = d = c
        else:
            return AssignmentError

        if 0 <= a <= d:
            return Finterval(0, 0, a, d)
        elif a <= d <= 0:
            return Finterval(a, d, 0, 0)
        elif a <= 0 <= d:
            return Finterval(a, 0, 0, d)


class Finterval:
    """New numeric class that represent the doupled interval <[a..b], [c..d]>
    """
    a: float = 0
    b: float = 0
    c: float = 0
    d: float = 0

    def __init__(self, a: float = 0, b: float = 0, c: float = 0, d: float = 0):
        self.a, self.b, self.c, self.d = a, b, c, d

    def __repr__(self):
        return f"Fintnerval({self.a}, {self.b}, {self.c}, {self.d})"

    def __format__(self, format_spec):
        if format_spec == '':
            return f"⟨❪{self.a}⠤{self.b}),({self.c}⠤{self.d}❫⟩"
        elif format_spec == 'ascii':
            return f"<({self.a}..{self.b}),({self.c}..{self.d})>"
        elif format_spec == 'unicode':
            return f"⟨〖{self.a}⠤{self.b}),({self.c}⠤{self.d}〗⟩"

    def __str__(self):
        return f"⟨【{self.a}⠤{self.b}】,【{self.c}⠤{self.d}】⟩"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    @staticmethod
    def _values(other):
        if isinstance(other, Finterval):
            return other.a, other.b, other.c, other.d
        elif isinstance(other, (int, float)):
            if other >=0:
                return 0, 0, other, other
            else:
                return other, other, 0, 0
        else:
            return ArithmeticError

    def __add__(self, other):
        a, b, c, d = self._values(other)
        return Finterval(self.a + a, self.b + b, self.c + c, self.d + d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        a, b, c, d = self._values(other)
        return Finterval(self.a - d, self.b - c, self.c - b, self.d - a)

    def __rsub__(self, other):
        a, b, c, d = self._values(other)
        return Finterval(a - self.d, b - self.c, c - self.b, d - self.a)

    def __neg__(self):
        return Finterval(-self.d, -self.c, -self.b, -self.a)

    # def __pos__(self):
    #     return NotImplemented

    def _products(self, other):
        a, b, c, d = self._values(other)
        products = (self.a * d + self.d * a, self.b * c + self.c * b,
                    self.b * b + self.c * c, self.a * a + self.d * d)
        return products

    def __mul__(self, other):
        a, b, c, d = self._products(other)
        return Finterval(a, b, c, d)

    def __rmul__(self, other):
        return self.__mul__(other)
