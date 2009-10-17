#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Perl6
%define	pnam	Junction
Summary:	Perl6::Junction - Perl6 style Junction operators in Perl5
Summary(pl.UTF-8):	Perl6::Junction - operatory Junction w stylu Perl6 dla Perl5
Name:		perl-Perl6-Junction
Version:	1.40000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CF/CFRANKS/Perl6-Junction-%{version}.tar.gz
# Source0-md5:	0d94cc39ac646175ad38451ef752e982
URL:		http://search.cpan.org/dist/Perl6-Junction/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a lightweight module which provides 'Junction' operators, the
most commonly used being any and all.

Inspired by the Perl6 design docs,
http://dev.perl.org/perl6/doc/design/exe/E06.html.

Provides a limited subset of the functionality of
Quantum::Superpositions, see /"SEE ALSO" for comment.

Notice in the /SYNOPSIS above, that if you want to match against a
regular expression, you must use == or !=. Not =~ or !~. You must also
use a regex object, such as qr/\d/, not a plain regex such as /\d/.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Perl6/*.pm
%{perl_vendorlib}/Perl6/Junction
%{_mandir}/man3/*
