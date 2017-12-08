%define debug_package %{nil}

%global commit             a0ff2567cfb70903282db057e799fd826784d41d
%global shortcommit        %(c=%{commit}; echo ${c:0:7})

Name:	        go-bindata
Version:	3.0.7
Release:	2.git%{shortcommit}%{?dist}
Summary:	A small utility which generates Go code from any file.

Group:		Development/Tools
License:	CC0
URL:		https://github.com/jteeuwen/go-bindata

# This tarball was created with the following commands.
#
# mkdir -p go-bindata
# cd go-bindata
# export GOPATH=$PWD
# go get -d github.com/jteeuwen/go-bindata/...
# cd src/github.com/jteeuwen/go-bindata
# git checkout a0ff2567cfb70903282db057e799fd826784d41d
# cd $GOPATH/..
# tar cf - go-bindata | gzip -9 > go-bindata.tar.gz
Source0:	go-bindata.tar.gz

BuildRoot:      %{name}
BuildRequires:  golang >= 1.8

%description
A small utility which generates Go code from any file.
Useful for embedding binary data in a Go program

%prep
%setup -c -n %{name}

%build
export GOPATH=%{_builddir}/%{name}/%{name}
cd "$GOPATH/src/github.com/jteeuwen/go-bindata"
go install ./...

%install
%{__rm} -rf %{buildroot}
%{__install} -pD -m 755 "%{_builddir}/%{name}/%{name}/bin/go-bindata" %{buildroot}%{_bindir}/go-bindata

%files
%defattr(0755,root,root,-)
%{_bindir}/go-bindata

%changelog
* Fri Dec  8 2017 <hnakamur@gmail.com> - 3.0.7-2.gita0ff256
- Initial release (commit a0ff2567cfb70903282db057e799fd826784d41d)
