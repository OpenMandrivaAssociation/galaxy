Summary:        Mandriva Galaxy theme
Name:           galaxy
Version:        1.0.6
Release:        6
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


%changelog
* Wed Nov 16 2011 Götz Waschk <waschk@mandriva.org> 1.0.6-5mdv2012.0
+ Revision: 731091
- rebuild
- rebuild

* Thu Nov 11 2010 Götz Waschk <waschk@mandriva.org> 1.0.6-3mdv2011.0
+ Revision: 596070
- remove KDE support

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Dec 09 2008 Götz Waschk <waschk@mandriva.org> 1.0.6-2mdv2009.1
+ Revision: 312182
- fix KDE build
- fix KDE build deps
- fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 30 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.6-1mdv2008.1
+ Revision: 114117
- Release 1.0.6 :
 - fix crash in Gimp with Small theme

* Fri Sep 21 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.5-3mdv2008.0
+ Revision: 91905
- Add conflicts to ease upgrade

* Thu Sep 13 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.5-2mdv2008.0
+ Revision: 84976
- Improve description for gnome subpackage (Mdv bug #19455)
- Split gtk1.2 theme in its own subpackage


* Mon Mar 12 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.5-1mdv2007.1
+ Revision: 141749
- Release 1.0.5 : fix build and add support for GTK2 color scheme
- Import galaxy

* Sat Sep 16 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0.4-3
- Update kde widget style

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.4-2mdv2007.0
- Rebuild with new gtk

* Thu May 18 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.4-1mdk
- Release 1.0.4 :
  - fix all metacity theme for utility-type windows (gimp toolbox ..)

* Thu May 04 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.3-1mdk
- Release 1.0.3
 - gtk-2.0 : fix transparency bug with gnome-panel

* Mon Dec 12 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-21
- Rebuild again qt (BIC changed)

* Thu Oct 27 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-20
- Rebuild with new qt

* Sat Sep 10 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-19
- Rebuild

* Mon Sep 05 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-18
- Rebuild

* Wed Aug 31 2005 Frederic Crozat <fcrozat@mandriva.com> 1.0.2-17mdk
- Fix gtk2 theme with combobox entries (Mdk bug #17097)

* Mon Aug 22 2005 Eskild Hustvedt <eskild@mandriva.org> 1.0.2-16mdk
- Fix URL
- %%mkrel

* Thu Aug 18 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-15mdk
- Rebuild

* Fri Jul 08 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-14mdk
- Rebuild for x86_64

* Wed Jun 29 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-13mdk
- Rebuild

* Fri May 27 2005 Frederic Crozat <fcrozat@mandriva.com> 1.0.2-12mdk 
- Add missing macro in gtk engine
- fix background drawing for button without relief in normal state

* Tue May 10 2005 Frederic Crozat <fcrozat@mandriva.com> 1.0.2-11mdk 
- Rebuild with automake 1.9
- fix some gcc 4 warnings
- change descriptions

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0.2-10mdk
- Rebuild with new gcc

* Fri Apr 01 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.2-9mdk
- Disable debug
- Fix drawcombobox color

* Wed Feb 16 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.2-8mdk 
- GTK2 : Fix prelight color for CD selector

* Mon Dec 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.2-7mdk
- Fix name of widget style

* Sat Oct 02 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.2-6mdk
- Improve path bar rendering in GTK2 file chooser
- Disable libtoolize (doesn't like libtool 1.5)

* Tue Sep 14 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.2-5mdk
- Enable libtoolize
- Fix crash with perl testcase

* Wed Aug 25 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.2-4mdk
- Fix close button size in tab (Mdk bug #10928)
- Fix tooltip color in gtk theme
- Fix column title theming in Epiphany bookmarks editor

* Sat Jun 05 2004 Laurent Montel <lmontel@mandrakesoft.com> 1.0.2-3mdk
- Rebuild

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.2-2mdk
- Fix buildrequires

* Sat May 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.2-1mdk
- Release 1.0.2 :
  - fix prelight text in GtkComboBox (seen in FileSelector Filter widget) 
  - GNOME package requires gnome-icon-theme (mdk bug #9688)

* Fri May 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.1-2mdk
- Rebuild against new qt

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.1-1mdk
- Release 1.0.1 :
   - GTK 2.4 friendly
   - fix multiscreen issue
   - realize radio pixmaps lazily.

