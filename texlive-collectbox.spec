Name:		texlive-collectbox
Version:	64967
Release:	1
Summary:	TeXLive collectbox package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.r64967.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.doc.r64967.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.source.r64967.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive collectbox package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/collectbox
%doc %{_texmfdistdir}/doc/latex/collectbox
#- source
%doc %{_texmfdistdir}/source/latex/collectbox

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
