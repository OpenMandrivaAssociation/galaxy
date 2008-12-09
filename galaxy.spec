Summary:        Mandriva Galaxy theme
Name:           galaxy
Version:        1.0.6
Release:        %mkrel 2
License:        GPLv2+
Group:          Graphical desktop/Other
URL:            http://www.mandrivalinux.com/
BuildRequires:  gtk+1.2-devel
BuildRequires:  gtk+2-devel
BuildRequires:  kdelibs-devel
BuildRequires:  kdebase3-devel >= 3.1.94-11mdk
BuildRequires:  gdk-pixbuf-devel
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mandriva Galaxy theme

 
%package gnome
Summary: Mandriva Galaxy theme for GTK+2 and GNOME
Group: Graphical desktop/GNOME
Requires: gnome-icon-theme
 
%description gnome
Mandriva theme for GNOME and GTK2 applications

%package gtk12
Summary: Mandriva Galaxy theme for GTK+ 1.2 applications
Group: Graphical desktop/GNOME
Conflicts: galaxy-gnome < 1.0.5-2mdv
 
%description gtk12
Mandriva Galaxy theme for GTK 1.2 applications

%package kde
Summary: 	Mandriva Galaxy theme for KDE - Widget design
Group: 		Graphical desktop/KDE

%description kde
Mandriva Galaxy theme for KDE - Widget design

%package kde-kwin
Summary:	Mandriva Galaxy theme for KDE - Window Decorations
Group:		Graphical desktop/KDE

%description kde-kwin
Mandriva Galaxy theme for KDE - Window Decorations


%prep
%setup -q 

%build

# FIXME: better fix *.m4 once and for all
export QTLIB="%{_prefix}/lib/qt3/%{_lib}"

%configure_kde3

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

# use same config lib for all galaxy theme
cp -r $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake_config.la $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake2_config.la
cp -r $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake_config.so $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake2_config.so
cp -r $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake_config.la $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake3_config.la
cp -r $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake_config.so $RPM_BUILD_ROOT/%_kde3_libdir/kde3/kwin_mandrake3_config.so

mkdir -p %buildroot{%_datadir,%_libdir}
mv %buildroot%_kde3_libdir/gtk* %buildroot%_libdir
mv %buildroot%_kde3_datadir/themes %buildroot%_datadir

#remove unpackaged files 
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la \
  $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files gnome
%defattr(-,root,root,-)
%doc README ChangeLog
%{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/*

%files gtk12
%defattr(-,root,root,-)
%{_libdir}/gtk/themes/engines/*.so

%files kde-kwin
%defattr(-,root,root,-)
%_kde3_libdir/kde3/kwin3_mandrake*.la
%_kde3_libdir/kde3/kwin3_mandrake*.so*
%_kde3_libdir/kde3/kwin_mandrake*.la
%_kde3_libdir/kde3/kwin_mandrake*.so*
%_kde3_appsdir/kwin/*.desktop



%files kde
%defattr(-,root,root,-)
%_kde3_libdir/kde3/plugins/styles/*.la
%_kde3_libdir/kde3/plugins/styles/*.so*
%_kde3_appsdir/kstyle/themes/galaxy.themerc


