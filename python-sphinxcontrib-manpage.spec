#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx Linux manpage extension
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do linuksowych stron man
Name:		python-sphinxcontrib-manpage
Version:	0.6
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-manpage/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-manpage/sphinxcontrib-manpage-%{version}.tar.gz
# Source0-md5:	435cee36a8d14e8f50547e3bc1171cce
URL:		https://pypi.org/project/sphinxcontrib-manpage/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx role to render HTML links to online Linux manpages. 

%description -l pl.UTF-8
Rola Sphinksa do renderowania odnośników HTML do linuksowych stron man
online.

%package -n python3-sphinxcontrib-manpage
Summary:	Sphinx Linux manpage extension
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do linuksowych stron man
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinxcontrib-manpage
Sphinx role to render HTML links to online Linux manpages. 

%description -n python3-sphinxcontrib-manpage -l pl.UTF-8
Rola Sphinksa do renderowania odnośników HTML do linuksowych stron man
online.

%prep
%setup -q -n sphinxcontrib-manpage-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/sphinxcontrib/manpage.py[co]
%{py_sitescriptdir}/sphinxcontrib_manpage-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_manpage-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-manpage
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/sphinxcontrib/manpage.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/manpage.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_manpage-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_manpage-%{version}-py*-nspkg.pth
%endif
