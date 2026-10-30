# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clonezilla
Version:        5.19.19
Release:        %autorelease
Summary:        Partition and disk imaging and cloning tool
License:        GPL-2.0-or-later
URL:            https://clonezilla.org/
VCS:            git:https://gitlab.com/stevenshiau/clonezilla.git
#!RemoteAsset:  sha256:8ebf6ff18208f0e840b1f61a98dca89a98ca4794a51fe1a48dd62fe06ced45e6
Source:         https://github.com/stevenshiau/clonezilla/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
# BuildSystem: none. Upstream only ships a hand-written Makefile, so the build
# and install stages are implemented explicitly below.

BuildRequires:  bash
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  make

Requires:       bash
Requires:       bc
Requires:       bzip2
Requires:       coreutils
Requires:       dialog
Requires:       drbl >= 5.11.22
Requires:       e2fsprogs
Requires:       findutils
Requires:       gawk
Requires:       gptfdisk
Requires:       grep
Requires:       gzip
Requires:       jq
Requires:       lz4
Requires:       lzop
Requires:       ntfs-3g
Requires:       parted
Requires:       partclone >= 0.3.50
Requires:       pbzip2
Requires:       perl
Requires:       procps-ng
Requires:       psmisc
Requires:       python3
Requires:       sed
Requires:       tar
Requires:       udpcast
Requires:       util-linux
Requires:       wget
Requires:       xz
Requires:       zstd

Recommends:     btrfs-progs
Recommends:     cifs-utils
Recommends:     cryptsetup
Recommends:     curl
Recommends:     dhcpcd
Recommends:     dosfstools
Recommends:     f2fs-tools
Recommends:     lvm2
Recommends:     mdadm
Recommends:     nmap
Recommends:     partimage
Recommends:     pigz
Recommends:     smartmontools
Recommends:     squashfs-tools
Recommends:     xfsprogs
Recommends:     xorriso

# Creating bootable media also needs isolinux, which is not packaged in
# openRuyi yet, so it is not listed as a dependency. The ocsmgrd daemon also
# needs the Logfile::Rotate Perl module, which is not packaged either.

%description
Clonezilla is a partition and disk imaging and cloning tool. It is based
on DRBL, Partclone and udpcast and can save and restore only the used
blocks of a partition.

Clonezilla supports many file systems, including ext2/3/4, XFS, Btrfs,
NTFS, FAT, exFAT, F2FS and HFS+, and can clone a single machine or many
machines at once over multicast.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%check
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
%doc %{_datadir}/clonezilla/doc
%{_datadir}/drbl/postrun/ocs
%{_datadir}/drbl/prerun/ocs
%{_datadir}/drbl/samples
%{_datadir}/drbl/sbin/ocs-chnthn-functions
%{_datadir}/drbl/sbin/ocs-functions
%{_datadir}/drbl/sbin/set-netboot-1st-efi-nvram
%{_datadir}/drbl/setup/files/gparted
%{_datadir}/drbl/setup/files/ocs
%{_datadir}/drbl/setup/files/riscv64
%{_mandir}/man8/ocs-onthefly.8*
%{_mandir}/man8/ocs-sr.8*
%config(noreplace) %{_sysconfdir}/drbl/drbl-ocs.conf

%changelog
%autochangelog
