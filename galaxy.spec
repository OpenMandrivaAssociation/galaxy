Summary:        Mandriva Galaxy theme
Name:           galaxy
Version:        1.0.6
Release:        %mkrel 6
License:        GPLv2+
Group:          Graphical desktop/GNOME
URL:            http://www.mandrivalinux.com/
BuildRequires:  gtk+1.2-devel
BuildRequires:  gtk+2-devel
BuildRequires:  gdk-pixbuf-devel
Source0:        %{name}-%{version}.tar.bz2
Patch0:		galaxy-1.0.6-no-kde.patch
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

%prep
%setup -q 
%apply_patches
autoreconf -fi

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

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
