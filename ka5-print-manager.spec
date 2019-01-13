%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		print-manager
Summary:	Print manager
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	91d5a8a0150d143e93f9ccb3fd735c5b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool for managing print jobs and printers.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/configure-printer
%attr(755,root,root) %{_bindir}/kde-add-printer
%attr(755,root,root) %{_bindir}/kde-print-queue
%attr(755,root,root) %{_libdir}/libkcupslib.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_printer_manager.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_printmanager.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/printmanager
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/printmanager/libprintmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/qmldir
%{_desktopdir}/org.kde.ConfigurePrinter.desktop
%{_desktopdir}/org.kde.PrintQueue.desktop
%{_desktopdir}/org.kde.kde-add-printer.desktop
%{_datadir}/knotifications5/printmanager.notifyrc
%{_datadir}/kservices5/kcm_printer_manager.desktop
%{_datadir}/kservices5/kded/printmanager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.printmanager.desktop
%{_datadir}/metainfo/org.kde.plasma.printmanager.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager
