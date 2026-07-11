%global tl_name listingsutf8
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Allow UTF-8 in listings input
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listingsutf8
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listingsutf8.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listingsutf8.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listingsutf8.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Package listings does not support files with multi-byte encodings such
as UTF-8. In the case of \lstinputlisting, a simple workaround is
possible if a one-byte encoding exists that the file can be converted
to. The package requires the e-TeX extensions under pdfTeX (in either
PDF or DVI output mode).

