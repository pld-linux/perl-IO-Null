#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Null
Summary:	IO::Null -- class for null filehandles
Summary(pl):	IO::Null - klasa do pustych uchwytów plików
Name:		perl-IO-Null
Version:	0.02
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	93d9ef6b237d916b5305520fb51a53fd
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
To jest klasa pustych uchwytów plików. Wywo³anie konstruktora tej
klasy zawsze koñczy siê sukcesem i zwracany jest pusty uchwyt pliku.
Zapis do dowolnego obiektu tej klasy jest pust± operacj±, zwracaj±c±
logiczn± prawdê. Czytanie z dowolnego obiektu tej klasy jest pust±
operacj±, zwracaj±c± pusty ci±g lub pust± listê.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
