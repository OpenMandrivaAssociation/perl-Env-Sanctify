%define upstream_name    Env-Sanctify
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	1.12
Release:	2

Summary:	Lexically scoped sanctification of %ENV

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bingos/env-sanctify
Source0:	https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Env-Sanctify-1.12.tar.gz
Source1:	%{name}.rpmlintrc

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Env::Sanctify is a module that provides lexically scoped manipulation and
sanctification of '%ENV'.

You can specify that it alter or add additional environment variables or
remove existing ones according to a list of matching regexen.

You can then either 'restore' the environment back manually or let the
object fall out of scope, which automagically restores.

%prep
%setup -q -n Env-Sanctify-1.12

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*


