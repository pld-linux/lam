Summary:	LAM/MPI (Local Area Multicomputer) programming environment
Summary(es.UTF-8):	LAM MPI
Summary(pl.UTF-8):	Środowisko programistyczne LAM/MPI
Summary(pt_BR.UTF-8):	LAM MPI
Name:		lam
Version:	7.1.3
Release:	6
Epoch:		2
License:	BSD
Group:		Development/Libraries
Source0:	http://www.lam-mpi.org/download/files/%{name}-%{version}.tar.bz2
# Source0-md5:	dccca92409654f4f822b1d343ca75be6
Patch0:		%{name}-m4.patch
URL:		http://www.lam-mpi.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-fortran
BuildRequires:	libtool
Provides:	mpi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAM (Local Area Multicomputer) is an MPI programming environment and
development system for heterogeneous computers on a network. With
LAM/MPI, a dedicated cluster or an existing network computing
infrastructure can act as a single parallel computer. LAM/MPI is
considered to be "cluster friendly", in that it offers daemon-based
process startup/control as well as fast client-to-client message
passing protocols. LAM/MPI can use TCP/IP and/or shared memory for
message passing.

LAM features a full implementation of MPI-1 (with the exception that
LAM does not support cancelling of sends), and much of MPI-2.
Compliant applications are source code portable between LAM/MPI and
any other implementation of MPI. In addition to providing a
high-quality implementation of the MPI standard, LAM/MPI offers
extensive monitoring capabilities to support debugging. Monitoring
happens on two levels. First, LAM/MPI has the hooks to allow a
snapshot of process and message status to be taken at any time during
an application run. This snapshot includes all aspects of
synchronization plus datatype maps/signatures, communicator group
membership, and message contents (see the XMPI application on the main
LAM web site). On the second level, the MPI library is instrumented to
produce a cummulative record of communication, which can be visualized
either at runtime or post-mortem.

%description -l es.UTF-8
LAM (Local Area Multicomputer) es un ambiente de desarrollo MPI para
computadores heterogéneos en una red. Con LAM, un cluster permanente o
una red ya existente pueden servir como un computador paralelo.

LAM tiene entre sus ventajas el soporte extensivo a la depuración
durante el ciclo de desarrollo de los aplicativos y un óptimo
desarrollo en el ambiente de ejecución. LAM implementa completamente
el patrón MPI.

%description -l pl.UTF-8
LAM (Local Area Multicomputer) jest środowiskiem programistycznym MPI
dla heterogenicznych komputerów w sieci. Z użyciem LAM/MPI dedykowany
klaster lub istniejąca infrastruktura obliczająca może się zachowywać
jak pojedynczy, równoległy komputer. LAM/MPI jest uważana za
"przyjazne dla klastrów" - oferuje bazującą na demonie kontrolę i
uruchamianie procesów oraz protokoły szybkiego przesyłania
komunikatów. LAM/MPI może używać TCP/IP lub dzielonej pamięci do
przesyłania komunikatów.

Możliwości LAM to pełna implementacja MPI-1 (z wyjątkiem tego, że LAM
nie obsługuje anulowania wysyłania) i dużej części MPI-2. Kompatybilne
aplikacje są przenośne na poziomie źródeł pomiędzy LAM/MPI i innymi
implementacjami standardu MPI. Oprócz implementacji standardu, LAM/MPI
oferuje rozszerzone możliwości monitorowania na potrzeby
odpluskwiania. Monitorowanie występuje na dwóch poziomach. Po
pierwsze, LAM/MPI pozwala na zrzut procesu i stanu komunikatu w
dowolnej chwili. Ten zrzut zawiera wszystko, co związane z
synchronizacją, plus mapy/sygnatury typów danych, członkowstwo w
grupach komunikacyjnych i zawartości komunikatów. Po drugie,
biblioteka MPI może zapisywać całą komunikację, która może być
wizualizowana na bieżąco lub post-mortem.

%description -l pt_BR.UTF-8
LAM (Local Area Multicomputer) é um ambiente de desenvolvimento MPI
para computadores heterogêneos em uma rede. Com LAM, um cluster
dedicado ou uma rede já existentes podem servir como um computador
paralelo.

LAM tem como vantagens o suporte extensivo a depuração durante o ciclo
de desenvolvimento dos aplicativos e ótima performance em ambiente de
execução. LAM implementa totalmente o padrão MPI.

%prep
%setup -q
%patch0 -p1

# Rename the ROMIO doc files so that we can install them in the same
# doc root later, and not overwrite LAM's doc files.
for file in README README_LAM COPYRIGHT; do
	mv romio/$file romio/romio-$file
done
mv romio/doc/users-guide.ps.gz romio/doc/romio-users-guide.ps.gz

%build
chmod -R u+w .
touch config/lam_check_fd_setsize.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
for i in $(find -name config.sub); do
	cp -f /usr/share/automake/config.sub $i
done

%configure \
	--with-pic \
	--with-rpi \
	--with-rsh="%{_bindir}/ssh -x" \
	--with-fc=gfortran

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -snf mpi2c++/mpi++.h $RPM_BUILD_ROOT%{_includedir}/mpi++.h

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv $RPM_BUILD_ROOT%{_mandir}/man{s,7}/mpi.share*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE HISTORY INSTALL README
%doc doc/*.pdf romio/doc/* romio/romio-{README*,COPYRIGHT}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-bhost.def
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-conf.lamd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-helpfile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-hostmap.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-ssi-boot-globus-helpfile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-ssi-boot-slurm-helpfile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-ssi-crlam-self-helpfile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lam-ssi-crmpi-self-helpfile
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[1357]/*
%{_libdir}/liblam.a
%{_libdir}/liblamf77mpi.a
%{_libdir}/liblammpi++.a
%{_libdir}/libmpi.a
%{_libdir}/liblam.la
%{_libdir}/liblamf77mpi.la
%{_libdir}/liblammpi++.la
%{_libdir}/libmpi.la
# not libtool lib
%{_libdir}/liblammpio.a
%{_libdir}/lam
%{_includedir}/lam_config*.h
%{_includedir}/mpi*.h
%{_includedir}/mpi2cxx
%{_examplesdir}/%{name}-%{version}
