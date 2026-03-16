# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Han Gao <gaohan@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
%global modpath %{_prefix}/lib/modules/%{kver}

%ifarch riscv64
#!BuildConstraint: hardware:jobs 32
%endif

# Whether dtbs needed for arch
%ifarch riscv64
%global need_dtbs 1
%else
%global need_dtbs 0
%endif

%global signmodules 1
%global kver %{version}-%{release}
%global kernel_make_flags LD=ld.bfd KBUILD_BUILD_VERSION=%{release}

Name:           linux
Version:        6.19.8
Release:        %autorelease
Summary:        The Linux Kernel
License:        GPL-2.0-only
URL:            https://www.kernel.org/
#!RemoteAsset:  sha256:aada4722db8bcfa0b9732851856d405082b6a4fa2e3ab067be8db17cdd115b38
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/%{name}-%{version}.tar.xz
Source1:        config.%{_arch}

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  binutils
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  bc
BuildRequires:  cpio
BuildRequires:  dwarves
BuildRequires:  gettext
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  zstd
BuildRequires:  libdebuginfod-dummy-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(slang)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  kmod
BuildRequires:  rpm-config-openruyi

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-modules%{?_isa} = %{version}-%{release}
%if %{need_dtbs}
Requires:       %{name}-dtbs%{?_isa} = %{version}-%{release}
%endif
Requires(post):   kmod
Requires(post):   kernel-install
Requires(postun): kernel-install

