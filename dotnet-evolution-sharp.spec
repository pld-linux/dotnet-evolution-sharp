Summary:	.NET language bindings for Evolution
Summary(pl):	Wi±zania Evolution dla .NET
Name:		evolution-sharp
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	90ec5b8df09b7303608d725968f5ee64
BuildRequires:	autoconf
Buildrequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	gtk-sharp-devel >= 0.16-2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Evolution libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z Evolution.

%package devel
Summary:	Development part of evolution-sharp
Summary(pl):	Programistyczna czê¶æ evolution-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Tools for developing applications using evolution-sharp.

%description devel -l pl
Narzêdzia potrzebne przy tworzeniu aplikacji korzystaj±cych z
evolution-sharp.

%prep
%setup -q

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
%{_libdir}/*.dll

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
%{_datadir}/gapi/*
