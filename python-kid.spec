Summary:	Kid - A simple and pythonic XML template language
Summary(pl):	Kid - prosty i pythonopodobny jêzyk szablonów XML
Name:		python-kid
Version:	0.8
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://lesscode.org/dist/kid/%{version}/kid-%{version}.tar.gz
# Source0-md5:	3ebc1df08ceb636fb5102fc3a1f6448e
URL:		http://kid.lesscode.org/
BuildRequires:	python-devel
BuildRequires:	python-elementtree
BuildRequires:	python-setuptools
%pyrequires_eq  python-modules
Requires:	python-elementtree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kid is a simple Python based template language for generating and
transforming XML vocabularies. Kid was spawned as a result of a kinky
love triangle between XSLT, TAL, and PHP. We believe many of the best
features of these languages live on in Kid with much of the
limitations and complexity stamped out (well, eventually :).

%description -l pl
Kid to prosty, oparty na Pythonie jêzyk szablonów do generowania i
przekszta³cania s³owników XML. Kid powsta³ jako wynik trójk±ta
mi³osnego miêdzy XSLT, TAL i PHP. Autorzy wierz±, ¿e w Kidzie ¿yj±
najlepsze cechy tych jêzyków bez wiêkszo¶ci ich ograniczeñ i
z³o¿ono¶ci.

%prep
%setup -q -n kid-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING HISTORY README doc/ examples/
%attr(755,root,root) %{_bindir}/kid*
%{py_sitescriptdir}/kid*
