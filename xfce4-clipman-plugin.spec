Summary:	A simple clipboard history for Xfce panel
Summary(pl.UTF-8):	Prosta historia schowka panelu Xfce
Name:		xfce4-clipman-plugin
Version:	1.1.3
Release:	4
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-clipman-plugin/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	2ba70c6bd710e2a18cba5add66d297dc
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
BuildRequires:	exo-devel >= 0.3.0
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfce4-panel-devel >= 4.6.0
Requires:	xfce4-panel >= 4.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is a clipboard history for the panel.

%description -l pl.UTF-8
Wtyczka ta jest historią schowka panelu.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/xdg/autostart/xfce4-clipman-plugin-autostart.desktop
%{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%attr(755,root,root) %{_bindir}/xfce4-clipman
%attr(755,root,root) %{_bindir}/xfce4-clipman-settings
%attr(755,root,root) %{_bindir}/xfce4-popup-clipman
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-clipman-plugin
%{_iconsdir}/hicolor/*/apps/xfce4-clipman-plugin.*
%{_desktopdir}/xfce4-clipman-plugin.desktop
%{_datadir}/xfce4/panel-plugins/xfce4-clipman-plugin.desktop

%{_datadir}/xfce4/doc/C/*
%lang(da) %{_datadir}/xfce4/doc/da/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(gl) %{_datadir}/xfce4/doc/gl/*
%lang(it) %{_datadir}/xfce4/doc/it/*
%lang(ja) %{_datadir}/xfce4/doc/ja/*
# this needs proper fix
%lang(zh_CN) %dir %{_datadir}/xfce4/doc/zh_CN
%lang(zh_CN) %{_datadir}/xfce4/doc/zh_CN/*
