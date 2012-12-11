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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-7mdv2010.0
+ Revision: 435345
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-6mdv2009.0
+ Revision: 262784
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-5mdv2009.0
+ Revision: 257931
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.2.2-3mdv2008.1
+ Revision: 141006
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 10:38:34 (55337)
- making package really noarch

* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 10:36:36 (55336)
- lib64 fix

* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 10:33:08 (55331)
Import yarssr

* Sun Apr 30 2006 Olivier Thauvin <nanardon@mandriva.org> 0.2.2-2mdk
- rebuild

* Wed Mar 23 2005 Olivier Thauvin <nanardon@mandrake.org> 0.2.2-1mdk
- From  Julien Hebert <juke@fr.st>
  - New Package

