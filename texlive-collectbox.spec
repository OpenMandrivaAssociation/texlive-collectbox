%global tl_name collectbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4c
Release:	%{tl_revision}.1
Summary:	Collect and process macro arguments as boxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/collectbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collectbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros to collect and process a macro argument
(i.e., something which looks like a macro argument) as a horizontal box
rather than as a real macro argument. The "arguments" are stored as if
they had been saved by \savebox or by the lrbox environment. Grouping
tokens \bgroup and \egroup may be used, which allows the user to have
the beginning and end of a group in different macro invocations, or to
place them in the begin and end code of an environment. Arguments may
contain verbatim material or other special use of characters. The macros
were designed for use within other macros.

