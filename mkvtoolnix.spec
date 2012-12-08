Summary:	Matroska multimedia file utils
Name:		mkvtoolnix
Version:	5.8.0
Release:	1
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
License:	GPLv2+ and LGPLv2+
Group:		Video
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	libmatroska-devel >= 1.3.0
BuildRequires:	libebml-devel >= 1.2.2
BuildRequires:	wxgtku-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	liblzo-devel
BuildRequires:	magic-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(expat)
BuildRequires:	boost-devel >= 1.46
BuildRequires:	gcc-c++ >= 4.6.0
BuildRequires:	ruby

%description
These tools allow information about (mkvinfo) or extraction
from (mkvdemux) or creation of (mkvmerge) or the splitting of
(mkvsplit) Matroska files. Matroska is a new multimedia file
format aiming to become THE new container format for the future. You
can find more information about it and its underlying technology, the
Extensible Binary Meta Language (EBML), at http://www.matroska.org/

%prep
%setup -q

%build
# Add workaround for bug in gcc 4.7.2_2012.07
# otherwise configure won't find lambda functions support
%setup_compile_flags
export CXXFLAGS=`echo $CXXFLAGS | %__sed s/-gdwarf-4//`

%configure2_5x --with-wx-config=%{_bindir}/wx-config-unicode
./drake %{_smp_mflags}

