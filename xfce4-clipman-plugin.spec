Summary:	A simple clipboard history for Xfce panel
Summary(pl.UTF-8):   Prosta historia schowka panelu Xfce
Name:		xfce4-clipman-plugin
Version:	0.8.0
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-clipman-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	808d4e8bc6e9a9d4ed30124fb2236c1d
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is a clipboard history for the panel.

%description -l pl.UTF-8
Wtyczka ta jest historią schowka panelu.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README THANKS
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-clipman-plugin
%{_datadir}/xfce4/panel-plugins/clipman.desktop
