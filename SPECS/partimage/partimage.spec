# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           partimage
Version:        0.6.9
Release:        %autorelease
Summary:        Partition imaging and cloning tool
License:        GPL-2.0-or-later
URL:            https://www.partimage.org/
VCS:            git:https://gitlab.com/partimage/partimage-sources.git
#!RemoteAsset:  sha256:753a6c81f4be18033faed365320dc540fe5e58183eaadcd7a5b69b096fec6635
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

# https://bugs.debian.org/662596
Patch2000:      2000-Fix-gzFile-type-for-modern-zlib.patch
# https://bugs.debian.org/859549
Patch2001:      2001-Use-OpenSSL-3-compatible-API.patch
# https://bugs.debian.org/915987
Patch2002:      2002-Fix-makedev-macro-for-glibc-2.28.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  newt-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)

Requires:       e2fsprogs
Requires:       util-linux

%description
Partimage saves and restores partitions as image files. Only the used
blocks of a partition are copied, so an image is usually much smaller than
the partition itself. The image can be written to a file, to a set of
split files, or transferred to a partimaged server over the network.

%conf -p
autoreconf -fiv

%check
# Upstream does not provide a test suite; check that the binaries start.
./src/client/partimage --version
./src/server/partimaged --version

%install -a
%find_lang %{name}

# The upstream Makefile installs its documentation into the package
# documentation directory; the files are shipped through %license and %doc
# instead.
rm -rf %{buildroot}%{_docdir}/%{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS BUGS ChangeLog README README.partimaged
%{_sbindir}/partimage
%{_sbindir}/partimaged
# Upstream deliberately installs the client allowlist with mode 0600.
%config(noreplace) %{_sysconfdir}/partimaged/partimagedusers

%changelog
%autochangelog
