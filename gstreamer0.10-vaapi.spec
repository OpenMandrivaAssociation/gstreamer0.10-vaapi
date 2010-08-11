
%define name	gstreamer0.10-vaapi
%define oname	gstreamer-vaapi
%define version	0.2.5
%define rel	1

%define api	0.10
%define major	0
%define libname	%mklibname gstvaapi %api %major
%define devname	%mklibname -d gstvaapi %api

Summary:	VA-API support for GStreamer
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
URL:		http://www.splitted-desktop.com/~gbeauchesne/gstreamer-vaapi/
Source:		http://www.splitted-desktop.com/~gbeauchesne/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.gz
Patch0:		gstreamer-vaapi-underlinking.patch
License:	GPLv2+
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libgstreamer-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libva-devel
BuildRequires:	ffmpeg-devel
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
%apply_patches

%build
autoreconf -if
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# unneeded files and static libs
rm %{buildroot}%{_libdir}/*/*.la
rm %{buildroot}%{_libdir}/*.{la,a}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_libdir}/gstreamer-%{api}/libgstvaapiconvert.so
%{_libdir}/gstreamer-%{api}/libgstvaapidecode.so
%{_libdir}/gstreamer-%{api}/libgstvaapisink.so

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgstvaapi*-%{api}.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_includedir}/gstreamer-%{api}/gst/vaapi
%{_libdir}/libgstvaapi*-%{api}.so
%{_libdir}/pkgconfig/gstreamer-vaapi*-%{api}.pc
