Summary:	LAL routines for inspiral and ringdown CBC gravitational wave data analysis
Summary(pl.UTF-8):	Procedury LAL do analizy danych fal grawitacyjnych układów podwójnych
Name:		lal-inspiral
Version:	5.0.0
Release:	3
Epoch:		1
License:	GPL v2
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/lalsuite/lalinspiral-%{version}.tar.xz
# Source0-md5:	a49538c22aaa7b6bc3ab3b763cabf5fb
Patch0:		%{name}-env.patch
Patch1:		no-Werror.patch
URL:		https://wiki.ligo.org/Computing/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gsl-devel >= 1.13
BuildRequires:	help2man >= 1.37
BuildRequires:	lal-devel >= 7.5.0
BuildRequires:	lal-burst-devel >= 2.0.0
BuildRequires:	lal-frame-devel >= 3.0.0
BuildRequires:	lal-metaio-devel >= 4.0.0
BuildRequires:	lal-simulation-devel >= 5.4.0
BuildRequires:	libframe-devel
BuildRequires:	libstdc++-devel
BuildRequires:	metaio-devel
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-numpy-devel >= 1:1.7
BuildRequires:	swig >= 4.1.0
BuildRequires:	swig-python >= 3.0.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gsl >= 1.13
Requires:	lal >= 7.5.0
Requires:	lal-burst >= 2.0.0
Requires:	lal-frame >= 3.0.0
Requires:	lal-metaio >= 4.0.0
Requires:	lal-simulation >= 5.4.0
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
Requires:	lal-devel >= 7.5.0
Requires:	lal-metaio-devel >= 4.0.0
Requires:	lal-simulation-devel >= 5.4.0
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
Requires:	octave-lal >= 7.5.0

%description -n octave-lalinspiral
Octave interface for LAL Inspiral.

%description -n octave-lalinspiral -l pl.UTF-8
Interfejs Octave do biblioteki LAL Inspiral.

%package -n python3-lalinspiral
Summary:	Python bindings for LAL Inspiral
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Inspiral
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python3-lal >= 7.5.0
Requires:	python3-lalsimulation >= 5.4.0
Requires:	python3-lscsoft-glue
Requires:	python3-modules >= 1:3.5
Requires:	python3-numpy >= 1:1.7
Requires:	python3-scipy
#Suggests:	python3-pycuda
Obsoletes:	python-lalinspiral < 1:2

%description -n python3-lalinspiral
Python bindings for LAL Inspiral.

%description -n python3-lalinspiral -l pl.UTF-8
Wiązania Pythona do biblioteki LAL Inspiral.

%prep
%setup -q -n lalinspiral-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python3} \
	--disable-silent-rules \
	--enable-swig

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/lalinspiral/_thinca.{a,la}
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
%attr(755,root,root) %ghost %{_libdir}/liblalinspiral.so.18
/etc/shrc.d/lalinspiral-user-env.csh
/etc/shrc.d/lalinspiral-user-env.fish
/etc/shrc.d/lalinspiral-user-env.sh
%{_mandir}/man1/lalinspiral_version.1*

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
%attr(755,root,root) %{_bindir}/lalinspiral_injfind
%attr(755,root,root) %{_bindir}/lalinspiral_thinca
%dir %{py3_sitedir}/lalinspiral
%attr(755,root,root) %{py3_sitedir}/lalinspiral/_lalinspiral.so
%attr(755,root,root) %{py3_sitedir}/lalinspiral/_thinca.so
%{py3_sitedir}/lalinspiral/*.py
%{py3_sitedir}/lalinspiral/__pycache__
%{_mandir}/man1/lalinspiral_injfind.1*
%{_mandir}/man1/lalinspiral_thinca.1*
