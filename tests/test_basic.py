import brc_nanobind as m


def test_add():
    assert m.add(1, 2) == 3