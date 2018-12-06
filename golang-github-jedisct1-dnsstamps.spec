# Run tests in check section
%bcond_without check

%global goipath         github.com/jedisct1/go-dnsstamps
%global commit          1e4999280f861b465e03e21e4f84d838f2f02b38

%global common_description %{expand:
DNS Stamps library for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        DNS Stamps library for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git1e49992
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180517git1e49992
- First package for Fedora

