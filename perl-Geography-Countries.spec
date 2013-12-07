%define modname	Geography-Countries
%define modver	2009041301

Summary:	Maps 2-letter, 3-letter, and numerical codes for countries
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Geography/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module maps country names, and their 2-letter, 3-letter and
numerical codes, as defined by the ISO-3166 maintenance agency,
and defined by the UNSD.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Geography
%{_mandir}/man3/*

