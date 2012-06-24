Summary:	3D file manager
Summary(pl):	Tr�jwymiarowy zarz�dca plik�w
Name:		3dfb
Version:	0.6.1
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/dz3d/%{name}-%{version}.tar.gz
# Source0-md5:	90f42a25f5fa4572faedcb00c20a8eb4
URL:		http://www.dangerz.net/3dfb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3dFB is a 3d file manager. 2d file managers work nicely, but with 3d
you can display much more information. The aim of this project is to
make a viable, workable, 3d file manager that is not a hog on
resources and can actually be usable.

%description -l pl
3dFB jest tr�jwymiarowym zarz�dc� plik�w. Dwuwymiarowi zarz�dcy
dzia�aj� dobrze, ale w 3 wymiarach mo�na wy�wietli� o wiele wi�cej
informacji. Celem tego projektu jest stworzenie u�ytecznego,
tr�jwymiarowego zarz�dcy plik�w kt�ry nie zabiera zbyt wiele zasob�w
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
