Summary:	LAL routines for inspiral and ringdown CBC gravitational wave data analysis
Summary(pl.UTF-8):	Procedury LAL do analizy danych fal grawitacyjnych układów podwójnych
Name:		lal-inspiral
Version:	2.0.3
Release:	2
Epoch:		1
License:	GPL v2
Group:		Libraries
Source0:	http://software.ligo.org/lscsoft/source/lalsuite/lalinspiral-%{version}.tar.xz
# Source0-md5:	4de85003454f6bfab3fe8b9a47ec627d
Patch0:		%{name}-env.patch
Patch1:		no-Werror.patch
URL:		https://wiki.ligo.org/DASWG/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gsl-devel >= 1.13
BuildRequires:	lal-devel >= 6.18.0
BuildRequires:	lal-burst-devel
BuildRequires:	lal-frame-devel >= 1.4.3
BuildRequires:	lal-metaio-devel >= 1.3.1
BuildRequires:	lal-simulation-devel >= 1.7.0
BuildRequires:	libframe-devel
BuildRequires:	libstdc++-devel
BuildRequires:	metaio-devel
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	python3-numpy-devel
BuildRequires:	swig >= 3.0.12
BuildRequires:	swig-python >= 2.0.12
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gsl >= 1.13
Requires:	lal >= 6.18.0
Requires:	lal-frame >= 1.4.3
Requires:	lal-metaio >= 1.3.1
Requires:	lal-simulation >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL routines for inspiral and ringdown CBC gravitational wave data
analysis.

%description -l pl.UTF-8
Procedury LAL do analizy danych fal grawitacyjnych układów podwójnych.

%package devel
Summary:	Header files for lal-inspiral library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lal-inspiral
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gsl-devel >= 1.13
Requires:	lal-devel >= 6.18.0
Requires:	lal-metaio-devel >= 1.3.1
Requires:	lal-simulation-devel >= 1.7.0
Requires:	metaio-devel

%description devel
Header files for lal-inspiral library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lal-inspiral.

%package static
Summary:	Static lal-inspiral library
Summary(pl.UTF-8):	Statyczna biblioteka lal-inspiral
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static lal-inspiral library.

%description static -l pl.UTF-8
Statyczna biblioteka lal-inspiral.

%package -n octave-lalinspiral
Summary:	Octave interface for LAL Inspiral
Summary(pl.UTF-8):	Interfejs Octave do biblioteki LAL Inspiral
Group:		Applications/Math
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	octave-lal >= 6.18.0

%description -n octave-lalinspiral
Octave interface for LAL Inspiral.

%description -n octave-lalinspiral -l pl.UTF-8
Interfejs Octave do biblioteki LAL Inspiral.

%package -n python3-lalinspiral
Summary:	Python bindings for LAL Inspiral
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Inspiral
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python3-lal >= 6.18.0
Requires:	python3-lalsimulation >= 1.7.0
Requires:	python3-modules >= 1:2.6
Requires:	python3-numpy
Requires:	python3-scipy
#python3-glue (glue.iterutils, glue.ligolw)
#Suggests:	python3-pycuda

%description -n python3-lalinspiral
Python bindings for LAL Inspiral.

%description -n python3-lalinspiral -l pl.UTF-8
Wiązania Pythona do biblioteki LAL Inspiral.

%prep
%setup -q -n lalinspiral-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-swig

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblalinspiral.la

install -d $RPM_BUILD_ROOT/etc/shrc.d
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lalinspiral_version
%attr(755,root,root) %{_libdir}/liblalinspiral.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalinspiral.so.16
/etc/shrc.d/lalinspiral-user-env.csh
/etc/shrc.d/lalinspiral-user-env.fish
/etc/shrc.d/lalinspiral-user-env.sh

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalinspiral.so
%{_includedir}/lal/BBHPhenomCoeffs.h
%{_includedir}/lal/CoincInspiralEllipsoid.h
%{_includedir}/lal/FindChirp*.h
%{_includedir}/lal/GenerateInspRing.h
%{_includedir}/lal/GenerateInspiral.h
%{_includedir}/lal/GeneratePPNInspiral.h
%{_includedir}/lal/InspiralInjectionParams.h
%{_includedir}/lal/LALEOBNRv2Waveform.h
%{_includedir}/lal/LALInspiral*.h
%{_includedir}/lal/LALNoiseModelsInspiral.h
%{_includedir}/lal/LALSQTPN*.h
%{_includedir}/lal/LALSTPNWaveform*.h
%{_includedir}/lal/LALTrigScanCluster.h
%{_includedir}/lal/LIGOLwXMLInspiralRead.h
%{_includedir}/lal/LIGOLwXMLRingdownRead.h
%{_includedir}/lal/LIGOMetadataInspiralUtils.h
%{_includedir}/lal/LIGOMetadataRingdownUtils.h
%{_includedir}/lal/NRWaveIO.h
%{_includedir}/lal/NRWaveInject.h
%{_includedir}/lal/RingUtils.h
%{_includedir}/lal/SWIGLALInspiralTest.h
%{_includedir}/lal/SWIGLALInspiral*.i
%{_includedir}/lal/TemplateBankGeneration.h
%{_includedir}/lal/TrigScanEThincaCommon.h
%{_includedir}/lal/swiglalinspiral.i
%{_pkgconfigdir}/lalinspiral.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblalinspiral.a

%files -n octave-lalinspiral
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/lalinspiral.oct

%files -n python3-lalinspiral
%defattr(644,root,root,755)
%dir %{py3_sitedir}/lalinspiral
%attr(755,root,root) %{py3_sitedir}/lalinspiral/_lalinspiral.so
%attr(755,root,root) %{py3_sitedir}/lalinspiral/_thinca.so
%{py3_sitedir}/lalinspiral/*.py
%{py3_sitedir}/lalinspiral/__pycache__
%dir %{py3_sitedir}/lalinspiral/sbank
%{py3_sitedir}/lalinspiral/sbank/*.py
%{py3_sitedir}/lalinspiral/sbank/__pycache__
