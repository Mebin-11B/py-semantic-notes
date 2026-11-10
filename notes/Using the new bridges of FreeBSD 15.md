---
title: "Using the new bridges of FreeBSD 15"
url: https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/
clipped: 2026-06-17 01:41:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Using the new bridges of FreeBSD 15](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/)

## Digest Summary
FreeBSD 15 introduces a new bridge driver that natively supports VLAN tagging and deprecates layer‑3 addresses on bridge members (controlled by net.link.bridge.member_ifaddrs, to be removed in 16.0). The key changes are:

- A single bridge can now handle multiple tagged/untagged VLANs per interface via the vlanfilter flag, eliminating the need for separate per‑VLAN bridges.
- Configuration is reduced to one ifconfig statement, e.g. `ifconfig bridge0 "vlanfilter addm ix1 tagged 2,3,128"`.
- Adding members without vlanfilter allows only untagged VLANs; attempting to add tagged VLANs yields “VLAN filtering not enabled”.

For VNET jails, the older jib script is superseded by stable epair(4) interfaces, which now generate persistent MACs via net.link.epair.ether_gen_addr. A custom script creates an epair, disables IPv6 link‑local, and attaches the “e0a” end to the bridge with the appropriate untagged VLAN.

Bhyve VMs lack native support for the new bridge+VLAN model; the author uses manually created tap interfaces added to the bridge via rc.local and a manual switch definition. Stable MACs must be set when the tap device is created. This approach works but is acknowledged as a temporary workaround.

## Discussion Summary
The discussion reflects heightened interest in recent FreeBSD developments, with participants noting an influx of related posts and expressing curiosity about any new releases or features. There is widespread confusion over the complex abstractions of jail, iojail, Sylve, Bastille, and bhyve, prompting calls for clearer, mutually consistent documentation. Technical questions arise regarding performance‑related flags such as TSO and LRO, while overall sentiment remains supportive, welcoming progress on the BSD front despite current difficulty in understanding the systems.

---

## Full Article

