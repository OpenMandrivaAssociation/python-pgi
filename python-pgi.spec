%global pypi_name pgi

Name:           python-%{pypi_name}
Version:        0.0.11.2
Release:        1
Group:          Development/Python
Summary:        Pure Python GObject Introspection Bindings. Needed for gi with pypy
License:        LGPL-2.1
URL:            https://github.com/pygobject/pgi
Source0:        https://pypi.python.org/packages/source/p/pgi/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(cairocffi)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires: gobject-introspection
Requires: python
Requires: python3dist(pygobject)
Requires: python3dist(py)
Requires: python3dist(cffi)
Requires: python3dist(cairocffi)
  
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
GObject Introspection bindings written in pure Python using ctypes and cffi (optional). API compatible with PyGObject.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/pgi-%{version}-py*.*.egg-info/PKG-INFO
%{python_sitelib}/pgi-%{version}-py*.*.egg-info/
%{python_sitelib}/pgi/*
