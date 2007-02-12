#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Null
Summary:	IO::Null - class for null filehandles
Summary(pl.UTF-8):   IO::Null - klasa do pustych uchwytów plików
Name:		perl-IO-Null
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	54d6084398f8b4e7062660b9ccc835a8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a class for null filehandles.

Calling a constructor of this class always succeeds, returning a new
null filehandle.

Writing to any object of this class is always a no-operation, and
returns true.

Reading from any object of this class is always no-operation, and
returns empty-string or empty-list, as appropriate.

%description -l pl.UTF-8
To jest klasa pustych uchwytów plików. Wywołanie konstruktora tej
klasy zawsze kończy się sukcesem i zwracany jest pusty uchwyt pliku.
Zapis do dowolnego obiektu tej klasy jest pustą operacją, zwracającą
logiczną prawdę. Czytanie z dowolnego obiektu tej klasy jest pustą
operacją, zwracającą pusty ciąg lub pustą listę.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
