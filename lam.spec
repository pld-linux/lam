Summary:	LAM/MPI (Local Area Multicomputer) programming environment
Summary(es):	LAM MPI
Summary(pl):	�rodowisko programistyczne LAM/MPI
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
computadores heterog�neos en una red. Con LAM, un cluster permanente o
una red ya existente pueden servir como un computador paralelo.

LAM tiene entre sus ventajas el soporte extensivo a la depuraci�n
durante el ciclo de desarrollo de los aplicativos y un �ptimo
desarrollo en el ambiente de ejecuci�n. LAM implementa completamente
el patr�n MPI.

%description -l pl
LAM (Local Area Multicomputer) jest �rodowiskiem programistycznym MPI
dla heterogenicznych komputer�w w sieci. Z u�yciem LAM/MPI dedykowany
klaster lub instniej�ca infrastruktura obliczaj�ca mo�e si� zachowywa�
jak pojedynczy, r�wnoleg�y komputer. LAM/MPI jest uwa�ana za
"przyjazne dla klastr�w" - oferuje bazuj�c� na demonie kontrol� i
uruchamianie proces�w oraz protoko�y szybkiego przesy�ania
komunikat�w. LAM/MPI mo�e u�ywa� TCP/IP lub dzielonej pami�ci do
przesy�ania komunikat�w (aktualnie s�u�� do tego r�ne pakiety).

Mo�liwo�ci LAM to pe�na implementacja MPI-1 (z wyj�tkiem tego, �e LAM
nie obs�uguje anulowania wysy�ania) i du�ej cz�ci MPI-2. Kompatybilne
aplikacje s� przeno�ne na poziomie �r�de� pomi�dzy LAM/MPI i innymi
implementacjami standardu MPI. Opr�cz implementacji standardu, LAM/MPI
oferuje rozszerzone mo�liwo�ci monitorowania na potrzeby
odpluskwiania. Monitorowanie wyst�puje na dw�ch poziomach. Po
pierwsze, LAM/MPI pozwala na zrzut procesu i stanu komunikatu w
dowolnej chwili. Ten zrzut zawiera wszystko, co zwi�zane z
synchronizacj�, plus mapy/sygnatury typ�w danych, cz�onkowstwo w
grupach komunikacyjnych i zawarto�ci komunikat�w. Po drugie,
biblioteka MPI mo�e zapisywa� ca�� komunikacj�, kt�ra mo�e by�
wizualizowana na bie��co lub post-mortem.

%description -l pt_BR
LAM (Local Area Multicomputer) � um ambiente de desenvolvimento MPI
para computadores heterog�neos em uma rede. Com LAM, um cluster
dedicado ou uma rede j� existentes podem servir como um computador
paralelo.

LAM tem como vantagens o suporte extensivo a depura��o durante o ciclo
de desenvolvimento dos aplicativos e �tima performance em ambiente de
execu��o. LAM implementa totalmente o padr�o MPI.

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
