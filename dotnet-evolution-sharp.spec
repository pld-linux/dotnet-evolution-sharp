Summary:	Evolution# - .NET language bindings for Evolution
Summary(pl):	Evolution# - Wi±zania Evolution dla .NET
Name:		dotnet-evolution-sharp
Version:	0.3
Release:	3
License:	GPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-sharp/0.3/evolution-sharp-%{version}.tar.bz2
# Source0-md5:	3e2a5ee5a17e6d96b2fbf416894d82f3
Patch0:		%{name}-mint.patch
Patch1:		%{name}-libebook.patch
Obsoletes:	dotnet-evolution
Provides:	dotnet-evolution
BuildRequires:	autoconf
Buildrequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	dotnet-gtk-sharp-devel >= 0.93
BuildRequires:	pkgconfig
Requires:	evolution-data-server
Requires:	dotnet-gtk-sharp
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Evolution libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z Evolution.

%package devel
Summary:	Development part of Evolution#
Summary(pl):	Programistyczna czê¶æ Evolution#
Obsoletes:	dotnet-evolution-devel
Provides:	dotnet-evolution-devel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Tools for developing applications using evolution-sharp.

%description devel -l pl
Narzêdzia potrzebne przy tworzeniu aplikacji korzystaj±cych z
evolution-sharp.

%prep
%setup -q -n evolution-sharp-%{version}
%patch0 -p1
%patch1 -p1

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
