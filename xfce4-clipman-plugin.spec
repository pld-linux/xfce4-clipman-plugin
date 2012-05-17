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

#%{_datadir}/xfce4/doc/C/*.html
#%lang(ca) %{_datadir}/xfce4/doc/ca/*.html
#%lang(ca) %{_datadir}/xfce4/doc/ca/images/*.png
#%lang(da) %{_datadir}/xfce4/doc/da/*.html
#%lang(da) %{_datadir}/xfce4/doc/da/images/*.png
#%lang(el) %{_datadir}/xfce4/doc/el/*.html
#%lang(el) %{_datadir}/xfce4/doc/el/images/*.png
#%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
#%lang(fr) %{_datadir}/xfce4/doc/fr/images/*.png
#%lang(gl) %{_datadir}/xfce4/doc/gl/*.html
#%lang(gl) %{_datadir}/xfce4/doc/gl/images/*.png
#%lang(it) %{_datadir}/xfce4/doc/it/*.html
#%lang(it) %{_datadir}/xfce4/doc/it/images/*.png
#%lang(ja) %{_datadir}/xfce4/doc/ja/*.html
#%lang(ja) %{_datadir}/xfce4/doc/ja/images/*.png
#%lang(pt) %{_datadir}/xfce4/doc/pt/*.html
#%lang(pt) %{_datadir}/xfce4/doc/pt/images/*.png
#%lang(ru) %{_datadir}/xfce4/doc/ru/*.html
#%lang(ru) %{_datadir}/xfce4/doc/ru/images/*.png
#%lang(tr) %{_datadir}/xfce4/doc/tr/*.html
#%lang(tr) %{_datadir}/xfce4/doc/tr/images/*.png
#%lang(ug) %{_datadir}/xfce4/doc/ug/*.html
#%lang(ug) %{_datadir}/xfce4/doc/ug/images/*.png
#%lang(uk) %{_datadir}/xfce4/doc/uk/*.html
#%lang(uk) %{_datadir}/xfce4/doc/uk/images/*.png
#%lang(zh_CN) %{_datadir}/xfce4/doc/zh_CN/*.html
#%lang(zh_CN) %{_datadir}/xfce4/doc/zh_CN/images/*.png
