#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : bovo
Version  : 24.12.0
Release  : 75
URL      : https://download.kde.org/stable/release-service/24.12.0/src/bovo-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/bovo-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/bovo-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: bovo-bin = %{version}-%{release}
Requires: bovo-data = %{version}-%{release}
Requires: bovo-license = %{version}-%{release}
Requires: bovo-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n bovo-24.12.0
cd %{_builddir}/bovo-24.12.0
pushd ..
cp -a bovo-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735193608
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735193608
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bovo
cp %{_builddir}/bovo-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/bovo/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/bovo-%{version}/COPYING %{buildroot}/usr/share/package-licenses/bovo/3860f7708aae6a8ddfe8483263b2a5f29b83c975 || :
cp %{_builddir}/bovo-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/bovo/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
cp %{_builddir}/bovo-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/bovo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang bovo
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/bovo
/usr/bin/bovo

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.bovo.desktop
/usr/share/bovo/themes/gomoku/theme.svgz
/usr/share/bovo/themes/gomoku/themerc
/usr/share/bovo/themes/highcontrast/theme.svgz
/usr/share/bovo/themes/highcontrast/themerc
/usr/share/bovo/themes/scribble/theme.svgz
/usr/share/bovo/themes/scribble/themerc
/usr/share/bovo/themes/spacy/theme.svgz
/usr/share/bovo/themes/spacy/themerc
/usr/share/icons/hicolor/128x128/apps/bovo.png
/usr/share/icons/hicolor/16x16/apps/bovo.png
/usr/share/icons/hicolor/22x22/apps/bovo.png
/usr/share/icons/hicolor/32x32/apps/bovo.png
/usr/share/icons/hicolor/48x48/apps/bovo.png
/usr/share/icons/hicolor/64x64/apps/bovo.png
/usr/share/metainfo/org.kde.bovo.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/bovo/index.cache.bz2
/usr/share/doc/HTML/ca/bovo/index.docbook
/usr/share/doc/HTML/ca/bovo/mainscreen.png
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
/usr/share/doc/HTML/fr/bovo/index.cache.bz2
/usr/share/doc/HTML/fr/bovo/index.docbook
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
/usr/share/doc/HTML/sl/bovo/index.cache.bz2
/usr/share/doc/HTML/sl/bovo/index.docbook
/usr/share/doc/HTML/sv/bovo/index.cache.bz2
/usr/share/doc/HTML/sv/bovo/index.docbook
/usr/share/doc/HTML/uk/bovo/index.cache.bz2
/usr/share/doc/HTML/uk/bovo/index.docbook
/usr/share/doc/HTML/uk/bovo/mainscreen.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bovo/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/bovo/3860f7708aae6a8ddfe8483263b2a5f29b83c975
/usr/share/package-licenses/bovo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/bovo/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f bovo.lang
%defattr(-,root,root,-)

