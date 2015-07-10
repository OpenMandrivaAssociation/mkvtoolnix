# needed or qt5 test program wont compile
%define Werror_cflags %nil

Summary:	Matroska multimedia file utils

Name:		mkvtoolnix
Version:	8.1.0
Release:	1
Url:		http://www.bunkus.org/videotools/mkvtoolnix/
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.xz
Patch1:		mkvtoolnix-8.1.0-qt5.5.patch
License:	GPLv2+ and LGPLv2+
Group:		Video
BuildRequires:	bzip2-devel
BuildRequires:	libebml-devel >= 1.3.0
BuildRequires:	lzo-devel
BuildRequires:	libmatroska-devel >= 1.4.1
BuildRequires:	magic-devel
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	boost-devel >= 1.46
BuildRequires:	ruby
BuildRequires:  rubygems

%description
These tools allow information about (mkvinfo) or extraction
from (mkvdemux) or creation of (mkvmerge) or the splitting of
(mkvsplit) Matroska files. Matroska is a new multimedia file
format aiming to become THE new container format for the future. You
can find more information about it and its underlying technology, the
Extensible Binary Meta Language (EBML), at http://www.matroska.org/

%files -f %{name}.lang
%doc  TODO ChangeLog* COPYING
%{_bindir}/*
# %{_datadir}/applications/mkvinfo.desktop
# %{_datadir}/applications/mkvmergeGUI.desktop
# %{_datadir}/icons/hicolor/*/apps/*.*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(nl) %{_mandir}/nl/man1/*
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
	--disable-wxwidgets
./drake %{_smp_mflags}

%install
./drake install DESTDIR=%{buildroot}
%find_lang %{name}
