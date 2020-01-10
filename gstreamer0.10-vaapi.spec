
%define name	gstreamer0.10-vaapi
%define oname	gstreamer-vaapi
# tag 0.4.0 from git://gitorious.org/vaapi/gstreamer-vaapi.git
%define version	0.4.0
%define rel	1

%define api	0.10
%define major	0
%define libname	%mklibname gstvaapi %api %major
%define devname	%mklibname -d gstvaapi %api

Summary:	VA-API support for GStreamer
Name:		%{name}
Version:	%{version}
Release:	%rel
URL:		http://www.splitted-desktop.com/~gbeauchesne/gstreamer-vaapi/
Source0:		http://www.splitted-desktop.com/~gbeauchesne/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.gz
source1:		.abf.yml
License:	GPLv2+
Group:		Video
BuildRequires:	libgstreamer-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libva-devel
buildrequires:	pkgconfig(gstreamer-basevideo-0.10)
buildrequires:	pkgconfig(gstreamer-codecparsers-0.10)
BUildRequires:	gtk-doc

%description
gstreamer-vaapi consists of a collection of VA-API based plugins for
GStreamer and helper libraries, allowing the use of VA-API acceleration
in applications that GStreamer for video playback.

%package -n %{libname}
Summary:	GStreamer VA-API support libraries
License:	LGPLv2+
Group:		System/Libraries

%description -n %{libname}
Helper libraries used by gstreamer0.10-vaapi.

%package -n %{devname}
Summary:	Development files for libgstvaapi
License:	LGPLv2+
Group:		System/Libraries

%description -n %{devname}
Development files for the libgstvaapi helper libraries.

%prep
%setup -q -n %{oname}-%{version}
%autopatch -p1

%build
export LIBS="-ldl"
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

# unneeded files and static libs
rm %{buildroot}%{_libdir}/*.a

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_libdir}/gstreamer-%{api}/libgstvaapi.so

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgstvaapi*-%{api}.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_includedir}/gstreamer-%{api}/gst/vaapi
%{_libdir}/libgstvaapi*-%{api}.so
%{_libdir}/pkgconfig/gstreamer-vaapi*-%{api}.pc


%changelog
* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.2.5-2mdv2011.0
+ Revision: 593569
- rebuild for gstreamer provides

* Thu Aug 12 2010 Anssi Hannula <anssi@mandriva.org> 0.2.5-1mdv2011.0
+ Revision: 569183
- initial Mandriva release

