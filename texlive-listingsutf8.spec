Name:		texlive-listingsutf8
Version:	53097
Release:	2
Summary:	Allow UTF-8 in listings input
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listingsutf8
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listingsutf8.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listingsutf8.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listingsutf8.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Package listings does not support files with multi-byte
encodings such as UTF-8. In the case of \lstinputlisting, a
simple workaround is possible if a one-byte encoding exists
that the file can be converted to. The package requires the
e-TeX extensions under pdfTeX (in either PDF or DVI output
mode).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/listingsutf8
%{_texmfdistdir}/tex/latex/listingsutf8
%doc %{_texmfdistdir}/doc/latex/listingsutf8

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
