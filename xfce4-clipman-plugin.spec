Summary:	A simple clipboard history for Xfce panel
Summary(pl.UTF-8):	Prosta historia schowka panelu Xfce
Name:		xfce4-clipman-plugin
Version:	1.7.0
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-clipman-plugin/1.7/%{name}-%{version}.tar.xz
# Source0-md5:	69f91c2ab381c5f4efd1a428397ce215
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	glib2-devel >= 2.60.0
BuildRequires:	gtk+3-devel >= 3.22.29
BuildRequires:	libxfce4ui-devel >= 4.18.0
BuildRequires:	libxfce4util-devel >= 4.18.0
BuildRequires:	meson >= 0.61.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	qrencode-devel >= 3.3.0
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	wayland-devel >= 1.15.0
BuildRequires:	xfce4-dev-tools >= 4.18.0
BuildRequires:	xfce4-panel-devel >= 4.18.0
BuildRequires:	xfconf-devel >= 4.18.0
BuildRequires:	xorg-lib-libX11-devel >= 1.6.7
BuildRequires:	xorg-lib-libXtst-devel >= 1.0.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-dirs >= 4.6
Requires:	xfce4-panel >= 4.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is a clipboard history for the panel.

%description -l pl.UTF-8
Wtyczka ta jest historią schowka panelu.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
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
