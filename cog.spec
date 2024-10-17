%define name cog
%define version 0.8.0
%define release %mkrel 8

Name: %name
Summary: Another Gnome config tool
Version: %{version}
Release: %{release}
License: GPL
Url: https://www.krakoa.dk/linux-software.html
Group: Graphical desktop/GNOME
Source: http://www.krakoa.dk/progs/cog/%{name}-%{version}.tar.bz2
Source10:   %{name}-16.png
Source11:   %{name}-32.png
Source12:   %{name}-48.png
BuildRoot: %{_tmppath}/build-root-%{name}

BuildRequires: automake >= 1.4
Buildrequires: libgnomeui2-devel >= 2.0
Buildrequires: libglade2.0-devel >= 2.0

%description
Edit advanced Gnome settings in an easy way.

%prep
%setup -q

%build
%configure

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
install -m644 %SOURCE10 -D %{buildroot}/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %{buildroot}/%_iconsdir/%name.png
install -m644 %SOURCE12 -D %{buildroot}/%_liconsdir/%name.png


%find_lang %name --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root,0755)
%doc NEWS README TODO AUTHORS
%{_bindir}/*
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/pixmaps/%{name}*
%{_datadir}/applications/%name.desktop
%{_datadir}/cog


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-8mdv2011.0
+ Revision: 617402
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.8.0-7mdv2010.0
+ Revision: 424912
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.8.0-6mdv2009.0
+ Revision: 243591
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.8.0-4mdv2008.1
+ Revision: 148082
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Olivier Thauvin <nanardon@mandriva.org> 0.8.0-4mdv2008.0
+ Revision: 66743
- rebuild


* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 23:49:40 (53141)
- xdg menu

* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 23:45:52 (53140)
Import cog

* Mon Apr 17 2006 Olivier Thauvin <nanardon@mandriva.org> 0.8.0-2mdk
- rebuild

* Mon Mar 28 2005 Olivier Thauvin <nanardon@mandrake.org> 0.8.0-1mdk
- 0.8.0
- update url
- %%mkrel
- fix menu entry

* Wed Feb 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.1-2mdk
- Fix menu entry

* Sun Sep 14 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.6.1-1mdk
- From Bellegarde Cedric <gnumdk@wanadoo.fr>
	- Make a spec file

