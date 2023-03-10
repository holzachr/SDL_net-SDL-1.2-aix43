%define name SDL_net
%define version 1.2.9
%define release 1

Summary: SDL portable network library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_net/
License: LGPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-buildroot
Prefix: %{_prefix}
Requires: SDL

%description
This is a portable network library for use with SDL.

%package devel
Summary: Libraries and includes to develop SDL networked applications.
Group: Development/Libraries
Requires: %{name}

%description devel
This is a portable network library for use with SDL.

This is the libraries and include files you can use to develop SDL networked applications.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --disable-gui
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README CHANGES COPYING
%{prefix}/lib/lib*.a
%{prefix}/lib/lib*.la
%{prefix}/lib/lib*.so
%{prefix}/include/SDL/
%{prefix}/lib/pkgconfig/*.pc

%changelog
* Sat Feb  3 2001 Paul S Jenner <psj@firstlinux.net>
- First spec file based on SDL spec file

# end of file
