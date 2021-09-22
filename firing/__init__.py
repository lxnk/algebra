# -*- coding: utf-8 -*-
"""
Intervals

Interval arithmetic
https://en.wikipedia.org/wiki/Interval_arithmetic

https://tel.archives-ouvertes.fr/tel-00680352/document

https://pyinterval.readthedocs.io/en/latest/guide.html

https://conference.scipy.org/proceedings/scipy2008/paper_3/full_text.pdf

"""


# # This hook works for the importing allows to access modules as
#
# from firing import *
#
# interval.some_function()

__all__ = ["interval"]

# # This hook works for the importing allows to access modules as
#
# import methods
#
# firing.interval.some_function()

from . import interval

# # This importing allows to access modules even if __init__.py is absent
#
# from firing import interval
#
# interval.some_function()
