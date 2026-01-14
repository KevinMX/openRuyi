# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:    dwz
Version: 0.16
Release: %autorelease
Summary: A DWARF optimization and duplicate removal tool
License: GPLv2+ and GPLv3+
URL: https://sourceware.org/dwz/
#!RemoteAsset
Source0:https://sourceware.org/ftp/dwz/releases/%{name}-%{version}.tar.xz
Patch0: remove-gold-tests.patch
BuildRequires: gcc gcc-c++ dejagnu
BuildRequires: xxhash-devel libelf-devel
# For %check
BuildRequires: gdb
BuildSystem:   autotools
BuildOption(build): prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir} CFLAGS='%{build_cflags}'
BuildOption(install): prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%description
The package contains a program that attempts to optimize DWARF debugging
information contained in ELF shared libraries and ELF executables for size,
by replacing DWARF information representation with equivalent smaller
representation where possible and by reducing the amount of duplication
using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information and
using DW_TAG_imported_unit to import it into each CU that needs it.

# no configure scripts.
%conf
:

%check -p
# Avoid failure due to dwz warn: Found compressed .debug_info section
export CC='cc -gz=none'
export CXX='g++ -gz=none'

%files
%defattr(-,root,root,-)
%license COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%{_mandir}/man1/dwz*

%changelog
%{?autochangelog}
