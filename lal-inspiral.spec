Summary:	LAL routines for inspiral and ringdown CBC gravitational wave data analysis
Name:		lal-inspiral
Version:	1.0.0
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	https://www.lsc-group.phys.uwm.edu/daswg/download/software/source/lalsuite/lalinspiral-%{version}.tar.gz
# Source0-md5:	e3f22d1a0873b6d3c554e1591942a063
URL:		https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html
BuildRequires:	lal-metaio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL routines for inspiral and ringdown CBC gravitational wave data
analysis.

%package devel
Summary:	Header files for lal-inspiral library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lal-inspiral library.

%package static
Summary:	Static lal-inspiral library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lal-inspiral library.

%prep
%setup -q -n lalinspiral-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/shrc.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
/etc/shrc.d/lalinspiral-user-env*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/lal/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
