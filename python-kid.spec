Summary:	Kid - A simple and pythonic XML template language
Summary(pl.UTF-8):   Kid - prosty i pythonopodobny język szablonów XML
Name:		python-kid
Version:	0.9.4
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://www.kid-templating.org/dist/%{version}/kid-%{version}.tar.gz
# Source0-md5:	2122ee32062079418db34cfd5fc15c37
URL:		http://www.kid-templating.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%pyrequires_eq  python-modules
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kid is a simple Python based template language for generating and
transforming XML vocabularies. Kid was spawned as a result of a kinky
love triangle between XSLT, TAL, and PHP. We believe many of the best
features of these languages live on in Kid with much of the
limitations and complexity stamped out (well, eventually :).

%description -l pl.UTF-8
Kid to prosty, oparty na Pythonie język szablonów do generowania i
przekształcania słowników XML. Kid powstał jako wynik trójkąta
miłosnego między XSLT, TAL i PHP. Autorzy wierzą, że w Kidzie żyją
najlepsze cechy tych języków bez większości ich ograniczeń i
złożoności.

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
