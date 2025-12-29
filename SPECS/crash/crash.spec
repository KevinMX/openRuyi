# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name: crash
Version: 9.0.1
Release: %autorelease
Summary: Kernel analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles
License: GPL-3.0-only
URL: https://crash-utility.github.io
#!RemoteAsset
Source0: https://github.com/crash-utility/%{name}/archive/refs/tags/%{version}.tar.gz
#!RemoteAsset
Source1: http://ftp.gnu.org/gnu/gdb/gdb-16.2.tar.gz
Patch0: lzo_snappy_zstd.patch
Patch1: crash-9.0.1_build.patch

BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: lzo-devel
BuildRequires: snappy-devel
BuildRequires: bison
BuildRequires: texinfo
BuildRequires: zstd-devel
BuildRequires: gmp-devel
BuildRequires: mpfr-devel
Requires: binutils

Provides: bundled(libiberty)
Provides: bundled(gdb) = 16.2

BuildSystem:autotools
BuildOption(build): RPMPKG="%{version}-%{release}"
BuildOption(build): CFLAGS="%{optflags}"
BuildOption(build): CXXFLAGS="%{optflags}"
BuildOption(build): LDFLAGS="%{build_ldflags}"

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%conf

%build -p
cp %{SOURCE1} .

%install -a
mkdir -p %{buildroot}%{_mandir}/man8
cp -p crash.8 %{buildroot}%{_mandir}/man8/crash.8
mkdir -p %{buildroot}%{_includedir}/crash
chmod 0644 defs.h
cp -p defs.h %{buildroot}%{_includedir}/crash

# No tests
%check

%files
%{_bindir}/crash
%{_mandir}/man8/crash.8*
%doc README COPYING3
%{_includedir}/*

%changelog
%{?autochangelog}
