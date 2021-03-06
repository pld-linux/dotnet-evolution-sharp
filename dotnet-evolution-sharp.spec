#
#
Summary:	Evolution# - .NET language bindings for Evolution
Summary(pl.UTF-8):	Evolution# - Wiązania Evolution dla .NET
Name:		dotnet-evolution-sharp
Version:	0.20.0
Release:	7
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-sharp/0.20/evolution-sharp-%{version}.tar.bz2
# Source0-md5:	ca4f75a795aa2af36c4573971c0534f7
Patch0:		%{name}-mint.patch
Patch1:		evolution-data-server-228.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.2
BuildRequires:	evolution-data-server-devel >= 2.24.0
BuildRequires:	libgdata-devel
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
Requires:	evolution-data-server-libs >= 2.24.0
Requires:	mono >= 1.1.16.1
Provides:	dotnet-evolution
Obsoletes:	dotnet-evolution
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Evolution libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek z Evolution.

%package devel
Summary:	Development part of Evolution#
Summary(pl.UTF-8):	Programistyczna część Evolution#
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.10.2
Provides:	dotnet-evolution-devel
Obsoletes:	dotnet-evolution-devel

%description devel
Tools for developing applications using evolution-sharp.

%description devel -l pl.UTF-8
Narzędzia potrzebne przy tworzeniu aplikacji korzystających z
evolution-sharp.

%package static
Summary:	Static evolution-sharp libraries
Summary(pl.UTF-8):	Biblioteki statyczne evolution-sharp
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static evolution-sharp libraries.

%description static -l pl.UTF-8
Biblioteki statyczne evolution-sharp.

%prep
%setup -q -n evolution-sharp-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%attr(755,root,root) %{_libdir}/libevolutionglue.so
%{_libdir}/libevolutionglue.la
%{_prefix}/lib/mono/gac/evolution-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/evolution-sharp
%{_datadir}/gapi-2.0/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libevolutionglue.a
