# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lzlib
Version:        1.15
Release:        %autorelease
Summary:        Lzip data compression C library
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://www.nongnu.org/lzip/lzlib.html
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://download.savannah.nongnu.org/releases/lzip/lzlib/lzlib-%{version}.tar.gz
#!RemoteAsset
Source1:        https://download.savannah.nongnu.org/releases/lzip/lzlib/lzlib-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-shared

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  texinfo

%description
Lzlib is a C library for in-memory LZMA compression and decompression in
the lzip format.  It supports integrity checking of the decompressed data, and
all functions are thread-safe.  The library should never crash, even in case of
corrupted input.

%package        devel
Summary:        Development files for the lzlib
License:        BSD-2-Clause
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This subpackage contains libraries and header files for developing
applications that want to make use of lzlib.

%files
%doc README
%license COPYING COPYING.GPL
%{_libdir}/liblz.so*

%files devel
%{_includedir}/lzlib.h
%{_libdir}/liblz.so
%{_infodir}/*

%changelog
%{?autochangelog}
