# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           drbl
Version:        5.11.22
Release:        %autorelease
Summary:        Diskless Remote Boot in Linux
License:        GPL-2.0-only
URL:            https://drbl.org/
VCS:            git:https://github.com/stevenshiau/drbl.git
#!RemoteAsset:  sha256:feae4f50575ba4ae2f201e0842139f71fed83eebf2afc1d26a969e379e2e7ba2
Source:         https://github.com/stevenshiau/drbl/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# BuildSystem: none. Upstream only ships a hand-written Makefile, so the build
# and install stages are implemented explicitly below.

BuildRequires:  bash
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl

Requires:       bash
Requires:       coreutils
Requires:       gawk
Requires:       grep
Requires:       ipcalc
Requires:       perl
Requires:       procps-ng
Requires:       psmisc
Requires:       sed
Requires:       util-linux

Recommends:     curl
Recommends:     nmap
Recommends:     openssh-server
Recommends:     rsync
Recommends:     tftp-server
Recommends:     wget

# PXE booting also needs syslinux (syslinux-common and pxelinux), which is
# not packaged in openRuyi yet, so it is not listed as a dependency.

%description
DRBL (Diskless Remote Boot in Linux) provides a diskless or systemless
environment for client machines. It uses distributed hardware resources
and makes it possible for clients to fully access local hardware.

DRBL is the framework Clonezilla is built on. It also contains the
clonezilla command line tools used to save and restore partitions over the
network.

%prep
%autosetup

%build
# pkg-misc regenerates fail-mbr.bin with xxd; the archive already contains
# the generated file, so it is skipped to avoid a needless build dependency.
%make_build drbl-sbin-link languages

%check
%make_build -C lang check
for script in $(find bin sbin scripts -type f); do
    [ -L "$script" ] && continue
    if head -n 1 "$script" | grep -q bash; then
        bash -n "$script"
    fi
done

%install
make install DESTDIR=%{buildroot}

# openRuyi merges /usr/sbin into /usr/bin, so move the scripts the Makefile
# installed into /usr/sbin to their merged location.
%if "%{_sbindir}" == "%{_bindir}"
if [ -d %{buildroot}/usr/sbin ]; then
    cp -a %{buildroot}/usr/sbin/. %{buildroot}/usr/bin/
    rm -rf %{buildroot}/usr/sbin
fi
%endif

%files
%license LICENSE
%doc README
%if "%{_sbindir}" == "%{_bindir}"
%{_bindir}/*
%else
%{_bindir}/*
%{_sbindir}/*
%endif
%doc %{_datadir}/drbl/doc
%{_datadir}/drbl/bin
%{_datadir}/drbl/image
%{_datadir}/drbl/lang
%{_datadir}/drbl/pkg
%{_datadir}/drbl/pki
%{_datadir}/drbl/postrun/drbl
%{_datadir}/drbl/prerun/drbl
%{_datadir}/drbl/sbin
%{_datadir}/drbl/setup/files/DBN
%{_datadir}/drbl/setup/files/LinuxMint
%{_datadir}/drbl/setup/files/RH
%{_datadir}/drbl/setup/files/SUSE
%{_datadir}/drbl/setup/files/Ubuntu
%{_datadir}/drbl/setup/files/boinc
%{_datadir}/drbl/setup/files/misc
%{_datadir}/drbl/setup/rpm-md-repos
%{_datadir}/drbl/setup/yum-repos
%{_datadir}/gdm/themes/drbl-gdm
%config(noreplace) %{_sysconfdir}/drbl/*

%changelog
%autochangelog
