%define version 0.2.0
%define rel	1
%define release %mkrel %rel

Summary:	GUI Frontend of Go, Amazons and Othello
Name:		quarry
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Boards
URL:		http://home.gna.org/quarry/
Source0:	http://download.gna.org/%{name}/%{name}-%{version}.tar.gz
Source1:	http://download.gna.org/%{name}/%{name}-%{version}.tar.gz.sig
Patch0:		quarry-0.2.0-fix-str-fmt.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	librsvg2-devel
BuildRequires:	scrollkeeper
BuildRequires:	desktop-file-utils
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
%patch0 -p0

%build
%configure --bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Fix desktop file
sed -i -e 's/%{name}.png/%{name}/' \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install \
	--remove-key=Encoding \
	--remove-key=Version \
	--remove-category=Application \
	--add-category=X-MandrivaLinux-MoreApplications-Games-Boards \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%if %mdkversion < 200900
%post
%update_menus
%update_scrollkeeper
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_scrollkeeper
%clean_mime_database
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING-DOC ChangeLog NEWS README
%doc THANKS TODO
%{_gamesbindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/omf/%{name}
%{_datadir}/applications/%{name}.desktop

