Summary:	Evolution# - .NET language bindings for Evolution
Summary(pl):	Evolution# - Wi±zania Evolution dla .NET
Name:		dotnet-evolution-sharp
Version:	0.4
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-sharp/0.4/evolution-sharp-%{version}.tar.bz2
# Source0-md5:	cc4f968f1d6d9ca81638ecb8cbd884e0
Patch0:		%{name}-mint.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	evolution-data-server-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp
Requires:	evolution-data-server
Provides:	dotnet-evolution
Obsoletes:	dotnet-evolution
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Evolution libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z Evolution.

%package devel
Summary:	Development part of Evolution#
Summary(pl):	Programistyczna czê¶æ Evolution#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	dotnet-evolution-devel
Obsoletes:	dotnet-evolution-devel

%description devel
Tools for developing applications using evolution-sharp.

%description devel -l pl
Narzêdzia potrzebne przy tworzeniu aplikacji korzystaj±cych z
evolution-sharp.

%prep
%setup -q -n evolution-sharp-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_libdir}/mono/gac/evolution-sharp

%files devel
%defattr(644,root,root,755)
%{_libdir}/mono/evolution-sharp
%{_pkgconfigdir}/*.pc
%{_datadir}/gapi/*
