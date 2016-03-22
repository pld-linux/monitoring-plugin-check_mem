%define		plugin	check_mem
%include	/usr/lib/rpm/macros.perl
Summary:	Improved check_mem.pl Nagios Plugin
Name:		monitoring-plugin-%{plugin}
Version:	1.0
Release:	1
License:	MIT
Group:		Networking
Source0:	https://github.com/justintime/nagios-plugins/archive/master/%{plugin}.tar.gz
# Source0-md5:	6f2a4cf077b42d101670668ca1fcd77f
Source1:	%{plugin}.cfg
URL:		https://github.com/justintime/nagios-plugins
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		nrpeddir	/etc/nagios/nrpe.d
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Revision of check_mem.pl that splits out cache memory from application
memory.

%prep
%setup -qc
mv nagios-plugins-*/* .
mv check_mem/* .
cp -p %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{nrpeddir},%{plugindir}}
install -p %{plugin}.pl $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{plugin}.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
