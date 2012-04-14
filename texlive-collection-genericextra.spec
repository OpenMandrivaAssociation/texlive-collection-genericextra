# revision 25779
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-genericextra
Epoch:		1
Version:	20120413
Release:	1
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
