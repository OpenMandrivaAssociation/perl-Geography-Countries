%define upstream_name	 Geography-Countries
%define upstream_version 2009041301

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Maps 2-letter, 3-letter, and numerical codes for countries
License:	MIT
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Geography/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module maps country names, and their 2-letter, 3-letter and
numerical codes, as defined by the ISO-3166 maintenance agency,
and defined by the UNSD.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Geography
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2009041301.0.0-4mdv2012.0
+ Revision: 765283
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2009041301.0.0-3
+ Revision: 763776
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2009041301.0.0-2
+ Revision: 667178
- mass rebuild

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 2009041301.0.0-1mdv2010.1
+ Revision: 399585
- update to 2009041301
- using %%perl_convert_version
- fixed license & source fields

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.4-7mdv2009.1
+ Revision: 351771
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 223768
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-5mdv2008.1
+ Revision: 180404
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-4mdv2007.0
+ Revision: 113985
- rebuild
- Import perl-Geography-Countries

* Mon Jan 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-3mdk
- spe cleanup
- rpmbuildupdate aware
- %%mkrel
- enable tests
- better URL

* Fri Jan 21 2005 Abel Cheung <deaddog@mandrake.org> 1.4-2mdk
- rebuild