%patchlist
0001-UPSTREAM-PCI-MSI-Convert-the-boolean-no_64bit_msi-fl.patch
0002-UPSTREAM-PCI-MSI-Check-the-device-specific-address-m.patch
0003-UPSTREAM-drm-radeon-Make-MSI-address-limit-based-on-.patch
0004-UPSTREAM-ALSA-hda-intel-Make-MSI-address-limit-based.patch
0005-UPSTREAM-riscv-dts-sophgo-enable-hardware-clock-RTC-.patch
0006-UPSTREAM-riscv-dts-sophgo-Move-PLIC-and-CLINT-node-i.patch
0007-UPSTREAM-riscv-dts-sophgo-fix-the-node-order-of-SG20.patch
0008-UPSTREAM-riscv-dts-spacemit-Enable-i2c8-adapter-for-.patch
0009-UPSTREAM-riscv-dts-spacemit-Define-fixed-regulators-.patch
0010-UPSTREAM-riscv-dts-spacemit-Define-the-P1-PMIC-regul.patch
0011-UPSTREAM-pwm-th1520-Replace-kernel-c_str-with-C-Stri.patch
0012-UPSTREAM-dt-bindings-phy-spacemit-Add-SpacemiT-PCIe-.patch
0013-UPSTREAM-dt-bindings-phy-spacemit-Introduce-PCIe-PHY.patch
0014-UPSTREAM-phy-spacemit-Introduce-PCIe-combo-PHY.patch
0015-UPSTREAM-riscv-dts-spacemit-Add-a-PCIe-regulator.patch
0016-UPSTREAM-riscv-dts-spacemit-PCIe-and-PHY-related-upd.patch
0017-UPSTREAM-dt-bindings-i2c-spacemit-add-optional-reset.patch
0018-UPSTREAM-i2c-k1-add-reset-support.patch
0019-UPSTREAM-riscv-dts-spacemit-add-reset-property.patch
0020-UPSTREAM-dt-bindings-phy-spacemit-add-K1-USB2-PHY.patch
0021-UPSTREAM-phy-spacemit-support-K1-USB2.0-PHY-controll.patch
0022-UPSTREAM-riscv-dts-spacemit-Add-USB2-PHY-node-for-K1.patch
0023-UPSTREAM-riscv-dts-spacemit-Add-DWC3-USB-3.0-control.patch
0024-UPSTREAM-riscv-dts-spacemit-Enable-USB3.0-on-BananaP.patch
0025-UPSTREAM-dt-bindings-pinctrl-spacemit-convert-drive-.patch
0026-UPSTREAM-dt-bindings-pinctrl-spacemit-add-K3-SoC-sup.patch
0027-UPSTREAM-pinctrl-spacemit-k3-add-initial-pin-support.patch
0028-UPSTREAM-pinctrl-spacemit-k3-adjust-drive-strength-a.patch
0029-UPSTREAM-dt-bindings-pinctrl-spacemit-add-syscon-pro.patch
0030-UPSTREAM-pinctrl-spacemit-support-I-O-power-domain-c.patch
0031-UPSTREAM-riscv-dts-spacemit-pinctrl-update-register-.patch
0032-UPSTREAM-dt-bindings-riscv-update-ratified-version-o.patch
0033-UPSTREAM-dt-bindings-riscv-Add-B-ISA-extension-descr.patch
0034-UPSTREAM-dt-bindings-riscv-Add-descriptions-for-Za64.patch
0035-UPSTREAM-dt-bindings-riscv-Add-Ssccptr-Sscounterenw-.patch
0036-UPSTREAM-dt-bindings-riscv-Add-Sha-and-its-comprised.patch
0037-UPSTREAM-riscv-dts-sophgo-sg2044-Add-b-ISA-extension.patch
0038-UPSTREAM-riscv-dts-spacemit-k1-Add-b-ISA-extension.patch
0039-UPSTREAM-dt-bindings-riscv-add-SpacemiT-X100-CPU-com.patch
0040-UPSTREAM-dt-bindings-timer-add-SpacemiT-K3-CLINT.patch
0041-UPSTREAM-dt-bindings-interrupt-controller-add-Spacem.patch
0042-UPSTREAM-dt-bindings-interrupt-controller-add-Spacem.patch
0043-UPSTREAM-dt-bindings-riscv-spacemit-add-K3-and-Pico-.patch
0044-UPSTREAM-riscv-dts-spacemit-add-initial-support-for-.patch
0045-UPSTREAM-riscv-dts-spacemit-add-K3-Pico-ITX-board-su.patch
0046-UPSTREAM-clk-spacemit-Hide-common-clock-driver-from-.patch
0047-UPSTREAM-clk-spacemit-prepare-common-ccu-header.patch
0048-UPSTREAM-clk-spacemit-extract-common-ccu-functions.patch
0049-UPSTREAM-clk-spacemit-add-platform-SoC-prefix-to-res.patch
0050-UPSTREAM-reset-spacemit-fix-auxiliary-device-id.patch
0051-UPSTREAM-dt-bindings-soc-spacemit-k3-add-clock-suppo.patch
0052-UPSTREAM-clk-spacemit-ccu_mix-add-inverted-enable-ga.patch
0053-UPSTREAM-clk-spacemit-ccu_pll-add-plla-type-clock.patch
0054-UPSTREAM-clk-spacemit-k3-extract-common-header.patch
0055-UPSTREAM-clk-spacemit-k3-add-the-clock-tree.patch
0056-UPSTREAM-dt-bindings-soc-spacemit-Add-K3-reset-suppo.patch
0057-UPSTREAM-reset-Create-subdirectory-for-SpacemiT-driv.patch
0058-UPSTREAM-reset-spacemit-Extract-common-K1-reset-code.patch
0059-UPSTREAM-reset-spacemit-Add-SpacemiT-K3-reset-driver.patch
0060-UPSTREAM-dt-bindings-gpio-spacemit-add-compatible-na.patch
0061-UPSTREAM-gpio-spacemit-Add-GPIO-support-for-K3-SoC.patch
0062-UPSTREAM-riscv-dts-spacemit-Disable-ETH-PHY-sleep-mo.patch
0063-UPSTREAM-dt-bindings-clock-thead-th1520-clk-ap-Add-I.patch
0064-UPSTREAM-clk-thead-th1520-ap-Add-C910-bus-clock.patch
0065-UPSTREAM-clk-thead-th1520-ap-Support-setting-PLL-rat.patch
0066-UPSTREAM-clk-thead-th1520-ap-Add-macro-to-define-mul.patch
0067-UPSTREAM-clk-thead-th1520-ap-Support-CPU-frequency-s.patch
0068-UPSTREAM-net-spacemit-display-phy-driver-information.patch
0069-UPSTREAM-gpio-spacemit-k1-Use-PDR-for-pin-direction-.patch
0070-UPSTREAM-phy-Kconfig-spacemit-add-COMMON_CLK-depende.patch
0071-UPSTREAM-mfd-Kconfig-Default-MFD_SPACEMIT_P1-to-m-if.patch
0072-UPSTREAM-riscv-dts-spacemit-sdhci-add-reset-support.patch
0073-UPSTREAM-dt-bindings-interrupt-controller-sifive-pli.patch
0074-UPSTREAM-PCI-dwc-Use-multiple-iATU-windows-for-mappi.patch
0075-UPSTREAM-powerpc-pci-Initialize-msi_addr_mask-for-OF.patch
0076-UPSTREAM-sparc-PCI-Initialize-msi_addr_mask-for-OF-c.patch
0077-UPSTREAM-net-spacemit-Fix-error-handling-in-emac_all.patch
0078-UPSTREAM-net-spacemit-Fix-error-handling-in-emac_tx_.patch
0079-FROMLIST-riscv-errata-Add-ERRATA_THEAD_WRITE_ONCE-fi.patch
0080-FROMLIST-PCI-Release-BAR0-of-an-integrated-bridge-to.patch
0081-BACKPORT-FROMLIST-drm-ttm-save-the-device-s-DMA-cohe.patch
0082-BACKPORT-FROMLIST-drm-ttm-downgrade-cached-to-write_.patch
0083-FROMLIST-NFU-riscv-dts-thead-Add-CPU-clock-and-OPP-t.patch
0084-FROMLIST-dt-bindings-vendor-prefixes-add-verisilicon.patch
0085-FROMLIST-dt-bindings-display-add-verisilicon-dc.patch
0086-FROMLIST-drm-verisilicon-add-a-driver-for-Verisilico.patch
0087-FROMLIST-dt-bindings-display-bridge-add-binding-for-.patch
0088-FROMLIST-drm-bridge-add-a-driver-for-T-Head-TH1520-H.patch
0089-FROMLIST-riscv-dts-thead-add-DPU-and-HDMI-device-tre.patch
0090-FROMLIST-riscv-dts-thead-lichee-pi-4a-enable-HDMI.patch
0091-FROMLIST-MAINTAINERS-assign-myself-as-maintainer-for.patch
0092-FROMLIST-mailmap-map-all-Icenowy-Zheng-s-mail-addres.patch
0093-FROMLIST-dt-bindings-usb-Add-T-HEAD-TH1520-USB-contr.patch
0094-FROMLIST-usb-dwc3-add-T-HEAD-TH1520-usb-driver.patch
0095-FROMLIST-rust-export-BINDGEN_TARGET-from-a-separate-.patch
0096-FROMLIST-rust-generate-a-fatal-error-if-BINDGEN_TARG.patch
0097-FROMLIST-rust-add-a-Kconfig-function-to-test-for-sup.patch
0098-FROMLIST-RISC-V-handle-extension-configs-for-bindgen.patch
0099-FROMLIST-rust-clk-implement-Send-and-Sync.patch
0100-FROMLIST-tyr-remove-impl-Send-Sync-for-TyrData.patch
0101-FROMLIST-pwm-th1520-remove-impl-Send-Sync-for-Th1520.patch
0102-FROMLIST-dt-bindings-mmc-spacemit-sdhci-add-reset-su.patch
0103-FROMLIST-mmc-sdhci-of-k1-add-reset-support.patch
0104-FROMLIST-i2c-spacemit-move-i2c_xfer_msg.patch
0105-FROMLIST-i2c-spacemit-introduce-pio-for-k1.patch
0106-FROMLIST-mfd-simple-mfd-i2c-add-a-reboot-cell-for-th.patch
0107-FROMLIST-regulator-spacemit-MFD_SPACEMIT_P1-as-depen.patch
0108-FROMLIST-rtc-spacemit-default-module-when-MFD_SPACEM.patch
0109-FROMLIST-dt-bindings-spi-add-SpacemiT-K1-SPI-support.patch
0110-FROMLIST-spi-spacemit-introduce-SpacemiT-K1-SPI-cont.patch
0111-FROMLIST-riscv-dts-spacemit-define-a-SPI-controller-.patch
0112-FROMLIST-dt-bindings-thermal-Add-SpacemiT-K1-thermal.patch
0113-FROMLIST-thermal-spacemit-k1-Add-thermal-sensor-supp.patch
0114-FROMLIST-riscv-dts-spacemit-Add-thermal-sensor-for-K.patch
0115-FROMLIST-pwm-th1520-fix-CLIPPY-1-warning.patch
0116-FROMLIST-dt-bindings-mfd-spacemit-p1-Add-individual-.patch
0117-FROMLIST-regulator-spacemit-p1-Update-supply-names.patch
0118-FROMLIST-riscv-dts-spacemit-Update-PMIC-supply-prope.patch
0119-FROMLIST-dt-bindings-mmc-spacemit-sdhci-add-support-.patch
0120-FROMLIST-mmc-sdhci-of-k1-spacemit-Add-support-for-K3.patch
0121-FROMLIST-PCI-cadence-Support-platform-specific-hooks.patch
0122-FROMLIST-PCI-sg2042-Avoid-L0s-and-L1-on-Sophgo-2042-.patch
0123-FROMLIST-riscv-dts-spacemit-adapt-regulator-node-nam.patch
0124-FROMLIST-riscv-dts-spacemit-pcie-fix-missing-power-r.patch
0125-FROMLIST-net-spacemit-Remove-unused-buff_addr-fields.patch
0126-FROMLIST-net-spacemit-Free-rings-of-memory-after-unm.patch
0127-FROMLIST-riscv-mm-Extract-helper-mark_new_valid_map.patch
0128-FROMLIST-riscv-kfence-Call-mark_new_valid_map-for-kf.patch
0129-FROMLIST-riscv-mm-Rename-new_vmalloc-into-new_valid_.patch
0130-FROMLIST-riscv-mm-Use-the-bitmap-API-for-new_valid_m.patch
0131-FROMLIST-riscv-mm-Unconditionally-sfence.vma-for-spu.patch
0132-FROMLIST-dt-bindings-serial-8250-spacemit-fix-clock-.patch
0133-FROMLIST-riscv-dts-spacemit-k3-add-clock-tree.patch
0134-FROMLIST-riscv-dts-spacemit-k3-add-pinctrl-support.patch
0135-FROMLIST-riscv-dts-spacemit-k3-add-GPIO-support.patch
0136-FROMLIST-riscv-dts-spacemit-k3-add-full-resource-to-.patch
0137-FROMLIST-dt-bindings-net-Add-support-for-Spacemit-K3.patch
0138-FROMLIST-net-stmmac-platform-Add-snps-dwmac-5.40a-IP.patch
0139-FROMLIST-net-stmmac-Add-glue-layer-for-Spacemit-K3-S.patch
0140-FROMLIST-riscv-dts-spacemit-k3-Add-ethernet-device-n.patch
0141-FROMLIST-phy-k1-usb-add-disconnect-function-support.patch
0142-FROMLIST-dt-bindings-phy-spacemit-k3-add-USB2-PHY-su.patch
0143-FROMLIST-phy-k1-usb-k3-add-USB2-PHY-support.patch
0144-FROMLIST-clk-spacemit-ccu_mix-fix-inverted-condition.patch
0145-FROMLIST-riscv-enable-HAVE_IOREMAP_PROT.patch
0146-FROMLIST-cpufreq-dt-platdev-Add-SpacemiT-K1-SoC-to-t.patch
0147-FROMLIST-riscv-dts-spacemit-Add-cpu-scaling-for-K1-S.patch
0148-FROMLIST-riscv-dts-spacemit-Add-linux-pci-domain-to-.patch
0149-FROMLIST-riscv-mm-WARN_ON-for-bad-addresses-in-vmemm.patch
0150-FROMLIST-riscv-mm-Define-DIRECT_MAP_PHYSMEM_END.patch
0151-FROMLIST-drm-verisilicon-add-max-cursor-size-to-HWDB.patch
0152-FROMLIST-drm-verisilicon-add-support-for-cursor-plan.patch
0153-FROMLIST-riscv-dts-spacemit-Enable-i2c8-adapter-for-.patch
0154-FROMLIST-riscv-dts-spacemit-Define-fixed-regulators-.patch
0155-FROMLIST-riscv-dts-spacemit-Define-the-P1-PMIC-regul.patch
0156-FROMLIST-riscv-dts-spacemit-Enable-USB3.0-PCIe-on-Or.patch
0157-FROMLIST-dt-bindings-hwmon-moortec-mr75203-adapt-mul.patch
0158-FROMLIST-riscv-dts-thead-th1520-add-coefficients-to-.patch
0159-FROMLIST-pinctrl-spacemit-return-ENOTSUPP-for-unsupp.patch
0160-FROMLIST-gpio-spacemit-k1-Add-set_config-callback-su.patch
0161-FROMLIST-reset-spacemit-k3-Decouple-composite-reset-.patch
0162-FROMLIST-irqchip-riscv-rpmi-sysmsi-Fix-mailbox-chann.patch
0163-XUANTIE-riscv-dts-th1520-add-licheepi4a-16g-support.patch
0164-XUANTIE-riscv-dts-thead-Add-TH1520-USB-nodes.patch
0165-XUANTIE-riscv-dts-thead-Add-TH1520-I2C-nodes.patch
0166-XUANTIE-riscv-dts-thead-Add-Lichee-Pi-4A-IO-expansio.patch
0167-XUANTIE-riscv-dts-thead-Enable-Lichee-Pi-4A-USB.patch
0168-REVYOS-riscv-dts-th1520-rename-thead-to-xuantie.patch
0169-REVYOS-riscv-dts-th1520-add-xuantie-th1520-mbox-r.patch
0170-SOPHGO-dt-bindings-nvmem-Add-SG2044-eFuse-controller.patch
0171-SOPHGO-nvmem-Add-Sophgo-SG2044-eFuse-driver.patch
0172-SOPHGO-riscv-dts-sophgo-sg2044-Add-eFUSE-device.patch
0173-SOPHGO-riscv-sg2042-errata-Replace-thead-cache-clean.patch
0174-SOPHGO-dts-sg2044-Modify-pcie-bar-address.patch
0175-REVYSR-dt-bindings-net-ultrarisc-dp1000-gmac-Add-sup.patch
0176-REVYSR-net-stmmac-add-support-for-dwmac-5.10a.patch
0177-RVCK-riscv-dp1000-8250_dw-support-ultrarisc-dp1000-u.patch
0178-RVCK-riscv-dts-add-dp1000.dts-for-UltraRIsc-DP1000-S.patch
0179-RVCK-riscv-dp1000-arch-add-UltraRISC-DP1000-SoC-supp.patch
0180-RVCK-riscv-dp1000-pci-support-UltraRISC-pcie-rc.patch
0181-RVCK-pinctrl-add-pinctrl-dirver-for-UltraRisc-DP1000.patch
0182-RVCK-dts-add-pinctrl-dtsi-dts-for-UltraRisc-DP1000.patch
0183-RVCK-riscv-dp1000-pci-Add-custom-PCI-host-ops.patch
0184-RVCK-riscv-dp1000-dts-add-the-dts-of-UltraRISC-dp100.patch
0185-RVCK-riscv-dp1000-dts-Move-mmc0-node-from-SoC-to-boa.patch
0186-RVCK-riscv-dp1000-plic-add-plic-early-init-supports.patch
0187-RVCK-pcie-ultrarisc-Add-suspend-resume-support.patch
0188-RVCK-riscv-dp1000-dts-Move-chosen-node-from-common-t.patch
0189-RVCK-dts-riscv-ultrarisc-Refactor-DP1000-device-tree.patch
0190-RVCK-riscv-pinctrl-ultrarisc-Implement-pin-configura.patch
0191-RVCK-riscv-dts-dp1000-add-dts-dtsi-for-Milk-V-Titan-.patch
0192-REVYSR-pinctrl-ultrarisc-cleanup-probe-remove.patch

