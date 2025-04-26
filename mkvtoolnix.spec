%define _empty_manifest_terminate_build 0
# needed or qt5 test program wont compile
%define Werror_cflags %nil

Summary:	Matroska multimedia file utils

Name:		mkvtoolnix
Version:	92.0
Release:	1
Url:		https://mkvtoolnix.download/
Source0:	https://mkvtoolnix.download/sources/%{name}-%{version}.tar.xz
# 29.0.0 fail to build with boost-1.69. Import and revork FreeBSD patch. (penguin)
# https://svnweb.freebsd.org/ports/head/multimedia/mkvtoolnix/files/patch-boost-1.69?view=markup&pathrev=482787
#Patch0:		fix-build-with-boost.patch
License:	GPLv2+ and LGPLv2+
Group:		Video
BuildRequires:	pkgconfig(zlib)
BuildRequires:	desktop-file-utils
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(libebml) >= 1.3.7
BuildRequires:	lzo-devel
BuildRequires:	pkgconfig(libmatroska) >= 1.5.0
BuildRequires:	magic-devel
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(gmp)
BuildRequires:	appstream-util
BuildRequires:	boost-devel >= 1.46
BuildRequires:	ruby
BuildRequires:  rubygems
#BuildRequires:	rubygem-rake
#BuildRequires:	rubygem-json
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

%files -f %{name}.lang -f %{name}-gui.lang
%doc README.md COPYING
%{_bindir}/*
#{_datadir}/applications/mkvinfo.desktop
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_datadir}/metainfo/org.bunkus.mkvtoolnix-gui.appdata.xml
%{_datadir}/mime/packages/org.bunkus.mkvtoolnix-gui.xml
%{_datadir}/mkvtoolnix/qt_resources.rcc
%{_datadir}/icons/hicolor/*/apps/*.*
#{_datadir}/mime/packages/mkvtoolnix.xml
%{_datadir}/%{name}/sounds/finished*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
# Add workaround for bug in gcc 4.7.2_2012.07
# otherwise configure won't find lambda functions support
%setup_compile_flags
export CXXFLAGS=`echo $CXXFLAGS | sed s/-gdwarf-4//`
%configure \
	--enable-qt6 \
	
rake %{_smp_mflags}

%install
rake DESTDIR=$RPM_BUILD_ROOT TOOLS=1 install
desktop-file-validate %{buildroot}%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.bunkus.mkvtoolnix-gui.appdata.xml

%find_lang %{name}
%find_lang mkvextract --with-man
%find_lang mkvmerge --with-man
%find_lang mkvpropedit --with-man
%find_lang mkvinfo --with-man
cat mkv{extract,info,merge,propedit}.lang >> mkvtoolnix.lang
%find_lang mkvtoolnix-gui --with-man
