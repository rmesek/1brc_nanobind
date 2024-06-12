1brc_nanobind
================

|      CI              | status |
|----------------------|--------|
| pip builds           | [![Pip Action Status][actions-pip-badge]][actions-pip-link] |
| wheels               | [![Wheel Action Status][actions-wheels-badge]][actions-wheels-link] |

[actions-pip-link]:        https://github.com/rmesek/1brc_nanobind/actions?query=workflow%3APip
[actions-pip-badge]:       https://github.com/rmesek/1brc_nanobind/workflows/Pip/badge.svg
[actions-wheels-link]:     https://github.com/rmesek/1brc_nanobind/actions?query=workflow%3AWheels
[actions-wheels-badge]:    https://github.com/rmesek/1brc_nanobind/workflows/Wheels/badge.svg


This repository contains a project showing how to create C++ bindings using [nanobind](https://github.com/wjakob/nanobind) and [scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/index.html) in order to solve [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc). It was derived from [nanobind example](https://github.com/wjakob/nanobind_example) developed by [@wjakob](https://github.com/wjakob).

Installation
------------

1. Clone this repository
2. Run `pip install ./1brc_nanobind`

Afterwards, you should be able to issue the following commands (shown in an
interactive Python session):

```pycon
>>> import brc_nanobind
>>> brc_nanobind.add(1, 2)
3
```

Usage
------------

<!-- TODO -->

Installation
------------

1. Run `pip uninstall brc-nanobind`

CI Examples
-----------

The `.github/workflows` directory contains two continuous integration workflows
for GitHub Actions. The first one (`pip`) runs automatically after each commit
and ensures that packages can be built successfully and that tests pass.

The `wheels` workflow uses
[cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/) to automatically
produce binary wheels for a large variety of platforms. If a `pypi_password`
token is provided using GitHub Action's _secrets_ feature, this workflow can
even automatically upload packages on PyPI.
