Summary:	A simple clipboard history for XFce panel
Summary(pl):	Prosta historia schowka panelu XFce
Name:		xfce4-clipman-plugin
Version:	0.4.0
Release:	2
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	a291b385374a91f070969d1f430f9653
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	libxfce4util-devel >= 3.99
BuildRequires:	libxfcegui4-devel >= 3.99
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99
Requires:	xfce4-panel >= 3.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is a clipboard history for the panel.

%description -l pl
Wtyczka ta jest histori± schowka panelu.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
