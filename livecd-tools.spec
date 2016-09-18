Name:           livecd-tools
Epoch:          1
Version:        23.4
Release:        1%{?dist}
Summary:        Tools for building live CDs

License:        GPLv2
URL:            https://github.com/rhinstaller/livecd-tools
Source0:        https://github.com/rhinstaller/livecd-tools/archive/livecd-tools-%{version}.tar.gz
Patch0:         0000-revert-default-vc-font.patch
Patch2:         0002-conditional-network-configuration.patch

Requires:       python-imgcreate = %{epoch}:%{version}-%{release}
Requires:       mkisofs
Requires:       isomd5sum
Requires:       parted
Requires:       pyparted
Requires:       util-linux
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       lorax >= 18.3
Requires:       rsync
Requires:       hfsplus-tools
Requires:       syslinux
Requires:       syslinux-extlinux
Requires:       dumpet
Requires:       sssd-client
Requires:       dkms-hfsplus

BuildRequires:  python
BuildRequires:  /usr/bin/pod2man


%description
Tools for generating live CDs on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.


%package -n python-imgcreate
Summary:        Python modules for building system images
Requires:       util-linux
Requires:       coreutils
Requires:       e2fsprogs
Requires:       yum >= 3.2.18
Requires:       squashfs-tools
Requires:       pykickstart
Requires:       dosfstools >= 2.11-8
Requires:       system-config-keyboard >= 1.3.0
Requires:       python-urlgrabber
Requires:       libselinux-python
Requires:       dbus-python
Requires:       policycoreutils


%description -n python-imgcreate
Python modules that can be used for building images for things
like live image or appliances.


%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch2 -p1

%build
make


%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}%{_datadir}/doc/


%files
%doc AUTHORS COPYING README HACKING config/livecd-fedora-minimal.ks
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_bindir}/image-creator
%{_bindir}/liveimage-mount
%{_bindir}/edit-livecd
%{_bindir}/mkbiarch
%{_mandir}/man*/*


%files -n python-imgcreate
%doc API COPYING
%dir %{python_sitelib}/imgcreate
%{python_sitelib}/imgcreate/*.py
%{python_sitelib}/imgcreate/*.pyo
%{python_sitelib}/imgcreate/*.pyc


%changelog
* Sun Sep 18 2016 Jajauma's Packages <jajauma@yandex.ru> - 1:23.4-1
- Public release
