# revision 26557
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collectbox
Version:	20120807
Release:	9
Summary:	TeXLive collectbox package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.source.tar.xz
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
%{_texmfdistdir}/tex/latex/collectbox/collectbox.sty
%doc %{_texmfdistdir}/doc/latex/collectbox/README
%doc %{_texmfdistdir}/doc/latex/collectbox/collectbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/collectbox/collectbox.dtx
%doc %{_texmfdistdir}/source/latex/collectbox/collectbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120807-1
+ Revision: 812143
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 750335
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 718093
- texlive-collectbox
- texlive-collectbox
- texlive-collectbox
- texlive-collectbox
- texlive-collectbox

