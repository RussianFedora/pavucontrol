Name:           pavucontrol
Version:        0.9.10
Release:        3%{?dist}.R
Summary:        Volume control for PulseAudio

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://0pointer.de/lennart/projects/pavucontrol
Source0:        http://0pointer.de/lennart/projects/pavucontrol/pavucontrol-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pulseaudio-libs-devel >= 0.9.15-3.test4
BuildRequires:  gtkmm24-devel libglademm24-devel
BuildRequires:  libsigc++20-devel lynx
BuildRequires:  desktop-file-utils
BuildRequires:  libcanberra-devel
BuildRequires:  intltool
Requires:	pulseaudio-libs >= 0.9.15-3.test5

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume control
tool ("mixer") for the PulseAudio sound server. In contrast to classic mixer
tools this one allows you to control both the volume of hardware devices and
of each playback stream separately.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/usr/share/doc/pavucontrol/README
rm $RPM_BUILD_ROOT/usr/share/doc/pavucontrol/README.html
rm $RPM_BUILD_ROOT/usr/share/doc/pavucontrol/style.css

desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --add-category="X-Fedora" --vendor="" \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc LICENSE doc/README
%{_bindir}/pavucontrol
%{_datadir}/pavucontrol
%{_datadir}/applications/pavucontrol.desktop

%changelog
* Thu Feb  2 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.9.10-3.R
- rebuilt for EL

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.10-1
- New upstream 0.9.10

* Thu Sep 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-1
- Final 0.9.9

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-0.test1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 2 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-1
- Preview of upcoming 0.9.9

* Mon Apr 13 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.8-1
- New upstream release 0.9.8

* Fri Apr 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.7-6
- Third preview of upcoming 0.9.8

* Thu Mar 5 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.7-5
- Second preview of upcoming 0.9.8

* Wed Feb 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.7-4
- Preview of upcoming 0.9.8

* Thu Oct 9 2008 Matthias Clasen  <mclasen@redhat.com> 0.9.7-3
- Handle locales properly

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.7-2
- Add intltool to deps

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.7-1
- Update to 0.9.7

* Tue Jul 15 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.1.git20080715
- Update from GIT snapshot

* Fri Mar 28 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.6-1
- Update to 0.9.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.5-2
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> 0.9.5-1
- Update to 0.9.5

* Tue Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.5-0.4.svn20070925
- Update from SVN

* Wed Sep 5 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.5-0.3.svn20070905
- Add versioned dependency on pulseaudio-libs

* Wed Sep 5 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.5-0.2.svn20070905
- Update from SVN snapshot

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.5-0.1.svn20070816
- Update from SVN snapshot

* Sat Sep  9 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-3
- Spec file cleanup.

* Sat Sep  9 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-2
- Add BuildRequires for desktop-file-utils.

* Fri Sep  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-1
- Update to 0.9.4
- Fix installation of desktop file.

* Sun Aug 20 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.3-1
- Update to 0.9.3

* Sun Jul  9 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.2-1
- Update to 0.9.2

* Thu Jun  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.1-1
- Update to 0.9.1

* Mon May 29 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.0-1
- Initial package for Fedora Extras
