%define name cog
%define version 0.8.0
%define release %mkrel 7

Name: %name
Summary: Another Gnome config tool
Version: %{version}
Release: %{release}
License: GPL
Url: http://www.krakoa.dk/linux-software.html
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
