Summary:	LAM/MPI (Local Area Multicomputer) programming environment
Summary(es):	LAM MPI
Summary(pl):	¦rodowisko programistyczne LAM/MPI
Summary(pt_BR):	LAM MPI
Name:		lam
Version:	6.5.6
Release:	6
Epoch:		2
Vendor:		LAM/MPI Team
License:	BSD
Group:		Development/Libraries
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.lam-mpi.org/
BuildRequires:	autoconf
BuildRequires:	automake
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
message passing (currently, different RPMs are supplied for this --
see the main LAM web site for details).

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

%description -l es
LAM (Local Area Multicomputer) es un ambiente de desarrollo MPI para
computadores heterogéneos en una red. Con LAM, un cluster permanente o
una red ya existente pueden servir como un computador paralelo.

LAM tiene entre sus ventajas el soporte extensivo a la depuración
durante el ciclo de desarrollo de los aplicativos y un óptimo
desarrollo en el ambiente de ejecución. LAM implementa completamente
el patrón MPI.

%description -l pl
LAM (Local Area Multicomputer) jest ¶rodowiskiem programistycznym MPI
dla heterogenicznych komputerów w sieci. Z u¿yciem LAM/MPI dedykowany
klaster lub instniej±ca infrastruktura obliczaj±ca mo¿e siê zachowywaæ
jak pojedynczy, równoleg³y komputer. LAM/MPI jest uwa¿ana za
"przyjazne dla klastrów" - oferuje bazuj±c± na demonie kontrolê i
uruchamianie procesów oraz protoko³y szybkiego przesy³ania
komunikatów. LAM/MPI mo¿e u¿ywaæ TCP/IP lub dzielonej pamiêci do
przesy³ania komunikatów (aktualnie s³u¿± do tego ró¿ne pakiety).

Mo¿liwo¶ci LAM to pe³na implementacja MPI-1 (z wyj±tkiem tego, ¿e LAM
nie obs³uguje anulowania wysy³ania) i du¿ej czê¶ci MPI-2. Kompatybilne
aplikacje s± przeno¶ne na poziomie ¼róde³ pomiêdzy LAM/MPI i innymi
implementacjami standardu MPI. Oprócz implementacji standardu, LAM/MPI
oferuje rozszerzone mo¿liwo¶ci monitorowania na potrzeby
odpluskwiania. Monitorowanie wystêpuje na dwóch poziomach. Po
pierwsze, LAM/MPI pozwala na zrzut procesu i stanu komunikatu w
dowolnej chwili. Ten zrzut zawiera wszystko, co zwi±zane z
synchronizacj±, plus mapy/sygnatury typów danych, cz³onkowstwo w
grupach komunikacyjnych i zawarto¶ci komunikatów. Po drugie,
biblioteka MPI mo¿e zapisywaæ ca³± komunikacjê, która mo¿e byæ
wizualizowana na bie¿±co lub post-mortem.

%description -l pt_BR
LAM (Local Area Multicomputer) é um ambiente de desenvolvimento MPI
para computadores heterogêneos em uma rede. Com LAM, um cluster
dedicado ou uma rede já existentes podem servir como um computador
paralelo.

LAM tem como vantagens o suporte extensivo a depuração durante o ciclo
de desenvolvimento dos aplicativos e ótima performance em ambiente de
execução. LAM implementa totalmente o padrão MPI.

%prep
%setup -q

%build
chmod -R u+w .
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure \
	--without-fc \
	--with-rsh="%{_bindir}/ssh -x"
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -f $RPM_BUILD_ROOT/usr/include/mpi++.h
ln -sf mpi2c++/mpi++.h $RPM_BUILD_ROOT/usr/include/mpi++.h

gzip -9nf LICENSE HISTORY INSTALL README RELEASE_NOTES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc examples
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%{_includedir}/*
%{_libdir}/*
