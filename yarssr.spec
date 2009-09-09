Summary:	An unobtrusive RSS Aggregator
Name:		yarssr
Version:	0.2.2
Release:	%mkrel 7
Group:		Networking/News
License:	GPL
URL:		http://yarssr.sourceforge.net/
Source:		http://osdn.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/root-%{name}-%{version}
BuildRequires:	coreutils, gettext
BuildArch:	noarch

%description
Yet Another RSS Reader is an RSS aggregator and reader that displays its
results in the GNOME or KDE system tray (notification area). To view the
contents of the feed just click the menu-item and it will launch in your
favorite browser. It is written in Perl and uses gtk2-perl for its
interface. YARSSR is still early in development, but is entirely usable.

%prep
%setup -q

%build
%make PREFIX=%{_prefix}

%install
%makeinstall_std PREFIX=%{_prefix}
%find_lang %name

%clean
 [ %buildroot != '/' ] && rm -fr %buildroot	

%files -f %name.lang
%defattr(-,root,root,0755)
%doc ChangeLog INSTALL README TODO
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/%{name}

