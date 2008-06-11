%define version 0.1.15
%define rel	1
%define release %mkrel %rel

Summary:	GUI Frontend of Go, Amazons and Othello
Name:		quarry
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://home.gna.org/quarry/
Source0:	http://download.gna.org/%{name}/%{name}-%{version}.tar.gz
Source1:	http://download.gna.org/%{name}/%{name}-%{version}.tar.gz.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	librsvg2-devel
BuildRequires:	scrollkeeper
Requires(post,postun):		scrollkeeper

%description
Quarry is a multi-purpose GUI for several board games, at present Go,
Amazons and Othello. It allows users to play against computer players
(third-party programs, e.g. GNU Go) or other humans, view and edit
game records. Future versions will also support Internet game servers
(like NNGS, a Go server) and provide certain features for developers
of board game-playing engines for enhancing their programs.


%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=strategy_section
Comment=Universal board game interface
Categories=BoardGame;
Name=Quarry
EOF

%find_lang %{name} --with-gnome

%post
%update_menus
%update_scrollkeeper

%postun
%clean_menus
%clean_scrollkeeper

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_gamesbindir}/*
%{_datadir}/%{name}
%{_datadir}/omf/*
%{_datadir}/applications/mandriva-%{name}.desktop

