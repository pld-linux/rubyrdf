%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_rubylibdir		%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	RDF module for Ruby
Summary(pl):	Modu³ RDF dla Ruby
Name:		rubyrdf
Version:	0
Release:	0.20030621.1
License:	GPL
Group:		Development/Languages
Source0:	http://www.w3.org/2001/12/rubyrdf/%{name}-plus.tar.gz
# Source0-md5:	42c62be30afa530fde71223e06d8cf24
URL:	http://www.w3.org/2001/12/rubyrdf/
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch: noarch

%description
RDF module for Ruby.

%description -l pl
Modu³ RDF dla Ruby.

%prep
%setup -q -n pack

ruby install.rb config \
	--std-ruby=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	--site-ruby=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	--so-dir=$RPM_BUILD_ROOT%{ruby_archdir}


%build
ruby install.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{_examplesdir}/%{name}}

ruby install.rb install


cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{ruby_rubylibdir}/*
%{_examplesdir}/*
