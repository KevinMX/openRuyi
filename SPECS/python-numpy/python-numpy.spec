# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname numpy

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        NumPy: array processing for numbers, strings, records, and objects
License:        BSD-3-Clause
URL:            https://github.com/numpy/numpy
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildOption(build):  -Csetup-args=-Dblas=openblas
BuildOption(build):  -Csetup-args=-Dlapack=lapack

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-meson-python >= 0.15.0
BuildRequires:  python3-Cython >= 3.0.6
BuildRequires:  pkgconfig
BuildRequires:  openblas-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
Provides:       python3-%{srcname}-f2py
%python_provide python3-%{srcname}-f2py

%description
NumPy is the fundamental package for scientific computing with Python.
It contains among other things:
- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

%generate_buildrequires
%pyproject_buildrequires -R

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.md THANKS.txt
%{_bindir}/f2py
%{_bindir}/numpy-config

%changelog
%{?autochangelog}
