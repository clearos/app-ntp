
Name: app-ntp
Epoch: 1
Version: 2.4.0
Release: 1%{dist}
Summary: NTP Server
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-network

%description
The NTP Server app provides the network time protocol service for your systems.  Computers and Internet devices can synchronize their clocks against this server to achieve a  high degree of time accuracy.

%package core
Summary: NTP Server - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-date-core >= 1:1.4.8
Requires: app-network-core >= 1:1.4.70
Requires: ntp >= 4.2.4
Requires: syswatch

%description core
The NTP Server app provides the network time protocol service for your systems.  Computers and Internet devices can synchronize their clocks against this server to achieve a  high degree of time accuracy.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/ntp
cp -r * %{buildroot}/usr/clearos/apps/ntp/

install -d -m 0755 %{buildroot}/etc/clearos/firewall.d
install -d -m 0755 %{buildroot}/var/clearos/ntp
install -d -m 0755 %{buildroot}/var/clearos/ntp/backup
install -D -m 0755 packaging/10-ntp %{buildroot}/etc/clearos/firewall.d/
install -D -m 0755 packaging/network-connected-event %{buildroot}/var/clearos/events/network_connected/ntp
install -D -m 0644 packaging/ntpd.php %{buildroot}/var/clearos/base/daemon/ntpd.php

%post
logger -p local6.notice -t installer 'app-ntp - installing'

%post core
logger -p local6.notice -t installer 'app-ntp-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/ntp/deploy/install ] && /usr/clearos/apps/ntp/deploy/install
fi

[ -x /usr/clearos/apps/ntp/deploy/upgrade ] && /usr/clearos/apps/ntp/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-ntp - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-ntp-core - uninstalling'
    [ -x /usr/clearos/apps/ntp/deploy/uninstall ] && /usr/clearos/apps/ntp/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/ntp/controllers
/usr/clearos/apps/ntp/htdocs
/usr/clearos/apps/ntp/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/ntp/packaging
%exclude /usr/clearos/apps/ntp/unify.json
%dir /usr/clearos/apps/ntp
%dir /etc/clearos/firewall.d
%dir /var/clearos/ntp
%dir /var/clearos/ntp/backup
/usr/clearos/apps/ntp/deploy
/usr/clearos/apps/ntp/language
/usr/clearos/apps/ntp/libraries
/etc/clearos/firewall.d/
/var/clearos/events/network_connected/ntp
/var/clearos/base/daemon/ntpd.php
