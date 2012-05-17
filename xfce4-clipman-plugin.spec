Summary:	A simple clipboard history for Xfce panel
Summary(pl.UTF-8):	Prosta historia schowka panelu Xfce
Name:		xfce4-clipman-plugin
Version:	1.2.3
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-clipman-plugin/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	61f3be97efa379cb358980c94e14692a
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	xfce4-panel-devel >= 4.10.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-dirs >= 4.6
Requires:	xfce4-panel >= 4.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is a clipboard history for the panel.

%description -l pl.UTF-8
Wtyczka ta jest historią schowka panelu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/xdg/autostart/xfce4-clipman-plugin-autostart.desktop
%{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%attr(755,root,root) %{_bindir}/xfce4-clipman
%attr(755,root,root) %{_bindir}/xfce4-clipman-settings
%attr(755,root,root) %{_bindir}/xfce4-popup-clipman
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libclipman.so
%{_iconsdir}/hicolor/*/apps/xfce4-clipman-plugin.*
%{_desktopdir}/xfce4-clipman.desktop
%{_datadir}/xfce4/panel/plugins/xfce4-clipman-plugin.desktop

%dir %{_datadir}/doc/xfce4-clipman-plugin
%dir %{_datadir}/doc/xfce4-clipman-plugin/html
%{_datadir}/doc/xfce4-clipman-plugin/html/C
%lang(ca) %{_datadir}/doc/xfce4-clipman-plugin/html/ca
%lang(da) %{_datadir}/doc/xfce4-clipman-plugin/html/da
%lang(el) %{_datadir}/doc/xfce4-clipman-plugin/html/el
%lang(fr) %{_datadir}/doc/xfce4-clipman-plugin/html/fr
%lang(gl) %{_datadir}/doc/xfce4-clipman-plugin/html/gl
%lang(it) %{_datadir}/doc/xfce4-clipman-plugin/html/it
%lang(ja) %{_datadir}/doc/xfce4-clipman-plugin/html/ja
%lang(pt) %{_datadir}/doc/xfce4-clipman-plugin/html/pt
%lang(ru) %{_datadir}/doc/xfce4-clipman-plugin/html/ru
%lang(tr) %{_datadir}/doc/xfce4-clipman-plugin/html/tr
%lang(ug) %{_datadir}/doc/xfce4-clipman-plugin/html/ug
%lang(uk) %{_datadir}/doc/xfce4-clipman-plugin/html/uk
%lang(zh_CN) %{_datadir}/doc/xfce4-clipman-plugin/html/zh_CN
