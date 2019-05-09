#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : bovo
Version  : 19.04.1
Release  : 7
URL      : https://download.kde.org/stable/applications/19.04.1/src/bovo-19.04.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.1/src/bovo-19.04.1.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.1/src/bovo-19.04.1.tar.xz.sig
Summary  : A Gomoku like game for two players
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: bovo-bin = %{version}-%{release}
Requires: bovo-data = %{version}-%{release}
Requires: bovo-license = %{version}-%{release}
Requires: bovo-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
EXTENDED

%package bin
Summary: bin components for the bovo package.
Group: Binaries
Requires: bovo-data = %{version}-%{release}
Requires: bovo-license = %{version}-%{release}

%description bin
bin components for the bovo package.


%package data
Summary: data components for the bovo package.
Group: Data

%description data
data components for the bovo package.


%package doc
Summary: doc components for the bovo package.
Group: Documentation

%description doc
doc components for the bovo package.


%package license
Summary: license components for the bovo package.
Group: Default

%description license
license components for the bovo package.


%package locales
Summary: locales components for the bovo package.
Group: Default

%description locales
locales components for the bovo package.


%prep
%setup -q -n bovo-19.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557431443
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557431443
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bovo
cp COPYING %{buildroot}/usr/share/package-licenses/bovo/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/bovo/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang bovo

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bovo

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.bovo.desktop
/usr/share/bovo/themes/gomoku/theme.svg
/usr/share/bovo/themes/gomoku/themerc
/usr/share/bovo/themes/highcontrast/theme.svg
/usr/share/bovo/themes/highcontrast/themerc
/usr/share/bovo/themes/scribble/theme.svg
/usr/share/bovo/themes/scribble/themerc
/usr/share/bovo/themes/spacy/theme.svg
/usr/share/bovo/themes/spacy/themerc
/usr/share/icons/hicolor/128x128/apps/bovo.png
/usr/share/icons/hicolor/16x16/apps/bovo.png
/usr/share/icons/hicolor/22x22/apps/bovo.png
/usr/share/icons/hicolor/32x32/apps/bovo.png
/usr/share/icons/hicolor/48x48/apps/bovo.png
/usr/share/icons/hicolor/64x64/apps/bovo.png
/usr/share/kxmlgui5/bovo/bovoui.rc
/usr/share/metainfo/org.kde.bovo.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/cs/bovo/index.cache.bz2
/usr/share/doc/HTML/cs/bovo/index.docbook
/usr/share/doc/HTML/de/bovo/index.cache.bz2
/usr/share/doc/HTML/de/bovo/index.docbook
/usr/share/doc/HTML/en/bovo/index.cache.bz2
/usr/share/doc/HTML/en/bovo/index.docbook
/usr/share/doc/HTML/en/bovo/mainscreen.png
/usr/share/doc/HTML/es/bovo/index.cache.bz2
/usr/share/doc/HTML/es/bovo/index.docbook
/usr/share/doc/HTML/et/bovo/index.cache.bz2
/usr/share/doc/HTML/et/bovo/index.docbook
/usr/share/doc/HTML/it/bovo/index.cache.bz2
/usr/share/doc/HTML/it/bovo/index.docbook
/usr/share/doc/HTML/nl/bovo/index.cache.bz2
/usr/share/doc/HTML/nl/bovo/index.docbook
/usr/share/doc/HTML/pt/bovo/index.cache.bz2
/usr/share/doc/HTML/pt/bovo/index.docbook
/usr/share/doc/HTML/pt_BR/bovo/index.cache.bz2
/usr/share/doc/HTML/pt_BR/bovo/index.docbook
/usr/share/doc/HTML/ru/bovo/index.cache.bz2
/usr/share/doc/HTML/ru/bovo/index.docbook
/usr/share/doc/HTML/sv/bovo/index.cache.bz2
/usr/share/doc/HTML/sv/bovo/index.docbook
/usr/share/doc/HTML/uk/bovo/index.cache.bz2
/usr/share/doc/HTML/uk/bovo/index.docbook
/usr/share/doc/HTML/uk/bovo/mainscreen.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bovo/COPYING
/usr/share/package-licenses/bovo/COPYING.DOC

%files locales -f bovo.lang
%defattr(-,root,root,-)

