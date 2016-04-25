#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pyCombo import combo, modularity
from _misc import _partitionGroup as _pg
from _misc import _get_test_graph

__author__ = "Philipp Kats"
__copyright__ = "Philipp Kats"
__license__ = "mit"


def test_combo():

    partition = combo(_get_test_graph(), weight='weight')
    assert _pg(partition) == _pg({0: 0, 1: 0, 2: 1, 3: 0, 4: 1})

    with pytest.raises(AssertionError):
		combo(42, weight='weight')


def test_modularity():
	G = _get_test_graph()
	partition = combo(G, weight='weight')
	assert modularity(G, partition, key='weight') == 0.08000000000000004

	with pytest.raises(AssertionError):
		combo(42, weight='weight')
