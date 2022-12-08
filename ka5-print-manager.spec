#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		print-manager
Summary:	Print manager
Name:		ka5-%{kaname}
Version:	22.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	306606f04c43605ee9aa2e5f4a7ccaa1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-plasma-framework-devel >= %{kframever}
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
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


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
%dir %{_libdir}/qt5/qml/org/kde/plasma/printmanager
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/printmanager/libprintmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/qmldir
%{_desktopdir}/org.kde.ConfigurePrinter.desktop
%{_desktopdir}/org.kde.PrintQueue.desktop
%{_desktopdir}/org.kde.kde-add-printer.desktop
%{_datadir}/knotifications5/printmanager.notifyrc
%{_datadir}/metainfo/org.kde.plasma.printmanager.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/printmanager.so
%{_datadir}/metainfo/org.kde.print-manager.metainfo.xml
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_printer_manager.so
%{_desktopdir}/kcm_printer_manager.desktop
