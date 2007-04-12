%define name cog
%define version 0.8.0
%define release %mkrel 3

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

mkdir -p %{buildroot}/%{_menudir}
cat << EOF > %{buildroot}/%{_menudir}/%{name}
?package(%name):command="%{_bindir}/cog" icon="%name.png" \
                needs="X11" section="System/Configuration/Other" \
 title="Cog" longtitle="Edit your gnome preferences" needs="gnome" \
xdg="true"
EOF

%find_lang %name --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root,0755)
%doc NEWS README TODO AUTHORS
%{_bindir}/*
%{_menudir}/%{name}
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/pixmaps/%{name}*
%{_datadir}/applications/%name.desktop
%{_datadir}/cog

