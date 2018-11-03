# needed or qt5 test program wont compile
%define Werror_cflags %nil

Summary:	Matroska multimedia file utils

Name:		mkvtoolnix
Version:	28.2.0
Release:	1
Url:		http://www.bunkus.org/videotools/mkvtoolnix/
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.xz
License:	GPLv2+ and LGPLv2+
Group:		Video
BuildRequires:	pkgconfig(zlib)
BuildRequires: desktop-file-utils
BuildRequires:	bzip2-devel
BuildRequires:	libebml-devel >= 1.3.0
BuildRequires:	lzo-devel
BuildRequires:	libmatroska-devel >= 1.4.1
BuildRequires:	magic-devel
BuildRequires:	qt5-devel
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	appstream-util
BuildRequires:	boost-devel >= 1.46
BuildRequires:	ruby
BuildRequires:  rubygems
BuildRequires:	rubygem-rake
BuildRequires:	rubygem-json
#BuildRequires:	ruby-rake
# Upstream need it both for man-page (penguin).
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc
# Optional - for building the translated man pages (penguin).
BuildRequires: po4a
BuildRequires: pkgconfig(libcmark)

%description
These tools allow information about (mkvinfo) or extraction
from (mkvdemux) or creation of (mkvmerge) or the splitting of
(mkvsplit) Matroska files. Matroska is a new multimedia file
format aiming to become THE new container format for the future. You
can find more information about it and its underlying technology, the
Extensible Binary Meta Language (EBML), at http://www.matroska.org/

%files -f %{name}.lang
%doc README.md COPYING
%{_bindir}/*
#{_datadir}/applications/mkvinfo.desktop
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_datadir}/metainfo/org.bunkus.mkvtoolnix-gui.appdata.xml
%{_datadir}/mime/packages/org.bunkus.mkvtoolnix-gui.xml
%{_datadir}/icons/hicolor/*/apps/*.*
#{_datadir}/mime/packages/mkvtoolnix.xml
%{_datadir}/%{name}/sounds/finished*
#{_mandir}/man1/*
%lang(ca) %{_mandir}/ca/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(uk) %{_mandir}/uk/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
# Add workaround for bug in gcc 4.7.2_2012.07
# otherwise configure won't find lambda functions support
%setup_compile_flags
export CXXFLAGS=`echo $CXXFLAGS | sed s/-gdwarf-4//`
%configure \
	--enable-qt \
	
rake %{_smp_mflags}

%install
rake DESTDIR=$RPM_BUILD_ROOT TOOLS=1 install
desktop-file-validate %{buildroot}%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.bunkus.mkvtoolnix-gui.appdata.xml

%find_lang %{name}
%find_lang mkvextract --with-man
%find_lang mkvmerge --with-man
%find_lang mkvpropedit --with-man
%find_lang mkvinfo --with-man
cat mkv{extract,info,merge,propedit}.lang >> mkvtoolnix.lang
%find_lang mkvtoolnix-gui --with-man
