Summary:	A simple clipboard history for XFce panel
Summary(pl):	Prosta historia schowka panelu XFce
Name:		xfce4-clipman-plugin
Version:	0.1
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	7054204ed94cf2f477056e71f7035cc3
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
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