%description
This is a meta-package that installs the core kernel image and modules.
For a minimal boot environment, install the 'linux-core' package instead.

%package        core
Summary:        The core Linux kernel image and initrd

%description    core
Contains the bootable kernel image (vmlinuz) and a generic, pre-built initrd,
providing the minimal set of files needed to boot the system.

%package        modules
Summary:        Kernel modules for the Linux kernel
Requires:       %{name}-core = %{version}-%{release}

%description    modules
Contains all the kernel modules (.ko files) and associated metadata for
the hardware drivers and kernel features.

%package        devel
Summary:        Development files for building external kernel modules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dwarves

%description    devel
This package provides the kernel headers and Makefiles necessary to build
external kernel modules against the installed kernel. The development files are
located at %{_usrsrc}/kernels/%{kver}, with symlinks provided under
%{_prefix}/lib/modules/%{kver}/ for compatibility.

%if %{need_dtbs}
%package        dtbs
Summary:        Devicetree blob files from Linux sources

%description    dtbs
This package provides the DTB files built from Linux sources that may be used
for booting.
%endif

%prep
%autosetup -p1
cp %{SOURCE1} .config
echo "-%{release}" > localversion

%conf
%make_build %{kernel_make_flags} olddefconfig

%build

%make_build %{kernel_make_flags}

