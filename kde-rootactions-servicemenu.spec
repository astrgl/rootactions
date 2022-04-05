%define oname	rootactions-servicemenu

Summary:	Root actions for Dolphin context menu
Name:		kde-rootactions-servicemenu
Version:	2.9.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-apps.org/content/show.php/?content=48411
Source0:	rootactions-servicemenu-master.zip
# adapt for kdesu in %{_libdir}/kde4/libexec/kdesu
Patch0:		rootactions-servicemenu-master-fix_kdesu.patch
BuildRequires:	kde5-macros
BuildArch:	noarch

%description
Root Actions servicemenu provides a convenient way to perform
several actions 'as root', from the right-click context menu in KDE
filemanager.

%files
%doc README changelog
%{_kde5_bindir}/rootactions-servicemenu.pl
%{_kde5_services}/ServiceMenus/10-rootactionsfolders.desktop
%{_kde5_services}/ServiceMenus/11-rootactionsfiles.desktop
%{_kde5_datadir}/polkit-1/action
%{_datadir}/kde4/services/ServiceMenus/10-rootactionsfolders.desktop
%{_datadir}/kde4/services/ServiceMenus/11-rootactionsfiles.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-master
%patch0 -p1

%build

%install
install -d -m755 %{buildroot}%{_bindir}
install -m755 usr/bin/rootactions-servicemenu.pl %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_datadir}/kde4/services/ServiceMenus
install -m644 usr/share/kde4/services/ServiceMenus/* %{buildroot}%{_datadir}/kde4/services/ServiceMenus

install -d -m755 %{buildroot}%{_kde5_services}/ServiceMenus
install -m644 usr/share/kservices5/ServiceMenus/* %{buildroot}%{_kde5_services}/ServiceMenus

install -d -m755 %{buildroot}%{_kde5_datadir}/polkit-1/actions
install -m644 usr/share/polkit-1/actions/* %{buildroot}%{_kde5_datadir}/polkit-1/action
