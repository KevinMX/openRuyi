# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# ignore the explicit bash requires from the kernel mod scripts
%define __requires_exclude ^/bin/bash$
Name:           rpm-config-openruyi
Version:        20251029
Release:        %autorelease
Summary:        specific RPM configuration files
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://git.oerv.ac.cn/openruyi/rpm-config-openruyi
Source:         https://git.oerv.ac.cn/openRuyi/rpm-config-openruyi/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gzip
#!BuildIgnore:  rpm-config-openruyi
# RPM owns the directories we need
Requires:       rpm
Provides:       rpm-config
BuildArch:      noarch

%description
This package contains the RPM configuration data for the openruyi
distribution families.

%prep
%autosetup -p1 -n rpm-config-openruyi

%build
# Set up the macros
sed -e 's/@ul_version@/%{?ul_version}%{!?ul_version:0}/' \
    -e '/@is_openruyi@%{?is_openruyi:nomatch}/d' \
    -e 's/@is_openruyi@/%{?is_openruyi}%{!?is_openruyi:0}/' \
  < macros.in > macros

%install
# Install vendor macros and rpmrc
mkdir -p %{buildroot}%{_rpmconfigdir}/openruyi
cp -a macros %{buildroot}%{_rpmconfigdir}/openruyi/macros

# Install vendor dependency generators
cp -a fileattrs %{buildroot}%{_rpmconfigdir}
cp -a scripts/* %{buildroot}%{_rpmconfigdir}
cp -a macros.d %{buildroot}%{_rpmconfigdir}

%files
%license COPYING
%doc README.md
%{_rpmconfigdir}/openruyi/
%{_rpmconfigdir}/macros.d/macros.*
%{_rpmconfigdir}/fileattrs/*
%{_rpmconfigdir}/brp-openruyi
%{_rpmconfigdir}/firmware.prov
%{_rpmconfigdir}/sysvinitdeps.sh
%{_rpmconfigdir}/locale.prov
# kmod deps
%{_rpmconfigdir}/find-provides.ksyms
%{_rpmconfigdir}/find-requires.ksyms
%{_rpmconfigdir}/find-supplements.ksyms

%changelog
%{?autochangelog}
