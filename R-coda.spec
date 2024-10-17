%global packname  coda
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.16.1
Release:          2
Summary:          Output analysis and diagnostics for MCMC
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/coda_0.16-1.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-lattice 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lattice

%description
Output analysis and diagnostics for Markov Chain Monte Carlo simulations.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.14_6-1
+ Revision: 775967
- Import R-coda
- Import R-coda


