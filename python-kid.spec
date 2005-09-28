
Name:		python-kid
Version:	0.6.4
Release:	1
Summary:	Kid - A simple and pythonic XML template language
Group:		Development/Languages/Python
License:	X11/MIT
Url:		http://kid.lesscode.org/
Source0:	http://lesscode.org/dist/kid/kid-%{version}.tar.gz
# Source0-md5:	e7e74a4387deff7cf473274dac442b36
BuildRequires:	python-devel
BuildRequires:	python-elementtree
%pyrequires_eq  python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python-elementtree

%description
Kid is a simple Python based template language for generating and
transforming XML vocabularies. Kid was spawned as a result of a kinky
love triangle between XSLT, TAL, and PHP. We believe many of the best
features of these languages live on in Kid with much of the
limitations and complexity stamped out (well, eventually :).


%prep
%setup -q -n kid-%{version}

%build
export CFLAGS="%{rpmcflags}"
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING HISTORY README doc/ examples/
%attr(755,root,root) %{_bindir}/kid*
%{py_sitescriptdir}/kid
