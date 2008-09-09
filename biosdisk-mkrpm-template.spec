
Summary: biosdisk RPM for installing Dell BIOS flash images
Name: %{name}
Version: %{version}
License: GPLv2+
Release: %{release}
Group:    Applications/File
Packager: biosdisk
Source0: %{destination}
BuildRoot: %{_tmppath}/%{name}
BuildArch: noarch
Requires: mkinitrd, syslinux, /sbin/grubby, /usr/lib/syslinux/memdisk

%description

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/boot

#place files
install -m 755 %{SOURCE0} %{buildroot}/boot

%clean
rm -rf %{buildroot}

%pre

%files
%defattr(-,root,root,-)
/boot

%post
#set up bootloader with BIOS image flash entry
if [ %{release} == "1" ]; then
    title=%{version}
else
    title=%{version}-%{release}
fi

cp -f /usr/lib/syslinux/memdisk /boot/memdisk.%{version}-%{release}
/sbin/grubby --add-kernel=/boot/memdisk.%{version}-%{release} --initrd=/boot/`basename %{SOURCE0}` --title="BIOS $title"

      
%preun
/sbin/grubby --remove-kernel=/boot/memdisk.%{version}-%{release}
rm -f /boot/memdisk.%{version}-%{release}

%postun

%changelog
