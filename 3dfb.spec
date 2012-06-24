Summary:	3D File Manager
Summary(pl):	Tr�jwymiarowy menad�er plik�w
Name:		3dfb
Version:	0.5.5
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/dz3d/%{name}-%{version}.tar.gz
# Source0-md5:	31a11043c43f81c1a2f792b82934c1db
URL:		https://sourceforge.net/projects/dz3d/
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3dFB is a 3d File Manager. 2d file managers work nicely, but with 3d
you can display much more information. The aim of this project is to
make a viable, workable, 3d file manager that is not a hog on
resources and can actually be usable.

%description -l pl
3dFB jest tr�jwymiarowym menad�erem plik�w. Dwuwymiarowe menad�ery
dzia�aj� dobrze, ale w 3 wymiarach mo�esz wy�wietli� o wiele wi�cej
informacji. Celem tego projektu jest stworzenie u�ytecznego,
tr�jwymiarowego menad�era plik�w kt�ry nie zabiera zbyt wiele zasob�w
oraz mo�e by� u�yteczny.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *README ChangeLog WISHLIST AUTHORS
%attr(755,root,root) %{_bindir}/*
