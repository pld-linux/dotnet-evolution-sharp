%include        /usr/lib/rpm/macros.mono
Summary:	Evolution# - .NET language bindings for Evolution
Summary(pl):	Evolution# - Wi±zania Evolution dla .NET
Name:		dotnet-evolution-sharp
Version:	0.10.2
Release:	3
License:	GPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-sharp/0.10/evolution-sharp-%{version}.tar.bz2
# Source0-md5:	66957006f02706490d244d4f01ec542d
Patch0:		%{name}-mint.patch
Patch1:		%{name}-monodir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.5
BuildRequires:	evolution-data-server-devel >= 1.4
BuildRequires:	evolution-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp2 >= 1.9.5
Requires:	evolution-data-server >= 1.4
Requires:	mono >= 1.1.7
Provides:	dotnet-evolution
Obsoletes:	dotnet-evolution
ExcludeArch:	i386 alpha sparc sparc64
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

%package static
Summary:        Static evolution-sharp libraries
Summary(pl):    Biblioteki statyczne evolution-sharp
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static evolution-sharp libraries.

%description static -l pl
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
