Name: linux-explorer
Summary: Linux Explorer Script 
Version: 0
Release: 106 
License: GPL
BuildArch: noarch
Group: Applications/Productivity
Source0: %{name}-%{version}-%{release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
Packager: joe
Vendor: Unix Consultants Ltd
URL: www.unix-consultants.co.uk 

%description
Collect Software and Hardware information for support purposes

%prep
%setup -q

%build
%install
mkdir -p  $RPM_BUILD_ROOT/opt/LINUXexplo/bin
install -m 0750 linux-explorer.sh $RPM_BUILD_ROOT/opt/LINUXexplo/bin

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "This will display after rpm installs the package!"

%files
%defattr(-,root,root,0755)
/opt/LINUXexplo/bin/linux-explorer.sh


