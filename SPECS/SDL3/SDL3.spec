# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond static 0

Name:           SDL3
Version:        3.3.2
Release:        %autorelease
Summary:        Cross-platform multimedia library
License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            https://github.com/libsdl-org/SDL
#!RemoteAsset
Source0:        https://www.libsdl.org/release/SDL3-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSDL_INSTALL_DOCS=OFF
BuildOption(conf):  -DSDL_DEPS_SHARED=ON
BuildOption(conf):  -DSDL_SSE3=OFF
BuildOption(conf):  -DSDL_RPATH=OFF
BuildOption(conf):  -DSDL_UNIX_CONSOLE_BUILD=ON

%if %{with static}
BuildOption(conf):  -DSDL_STATIC=ON
BuildOption(conf):  -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%else
BuildOption(conf):  -DSDL_STATIC=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device.

%package        devel
Summary:        Development files for SDL3
Requires:       %{name} = %{version}

%description devel
This package provides the libraries, include files, and other resources needed for
developing SDL applications.

%package        test
Summary:        Testing libraries for SDL3
Requires:       %{name}-devel = %{version}

%description    test
This package contains static testing libraries for SDL3.

%if %{with static}
%package        static
Summary:        Static libraries for SDL3
Requires:       %{name}-devel = %{version}

%description   static
Static libraries for SDL3.
%endif

%prep -a
sed -e 's/\r//g' -i README.md WhatsNew.txt BUGS.txt LICENSE.txt CREDITS.md

%files
%license LICENSE.txt
%doc BUGS.txt CREDITS.md README.md
%{_libdir}/libSDL3.so.0*

%files devel
%doc WhatsNew.txt
%{_libdir}/libSDL3.so
%{_libdir}/pkgconfig/sdl3.pc
%{_libdir}/cmake/SDL3/
%{_includedir}/SDL3/

%files test
%{_libdir}/libSDL3_test.a

%if %{with static}
%files static
%{_libdir}/libSDL3.a
%endif

%changelog
%{?autochangelog}
