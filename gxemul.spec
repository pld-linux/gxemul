Summary:	MIPS machine emulator
Summary(pl.UTF-8):	Emulator maszyn MIPS
Name:		gxemul
Version:	0.3.4
Release:	0.1
License:	BSD-like
Group:		Applications/Emulators
Source0:	http://gavare.se/gxemul/src/%{name}-%{version}.tar.gz
# Source0-md5:	dbf7ef59d2bb8f1e3082d0fa5fb434af
URL:		http://gavare.se/gxemul/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gxemul is a MIPS machine emulator. The goals are to emulate MIPS-like
CPUs and enough surrounding hardware to fake real machines, capable of
running real (unmodified) operating systems (such as NetBSD, Linux, or
OpenBSD), and to assist in experimenting with MIPS in general. This is
a spare time hobby project, and many things are not implemented yet.
The emulator is written in C, does not depend on any third-party
libraries (except X11, which is optional), and should compile and run
on any Unix-like system.

%description -l pl.UTF-8
Gxemul to emulator maszyn MIPS. Celem jest emulowanie procesorów MIPS
i wystarczającej ilości otaczającego je sprzętu, aby udawały prawdziwe
maszyny, na których mogą działać prawdziwe (nie zmodyfikowane) systemy
operacyjne (takie jak NetBSD, Linux czy OpenBSD) oraz pomoc przy
eksperymentowaniu z architekturą MIPS. Jest to projekt rozwijany jako
hobby w wolnym czasie i wiele rzeczy nie jest jeszcze
zaimplementowane. Emulator jest pisany w C, nie zależy od żadnych
zewnętrznych bibliotek (z wyjątkiem opcjonalnych X11) i powinien
kompilować się i działać na dowolnym systemie uniksowym.

%prep
%setup -q

%build
./configure \
	--enable-delays \
	--enable-caches
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS HISTORY RELEASE TODO
%attr(755,root,root) %{_bindir}/*
