%global goipath github.com/neilpa/yajsv
%global forgeurl https://github.com/neilpa/yajsv

Version: 1.3.0

%gometa

Name: yajsv
Release: 1%{?dist}
Summary: Yet Another JSON-Schema Validator
License: MIT
URL: %{gourl}
Source: %{gosource}
BuildRequires: golang(github.com/davecgh/go-spew/spew)
BuildRequires: golang(github.com/ghodss/yaml)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(github.com/stretchr/testify)
BuildRequires: golang(github.com/stretchr/objx)
BuildRequires: golang(github.com/xeipuuv/gojsonpointer)
BuildRequires: golang(github.com/xeipuuv/gojsonreference)
BuildRequires: golang(github.com/xeipuuv/gojsonschema)
BuildRequires: golang(gopkg.in/check.v1)
BuildRequires: golang(gopkg.in/yaml.v2)
# FIXME: copr can't find golang(github.com/pmezard/difflib)
BuildRequires: golang-github-pmezard-difflib-devel

%description
Yet Another JSON-Schema Validator. Command line tool for validating JSON and/or YAML documents against provided schemas.

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/yajsv %{goipath}

%install
install -Dpm 755 %{gobuilddir}/bin/yajsv %{buildroot}%{_bindir}/yajsv

%check
%gocheck

%files
%license LICENSE
%doc README.md
%{_bindir}/yajsv
