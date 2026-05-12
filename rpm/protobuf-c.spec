Name:           protobuf-c
Version:        1.5.2
Release:        1
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

%package compiler

Summary:        Protocol Buffers C compiler

Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description compiler
This package contains a modified version of the Protocol Buffers
compiler for the C programming language called protoc-c.

%package devel
Summary:        Protocol Buffers C headers and libraries
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-compiler%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

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

%check
make check

%install
%make_install

rm %buildroot/%_libdir/*.la


%files compiler
%license LICENSE
%_libdir/libprotobuf-c.so
%_libdir/libprotobuf-c.so.*

%files devel
%license LICENSE
%dir %{_includedir}/google
%{_includedir}/%{name}/
%{_includedir}/google/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
