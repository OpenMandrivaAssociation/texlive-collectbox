Name:		texlive-collectbox
Version:	0.4
Release:	1
Summary:	Collect and process macro arguments as boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collectbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides macros to collect and process a macro
argument (i.e., something which looks like a macro argument) as
a horizontal box rather than as a real macro argument. The
"arguments" are stored as if they had been saved by \savebox or
by the lrbox environment. Grouping tokens \bgroup and \egroup
may be used, which allows the user to have the beginning and
end of a group in different macro invocations, or to place them
in the begin and end code of an environment. Arguments may
contain verbatim material or other special use of characters.
The macros were designed for use within other macros.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
