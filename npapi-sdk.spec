Name:		npapi-sdk
License:	MPL-1.1 or GPL-2.0+ or LGPL-2.1+
Version:	0.27
Release:	7
Summary:	Netscape Plugin API (NPAPI)
Url:		https://wiki.mozilla.org/NPAPI
Group:		System/Libraries
Source0:	npapi-sdk-%{version}.tar.bz2
Source1:	npapi-sdk.pc.in
Source2:	npapi-sdk.rpmlintrc
Provides:	npapi-devel
BuildArch:      noarch

%description
This package provides the header and development files to create
NPAPI browser plugins.

%prep
%setup -qn npapi-sdk

%build
echo "empty"

%install
mkdir -p %{buildroot}%{_datadir}/pkgconfig
mkdir -p %{buildroot}%{_includedir}/npapi
cp headers/*.h %{buildroot}%{_includedir}/npapi/
sed "s:%%VERSION%%:%{version}:g" \
  %{SOURCE1} > %{buildroot}%{_datadir}/pkgconfig/npapi-sdk.pc

%files
%{_includedir}/npapi/
%{_datadir}/pkgconfig/*
