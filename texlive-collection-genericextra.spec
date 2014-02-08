# revision 26292
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-genericextra
Epoch:		1
Version:	20120810
Release:	2
Summary:	Extra generic packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-genericextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-abbr
Requires:	texlive-abstyles
Requires:	texlive-barr
Requires:	texlive-bitelist
Requires:	texlive-borceux
Requires:	texlive-c-pascal
Requires:	texlive-chronosys
Requires:	texlive-colorsep
Requires:	texlive-dinat
Requires:	texlive-dirtree
Requires:	texlive-dowith
Requires:	texlive-eijkhout
Requires:	texlive-encxvlna
Requires:	texlive-epigram
Requires:	texlive-fenixpar
Requires:	texlive-fltpoint
Requires:	texlive-fntproof
Requires:	texlive-gates
Requires:	texlive-ifetex
Requires:	texlive-iftex
Requires:	texlive-insbox
Requires:	texlive-lecturer
Requires:	texlive-librarian
Requires:	texlive-mathdots
Requires:	texlive-metatex
Requires:	texlive-midnight
Requires:	texlive-multi
Requires:	texlive-navigator
Requires:	texlive-ofs
Requires:	texlive-pdf-trans
Requires:	texlive-shade
Requires:	texlive-systeme
Requires:	texlive-tabto-generic
Requires:	texlive-texapi
Requires:	texlive-upca
Requires:	texlive-xlop
Requires:	texlive-yax
Requires:	texlive-collection-basic

%description
Extra packages that work with multiple formats, typically both
TeX and LaTeX.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813910
- Update to latest release.

* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120413-1
+ Revision: 790847
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120327-1
+ Revision: 787860
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780325
- Update to latest release.
- Import texlive-collection-genericextra
- Import texlive-collection-genericextra

