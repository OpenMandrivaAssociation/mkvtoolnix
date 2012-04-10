%define name mkvtoolnix
%define version 5.5.0
%define release %mkrel 1

Summary: Matroska multimedia file utils
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
URL: http://www.bunkus.org/videotools/mkvtoolnix/
License: GPLv2+ and LGPLv2+
Group: Video
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libvorbis-devel
BuildRequires: libmatroska-devel >= 1.3.0
BuildRequires: libebml-devel >= 1.2.2
BuildRequires: wxgtku-devel >= 2.8
BuildRequires: curl-devel
BuildRequires: liblzo-devel
BuildRequires: magic-devel
BuildRequires: libbzip2-devel
BuildRequires: libflac-devel
BuildRequires: libpcre-devel
BuildRequires: libexpat-devel
BuildRequires: boost-devel >= 1.46
BuildRequires: gcc-c++ >= 4.6.0
BuildRequires: ruby

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
%configure2_5x --with-wx-config=%{_bindir}/wx-config-unicode
./drake %_smp_mflags

%install
rm -rf $RPM_BUILD_ROOT
./drake install DESTDIR=%buildroot
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO ChangeLog* COPYING
%_bindir/*
%_datadir/applications/mkvinfo.desktop
%_datadir/applications/mkvmergeGUI.desktop
%_datadir/icons/hicolor/*/apps/*.*
%_datadir/mime/packages/%name.xml
%_mandir/man1/*
%lang(ja) %_mandir/ja/man1/*
%lang(nl) %_mandir/nl/man1/*
%lang(uk) %_mandir/uk/man1/*
%lang(zh_CN) %_mandir/zh_CN/man1/*
