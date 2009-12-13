%define name mkvtoolnix
%define version 3.0.0
%define release %mkrel 1

Summary: Matroska multimedia file utils
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
Source1: matroska-48.png
Source2: matroska-32.png
Source3: matroska-16.png
URL: http://www.bunkus.org/videotools/mkvtoolnix/
License: GPLv2+ and LGPLv2+
Group: Video
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libvorbis-devel
BuildRequires: libmatroska-devel >= 0.8.1
BuildRequires: wxgtku-devel >= 2.6
BuildRequires: liblzo-devel
BuildRequires: libmagic-devel
BuildRequires: libbzip2-devel
BuildRequires: libflac-devel
BuildRequires: libpcre-devel
BuildRequires: libexpat-devel
BuildRequires: boost-devel >= 1.32.0

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
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-mkvinfo.desktop << EOF
[Desktop Entry]
Name=Matroska Info
Comment=Shows information of Matroska video or audio files
Exec=mkvinfo -g
Icon=matroska
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;AudioVideoEditing;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-mmg.desktop << EOF
[Desktop Entry]
Name=Mkvmerge GUI
Comment=Create Matroska video or audio files
Exec=mmg
Icon=matroska
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;AudioVideoEditing;
EOF

install -D -m 644 %SOURCE1 %buildroot%_liconsdir/matroska.png
install -D -m 644 %SOURCE2 %buildroot%_iconsdir/matroska.png
install -D -m 644 %SOURCE3 %buildroot%_miconsdir/matroska.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus 
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO ChangeLog* COPYING
%_bindir/*
%_datadir/%name
%_datadir/applications/mandriva-*
%_mandir/man1/*
%_liconsdir/matroska.png
%_iconsdir/matroska.png
%_miconsdir/matroska.png