FreeBSD 15 comes with a [new bridging implementation](https://people.freebsd.org/~ivy/bridge_vlan_filtering.txt) which has native
support for VLANs. They have also soft-deprecated the ability to have
any layer 3 addresses on member interfaces which makes it behave like a
real hardware switch. The `net.link.bridge.member_ifaddrs` sysctl
controls this behavior and it will be removed in FreeBSD 16.0-RELEASE,
same as if set to zero.

One of the primary benefits of the new
implementation is that you can have a single bridge for everything and
the packet processing has been optimized. Previously the
[bridge performance would degrade](https://cgit.freebsd.org/src/commit/?id=85967694b4590a436c56a061b397620e342784ae)
for some operations as the number of member interfaces increased,
but I'm not clear on how significant it really was. It didn't impact
gigabit for me, but perhaps you'd see it if you were trying to get
10gbit line rate out of it.

[Old Bridging
------------](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/#old-bridging "Permalink to this section")

The old design when working with bridges and VLANs was like so:

* Create a bridge for a specific VLAN
* Create a VLAN interface off a physical interface
* Attach the VLAN interface to the bridge
* Now all your bridge members are able to communicate to that VLAN

As you can imagine this starts to get messy especially if you have a lot of
VLANs to work with or try to deploy jails that are meant to communicate over
multiple VLANs. An example from my old `rc.conf` looked something like this:

```
# Bhyve and VNET
# previously a long list of flags of disabled features were here
# and are irrelevant to this example
ifconfig_ix1="up"

vlans_ix1="vlan2 vlan3 vlan128"
create_args_vlan2="vlan 2"
create_args_vlan3="vlan 3"
create_args_vlan128="vlan 128"

cloned_interfaces="bridge0 bridge1 bridge2"

ifconfig_bridge0_name="vlan2bridge"
ifconfig_vlan2bridge="addm vlan2 up"

ifconfig_bridge1_name="vlan3bridge"
ifconfig_vlan3bridge="addm vlan3 up"

ifconfig_bridge2_name="vlan128bridge"
ifconfig_vlan128bridge="addm vlan128 addm"
```

It's a lot of work for something that feels so simple if you're familiar with real network gear.

[New Bridging
------------](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/#new-bridging "Permalink to this section")

The new design allows you to have a single bridge and specify
tagged and/or untagged VLANs for each bridge member. Here's what all of
that condenses down to.

```
# Bhyve and VNET
# previously a long list of flags of disabled features were here
# and are irrelevant to this example
ifconfig_ix1="up"

cloned_interfaces="bridge0"
ifconfig_bridge0="vlanfilter addm ix1 tagged 2,3,128"
```

That's it. Much simpler, isn't it? Please don't overlook the `vlanfilter` flag on the bridge. If you are missing this you can add members to the bridge with untagged VLANs but you'll get this error when trying to add tagged VLANs:

```
ifconfig: BRDGSIFVLANSET ix1: Invalid argument (extended error VLAN filtering not enabled)
```

[VNET Jails
----------](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/#vnet-jails "Permalink to this section")

VNET jails posed a problem for me because I was relying on the "unofficial" `/usr/share/examples/jails/jib` script which can handle creating [epair(4)](https://man.freebsd.org/cgi/man.cgi?epair(4)) devices for the jails. I'd copy this script into my `PATH`, make it executable, and then I could use it. A simplified example of this jail configuration looks like this:

```
webserver {
    exec.prestart += "jib addm $name vlan2";
    exec.poststop = "jib destroy $name";
    vnet;
    vnet.interface = "e0b_$name";
}
```

This would handle creating a stable name of `epair(4)` devices and attach it to the right bridge. e.g., "vlan2" becomes "vlan2bridge" in the jib script.

The jib script is old and has some features that I don't believe are necessary anymore. One feature tries to ensure your MAC addreses are stable, but this seems to be a native kernel feature of `epair(4)` now:

```
$ sysctl -d net.link.epair.ether_gen_addr
net.link.epair.ether_gen_addr: Generate MAC with FreeBSD OUI using ether_gen_addr(9)
```

And [ether\_gen\_addr(9)](https://man.freebsd.org/cgi/man.cgi?ether_gen_addr(9)) says:

```
By default, ether_gen_addr attempts to generate a stable MAC address
using the hostid of the jail that the ifp is being added to. During
early boot, the hostid may not be set on machines that haven't yet pop-
ulated /etc/hostid, or on machines that do not use loader(8).
```

Great, we seem to be covered there. But I still need a way to make stable `epair` device names for the jails and attach them to the bridge the new way, so I wrote a script for that:

```
#!/bin/sh
# /scripts/vnetif

set -eu

ENAME=$1
BRIDGE=$2
VLAN=$3

NEW_EPAIR=$(ifconfig -D epair create -vlanhwfilter up)
EPAIR_NUM=$(echo ${NEW_EPAIR##epair} | tr -d '[a]')

# Do not even want ipv6 link local on here, layer3 not allowed
# anymore on bridge members
ifconfig ${NEW_EPAIR} inet6 ifdisabled -auto_linklocal -accept_rtadv no_radr

ifconfig epair${EPAIR_NUM}a name e0a_${ENAME}
ifconfig epair${EPAIR_NUM}b name e0b_${ENAME}
ifconfig ${BRIDGE} addm e0a_${ENAME} untagged ${VLAN}
```

This is not well designed but it gets the job done.

Tip

On the `epair` device I had to set `-vlanhwfilter` -- another hidden requirement!

Now that this is sorted, my VNET jail config looks like this:

```
webserver {
    exec.prestart += "/scripts/vnetif $name bridge0 2";
    exec.poststop += "ifconfig e0a_$name destroy";
    vnet;
    vnet.interface = "e0b_$name";
}
```

It works! The VNET interface gets added to the bridge with the correct VLAN membership. It even seems to start the jail faster now...

[Bhyve VMs
---------](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/#bhyve-vms "Permalink to this section")

The Bhyve VM solution is not finalized for me right now. I'm using the [vm-bhyve](https://github.com/churchers/vm-bhyve/) tooling to manage my VMs, but it has no support for this new bridging+VLAN functionality. I've resorted to defining a manually managed switch in the configuration and pre-creating `tap` interfaces for each VM. Technically I could use `cloned_interfaces` in `/etc/rc.conf` and add them all to the bridge when the bridge is created, but as the number of VMs grow the configuration for this is getting really long and messy. I've opted to sidestep it for the moment and create all the `tap` interfaces in `/etc/rc.local`, and then the VM config looks like:

```
loader="grub"
cpu="2"
memory="4G"
network0_type="virtio-net"
network0_switch="bridge0" # the predefined manual bridge config in /vm-bhyve/.config/system.conf
network0_device="tap133" # my precreated tap interface
disk0_type="nvme"
disk0_name="disk0.img"
uuid="2109c019-9fd0-11f0-9ab1-d05099db8057"
network0_mac="58:9c:fc:0f:74:60" # seems to be ineffective now
disk1_type="ahci-cd"
disk1_name="seed.iso"
disk1_dev="file"
```

So if you want a stable MAC address, you need to set it where you create the `tap` interface.

For the record, that `/vm-bhyve/.config/system.conf` looks like:

```
switch_list="bridge0"
type_bridge0="manual"
bridge_bridge0="bridge0"
```

and my `/etc/rc.conf` has entries like:

```
# Linuxdev VM
cloned_interfaces="${cloned_interfaces} tap133"
ifconfig_tap133="up"
bridge_members="${bridge_members} addm tap133 untagged 2"

# ... later
cloned_interfaces="${cloned_interfaces} bridge0"
ifconfig_bridge0="vlanfilter ${bridge_members}"
```

This seems to be the cleanest way to handle it -- just keep building/accumulating `cloned_interfaces` and `bridge_members` variables and then it's easy to comment out/delete exactly what you want.

[Classic Jails
-------------](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/#classic-jails "Permalink to this section")

Classic jails share the host network stack with the jail, but what if the interface you want to use is attached to a bridge? You can create a VLAN sub-interface off the bridge and use that.

```
# /etc/rc.conf
# For Classic jails to use the 10gbit LAN interface
# we create a vlan sub-interface of the bridge
# which we can dynamically add IP addresses to
cloned_interfaces="bridge0"
vlans_bridge0="3"
ifconfig_bridge0="vlanfilter"
ifconfig_bridge0_3="inet x.x.x.x/yy" # if you want an IP added at boot
```

And a corresponding jail config:

```
# jail.conf
homeweb {
    host.hostname = "homeweb";
    ip4.addr = "bridge0.3|10.27.3.202/24";
}
```

Now it will apply the new IP address alias to the bridge's VLAN sub-interface.

[Conclusion
----------](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/#conclusion "Permalink to this section")

We've covered how to handle this new bridge design when working with VNET jails, Classic jails, and some Bhyve VMs. Hopefully this should be able to get you up and running with the new bridge+VLAN design in FreeBSD 15.0-RELEASE. I think in the long run the elegance of bridges working like a real hardware switch will outweigh the inconveniences.