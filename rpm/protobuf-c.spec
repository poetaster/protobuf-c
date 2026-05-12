Name:           protobuf-c
Version:        1.5.2
Release:        %autorelease
Summary:        C bindings for Google's Protocol Buffers
License:        BSD-2-Clause
URL:            https://github.com/protobuf-c/protobuf-c
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel

%description
This package provides a code generator and runtime libraries to use Protocol
Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%package -n protobuf-c
Summary:        C bindings for Google's Protocol Buffers
Group:          System/Libraries

%description -n protobuf-c
This package provides a code generator and runtime libraries to use Protocol
Buffers from pure C (not C++).

%package devel
Summary:        protobuf generator and headers
Group:          Development/Libraries/C and C++
Requires:       libprotobuf-c
Recommends:     (protobuf-devel >= 2.6.0 with protobuf-devel < 22)
Provides:       protobuf-c
Provides:       protobuf-c-devel

%description devel
This package provides a code generator and runtime libraries to use Protocol
Buffers from pure C (not C++).

%prep
%autosetup -p1

%build
%{!?make_build:%define make_build make -O %{?_smp_mflags} V=1 VERBOSE=1}
autoreconf -fvi
%configure \
    --enable-static=no

%make_build

%install
%make_install
rm %buildroot/%_libdir/*.la

%check
make check

%ldconfig_scriptlets -n libprotobuf-c

%files -n libprotobuf-c
%license LICENSE
%_libdir/libprotobuf-c.so
%_libdir/libprotobuf-c.so.*

%files devel
%license LICENSE
%dir %_includedir/protobuf-c
%dir %_includedir/google
%dir %_includedir/google/protobuf-c
%_includedir/protobuf-c/*
%_includedir/google/protobuf-c/protobuf-c.h
%_bindir/protoc-c
%_bindir/protoc-gen-c
%_libdir/libprotobuf-c.so
%_libdir/pkgconfig/libprotobuf-c.pc

%changelog
