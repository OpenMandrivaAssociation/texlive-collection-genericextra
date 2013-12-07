# revision 31402
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-genericextra
Epoch:		1
Version:	20131013
Release:	4
Summary:	Generic additional packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-genericextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-abbr
Requires:	texlive-abstyles
Requires:	texlive-barr
Requires:	texlive-bitelist
Requires:	texlive-borceux
Requires:	texlive-c-pascal
Requires:	texlive-catcodes
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
Requires:	texlive-lambda-lists
Requires:	texlive-langcode
Requires:	texlive-lecturer
Requires:	texlive-librarian
Requires:	texlive-mathdots
Requires:	texlive-metatex
Requires:	texlive-midnight
Requires:	texlive-navigator
Requires:	texlive-ofs
Requires:	texlive-pdf-trans
Requires:	texlive-plainpkg
Requires:	texlive-schemata
Requires:	texlive-shade
Requires:	texlive-systeme
Requires:	texlive-tabto-generic
Requires:	texlive-texapi
Requires:	texlive-upca
Requires:	texlive-xlop
Requires:	texlive-yax

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
