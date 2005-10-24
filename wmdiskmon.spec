Summary:	A dockapp to monitor disks usage
Summary(pl):	Aplet monitoruj±cy zajêto¶æ dysków
Name:		wmdiskmon
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
# Source0-md5:	4b02066a58752c3e7100abc0544c2c66
Source1:	%{name}.desktop
URL:		http://tnemeth.free.fr/projets/dockapps.html
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmdiskmon is a dockapp to monitor disks usage.

%description -l pl
wmdiskmon jest apletem monitoruj±cym zajêto¶æ dysków.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/docklets/*
