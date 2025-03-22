# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate aya-rustc-llvm-proxy

Name:           rust-aya-rustc-llvm-proxy
Version:        0.9.4
Release:        %autorelease
Summary:        Dynamically proxy LLVM calls into Rust own shared library

License:        MIT
URL:            https://crates.io/crates/aya-rustc-llvm-proxy
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Dynamically proxy LLVM calls into Rust own shared library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check

%endif

%changelog
%autochangelog