%if %{need_dtbs}
%make_build %{kernel_make_flags} dtbs
%endif

%install
%define ksrcpath %{buildroot}%{_usrsrc}/kernels/%{kver}
install -d %{buildroot}%{modpath} %{ksrcpath}

%make_build %{kernel_make_flags} INSTALL_MOD_PATH=%{buildroot}%{_prefix} INSTALL_MOD_STRIP=1 DEPMOD=true modules_install

%if %{need_dtbs}
%make_build %{kernel_make_flags} INSTALL_DTBS_PATH=%{buildroot}%{modpath}/dtb dtbs_install
%endif

%make_build run-command %{kernel_make_flags} KBUILD_RUN_COMMAND="$(pwd)/scripts/package/install-extmod-build %{ksrcpath}"

pushd %{buildroot}%{modpath}
ln -sf %{_usrsrc}/kernels/%{kver} build
ln -sf %{_usrsrc}/kernels/%{kver} source
popd

install -Dm644 $(make %{kernel_make_flags} -s image_name) %{buildroot}%{modpath}/vmlinuz

echo "Module signing would happen here for version %{kver}."

%post
%{_bindir}/kernel-install add %{kver} %{modpath}/vmlinuz

%postun
if [ $1 -eq 0 ] ; then
    %{_bindir}/kernel-install remove %{kver}
fi

%files
%license COPYING
%doc README

%files core
%{modpath}/vmlinuz

%files modules
%{modpath}/*
%exclude %{modpath}/vmlinuz
%exclude %{modpath}/build
%exclude %{modpath}/source

%files devel
%{_usrsrc}/kernels/%{kver}/
%{modpath}/build
%{modpath}/source

%if %{need_dtbs}
%files dtbs
%{modpath}/dtb
%endif

%changelog
%{?autochangelog}
