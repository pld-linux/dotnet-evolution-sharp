Summary:	Evolution# - .NET language bindings for Evolution
Summary(pl):	Evolution# - Wi±zania Evolution dla .NET
Name:		dotnet-evolution-sharp
Version:	0.6
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-sharp/0.6/evolution-sharp-%{version}.tar.bz2
# Source0-md5:	b99e0d8ed2ba352802649c213b5ab32e
Patch0:		%{name}-mint.patch
BuildRequires:	autoconf
BuildRequires:	automake
# just gtk-sharp
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	evolution-data-server-devel >= 1.2
# (optionally) gtkhtml-devel >= 3.0 < 3.2 (it tries to use 3.0 or 3.1, but not 3.6)
BuildRequires:	mono-csharp >= 0.91
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp >= 1.0
Requires:	evolution-data-server >= 1.2
Requires:	mono >= 0.91
Provides:	dotnet-evolution
Obsoletes:	dotnet-evolution
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
Requires:	dotnet-gtk-sharp-devel >= 1.0
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
