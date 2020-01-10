Name: hunspell-da
Summary: Danish hunspell dictionaries
Version: 1.7.42
Release: 1%{?dist}
Source: http://da.speling.org/filer/myspell-da-%{version}.tar.bz2
Group: Applications/Text
URL: http://da.speling.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Danish hunspell dictionaries.

%prep
%setup -q -n myspell-da-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README Copyright contributors COPYING
%{_datadir}/myspell/*

%changelog
* Thu Dec 31 2013 Caolán McNamara <caolanm@redhat.com> - 1.7.42-1
- latest version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 1.7.41-1
- latest version

* Mon Mar 12 2012 Caolán McNamara <caolanm@redhat.com> - 1.7.40-1
- latest version

* Fri Mar 09 2012 Caolán McNamara <caolanm@redhat.com> - 1.7.39-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 04 2011 Caolán McNamara <caolanm@redhat.com> - 1.7.37-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.36-1
- latest version

* Tue Sep 28 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.35-1
- latest version

* Wed Jul 28 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.34-1
- latest version

* Fri Mar 28 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.33-1
- latest version

* Thu Mar 11 2010 Caolán McNamara <caolanm@redhat.com> - 1.7.32-1
- latest version

* Thu Dec 10 2009 Caolán McNamara <caolanm@redhat.com> - 1.7.31-1
- latest version

* Thu Nov 05 2009 Caolán McNamara <caolanm@redhat.com> - 1.7.30-1
- latest version

* Fri Sep 04 2009 Caolán McNamara <caolanm@redhat.com> - 1.7.29-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Caolán McNamara <caolanm@redhat.com> - 1.7.28-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 02 2009 Caolán McNamara <caolanm@redhat.com> - 1.7.27-1
- latest version

* Sun Nov 23 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.26-1
- latest version

* Tue Oct 14 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.25-1
- latest version

* Mon Sep 08 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.24-1
- latest version

* Thu Aug 07 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.23-1
- latest version

* Mon Jul 07 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.22-1
- latest version

* Fri May 30 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.21-1
- latest version

* Thu Apr 24 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.20-1
- latest version

* Mon Mar 17 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.19-1
- latest version

* Wed Feb 13 2008 Caolán McNamara <caolanm@redhat.com> - 1.7.18-1
- latest version

* Wed Nov 28 2007 Caolán McNamara <caolanm@redhat.com> - 1.7.17-1
- latest version

* Fri Oct 05 2007 Caolán McNamara <caolanm@redhat.com> - 1.7.16-1
- latest version

* Thu Aug 30 2007 Caolán McNamara <caolanm@redhat.com> - 1.7.15-1
- latest version

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 1.7.14-2
- clarify license version

* Mon Jul 30 2007 Caolán McNamara <caolanm@redhat.com> - 1.7.14-1
- latest version

* Mon Jul 09 2007 Caolán McNamara <caolanm@redhat.com> - 1.7.13-1
- latest version

* Thu Feb 13 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070106-1
- new upstream dictionaries

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20050330-1
- initial version
