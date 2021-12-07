Name:           p4c-lang
Summary:        A p4 compiler
Version:        1.2.2
Release:        1%{?dist}
License:        ASL 2.0
ExclusiveArch:  x86_64
URL:            https://p4.org/
Source0:        https://github.com/p4lang/p4c/archive/refs/tags/v%{version}.tar.gz
# The runtime
%define         rt_version 1.2.0
Source1:        https://github.com/p4lang/p4runtime/archive/refs/tags/v%{rt_version}.tar.gz

# protobuf changed enum element name
Patch1:         p4c-runtime-status-enum.patch

BuildRequires:  bison boost-devel boost-graph
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++ gmp-devel gtest-devel
BuildRequires:  libbpf-devel libgc-devel
BuildRequires:  protobuf-devel python3 python3-scapy python3-thrift p4-bmv2-devel

Requires:       boost
Requires:       protobuf python3

%description
%{name} is a reference compiler for the P4 programming language.
It supports both P4-14 and P4-16

%prep
%setup -q -c -n p4c-lang-%{version}
%setup -q -T -D -a 1 -n p4c-lang-%{version}
cp -r p4runtime-%{rt_version}/* p4c-%{version}/control-plane/p4runtime/
%patch1 -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DENABLE_GTESTS=OFF \
       -DENABLE_PROTOBUF_STATIC=OFF \
       p4c-%{version}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/p4*
%{_datadir}/p4c/*

%changelog
* Wed Nov 3 2021 <trix@redhat.com> - 1.2.2-1
- Initial release




