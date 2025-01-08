#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: f9eab48
#
Name     : qcoro6
Version  : 0.10.0
Release  : 4
URL      : https://github.com/danvratil/qcoro/archive/v0.10.0/qcoro-0.10.0.tar.gz
Source0  : https://github.com/danvratil/qcoro/archive/v0.10.0/qcoro-0.10.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 MIT
Requires: qcoro6-lib = %{version}-%{release}
Requires: qcoro6-license = %{version}-%{release}
BuildRequires : Vulkan-Headers
BuildRequires : Vulkan-Tools
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : buildreq-qt6
BuildRequires : glibc-dev
BuildRequires : libxkbcommon-dev
BuildRequires : libxkbfile-dev
BuildRequires : qt6base-dev
BuildRequires : qt6websockets-dev
BuildRequires : qtbase-dev
BuildRequires : qttools
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Linux CI](https://github.com/danvratil/qcoro/actions/workflows/build-linux.yml/badge.svg)](https://github.com/danvratil/qcoro/actions/workflows/build-linux.yml)
[![Windows CI](https://github.com/danvratil/qcoro/actions/workflows/build-windows.yml/badge.svg)](https://github.com/danvratil/qcoro/actions/workflows/build-windows.yml)
[![MacOS CI](https://github.com/danvratil/qcoro/actions/workflows/build-macos.yml/badge.svg)](https://github.com/danvratil/qcoro/actions/workflows/build-macos.yml)
[![Docs build](https://github.com/danvratil/qcoro/actions/workflows/update-docs.yml/badge.svg?branch=main)](https://github.com/danvratil/qcoro/actions/workflows/update-docs.yml)
[![Latest release](https://img.shields.io/github/v/release/danvratil/qcoro?label=%F0%9F%93%A6%20Release)](https://github.com/danvratil/qcoro/releases)
![License: MIT](https://img.shields.io/badge/%E2%9A%96%EF%B8%8F%20License-MIT-brightgreen)
![C++20](https://img.shields.io/badge/C%2B%2B-20-%2300599C?logo=cplusplus)
![Supported Compilers](https://img.shields.io/badge/%E2%9A%99%EF%B8%8F%20Compilers-GCC%2C%20clang%2C%20MSVC-informational)

%package dev
Summary: dev components for the qcoro6 package.
Group: Development
Requires: qcoro6-lib = %{version}-%{release}
Provides: qcoro6-devel = %{version}-%{release}
Requires: qcoro6 = %{version}-%{release}

%description dev
dev components for the qcoro6 package.


%package lib
Summary: lib components for the qcoro6 package.
Group: Libraries
Requires: qcoro6-license = %{version}-%{release}

%description lib
lib components for the qcoro6 package.


%package license
Summary: license components for the qcoro6 package.
Group: Default

%description license
license components for the qcoro6 package.


%prep
%setup -q -n qcoro-0.10.0
cd %{_builddir}/qcoro-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718900470
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DUSE_QT_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DUSE_QT_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718900470
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qcoro6
cp %{_builddir}/qcoro-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qcoro6/7e78f78b7c473b6e330b02213c0a45f3d85a1d98 || :
cp %{_builddir}/qcoro-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qcoro6/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/qcoro-%{version}/LICENSES/GFDL-1.3-or-later.txt %{buildroot}/usr/share/package-licenses/qcoro6/9f4b4e87b606c795e2ff126522fec25546fb335f || :
cp %{_builddir}/qcoro-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/qcoro6/347ce7df3437ef947fc76d294e461f2d7af1ad2a || :
cp %{_builddir}/qcoro-%{version}/docs/about/license.md %{buildroot}/usr/share/package-licenses/qcoro6/c225c3c4debd821182d34d51796e174cf3ea54fd || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qcoro6/QCoro/QCoro
/usr/include/qcoro6/QCoro/QCoroAbstractSocket
/usr/include/qcoro6/QCoro/QCoroAsyncGenerator
/usr/include/qcoro6/QCoro/QCoroCore
/usr/include/qcoro6/QCoro/QCoroDBus
/usr/include/qcoro6/QCoro/QCoroDBusPendingCall
/usr/include/qcoro6/QCoro/QCoroDBusPendingReply
/usr/include/qcoro6/QCoro/QCoroFuture
/usr/include/qcoro6/QCoro/QCoroFwd
/usr/include/qcoro6/QCoro/QCoroGenerator
/usr/include/qcoro6/QCoro/QCoroIODevice
/usr/include/qcoro6/QCoro/QCoroImageProvider
/usr/include/qcoro6/QCoro/QCoroLocalSocket
/usr/include/qcoro6/QCoro/QCoroNetwork
/usr/include/qcoro6/QCoro/QCoroNetworkReply
/usr/include/qcoro6/QCoro/QCoroProcess
/usr/include/qcoro6/QCoro/QCoroQml
/usr/include/qcoro6/QCoro/QCoroQmlTask
/usr/include/qcoro6/QCoro/QCoroSignal
/usr/include/qcoro6/QCoro/QCoroTask
/usr/include/qcoro6/QCoro/QCoroTcpServer
/usr/include/qcoro6/QCoro/QCoroTest
/usr/include/qcoro6/QCoro/QCoroThread
/usr/include/qcoro6/QCoro/QCoroTimer
/usr/include/qcoro6/QCoro/QCoroWebSocket
/usr/include/qcoro6/QCoro/QCoroWebSocketServer
/usr/include/qcoro6/QCoro/QCoroWebSockets
/usr/include/qcoro6/QCoro/Task
/usr/include/qcoro6/qcoro/concepts_p.h
/usr/include/qcoro6/qcoro/config.h
/usr/include/qcoro6/qcoro/coroutine.h
/usr/include/qcoro6/qcoro/impl/connect.h
/usr/include/qcoro6/qcoro/impl/isqprivatesignal.h
/usr/include/qcoro6/qcoro/impl/task.h
/usr/include/qcoro6/qcoro/impl/taskawaiterbase.h
/usr/include/qcoro6/qcoro/impl/taskfinalsuspend.h
/usr/include/qcoro6/qcoro/impl/taskpromise.h
/usr/include/qcoro6/qcoro/impl/taskpromisebase.h
/usr/include/qcoro6/qcoro/impl/waitfor.h
/usr/include/qcoro6/qcoro/macros_p.h
/usr/include/qcoro6/qcoro/qcoro.h
/usr/include/qcoro6/qcoro/qcoroabstractsocket.h
/usr/include/qcoro6/qcoro/qcoroasyncgenerator.h
/usr/include/qcoro6/qcoro/qcorocore.h
/usr/include/qcoro6/qcoro/qcorocore_export.h
/usr/include/qcoro6/qcoro/qcorodbus.h
/usr/include/qcoro6/qcoro/qcorodbus_export.h
/usr/include/qcoro6/qcoro/qcorodbuspendingcall.h
/usr/include/qcoro6/qcoro/qcorodbuspendingreply.h
/usr/include/qcoro6/qcoro/qcorofuture.h
/usr/include/qcoro6/qcoro/qcorofwd.h
/usr/include/qcoro6/qcoro/qcorogenerator.h
/usr/include/qcoro6/qcoro/qcoroimageprovider.h
/usr/include/qcoro6/qcoro/qcoroiodevice.h
/usr/include/qcoro6/qcoro/qcorolocalsocket.h
/usr/include/qcoro6/qcoro/qcoronetwork.h
/usr/include/qcoro6/qcoro/qcoronetwork_export.h
/usr/include/qcoro6/qcoro/qcoronetworkreply.h
/usr/include/qcoro6/qcoro/qcoroprocess.h
/usr/include/qcoro6/qcoro/qcoroqml.h
/usr/include/qcoro6/qcoro/qcoroqml_export.h
/usr/include/qcoro6/qcoro/qcoroqmltask.h
/usr/include/qcoro6/qcoro/qcoroquick_export.h
/usr/include/qcoro6/qcoro/qcorosignal.h
/usr/include/qcoro6/qcoro/qcorotask.h
/usr/include/qcoro6/qcoro/qcorotcpserver.h
/usr/include/qcoro6/qcoro/qcorotest.h
/usr/include/qcoro6/qcoro/qcorothread.h
/usr/include/qcoro6/qcoro/qcorotimer.h
/usr/include/qcoro6/qcoro/qcorowebsocket.h
/usr/include/qcoro6/qcoro/qcorowebsockets.h
/usr/include/qcoro6/qcoro/qcorowebsockets_export.h
/usr/include/qcoro6/qcoro/qcorowebsocketserver.h
/usr/include/qcoro6/qcoro/task.h
/usr/include/qcoro6/qcoro/waitoperationbase_p.h
/usr/lib64/cmake/QCoro6/QCoro6Config.cmake
/usr/lib64/cmake/QCoro6/QCoro6ConfigVersion.cmake
/usr/lib64/cmake/QCoro6Core/QCoro6CoreConfig.cmake
/usr/lib64/cmake/QCoro6Core/QCoro6CoreConfigVersion.cmake
/usr/lib64/cmake/QCoro6Core/QCoro6CoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro6Core/QCoro6CoreTargets.cmake
/usr/lib64/cmake/QCoro6Coro/QCoro6CoroConfig.cmake
/usr/lib64/cmake/QCoro6Coro/QCoro6CoroConfigVersion.cmake
/usr/lib64/cmake/QCoro6Coro/QCoro6CoroTargets.cmake
/usr/lib64/cmake/QCoro6Coro/QCoroMacros.cmake
/usr/lib64/cmake/QCoro6DBus/QCoro6DBusConfig.cmake
/usr/lib64/cmake/QCoro6DBus/QCoro6DBusConfigVersion.cmake
/usr/lib64/cmake/QCoro6DBus/QCoro6DBusTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro6DBus/QCoro6DBusTargets.cmake
/usr/lib64/cmake/QCoro6Network/QCoro6NetworkConfig.cmake
/usr/lib64/cmake/QCoro6Network/QCoro6NetworkConfigVersion.cmake
/usr/lib64/cmake/QCoro6Network/QCoro6NetworkTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro6Network/QCoro6NetworkTargets.cmake
/usr/lib64/cmake/QCoro6Qml/QCoro6QmlConfig.cmake
/usr/lib64/cmake/QCoro6Qml/QCoro6QmlConfigVersion.cmake
/usr/lib64/cmake/QCoro6Qml/QCoro6QmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro6Qml/QCoro6QmlTargets.cmake
/usr/lib64/cmake/QCoro6Quick/QCoro6QuickConfig.cmake
/usr/lib64/cmake/QCoro6Quick/QCoro6QuickConfigVersion.cmake
/usr/lib64/cmake/QCoro6Quick/QCoro6QuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro6Quick/QCoro6QuickTargets.cmake
/usr/lib64/cmake/QCoro6Test/QCoro6TestConfig.cmake
/usr/lib64/cmake/QCoro6Test/QCoro6TestConfigVersion.cmake
/usr/lib64/cmake/QCoro6Test/QCoro6TestTargets.cmake
/usr/lib64/cmake/QCoro6WebSockets/QCoro6WebSocketsConfig.cmake
/usr/lib64/cmake/QCoro6WebSockets/QCoro6WebSocketsConfigVersion.cmake
/usr/lib64/cmake/QCoro6WebSockets/QCoro6WebSocketsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QCoro6WebSockets/QCoro6WebSocketsTargets.cmake
/usr/lib64/libQCoro6Core.so
/usr/lib64/libQCoro6DBus.so
/usr/lib64/libQCoro6Network.so
/usr/lib64/libQCoro6Qml.so
/usr/lib64/libQCoro6Quick.so
/usr/lib64/libQCoro6WebSockets.so
/usr/lib64/qt6/mkspecs/modules/qt_QCoroCore.pri
/usr/lib64/qt6/mkspecs/modules/qt_QCoroCoro.pri
/usr/lib64/qt6/mkspecs/modules/qt_QCoroDBus.pri
/usr/lib64/qt6/mkspecs/modules/qt_QCoroNetwork.pri
/usr/lib64/qt6/mkspecs/modules/qt_QCoroQml.pri
/usr/lib64/qt6/mkspecs/modules/qt_QCoroQuick.pri
/usr/lib64/qt6/mkspecs/modules/qt_QCoroTest.pri
/usr/lib64/qt6/mkspecs/modules/qt_QCoroWebSockets.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQCoro6Core.so.0.10.0
/V3/usr/lib64/libQCoro6DBus.so.0.10.0
/V3/usr/lib64/libQCoro6Network.so.0.10.0
/V3/usr/lib64/libQCoro6Qml.so.0.10.0
/V3/usr/lib64/libQCoro6Quick.so.0.10.0
/V3/usr/lib64/libQCoro6WebSockets.so.0.10.0
/usr/lib64/libQCoro6Core.so.0
/usr/lib64/libQCoro6Core.so.0.10.0
/usr/lib64/libQCoro6DBus.so.0
/usr/lib64/libQCoro6DBus.so.0.10.0
/usr/lib64/libQCoro6Network.so.0
/usr/lib64/libQCoro6Network.so.0.10.0
/usr/lib64/libQCoro6Qml.so.0
/usr/lib64/libQCoro6Qml.so.0.10.0
/usr/lib64/libQCoro6Quick.so.0
/usr/lib64/libQCoro6Quick.so.0.10.0
/usr/lib64/libQCoro6WebSockets.so.0
/usr/lib64/libQCoro6WebSockets.so.0.10.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qcoro6/347ce7df3437ef947fc76d294e461f2d7af1ad2a
/usr/share/package-licenses/qcoro6/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/qcoro6/7e78f78b7c473b6e330b02213c0a45f3d85a1d98
/usr/share/package-licenses/qcoro6/9f4b4e87b606c795e2ff126522fec25546fb335f
/usr/share/package-licenses/qcoro6/c225c3c4debd821182d34d51796e174cf3ea54fd
