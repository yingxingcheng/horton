# -*- coding: utf-8 -*-
# Horton is a Density Functional Theory program.
# Copyright (C) 2011 Toon Verstraelen <Toon.Verstraelen@UGent.be>, ...
#
# This file is part of Horton.
#
# Horton is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# Horton is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
#--
"""Define a molecular system and all aspects relevant for a computation"""


import numpy as np

from horton.io import load_geom


__all__ = ['System']


class System(object):
    def __init__(self, coordinates, numbers):
        self.coordinates = np.array(coordinates, dtype=float, copy=False)
        self.numbers = np.array(numbers, dtype=int, copy=False)

    @classmethod
    def from_file(cls, filename, *args, **kwargs):
        ext = filename[filename.rfind('.'):]
        coordinates, numbers = load_geom[ext](filename)
        return cls(coordinates, numbers, *args, **kwargs)
