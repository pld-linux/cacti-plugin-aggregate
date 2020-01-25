%define		plugin	aggregate
%define		php_min_version 5.0.0
Summary:	Cacti plugin to aggregate graphs from Graph Management
Name:		cacti-plugin-%{plugin}
Version:	0.75
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{version}.tgz
# Source0-md5:	cac76371acc48a0752ae1ab5044a50bf
URL:		http://docs.cacti.net/plugin:aggregate
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti
Requires:	cacti(pia) >= 2.8
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This plugin aggregates graphs from Graph Management.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
