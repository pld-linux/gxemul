%define		realver	20040723
Summary:	MIPS machine emulator.
Name:		mips64emul
Version:	0.1.1.%realver
Release:	0.1
License:	BSD-like
Group:		Applications/Emulators
Source0:	http://www.mdstud.chalmers.se/~md1gavan/mips64emul/src/%{name}-%{realver}.tar.gz
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mips64emul is a MIPS machine emulator. The goals are to emulate
MIPS-like CPUs and enough surrounding hardware to fake real machines,
capable of running real (unmodified) operating systems (such as
NetBSD, Linux, or OpenBSD), and to assist in experimenting with MIPS
in general. This is a spare time hobby project, and many things are
not implemented yet. The emulator is written in C, does not depend on
any third-party libraries (except X11, which is optional), and should
compile and run on any Unix-like system.

%prep
%setup -q -n mips64emul-%{realver}

%build
./configure --mips16 --delays --caches
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}