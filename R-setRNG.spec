#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-setRNG
Version  : 2022.4.1
Release  : 45
URL      : https://cran.r-project.org/src/contrib/setRNG_2022.4-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/setRNG_2022.4-1.tar.gz
Summary  : Set (Normal) Random Number Generator and Seed
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
the seed and the uniform and normal generators used when a random
	experiment is run. The utilities can be used in other functions 
	that do random experiments to simplify recording and/or setting all the 
	necessary information for reproducibility. 
	See the vignette and reference manual for examples.

%prep
%setup -q -c -n setRNG
cd %{_builddir}/setRNG

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649038805

%install
export SOURCE_DATE_EPOCH=1649038805
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library setRNG
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library setRNG
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library setRNG
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc setRNG || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/setRNG/DESCRIPTION
/usr/lib64/R/library/setRNG/INDEX
/usr/lib64/R/library/setRNG/LICENSE
/usr/lib64/R/library/setRNG/Meta/Rd.rds
/usr/lib64/R/library/setRNG/Meta/features.rds
/usr/lib64/R/library/setRNG/Meta/hsearch.rds
/usr/lib64/R/library/setRNG/Meta/links.rds
/usr/lib64/R/library/setRNG/Meta/nsInfo.rds
/usr/lib64/R/library/setRNG/Meta/package.rds
/usr/lib64/R/library/setRNG/Meta/vignette.rds
/usr/lib64/R/library/setRNG/NAMESPACE
/usr/lib64/R/library/setRNG/NEWS
/usr/lib64/R/library/setRNG/R/setRNG
/usr/lib64/R/library/setRNG/R/setRNG.rdb
/usr/lib64/R/library/setRNG/R/setRNG.rdx
/usr/lib64/R/library/setRNG/doc/index.html
/usr/lib64/R/library/setRNG/doc/setRNG.R
/usr/lib64/R/library/setRNG/doc/setRNG.Stex
/usr/lib64/R/library/setRNG/doc/setRNG.pdf
/usr/lib64/R/library/setRNG/help/AnIndex
/usr/lib64/R/library/setRNG/help/aliases.rds
/usr/lib64/R/library/setRNG/help/paths.rds
/usr/lib64/R/library/setRNG/help/setRNG.rdb
/usr/lib64/R/library/setRNG/help/setRNG.rdx
/usr/lib64/R/library/setRNG/html/00Index.html
/usr/lib64/R/library/setRNG/html/R.css
/usr/lib64/R/library/setRNG/tests/RNGtest.R
