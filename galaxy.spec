%define	rel 	1
%define	release %mkrel %{rel}

Summary:        Mandriva theme
Name:           galaxy
Version:        1.0.5
Release:        %{release}
License:        GPL
Group:          Graphical desktop/Other
URL:            http://www.mandrivalinux.com/
BuildRequires:  gtk+1.2-devel
BuildRequires:  gtk+2-devel
BuildRequires:  kdelibs-devel
BuildRequires:  kdebase-devel >= 3.1.94-11mdk
BuildRequires:  gdk-pixbuf-devel
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mandriva Galaxy theme

 
%package gnome
Summary: Mandriva theme for GNOME
Group: Graphical desktop/GNOME
Requires: gnome-icon-theme
 
%description gnome
Mandriva theme for GNOME

%package kde
Summary: 	Mandriva theme for KDE - Widget design
Group: 		Graphical desktop/KDE

%description kde
Mandriva theme for KDE - Widget design

%package kde-kwin
Summary:	Mandriva theme for KDE - Window Decorations
Group:		Graphical desktop/KDE

%description kde-kwin
Mandriva theme for KDE - Window Decorations


%prep
%setup -q 

%build

# FIXME: better fix *.m4 once and for all
export QTLIB="%{_prefix}/lib/qt3/%{_lib}"

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std


#remove unpackaged files 
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la \
  $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines/*.la

# use same config lib for all galaxy theme
cp -r $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake_config.la $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake2_config.la
cp -r $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake_config.so $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake2_config.so
cp -r $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake_config.la $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake3_config.la
cp -r $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake_config.so $RPM_BUILD_ROOT/%_libdir/kde3/kwin_mandrake3_config.so

%clean
rm -rf $RPM_BUILD_ROOT

%files gnome
%defattr(-,root,root,-)
%doc README ChangeLog
%{_libdir}/gtk-2.0/*/engines/*.so
%{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/*

%files kde-kwin
%defattr(-,root,root,-)
%_libdir/kde3/kwin3_mandrake*.la
%_libdir/kde3/kwin3_mandrake*.so*
%_libdir/kde3/kwin_mandrake*.la
%_libdir/kde3/kwin_mandrake*.so*
%_datadir/apps/kwin/*.desktop



%files kde
%defattr(-,root,root,-)
%_libdir/kde3/plugins/styles/*.la
%_libdir/kde3/plugins/styles/*.so*

%_datadir/apps/kstyle/themes/galaxy.themerc


