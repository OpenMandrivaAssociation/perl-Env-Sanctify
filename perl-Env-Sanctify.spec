%define upstream_name    Env-Sanctify
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Lexically scoped sanctification of %ENV

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Env/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	%{name}.rpmlintrc

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*


