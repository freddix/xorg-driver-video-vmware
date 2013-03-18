Summary:	X.org video driver for VMware virtual video cards
Name:		xorg-driver-video-vmware
Version:	13.0.0
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
# Source0-md5:	b72be57517cbc7a56362f2ee0f092269
Patch0:		%{name}-remove-mibstore.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libpciaccess-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VMware virtual video cards. It auto-detects the
version of any virtual VMware SVGA adapter.

%prep
%setup -qn xf86-video-vmware-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-vmwarectrl-client
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/vmwarectrl
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.4*

