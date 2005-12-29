Summary:	RDF module for Ruby
Summary(pl):	Modu³ RDF dla jêzyka Ruby
Name:		rubyrdf
Version:	0
Release:	0.20030621.2
License:	W3C
Group:		Development/Languages
Source0:	http://www.w3.org/2001/12/rubyrdf/%{name}-plus.tar.gz
# Source0-md5:	42c62be30afa530fde71223e06d8cf24
URL:		http://www.w3.org/2001/12/rubyrdf/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
Requires:	ruby
#BuildArch:	noarch
%ruby_mod_ver_requires_eq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RubyRDF is a library that provides some basic support for working with
W3C's RDF data format.


%description -l pl
RubyRDF to biblioteka dostarczaj±ca podstawowe wsparcie do pracy z
formatem danych RDF z W3C.

%prep
%setup -q -n pack
rm -rf examples/{examples,squish/README-tests.txt~,tests} 'lib/.#'*

%build
ruby install.rb config \
	--std-ruby=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	--site-ruby=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	--so-dir=$RPM_BUILD_ROOT%{ruby_archdir}

ruby install.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{_examplesdir}/%{name}-%{version}/tests}

ruby install.rb install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{ruby_rubylibdir}/RDF4R*
%{ruby_rubylibdir}/*.rb
%{_examplesdir}/%{name}-%{version}