%install
./drake install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc README TODO ChangeLog* COPYING
%{_bindir}/*
%{_datadir}/applications/mkvinfo.desktop
%{_datadir}/applications/mkvmergeGUI.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(uk) %{_mandir}/uk/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*



%changelog
* Tue Jul 10 2012 GÃ¶tz Waschk <waschk@mandriva.org> 5.7.0-1mdv2012.0
+ Revision: 808707
- update to new version 5.7.0

* Thu May 31 2012 GÃ¶tz Waschk <waschk@mandriva.org> 5.6.0-1
+ Revision: 801531
- update to new version 5.6.0

* Tue Apr 10 2012 GÃ¶tz Waschk <waschk@mandriva.org> 5.5.0-1
+ Revision: 790134
- update to new version 5.5.0

* Sat Mar 10 2012 GÃ¶tz Waschk <waschk@mandriva.org> 5.4.0-1
+ Revision: 783886
- update build deps
- new version

* Thu Feb 09 2012 GÃ¶tz Waschk <waschk@mandriva.org> 5.3.0-1
+ Revision: 772310
- update file list
- update to new version 5.3.0

* Mon Jan 02 2012 GÃ¶tz Waschk <waschk@mandriva.org> 5.2.1-1
+ Revision: 748743
- update to new version 5.2.1

* Mon Dec 19 2011 GÃ¶tz Waschk <waschk@mandriva.org> 5.2.0-1
+ Revision: 743662
- new version
- add uk man pages

* Wed Nov 30 2011 GÃ¶tz Waschk <waschk@mandriva.org> 5.1.0-1
+ Revision: 735538
- new version
- bump deps
- spec cleanup

* Sun Oct 09 2011 GÃ¶tz Waschk <waschk@mandriva.org> 5.0.1-1
+ Revision: 703929
- new version

* Mon Sep 26 2011 GÃ¶tz Waschk <waschk@mandriva.org> 5.0.0-1
+ Revision: 701260
- new version
- build against external matroska library
- build with curl support

* Tue Jul 12 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.9.1-1
+ Revision: 689627
- update to new version 4.9.1

* Mon Jul 11 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.9.0-1
+ Revision: 689435
- update to new version 4.9.0

* Tue May 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.8.0-1
+ Revision: 678085
- update to new version 4.8.0
- update build deps

* Thu Apr 21 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.7.0-1
+ Revision: 656469
- update to new version 4.7.0

* Tue Mar 15 2011 Funda Wang <fwang@mandriva.org> 4.6.0-2
+ Revision: 644924
- rebuild for new boost

* Thu Mar 10 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.6.0-1
+ Revision: 643452
- update to new version 4.6.0

* Thu Mar 10 2011 Funda Wang <fwang@mandriva.org> 4.5.0-2
+ Revision: 643228
- rebuild to obsolete old packages

* Tue Feb 01 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.5.0-1
+ Revision: 634647
- new version
- bump matroska dep
- update file list

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 4.4.0-2
+ Revision: 634170
- rebuild

* Tue Nov 02 2010 GÃ¶tz Waschk <waschk@mandriva.org> 4.4.0-1mdv2011.0
+ Revision: 591911
- update to new version 4.4.0

* Sun Sep 05 2010 GÃ¶tz Waschk <waschk@mandriva.org> 4.3.0-1mdv2011.0
+ Revision: 576128
- new version
- build with ruby's drake instead of make

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 4.2.0-3mdv2011.0
+ Revision: 572638
- rebuild

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 4.2.0-2mdv2011.0
+ Revision: 566030
- rebuild for new boost

* Wed Jul 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 4.2.0-1mdv2011.0
+ Revision: 562786
- new version

* Sat Jul 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 4.1.1-1mdv2011.0
+ Revision: 550534
- new version
- bump libmatroska dep
- use upstream icons and desktop entry
- update file list

* Thu Mar 25 2010 GÃ¶tz Waschk <waschk@mandriva.org> 3.3.0-1mdv2010.1
+ Revision: 527348
- update to new version 3.3.0
- bump wxgtk dep

* Sat Feb 13 2010 GÃ¶tz Waschk <waschk@mandriva.org> 3.2.0-1mdv2010.1
+ Revision: 505372
- new version
- add Chinese man pages

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 3.1.0-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 3.1.0-2mdv2010.1
+ Revision: 500092
- rebuild for new boost

* Wed Jan 20 2010 GÃ¶tz Waschk <waschk@mandriva.org> 3.1.0-1mdv2010.1
+ Revision: 494008
- bump boost dep
- disable qt build which was enabled by accident
- update build deps
- new version
- add japanese man pages

* Sun Dec 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 3.0.0-1mdv2010.1
+ Revision: 478108
- update to new version 3.0.0

* Thu Nov 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.9-1mdv2010.1
+ Revision: 470311
- update to new version 2.9.9

* Fri Aug 21 2009 Funda Wang <fwang@mandriva.org> 2.9.8-2mdv2010.0
+ Revision: 418869
- rebuild for new libboost

* Fri Aug 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.8-1mdv2010.0
+ Revision: 416276
- update to new version 2.9.8

* Thu Jul 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.7-1mdv2010.0
+ Revision: 391839
- new version

* Sun Jun 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.5-1mdv2010.0
+ Revision: 383754
- update to new version 2.9.5

* Mon Jun 01 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.0-1mdv2010.0
+ Revision: 381982
- update to new version 2.9.0

* Sat May 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.0-1mdv2010.0
+ Revision: 373843
- update to new version 2.8.0

* Fri Apr 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.7.0-1mdv2010.0
+ Revision: 368990
- new version
- bump boost dep

* Sun Mar 08 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.5.3-1mdv2009.1
+ Revision: 352896
- update to new version 2.5.3

* Sat Feb 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.5.2-1mdv2009.1
+ Revision: 346178
- update to new version 2.5.2
- reenable werror flag

* Mon Feb 23 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.5.1-1mdv2009.1
+ Revision: 344042
- new version
- disable format string werror
- update file list

* Sun Jan 18 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.2-1mdv2009.1
+ Revision: 330984
- new version
- drop patch

* Sun Dec 21 2008 Funda Wang <fwang@mandriva.org> 2.4.1-2mdv2009.1
+ Revision: 316869
- rebuild for new boost

* Sun Dec 07 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.1-1mdv2009.1
+ Revision: 311572
- new version
- fix build

* Mon Oct 13 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.0-1mdv2009.1
+ Revision: 293110
- new version

* Mon Sep 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.3.0-1mdv2009.0
+ Revision: 282822
- new version
- update license
- update build deps

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-3mdv2009.0
+ Revision: 252598
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.0-1mdv2008.1
+ Revision: 180145
- new version

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-1mdv2008.1
+ Revision: 148264
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Aug 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.1.0-1mdv2008.0
+ Revision: 67039
- new version


* Wed Feb 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.2-1mdv2007.0
+ Revision: 123804
- new version
- bump deps

* Sat Jan 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.0-1mdv2007.1
+ Revision: 108365
- new version
- fix build

* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.1-3mdv2007.1
+ Revision: 100701
- rebuild

* Fri Dec 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.1-2mdv2007.1
+ Revision: 89574
- rebuild for new flac

* Sun Nov 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.1-1mdv2007.1
+ Revision: 87328
- new version

* Sat Nov 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.0-2mdv2007.1
+ Revision: 81059
- fix buildrequires
- new version

* Wed Oct 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.7.0-4mdv2007.1
+ Revision: 65873
- fix buildrequires
- Import mkvtoolnix

* Wed Oct 18 2006 Götz Waschk <waschk@mandriva.org> 1.7.0-3mdv2007.1
- drop useless patch

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 1.7.0-2mdv2007.0
- xdg menu

* Sun Apr 30 2006 Götz Waschk <waschk@mandriva.org> 1.7.0-1mdk
- update buildrequires
- New release 1.7.0

* Wed Dec 07 2005 Götz Waschk <waschk@mandriva.org> 1.6.5-1mdk
- rediff the patch
- New release 1.6.5

* Wed Nov 30 2005 Götz Waschk <waschk@mandriva.org> 1.6.0-3mdk
- merge patches
- wxGTK unicode build

* Sat Oct 22 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.0-2mdk
- Rebuild

* Sat Oct 15 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.0-1mdk
- New release 1.6.0

* Thu Sep 08 2005 Götz Waschk <waschk@mandriva.org> 1.5.6-1mdk
- drop patch 0
- New release 1.5.6

* Mon Aug 22 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.5.5-1mdk
- New release 1.5.5

* Sat Jul 02 2005 Götz Waschk <waschk@mandriva.org> 1.5.0-1mdk
- New release 1.5.0

* Thu Jun 30 2005 Götz Waschk <waschk@mandriva.org> 1.4.2-4mdk
- patch 2 to build with new liblzo

* Thu Jun 02 2005 Götz Waschk <waschk@mandriva.org> 1.4.2-3mdk
- patch 1 to work around broken wx-config alternative
- mkrel
- rebuild for new lzo

* Wed Apr 27 2005 Götz Waschk <waschk@mandriva.org> 1.4.2-2mdk
- add the help file
- rebuild for new wxGTK

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 1.4.2-1mdk
- New release 1.4.2

* Tue Mar 15 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.4.1-1mdk
- New release 1.4.1

* Sat Feb 26 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.4.0-1mdk
- New release 1.4.0

* Mon Feb 07 2005 Götz Waschk <waschk@linux-mandrake.com> 1.0.2-1mdk
- requires new matroska
- New release 1.0.2

* Tue Dec 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.0.1-1mdk
- New release 1.0.1

* Wed Nov 17 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.0-1mdk
- New release 1.0

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.7-1mdk
- new version
- requires new libmatroska

* Tue Aug 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.5-1mdk
- requires new matroska
- New release 0.9.5

* Tue Aug 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.4-2mdk
- rebuild for new flac

* Mon Jul 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.4-1mdk
- requires new matroska
- New release 0.9.4

* Mon Jul 19 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.3-1mdk
- buildrequires flac
- New release 0.9.3

* Thu Jul 01 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.9.2-1mdk
- New release 0.9.2

* Mon Jun 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.9.1-1mdk
- New release 0.9.1

* Tue Jun 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.0-2mdk
- rebuild for new g++

* Wed Jun 02 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.9.0-1mdk
- New release 0.9.0

* Sat May 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.9-1mdk
- build with wxGTK 2.5
- add source URL
- new version

* Sat Apr 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.8-1mdk
- requires new libmatroska
- new version

* Sat Apr 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.7-1mdk
- new version

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.6-1mdk
- requires new ebml
- new version

* Mon Feb 23 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.5-1mdk
- new version

