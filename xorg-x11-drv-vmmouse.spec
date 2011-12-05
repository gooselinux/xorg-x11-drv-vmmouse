%global tarball xf86-input-vmmouse
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

Summary:    Xorg X11 vmmouse input driver
Name:	    xorg-x11-drv-vmmouse
Version:    12.6.5
Release:    3%{?dist}
URL:	    http://www.x.org
License:    MIT
Group:	    User Interface/X Hardware Support
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:    ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Patch0:	    abi.patch

# Yes, this is not the same as vmware.  Yes, this is intentional.
ExclusiveArch: %{ix86} x86_64

BuildRequires: xorg-x11-server-sdk >= 1.5.99.1-1

Requires: xorg-x11-server-Xorg >= 1.5.99.1-1

%description 
X.Org X11 vmmouse input driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1 -b .abi

%build
%configure --disable-static --with-hal-callouts-dir=%{_bindir}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/vmmouse_drv.so
%{_mandir}/man4/vmmouse.4*
%{_mandir}/man1/vmmouse_detect.1*
%{_bindir}/vmmouse_detect
%{_bindir}/hal-probe-vmmouse
%{_datadir}/hal/fdi/policy/20thirdparty/11-x11-vmmouse.fdi

%changelog
* Wed Jan 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 12.6.5-3
- Use global instead of define as per Packaging Guidelines

* Thu Aug 27 2009 Adam Jackson <ajax@redhat.com> 12.6.5-2
- abi.patch: Re-add. (#518589)

* Fri Aug 07 2009 Peter Hutterer <peter.hutterer@redhat.com> 12.6.5-1
- vmmouse 12.6.5
- vmmouse-12.6.4-abi.patch: Drop.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.6.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 12.6.4-2.1
- ABI bump

* Thu Jul 09 2009 Adam Jackson <ajax@redhat.com> 12.6.4-2
- Port to new server ABI (#509682)

* Wed May 13 2009 Peter Hutterer <peter.hutterer@redhat.com> 12.6.4-1
- vmmouse 12.6.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Peter Hutterer <peter.hutterer@redhat.com> 12.6.3-3
- Revert last commit, this is against Fedora policy.
  https://fedoraproject.org/wiki/Packaging:Guidelines#Configuration_files

* Mon Feb 09 2009 Peter Hutterer <peter.hutterer@redhat.com> 12.6.3-2
- Don't overwrite the fdi file on upgrade.

* Mon Dec 22 2008 Peter Hutterer <peter.hutterer@redhat.com> 12.6.3-1
- vmmouse 12.6.3

* Mon Nov 17 2008 Peter Hutterer <peter.hutterer@redhat.com> 12.6.2-1
- vmmouse 12.6.2

* Mon Oct 27 2008 Peter Hutterer <peter.hutterer@redhat.com> 12.6.1-1
- vmmouse 12.6.1

* Tue Oct 21 2008 Peter Hutterer <peter.hutterer@redhat.com> 12.5.2-1
- vmmouse 12.5.2

* Thu Mar 20 2008 Adam Jackson <ajax@redhat.com> 12.5.0-1
- vmmouse 12.5.0

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 12.4.3-4
- Autorebuild for GCC 4.3

* Wed Jan  2 2008 Jeremy Katz <katzj@redhat.com> - 12.4.3-3
- Add workaround for xserver not calling convert_proc in input drivers 
  anymore (patch from Joerg Platte on debian xmaint list)

* Tue Dec 18 2007 Jeremy Katz <katzj@redhat.com> - 12.4.3-2
- Rebuild for new xserver

* Thu Oct 11 2007 Adam Jackson <ajax@redhat.com> 12.4.3-1
- xf86-input-vmmouse 12.4.3

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 12.4.2-1
- xf86-input-vmmouse 12.4.2

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 12.4.0-4
- Rebuild for build ID

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 12.4.0-3
- Update Requires and BuildRequires.  Disown the module directories. 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 12.4.0-1
- Update to 12.4.0 from 7.1RC1.

* Wed Mar 29 2006 Adam Jackson <ajackson@redhat.com> 12.3.2.0-4
- Don't build on ia64, as per comments in the source.

* Wed Mar 29 2006 Adam Jackson <ajackson@redhat.com> 12.3.2.0-3
- Rebump to appease beehive.

* Wed Mar 29 2006 Adam Jackson <ajackson@redhat.com> 12.3.2.0-1
- Bump to 12.3.2.0 from upstream (LP64 fixes).

* Sun Feb  5 2006 Mike A. Harris <mharris@redhat.com> 12.3.1.0-1
- Initial spec file for vmmouse input driver, using xorg-x11-drv-mouse.spec
  version 1.0.3.1-1 as a template.
