Summary:	LAM/MPI (Local Area Multicomputer) programming environment
Name:		lam
Version:	6.5.6
Release:	1 
Vendor:		LAM/MPI Team
License:	BSD
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.lam-mpi.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Epoch:		2
Provides:	mpi
BuildRequires:	rsh

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

%prep
%setup -q

%build
aclocal
autoconf
%configure --without-fc
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -f $RPM_BUILD_ROOT/usr/include/mpi++.h
ln -s mpi2c++/mpi++.h $RPM_BUILD_ROOT/usr/include/mpi++.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE HISTORY INSTALL README RELEASE_NOTES 
%doc examples
%config %{_sysconfdir}
%{_bindir}/*
%{_mandir}/*/*
%{_includedir}/*
%{_libdir}/*
