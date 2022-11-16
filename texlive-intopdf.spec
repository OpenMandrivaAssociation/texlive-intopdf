Name:		texlive-intopdf
Version:	63987
Release:	1
Summary:	Embed non-PDF files into PDF with hyperlink
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/intopdf
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intopdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intopdf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intopdf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows to embed non-PDF files (e.g., BibTeX) into
PDF with a hyperlink.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/intopdf
%{_texmfdistdir}/tex/latex/intopdf
%doc %{_texmfdistdir}/doc/latex/intopdf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
