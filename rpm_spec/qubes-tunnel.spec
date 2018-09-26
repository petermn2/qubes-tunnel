Name:	qubes-tunnel
Version:	1.4.0
Release:	1%{?dist}
Summary:	Qubes service for simple, secure VPN tunnels.

Group:		Qubes
License:	GPL
URL:		http://github.com/tasket/qubes-tunnel
Source0:	%{name}-%{version}.tar.gz

Requires:	iptables
Requires:	qubes-core-agent-networking

%description
Qubes service for ProxyVMs as secure VPN tunnel gateways. Combines anti-leak
firewall, DNS and systemd service that accepts config files from your
VPN provider.


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
make rpmbuild DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
groupadd -rf qtunnel
systemctl daemon-reload
systemctl enable qubes-tunnel.service

%preun
systemctl stop qubes-tunnel.service >/dev/null 2>&1
systemctl disable qubes-tunnel.service
systemctl daemon-reload

%files
%attr(744,root,root) /usr/lib/qubes/qtunnel-setup
%attr(744,root,root) /usr/lib/qubes/qtunnel-connect
%attr(744,root,root) /usr/lib/qubes/tunnel-restrict-firewall
/lib/systemd/system/qubes-tunnel.service
/lib/systemd/system/qubes-tunnel.service.d/
/lib/systemd/system/qubes-tunnel.service.d/00_generic.example
/lib/systemd/system/qubes-tunnel.service.d/10_wg.example

