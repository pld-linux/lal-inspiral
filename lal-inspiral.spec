Summary:	LAL routines for inspiral and ringdown CBC gravitational wave data analysis
Name:		lal-inspiral
Version:	1.0.0.3
Release:	0.2
Epoch:		1
License:	GPL v2
Group:		Libraries
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	87b9e53659c570bb3488b8d30608b36e
Source1:	lalsuite_build.m4
Source2:	lalsuite_c99.m4
Source3:	lalsuite_gccflags.m4
Source4:	generate_vcs_info.py
Source5:	check_series_macros.h
URL:		https://www.lsc-group.phys.uwm.edu/daswg/projects/lalsuite.html
BuildRequires:	lal-metaio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL routines for inspiral and ringdown CBC gravitational wave data
analysis.

%package devel
Summary:	Header files for lal-inspiral library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for lal-inspiral library.

%package static
Summary:	Static lal-inspiral library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static lal-inspiral library.

%prep
%setup -q -n lalinspiral-%{version}
install %SOURCE1 %SOURCE2 %SOURCE3 gnuscripts
install %SOURCE4 %SOURCE5 src
rm gnuscripts/pkg.m4
cp %{_aclocaldir}/pkg.m4 gnuscripts

%build
%configure \
	CFLAGS="%{rpmcflags} \
	-w" \

%{__make} -w V=1

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
