# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit_date  20251031
%global commit       4badb276ca98398513a77d5e9bdc9892f7544762
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           blktests
Version:        %{commit_date}+git%{shortcommit}
Release:        %autorelease
Summary:        Linux kernel block layer testing framework
License:        GPL-2.0-or-later
URL:            https://github.com/osandov/blktests
#!RemoteAsset
Source0:        https://github.com/osandov/blktests/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildSystem:    autotools
BuildOption(prep): -p1 -n %{name}-%{commit}
BuildOption(build): CFLAGS="%{optflags} -g"
BuildOption(install): prefix="%{_prefix}/lib"

BuildRequires:  gcc-c++
Requires:       bash
Requires:       coreutils
Requires:       gawk
Requires:       util-linux
Requires:       fio
Requires:       gcc
Requires:       make
Requires:       systemd-udev
Recommends:     blktrace
Recommends:     e2fsprogs
Recommends:     xfsprogs
Recommends:     f2fs-tools
Recommends:     btrfs-progs
Recommends:     nvme-cli
Recommends:     multipath-tools
Recommends:     device-mapper
Recommends:     nbdkit-server
Recommends:     python3
Recommends:     ethtool
Recommends:     iproute2

%description
blktests is a test framework for the Linux kernel block layer and
storage stack. It is inspired by the xfstests filesystem testing
framework.

# no configure script.
%conf

# XXX: test require shellcheck.
%check

%files
%doc README.md
%license LICENSES/GPL-2.0 LICENSES/GPL-3.0
%{_prefix}/lib/blktests

%changelog
%{?autochangelog}
