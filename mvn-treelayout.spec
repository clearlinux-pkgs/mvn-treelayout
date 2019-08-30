#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-treelayout
Version  : 1.0.3
Release  : 3
URL      : https://github.com/abego/treelayout/archive/v1.0.3.tar.gz
Source0  : https://github.com/abego/treelayout/archive/v1.0.3.tar.gz
Source1  : https://repo1.maven.org/maven2/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.jar
Source2  : https://repo1.maven.org/maven2/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.pom
Source3  : https://repo1.maven.org/maven2/org/abego/treelayout/org.abego.treelayout.core/1.0.3/org.abego.treelayout.core-1.0.3.jar
Source4  : https://repo1.maven.org/maven2/org/abego/treelayout/org.abego.treelayout.core/1.0.3/org.abego.treelayout.core-1.0.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-treelayout-data = %{version}-%{release}
Requires: mvn-treelayout-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
# abego TreeLayout
__Efficient and Customizable Tree Layout Algorithm in Java__
The TreeLayout creates tree layouts for arbitrary trees. It is not restricted to a specific output or format, but can be used for any kind of two dimensional diagram. Examples are Swing based components, SVG files, and many more. This is possible because TreeLayout separates the layout of a tree from the actual rendering.

%package data
Summary: data components for the mvn-treelayout package.
Group: Data

%description data
data components for the mvn-treelayout package.


%package license
Summary: license components for the mvn-treelayout package.
Group: Default

%description license
license components for the mvn-treelayout package.


%prep
%setup -q -n treelayout-1.0.3

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-treelayout
cp org.abego.treelayout.demo/src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/mvn-treelayout/org.abego.treelayout.demo_src_LICENSE.TXT
cp org.abego.treelayout/src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/mvn-treelayout/org.abego.treelayout_src_LICENSE.TXT
cp org.abego.treelayout/src/main/java/org/abego/treelayout/doc-files/LICENSE.TXT %{buildroot}/usr/share/package-licenses/mvn-treelayout/org.abego.treelayout_src_main_java_org_abego_treelayout_doc-files_LICENSE.TXT
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.3/org.abego.treelayout.core-1.0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.3/org.abego.treelayout.core-1.0.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.jar
/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.pom
/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.3/org.abego.treelayout.core-1.0.3.jar
/usr/share/java/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.3/org.abego.treelayout.core-1.0.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-treelayout/org.abego.treelayout.demo_src_LICENSE.TXT
/usr/share/package-licenses/mvn-treelayout/org.abego.treelayout_src_LICENSE.TXT
/usr/share/package-licenses/mvn-treelayout/org.abego.treelayout_src_main_java_org_abego_treelayout_doc-files_LICENSE.TXT
