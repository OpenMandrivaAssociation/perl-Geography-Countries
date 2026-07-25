%define modname	Geography-Countries
%define modver	2009041301

Summary:	Maps 2-letter, 3-letter, and numerical codes for countries
Name:		perl-%{modname}
Version:	%{modver}
Release:	19
License:	MIT
Group:		Development/Perl
Url:		https://github.com/Abigail/geography--countries
Source0:	https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Geography-Countries-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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

