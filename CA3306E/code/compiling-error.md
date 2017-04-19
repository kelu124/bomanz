[  545.211970] ca3306_drv: no symbol version for module_layout
[  545.211990] ca3306_drv: loading out-of-tree module taints kernel.
[  545.212002] ca3306_drv: module license 'unspecified' taints kernel.
[  545.212005] Disabling lock debugging due to kernel taint
[  545.212464] Unable to handle kernel paging request at virtual address 7e84cc2c
[  545.212487] pgd = cf910000
[  545.212496] [7e84cc2c] *pgd=00000000
[  545.212515] Internal error: Oops: 5 [#1] ARM
[  545.212525] Modules linked in: ca3306_drv(PO+) bnep hci_uart btbcm bluetooth brcmfmac brcmutil snd_bcm2835 cfg80211 rfkill snd_pcm snd_timer snd bcm2835_gpiomem uio_pdrv_genirq uio fixed i2c_dev fuse usb_f_ecm g_ether usb_f_rndis u_ether libcomposite dwc2 udc_core ipv6
[  545.212611] CPU: 0 PID: 2484 Comm: insmod Tainted: P           O    4.9.22+ #987
[  545.212620] Hardware name: BCM2835
[  545.212629] task: cf84d1c0 task.stack: da59e000
[  545.212659] PC is at load_module+0x1b80/0x1fb8
[  545.212687] LR is at mutex_lock+0x1c/0x48
[  545.212700] pc : [<c00838bc>]    lr : [<c05d126c>]    psr: 30000013 sp : da59fe68  ip : da59fe50  fp : da59ff14
[  545.212711] r10: d80e38c4  r9 : c05d81d4  r8 : 00000000
[  545.212720] r7 : bf426660  r6 : bf42666c  r5 : 7e84cc18  r4 : da59ff3c
[  545.212728] r3 : bf426824  r2 : 00000000  r1 : 00000000  r0 : 00000000
[  545.212738] Flags: nzCV  IRQs on  FIQs on  Mode SVC_32  ISA ARM  Segment user
[  545.212747] Control: 00c5387d  Table: 0f910008  DAC: 00000055
[  545.212755] Process insmod (pid: 2484, stack limit = 0xda59e188)
[  545.212764] Stack: (0xda59fe68 to 0xda5a0000)
[  545.212778] fe60:                   bf42666c 00007fff bf426660 c0080f1c da59fea4 00000000
[  545.212792] fe80: bf42666c bf42666c bf4304f0 bf426824 bf426754 bf4266a8 da59fee4 da59fea8
[  545.212806] fea0: c014b0cc c014aa50 dd76d000 00000000 00000000 00000000 00000000 00000000
[  545.212818] fec0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
[  545.212832] fee0: 00000000 00000000 7fffffff 00000000 00000003 7f5ab3b0 0000017b 7fffffff
[  545.212846] ff00: 00000000 00000000 da59ffa4 da59ff18 c0083ecc c0081d48 7fffffff 00000000
[  545.212859] ff20: 00000003 c0106a98 da59ff74 dd76d000 000016b8 00000000 00000002 dd76d000
[  545.212873] ff40: 000016b8 dd76e320 dd76d94c dd76dec8 0000a4f0 0000a760 00000000 00000000
[  545.212886] ff60: 00000000 000006a8 00000015 00000016 0000000e 0000000b 0000000a 00000000
[  545.212900] ff80: bef19838 ec95ed00 7f5bd000 bef19838 c000ffc4 da59e000 00000000 da59ffa8
[  545.212914] ffa0: c000fe40 c0083e3c ec95ed00 7f5bd000 00000003 7f5ab3b0 00000000 00000002
[  545.212927] ffc0: ec95ed00 7f5bd000 bef19838 0000017b 7f5ab3b0 00000002 7f5a720c 00000000
[  545.212942] ffe0: bef19670 bef19660 7f5a00ac b6e69c40 60000010 00000003 1bffa861 1bffac61
[  545.212975] [<c00838bc>] (load_module) from [<c0083ecc>] (SyS_finit_module+0x9c/0xac)
[  545.213006] [<c0083ecc>] (SyS_finit_module) from [<c000fe40>] (ret_fast_syscall+0x0/0x1c)
[  545.213023] Code: e51b3088 e1530005 e2455008 0a000009 (e5953014) 
[  545.213036] ---[ end trace c4f8f6dfd4f3a03c ]---

