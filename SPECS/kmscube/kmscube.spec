# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

# No release or tag,so we use the latest commit.
%global commit f60e50e887d3c49e91ac9b06d8199b36152632fa
%global commit_date 20251024
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           kmscube
Version:        %{commit_date}+git%{shortcommit}
Release:        %autorelease
Summary:        Example KMS/GBM/EGL application
License:        MIT
URL:            https://gitlab.freedesktop.org/mesa/kmscube/
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/mesa/kmscube/-/archive/%{commit}/kmscube-%{commit}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dgstreamer=disabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gbm)

%description
kmscube is a demonstration program for how to drive bare metal graphics
without a compositor like X11 or Wayland. It uses DRM/KMS, GBM and EGL
for rendering content using OpenGL ES.

%files
%license COPYING
%{_bindir}/kmscube
%{_bindir}/texturator

%changelog
%{?autochangelog}
