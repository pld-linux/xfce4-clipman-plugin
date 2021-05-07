Summary:	A simple clipboard history for Xfce panel
Summary(pl.UTF-8):	Prosta historia schowka panelu Xfce
Name:		xfce4-clipman-plugin
Version:	1.6.2
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-clipman-plugin/1.6/%{name}-%{version}.tar.bz2
# Source0-md5:	12227f4b84c0c16878522f501519d75b
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	qrencode-devel >= 3.3.0
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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hy_AM
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%{_sysconfdir}/xdg/autostart/xfce4-clipman-plugin-autostart.desktop
%{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%attr(755,root,root) %{_bindir}/xfce4-clipman
%attr(755,root,root) %{_bindir}/xfce4-clipman-history
%attr(755,root,root) %{_bindir}/xfce4-clipman-settings
%attr(755,root,root) %{_bindir}/xfce4-popup-clipman
%attr(755,root,root) %{_bindir}/xfce4-popup-clipman-actions
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libclipman.so
%{_iconsdir}/hicolor/*/apps/clipman-symbolic.*
%{_iconsdir}/hicolor/*/apps/xfce4-clipman-plugin.*
%{_desktopdir}/xfce4-clipman.desktop
%{_datadir}/xfce4/panel/plugins/xfce4-clipman-plugin.desktop
%{_desktopdir}/xfce4-clipman-settings.desktop
%{_datadir}/metainfo/xfce4-clipman.appdata.xml
