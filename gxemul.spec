%define		realver	20040723
Summary:	MIPS machine emulator
Summary(pl):	Emulator maszyn MIPS
Name:		mips64emul
Version:	0.1.1.%{realver}
Release:	0.1
License:	BSD-like
Group:		Applications/Emulators
Source0:	http://www.mdstud.chalmers.se/~md1gavan/mips64emul/src/%{name}-%{realver}.tar.gz
# Source0-md5:	5dbe555130c0abde4f8e8b7f157c95d2
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

%description -l pl
mips64emul to emulator maszyn MIPS. Celem jest emulowanie procesorów
MIPS i wystarczaj±cej ilo¶ci otaczaj±cego je sprzêtu, aby udawa³y
prawdziwe maszyny, na których mog± dzia³aæ prawdziwe (nie
zmodyfikowane) systemy operacyjne (takie jak NetBSD, Linux czy
OpenBSD) oraz pomoc przy eksperymentowaniu z architektur± MIPS. Jest
to projekt rozwijany jako hobby w wolnym czasie i wiele rzeczy nie
jest jeszcze zaimplementowane. Emulator jest pisany w C, nie zale¿y od
¿adnych zewnêtrznych bibliotek (z wyj±tkiem opcjonalnych X11) i
powinien kompilowaæ siê i dzia³aæ na dowolnym systemie uniksowym.

%prep
%setup -q -n %{name}-%{realver}

%build
./configure \
	--mips16 \
	--delays \
	--caches
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
