%include	/usr/lib/rpm/macros.perl
Summary:	Tool for flexible configuration software packages
Summary(pl):	Narz�dzie do �atwego konfigurowania pakiet�w
Name:		itchconfig
Version:	0.0.4
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	fd10a534c3a845f07cac8be8c301e266
URL:		http://itchconfig.sourceforge.net/
BuildRequires:	m4 >= 1.3
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
itchconfig is a tool for the flexible, non-interactive configuration
of software packages on Unix-like operating systems. Similar to the
GNU autoconf/automake tools, a configure script  generated by
itchconfig checks several properties  of a user's computer (C
compiler, libraries, ...) and generates all files (e.g. the Makefile)
which are necessary to build an executable program from the source
code of a software package on the user's computer.

%description -l pl
itchconfig jest narz�dziem do �atwego, nie interaktywnego ustawiania
konfiguracji pakiet�w na systemach UNIX-owych. Podobnie jak GNU
autoconf/automake skrypt configure wygenerowany przez itchconfig
sprawdza kilka w�asno�ci komputera u�ytkownika(kompilator C, biblioteki,
...) oraz generuje wszystkie pliki(np Makefile) potrzebne do zbudowania
wersji wykonywalnej programu z �r�de� na komputerze u�ytkownika.

%prep
%setup -q

%build
./configure \
	--path-prefix=%{_prefix} \
	--path-man=%{_mandir} \
	--path-info=%{_infodir}

%install
rm -rf $RPM_BUILD_ROOT

# doesn't work. how to fix it???

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
