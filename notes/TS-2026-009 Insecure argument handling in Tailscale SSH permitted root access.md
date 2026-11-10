---
title: "TS-2026-009: Insecure argument handling in Tailscale SSH permitted root access"
url: https://tailscale.com/security-bulletins
clipped: 2026-08-31 12:22:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [TS-2026-009: Insecure argument handling in Tailscale SSH permitted root access](https://tailscale.com/security-bulletins)

## Digest Summary
Tailscale versions prior to 1.66.0 allowed Linux exit nodes, subnet routers, and app connectors to accept inbound packets from their local LAN when ACLs used `"src": "*"`. This shorthand was interpreted as any IP (`0.0.0.0/0, ::/0`), enabling external LAN hosts to reach tailnet nodes through the packet‑forwarding node, bypassing intended source filtering. The issue affected nodes running version 1.65 or earlier on Linux and any regular node communicating with them; tailnets without `"src": "*"` were not impacted. No known active exploitation was reported.

Mitigation includes upgrading to Tailscale 1.66.0 or later, which introduces three defenses: (1) redefining `"src": "*"` to match only tailnet nodes and approved subnet routes, with an optional `autogroup:danger-all` for legacy behavior; (2) enabling stateful packet filtering on Linux forwarding nodes to drop unsolicited inbound packets; and (3) client‑side quarantining of shared nodes to reject all inbound traffic from them regardless of source IP. Server‑side changes also adjust `"src": "*"` handling for exit nodes. Auto‑updates are recommended but not required for remediation.

---

## Full Article

[DNS filtering by Control D, with one less bill.Read the blog →](http://tailscale.com/blog/dns-filtering-by-control-d)

# Security Bulletins

Security notifications affecting the Tailscale client and service.

Read our [incident disclosure and notification policy](https://tailscale.com/security-policies/incident-disclosure). If you’re directly affected by a security issue in Tailscale, and [we have your contact information](https://tailscale.com/kb/1224/contact-preferences), we will contact you.[Subscribe via RSS](https://tailscale.com/security-bulletins/index.xml)[Report a vulnerability](https://tailscale.com/security)

Description: Insufficient validation of 4via6 subnet router destinations permitted access to host-scoped addresses, including cloud metadata and loopback services.

#### What happened?

[4via6 subnet routers](https://tailscale.com/docs/features/subnet-routers/4via6-subnets) embed an IPv4 address within an IPv6 address. When a peer sends traffic to such an address, the router unmaps the embedded IPv4 address and forwards the traffic to it.

Previously, this forwarding path did not check the class of the embedded IPv4 address. A peer with ACL access to an advertised 4via6 site could therefore reach host-scoped addresses as seen from the router, including its cloud metadata service and services bound to loopback. Tailscale's packet filter already drops link-local destinations, but for 4via6 traffic it only sees the outer IPv6 address, so that check previously did not run against the embedded IPv4 destination.

Tailscale now refuses host-scoped IPv4 destinations (loopback, link-local, multicast and broadcast) at every point that acts on an unmapped 4via6 address.

This vulnerability is fixed in Tailscale version 1.102.3 or newer.

#### What was the impact?

A peer with ACL access to an advertised 4via6 route could reach host-scoped addresses from the router's network namespace. On cloud-hosted routers, this included the cloud metadata service, allowing the peer to obtain the router's instance credentials. On any router, services bound to loopback became reachable, bypassing the host firewall.

#### Who was affected?

Tailnets using 4via6 subnet routing where a subnet router advertises a site prefix and a peer has ACL access to it.

#### What do I need to do?

If you use 4via6 subnet routing, upgrade your subnet routers to Tailscale version 1.102.3 or newer.

#### Credits

We would like to thank the Anthropic infrastructure security team for reporting this issue.

Description: Tailscale SSH exposed accepted environment variable values on the command line of a local process, disclosing them to other local users and to logs.

#### What happened?

[Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh) allows the configured  `acceptEnv`  environment variables to be forwarded from an SSH client to the process launched on the host. Previously, these accepted variables were JSON-encoded and passed to a child process via an  `--encoded-env`  command line flag.

As a result, the names and values of the forwarded environment variables were visible in  `/proc/<pid>/cmdline`  to any other local user on the host for the duration of process startup. They were also recorded in the session-start arguments that Tailscale logs locally and, unless the node was configured with  `--no-logs-no-support` , to  `log.tailscale.com` . Environment variables commonly carry secrets such as tokens or credentials, which could therefore be disclosed to unintended parties.

Tailscale SSH now passes accepted environment variables to the child process through an inherited file descriptor rather than on the command line and keeps their values out of session logs.

This vulnerability is fixed in Tailscale version 1.102.1 or newer.

#### What was the impact?

Secrets carried in forwarded environment variables could be disclosed to other local users on the host via  `/proc` , and were written to session logs both locally and to  `log.tailscale.com` .

#### Who was affected?

Users of Tailscale SSH who forward environment variables via  `acceptEnv` , particularly on shared hosts with other local users.

#### What do I need to do?

If you use Tailscale SSH with  `acceptEnv` , upgrade to Tailscale version 1.102.1 or newer. If you use  `acceptEnv`  to pass credentials, revoke and rotate any impacted credentials.

#### Credits

We would like to thank Dante Bertana for reporting this issue.

Description: Insecure command line argument handling in Tailscale SSH permitted  `root`  user access in violation of ACLs.

#### What happened?

[Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh) previously accepted usernames that contained a leading  `-`  character. On Linux platforms these usernames were passed as arguments to  `getent(1)`  to retrieve the corresponding  `passwd`  entry, where they were interpreted as flags permitting attacker-controlled behavior. Specifically, if a user connected with the username  `-i`  this would have been interpreted as  `--no-idn`  and  `getent`  would have printed the entire  `passwd`  file contents starting with the  `root`  user, causing Tailscale to open an interactive  `root`  session.

Tailscale SSH now rejects usernames with leading dashes.

This vulnerability is fixed in Tailscale version 1.98.9 or newer.

#### What was the impact?

A user with SSH access to a Linux node would have been able to obtain a  `root`  session by connecting with the username  `-i` , in violation of ACL policy.

#### Who was affected?

Users of Tailscale SSH on Linux hosts that rely on  `autogroup:nonroot`  user restrictions in Tailscale ACLs.

#### What do I need to do?

If you use Tailscale SSH, upgrade to Tailscale version 1.98.9 or newer.

#### Credits

We would like to thank Anthropic and Ada Logics for reporting this issue.

Description: A single malformed HTTP request to a node running Tailscale Serve or Funnel could pin a CPU core indefinitely, causing denial of service.

#### What happened?

[Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve) and [Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel) proxy incoming HTTP requests to local backends by matching the request path against the configured mount points. When resolving the handler for a request, Tailscale walked the request path upward one directory at a time, expecting the walk to eventually terminate at the root path  `/` .

For requests whose path did not begin with  `/` , this walk never reached  `/`  and never matched a mount point, causing the loop to spin forever. As the server enforced no request timeout, nothing interrupted the spin, and the goroutine held one core at 100% for the life of the process.

Tailscale now terminates the path walk for non-absolute paths, returning no handler and closing the request.

This vulnerability is fixed in Tailscale version 1.98.9 or newer.

#### What was the impact?

An attacker could send a crafted HTTP request to permanently consume one CPU core on the target node.

For Tailscale Serve, the request could originate from any peer on the tailnet with access to the node. For Tailscale Funnel, the request could originate from any unauthenticated host on the internet.

#### Who was affected?

Nodes running Tailscale Serve or Tailscale Funnel on versions prior to 1.98.9.

#### What do I need to do?

If you run Tailscale Serve or Tailscale Funnel, upgrade to Tailscale version 1.98.9 or newer.

#### Credits

We would like to thank Anthropic and Ada Logics for reporting this issue.

Description: Insufficient inbound packet filtering in Services permitted access to loopback-bound listeners.

#### What happened?

Tailscale [Services](https://tailscale.com/docs/features/tailscale-services) are virtual tailnet destinations that can be hosted from one or more nodes on your tailnet. They allow you to manage networked resources such as databases separately from the nodes that back them.

In Tailscale versions prior to 1.98.9, nodes advertising services could accept inbound traffic to service IPs on ports that they did not advertise. In these scenarios Tailscale would forward these packets to any process on the host loopback interface listening on the same port, allowing them to be accessed remotely.

Tailscale now filters and rejects these packets with the appropriate TCP RST response when no corresponding handler exists for the service port.

This vulnerability is fixed in Tailscale version 1.98.9 or newer.

#### What was the impact?

A user with ACL grants to a Tailscale Service could address it on non-advertised ports and reach processes listening on loopback on the node hosting the service.

#### Who was affected?

Users of Tailscale Services that rely on loopback-only network access restrictions on the nodes they use to host services.

#### What do I need to do?

If you host Tailscale Services on nodes alongside processes bound to loopback, upgrade to Tailscale version 1.98.9 or newer.

Description: Tailscale SSH allowed users to be addressed by numeric UID, bypassing  `root`  user restrictions in ACLs.

#### What happened?

[Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh) previously allowed users to be addressed by their username or UID value, however the  `root`  user restrictions in ACL enforcement only considered the former. A user with non- `root`  SSH access who addressed  `0@host`  would have been able to access  `root`  in violation of ACLs.

Tailscale now disallows the use of UIDs or numeric-only usernames via SSH to avoid this ambiguity.

This vulnerability is fixed in Tailscale version 1.98.9 or newer.

#### What was the impact?

A user with SSH access to a node would have been able to SSH as  `root`  using the username  `0`  in violation of ACL policy.

#### Who was affected?

Users of Tailscale SSH on Linux/Unix hosts that rely on  `autogroup:nonroot`  user restrictions in Tailscale ACLs.

#### What do I need to do?

If you use Tailscale SSH, upgrade to Tailscale version 1.98.9 or newer.

#### Credits

We would like to thank Tim Hoffman (GM) for reporting this issue.

Description: Tailscale Serve Unix socket proxy targets were not restricted to  `root` , allowing a non-root operator to proxy privileged sockets.

#### What happened?

[Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve) can proxy incoming connections to local backends, including Unix domain sockets configured as  `proxy`  targets (for example,  `proxy: unix:/var/run/docker.sock` ). A non-root local user configured as the [Tailscale operator](https://tailscale.com/docs/reference/tailscale-cli) can write Serve configuration through the LocalAPI.

Tailscale restricts the ability to specify filesystem paths as Serve targets to the root user to prevent privilege escalations, however this check did not cover Unix socket proxy targets. A non-root operator could therefore have the  `tailscaled`  process running as root proxy to a privileged Unix socket, bypassing the filesystem permissions that would otherwise deny them access.

Tailscale now restricts Unix socket proxy targets to the  `root`  user, matching the requirement already applied to filesystem handlers.

This vulnerability is fixed in Tailscale version 1.98.9 or newer.

#### What was the impact?

A non-root user configured as the Tailscale operator could cause the  `tailscaled`  process running as  `root`  to connect to privileged Unix sockets they could not otherwise access.

#### Who was affected?

Linux/Unix hosts running Tailscale Serve where a non-root local user was configured as the Tailscale operator and privileged Unix sockets (such as Docker, containerd, or CRI sockets) were present.

#### What do I need to do?

If you use Tailscale Serve, upgrade to Tailscale version 1.98.9 or newer.

#### Credits

We would like to thank Tim Sageser ([dtrsecurity](https://dtrsecurity.com)) for reporting this issue.

Description: Tailscale SSH Unix socket forwarding did not respect symlink permissions, allowing privileged socket access.

#### What happened?

[Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh) includes the ability to forward both TCP and Unix sockets between the client and host. A bug in the filesystem permission checks within Tailscale SSH's Unix socket forwarding permitted an unprivileged user to bind and access a privileged socket on the remote host.

Previously, when Tailscale SSH evaluated filesystem permissions for requested sockets, it only performed lexical matching of the requested path against its allowlists and denylists. An attacker who created a symlink at a path they owned (e.g.,  `/home/$USER/my.sock` ) that pointed to a protected resource (e.g.,  `/var/run/docker.sock` ) would have been able to bind and access the latter path in an SSH connection. This is possible because Tailscale runs as  `root`  and so has access to the privileged destination.

In addition to lexical matching, Tailscale SSH now checks the requested and configured paths for symlinks and evaluates them to ensure that their destinations are also authorized. Symlinks with destinations outside of the configured allowlist will be denied.

This vulnerability is fixed in Tailscale version 1.98.9 or newer.

#### What was the impact?

An unprivileged user would have been able to access privileged Unix sockets on the remote host.

#### Who was affected?

Users of Tailscale SSH on shared Linux/Unix hosts that rely on filesystem permissions to restrict access to Unix sockets.

#### What do I need to do?

If you use Tailscale SSH, upgrade to Tailscale version 1.98.9 or newer.

#### Credits

We would like to thank Tim Sageser ([dtrsecurity](https://dtrsecurity.com)) for reporting this issue.

Description: OAuth access tokens recorded in tailnet audit logs.

#### What happened?

The Tailscale coordination server emits an [audit log](https://tailscale.com/docs/features/logging/audit-logging) recording all changes to a tailnet's configuration including the creation and management of access credentials.

A bug in the Tailscale coordination server caused it to record the complete [OAuth client access tokens](https://tailscale.com/docs/features/oauth-clients) within the audit log entries that describe their creation. This made the OAuth access tokens accessible to other tailnet actors who had access to the logs.

#### What was the impact?

A tailnet admin with access to audit logs would have been able to retrieve OAuth access tokens from the logs and use them to make authorized requests to the Tailscale API within the token's one hour validity window.

#### Who was affected?

All tailnets that used OAuth Clients to create access tokens from March 1st, 2026 to May 29th, 2026 are impacted.

#### What do I need to do?

There is no action necessary on the part of customers. New access tokens are now recorded in a redacted form in the audit log. Access tokens are created with a maximum valid lifetime of one hour so all historical tokens have already expired.

#### Credits

We would like to thank Conor Power (Snapchat) for reporting this issue.

Description: ACL capability bypass in the Tailscale client's web interface

#### What happened?

The Tailscale client runs a [local web interface](https://tailscale.com/docs/features/client/device-web-interface) to manage
its settings. This web interface can optionally be opened to other tailnet
peers, for example to manage a tagged node on a headless host without SSH
access. By default the interface is read-only, but tailnet admins can grant
permissions to change certain settings using ACL grants.

The  `/api/routes`  endpoint on the web interface allows changing the active
[exit node](https://tailscale.com/docs/features/exit-nodes) and advertised [subnet routes](https://tailscale.com/docs/features/subnet-routers).
These settings are gated behind  `exitNodes`  and  `subnets`  grants respectively.

There was a bug in the handler that reset both settings to their empty state if
the request body was empty, even if the caller doesn't have either grant to
allow that.

This vulnerability is fixed in Tailscale version 1.98.0 and newer.

#### What was the impact?

A malicious tailnet node could disable the exit node and clear advertised
subnet routes on other tailnet nodes that run the web interface. The malicious
user would need to perform a login check and be granted access to port  `5252` 
on the target node via tailnet ACLs.

#### Who was affected?

Linux, macOS, and Windows nodes running Tailscale between versions 1.56.0 and
1.98.0 and with the web interface explicitly enabled.

#### What do I need to do?

If you are using the web interface to manage remote nodes, update those nodes
to version 1.98.0 or newer.

#### Credits

We would like to thank [N0zoM1z0](https://github.com/N0zoM1z0) for reporting
this issue.

Description: Arbitrary command execution with elevated privileges in tssentineld

#### What happened?

 `tssentineld`  is a launchd service that is installed in [managed environments](https://tailscale.com/kb/1362/mdm)
when the [AlwaysOn.Enabled](https://tailscale.com/kb/1315/mdm-keys#set-tailscale-to-always-be-connected) MDM policy is present on macOS. Its sole
responsibility is to ensure that Tailscale.app is relaunched if terminated.
As a launchd service, it runs as  `root` .

The implementation used an NSTask and  `/bin/sh -c sudo -u [username]` , using basic string
template substitution for the username. An attacker with either direct access
to the memory backing the username string or by setting the current username
to a malicious value could use this to inject commands running with the same
privileges as  `tssentineld` .

This vulnerability is fixed in Tailscale version 1.94.0 and newer.

#### What was the impact?

Malicious local users that can manipulate their username or manipulate memory of tssentineld
can execute arbitrary commands as root.

#### Who was affected?

The [macOS standalone variant](https://tailscale.com/kb/1065/macos-variants) from 1.84.0 to 1.92.3, when configured
via MDM to enable the [AlwaysOn.Enabled](https://tailscale.com/kb/1315/mdm-keys#set-tailscale-to-always-be-connected) policy is affected.

 `tssentineld`  is only activated on clients managed by MDM and employing the
[AlwaysOn.Enabled](https://tailscale.com/kb/1315/mdm-keys#set-tailscale-to-always-be-connected) policy and requires admin permission to install and
activate. Memory manipulation to inject a malicious command requires a separate
vulnerability or existing root access. The user may, however, modify their username
in such a way that  `tssentineld`  could execute arbitrary shell commands with elevated
privileges.

The [macOS package available from the App Store](https://tailscale.com/kb/1065/macos-variants) does not support the
installation of launchd daemons and is not affected.

#### What do I need to do?

If you are using the [AlwaysOn.Enabled](https://tailscale.com/kb/1315/mdm-keys#set-tailscale-to-always-be-connected) policy with standalone macOS clients, update to version 1.94.0 or newer.

Description: Nodes without  `--statedir`  or  `TS_STATE_DIR`  failed to enforce signing checks in tailnets with Tailnet Lock enabled.

#### What happened?

In tailnets where [Tailnet Lock](https://tailscale.com/kb/1226/tailnet-lock) is enabled, unsigned nodes running the  `tailscaled`  daemon (for example, on Linux) without specifying a  `--statedir`  or  `--state`  failed to enforce the required signing checks. This allowed them to communicate with other similarly misconfigured, unsigned nodes, or with malicious nodes that joined the tailnet. This behaviour bypassed the Tailnet Lock security policy for a specific subset of nodes.

When Tailnet Lock is enabled, Tailscale nodes will only communicate if their node keys have been signed by a trusted signing node.

The set of trusted signing nodes is tracked by the [tailnet key authority (TKA)](https://tailscale.com/kb/1226/tailnet-lock#tailnet-key-authority). This set is distributed to all nodes in the tailnet, and each node must store this state locally so that it can verify peer signatures.

The TKA state is stored on disk in the state directory.
Prior to 1.90.8, this was the only storage option.

- If you use the macOS, Windows, iOS, Android, and tvOS clients, the state directory is set automatically.

- If you run the  `tailscaled`  daemon, the state directory is set by the  `` [--statedir](https://tailscale.com/kb/1278/tailscaled#flags-to-tailscaled) or  `--state`  flags.

- If you use the default systemd unit files distributed with the official Tailscale  `deb` ,  `rpm` , and  `tar.gz`  packages, the  `--state`  flag is set automatically.

- If you use Tailscale in Docker or Kubernetes, the state directory is set by the  `` [TS_STATE_DIR environment variable](https://tailscale.com/kb/1282/docker#ts_state_dir).

If  `tailscaled`  was started without a state directory ( `--statedir` ,  `--state` , and/or  `TS_STATE_DIR`  were omitted), it would be unable to store the set of trusted signing nodes. Rather than failing and reporting an error, such a node erroneously skipped checking whether peer signatures were signed, which is a failure to enforce Tailnet Lock.

#### What was the impact?

There is no indication of this issue being exploited in the wild.

The bug allowed communication between two or more unsigned nodes, each running without a state directory, even though Tailnet Lock was enabled.

While the bug is present across many versions, the risk of exploitation is low. It was not possible for an unsigned node without a  `--statedir`  to connect to a node that did have a state directory, as the latter would correctly enforce the policy and reject the connection from the unsigned peer.

#### Who was affected?

The vulnerability only manifests when all three of the following conditions are met:

- Tailnet Lock is enabled in the tailnet,

- At least two nodes were running the  `tailscaled`  daemon without the  `--statedir` / `--state`  flags, or without the  `TS_STATE_DIR`  environment variable, and

- At least one of the node keys was not signed.

This bug was present in all Tailscale clients from the introduction of Tailnet Lock, and is fixed in version 1.90.8.

You can tell if a node is affected by this issue by running  `tailscale lock status` .
If the output says  `Tailnet Lock is NOT enabled`  but Tailnet Lock is enabled in your Tailnet, the node is not enforcing signing checks correctly.

Alternatively, you can look for the following text in your [client logs](https://tailscale.com/kb/1011/log-mesh-traffic):
 ` `network-lock unavailable; no state directory
` ` 

(The pre-release name for Tailnet Lock was "network lock", which still persists in parts of the codebase.)

#### What do I need to do?

If you don't use Tailnet Lock, no action is required.

If you do use Tailnet Lock:

- 

Review the configuration of any nodes that run the  `tailscaled`  daemon.
Specifically, check the startup parameters for the  `tailscaled`  service.
Any nodes running  `tailscaled`  without a state directory are potentially vulnerable until upgraded.

- 

Upgrade all nodes running the  `tailscaled`  daemon to 1.90.8 or later.
Alternatively, set a state directory by:

- Adding the  `--statedir`  flag if you run the  `tailscaled`  daemon, or

- Adding the  `TS_STATE_DIR`  environment variable if you run Tailscale in Docker or Kubernetes.

In version 1.90.8 and later, nodes without a state directory will now store the TKA in memory and enforce Tailnet Lock signing requirements.

However, nodes that store TKA in memory must re-fetch the complete TKA from the coordination server whenever they start.
We strongly recommend setting a state directory for all nodes, allowing them to store the TKA on disk and eliminate the startup control plane dependency.

Description: A one-off auth key could be reused from multiple devices

#### What happened?

A time-of-check/time-of-use (TOCTOU) issue allowed multiple nodes to register
using the same [one-off auth key](https://tailscale.com/kb/1085/auth-keys). These registration attempts
would have to happen at approximately the same time to succeed.

The Tailscale coordination server relies on database transactions to ensure
consistency and prevent race conditions. The API handler for node registration
requests uses a read transaction to validate the request, including the auth
key, and then a separate write transaction to complete the registration.
One-off auth keys are invalidated during the write transaction stage.
Previously, if two registration requests came in at the same time they would
both successfully validate the auth key during the read transaction and proceed
to register the node. We fixed the API handler to re-validate the auth key
during the write transaction stage to catch this race condition.

#### What was the impact?

A one-off auth key could be reused multiple times to register multiple
nodes, rather than just one.

#### Who was affected?

Tailnets using one-off auth keys through automation. All nodes would have to
obtain a legitimate auth key for the tailnet. Malicious nodes cannot abuse this
issue to join the tailnet.

Tailscale audit logs do not have enough information to detect this race
condition happening. We plan to improve our audit logs to make detection of
incidents involving auth keys easier in the future.

#### What do I need to do?

No action is required. Tailscale has deployed a fix to the coordination server as of 2025-11-07.

#### Credits

We would like to thank [madisp](https://github.com/madisp) for reporting this issue.

Description: A potential access control logic issue affected shared subnet router nodes between tailnets.

#### What happened?

Tailscale nodes that are subnet routers and shared with other tailnets did not enforce protocol filters in ACLs. For example, a subnet router with an IP grant of  `"udp:1234"`  in the policy file would allow TCP, UDP, and any other protocol connections to port  `1234` . This bug was fixed in our control plane and does not require any update.

The Tailscale Control Plane performs a process known as [network map trimming](https://tailscale.com/kb/1087/device-visibility) to ensure that only nodes with authorized access to each other appear in their respective clients.

As part of this process, the Control Plane transforms ACLs for nodes that serve as [subnet routers](https://tailscale.com/kb/1019/subnets), [exit node](https://tailscale.com/kb/1103/exit-nodes), or [app connector](https://tailscale.com/kb/1281/app-connectors) and are [shared externally](https://tailscale.com/kb/1084/sharing) with other tailnets to constrain the access of external tailnet members to only the shared node and prohibit their access to the routed subnets.

This filtering contained a bug, producing ACLs for these nodes that omitted their IP Protocol number information entirely. This caused those nodes to accept connections using arbitrary protocols from both local and external tailnets the node was shared with. The  `src` / `dst`  restrictions, as well as port restrictions still applied, so these nodes were not accessible broadly.

For ACL rules that relied on protocol-based filtering, such as  `imcp:*`  this would have allowed connections from the source using arbitrary protocols to the destination.

#### What was the impact?

Local and external tailnet members with existing access to subnet routers that were shared externally would have been able to exceed their authorized access and establish connections using arbitrary protocols to these nodes.

Local and external members who were not included in the source of the impacted ACL groups would not have been able to access impacted nodes using these rules.

There is no indication of this issue being exploited in the wild. The exposure is limited to nodes that were intentionally shared to another tailnet.

#### Who was affected?

Tailnets with nodes that are subnet routers, that were also shared with external tailnets, and whose ACLs for these nodes relied on protocol filtering were affected.

This bug was present in all Tailscale clients from the introduction of these features, and was fixed for all clients through the Tailscale control plane on October 29th 2025.

#### What do I need to do?

No action is required. Tailscale has deployed a fix to the control plane as of 2025-10-29.

#### Credits

We would like to thank [Thariq Shanavas](https://www.linkedin.com/in/thariq-shanavas) for reporting this issue.

Description: Logging of MDM-provided auth keys

#### What happened?

A change in Tailscale version 1.84.0 on macOS and iOS caused all
[MDM-provided](https://tailscale.com/kb/1315/mdm-keys) configuration values to be logged and uploaded to the
Tailscale [log server](https://tailscale.com/kb/1011/log-mesh-traffic#client-logs). One of the possible MDM values is an [auth
key](https://tailscale.com/kb/1315/mdm-keys#set-an-auth-key) used to automatically register the node. This resulted in
the Tailscale log server storing user [auth keys](https://tailscale.com/kb/1085/auth-keys) along with
other client logs.

The logs collected by the Tailscale log server are only accessible to Tailscale
employees, so no auth keys were leaked to potential attackers.

Tailscale version 1.86.4 redacts the auth key, and other textual values, before logging
them.

#### What was the impact?

MDM-provisioned auth keys were uploaded to the Tailscale log server. No keys
have leaked outside of Tailscale infrastructure. Auth keys provided on the CLI
or using environment variables were never logged.

The impact depends on the [type of auth key](https://tailscale.com/kb/1085/auth-keys#types-of-auth-keys) used:

- One-off auth keys are used and invalidated when the node is registered; there
is no risk to your tailnet

- Reusable auth keys could be used again to register nodes if stolen

- [Pre-signed auth keys for Tailnet Lock](https://tailscale.com/kb/1226/tailnet-lock#add-a-node-using-a-pre-signed-auth-key) are
like reusable auth keys, but can also register nodes that don't need to be
signed by another signing node in the tailnet

#### Who was affected?

Customers using [MDM to distribute auth keys](https://tailscale.com/kb/1315/mdm-keys#set-an-auth-key), with macOS and
iOS clients running Tailscale versions between 1.84.0 and 1.86.2, are affected.

#### What do I need to do?

If you don't use MDM to distribute auth keys to your devices, no action is
needed.

If you do distribute auth keys with MDM, upgrade all macOS and iOS nodes to
Tailscale version 1.86.4 or later. Additionally, if you distribute reusable auth keys,
or pre-signed auth keys for Tailnet Lock, we recommend that you rotate these
keys.

Description: Tailnets using shared public email providers

#### What happened?

On May 22, 2025 our Reddit community gave us [the necessary kick](https://www.reddit.com/r/Tailscale/comments/1ksy3xy/someone_just_randomly_joined_my_tailnet/)
to address an issue with handling shared public email provider domains ("shared
domains"). We mitigated the risk for new tailnets being created on previously
unknown shared domains by enabling [user approval](https://tailscale.com/kb/1239/user-approval) by
default. This issue affects only a small portion of our user base, and this
bulletin provides some background, mitigation steps, and our future plans.

##### Background

Tailscale users are mapped to tailnets by their email address domain (with a
few exceptions*). This means that  `user1@example.com`  and  `user2@example.com` 
can both log in to tailnet  `example.com` . We chose this default behavior because
it reduces onboarding friction for new users and tailnet admins.

The downside of this default behavior is that if a user's email address comes
from a shared domain, multiple unrelated users may be able to join the same
tailnet without realizing that others are in their tailnet too.

Tailscale has a workaround for this scenario: we flag known shared domains in
our database. For example, when  `user@gmail.com`  logs in for the first time, we
create a personal tailnet named  `user@gmail.com`  for them instead of adding
them to one giant  `gmail.com`  tailnet. If there is an existing shared domain
tailnet, we "decompose" it - break it up into new personal tailnets for each
user with only their nodes. Very popular email providers, like Gmail or Yahoo,
have been decomposed from the very beginning.

This workaround has an obvious flaw: we can't flag all shared domains in our
database proactively, because there is no authoritative list of such domains
and new providers can show up at any time. So far we have patched over this
flaw by retroactively flagging new shared domains when users report them to us.
This has been convenient for ease of onboarding new users, especially users on
corporate domains.

* We use special OIDC claims to map logins to tailnets on Google Workspace
( `hd`  claim) and Microsoft Entra ( `tid`  claim).

##### What changed

On May 22, 2025 a post on Reddit made the severity of this issue more obvious.
The poster was using a previously unknown shared domain. We flagged the new
shared domain and decomposed the tailnet.

To mitigate the potential risk for tailnets on shared domains, we enabled [user
approval](https://tailscale.com/kb/1239/user-approval) by default for all new tailnets. This way, even if
unexpected users log in using a shared domain that is not decomposed yet, an
administrator will have to approve them first. We did not change the setting
for any existing tailnets to avoid breaking any workflows.

Since May 22nd, we also decomposed 130 additional tailnets based on signals
like: number of users, payment plan, recent activity, whether they have a
Google Workspace or a Microsoft Entra tenant, and basic online research. Before
May 22nd, we had already flagged and decomposed 534 shared domains, many
proactively, but some in response to support tickets.

##### What we're doing next

We have certainly dug ourselves into a hole here. There are various public
lists of shared domains, but it is tricky to figure out which existing tailnets
are meant to be single-user and which are not. There are shared email
hosting providers, customer emails created by ISPs, university emails,
disposable email providers, etc. In all cases a tailnet could be a legitimate
corporate tailnet for the company or university, and decomposing the tailnet
could break their setup.

There are several planned actions and projects that should improve the
situation:

- Short-term

- Proactively flag more shared domains that don't have tailnets yet, using
public email provider lists and the [Public Suffix List](https://publicsuffix.org).

- Reach out to admins of tailnets that are potentially on shared domains,
but where we can't be certain, with advice on how to protect and audit their
tailnets.

- Medium-term

- Mark any new domain coming through a Google or Microsoft login as shared
if it's not associated with Google Workspace or a private Microsoft Entra
tenant.

- Prompt owners of existing tailnets like the above to enable User
Approval on next login. Today this is ~1.7% of all tailnets.

- Create a process for unflagging a shared domain through a support ticket
and DNS ownership verification in case of false positives.

- We are discussing changing the default ACL in new tailnets, but no
decision has been made yet.

- Long-term: a large identity model change has been in the works for roughly a
year that, among other things, will make all new user registrations create a
personal tailnet instead of a domain-wide tailnet by default.

#### What was the impact?

There are two potentially risky scenarios with shared domains: malicious users
and malicious admins.

Malicious users could join a tailnet of an unsuspecting user and access exposed
ports on that user's nodes. Tailnet ACLs could limit that impact, but default
ACLs allow access to all ports on all nodes. Note that [Tailscale SSH](https://tailscale.com/kb/1193/tailscale-ssh)
is not allowed between nodes of different users, so a malicious user would need
to exploit some other software on a victim's node to gain access or
information. Also note that the free plan of Tailscale is limited to 3 users.

Malicious admins could create a tailnet on a shared domain and wait, or
social-engineer victims to join it. Once victims join the tailnet, a malicious
admin could access all open ports on victims' nodes, and set up a [subnet
router](https://tailscale.com/kb/1019/subnets) to intercept their traffic. A malicious admin could
also set up their own [DNS server](https://tailscale.com/kb/1054/dns#override-dns-servers) for the tailnet to record
and spoof DNS responses.

We are not aware of any instances of either of these scenarios happening.

#### Who was affected?

Users of 664 known shared domains out of a total 166,488 unique domains we've
seen across all tailnets may have had their nodes exposed to other users with
the same email domain. 534 of these shared domains have been been decomposed
throughout Tailscale's history and not recently.

There may be other tailnets using shared domains that we haven't discovered
yet.

##### Who was not affected?

The following categories of users are not affected:

- Users with custom email domains (corporate or personal)

- Users with [custom OIDC providers](https://tailscale.com/kb/1240/sso-custom-oidc)

- GitHub users, including personal and org tailnets

- Owners of tailnets with [User Approval](https://tailscale.com/kb/1239/user-approval) or [Device
Approval](https://tailscale.com/kb/1099/device-approval) enabled

- Owners of tailnets with [Tailnet Lock](https://tailscale.com/kb/1226/tailnet-lock) enabled

- Users of very popular email providers, like  `gmail.com` ,  `outlook.com` ,
 `yahoo.com` ,  `protonmail.com` , and others

- Users with custom restrictive [ACLs](https://tailscale.com/kb/1018/acls) that avoid  `autogroup:member` 
and other broad selectors in  `src`  clauses

#### What do I need to do?

If your tailnet name in the top-left corner of the [Admin
Console](https://login.tailscale.com/) is an email address rather than a bare domain, no
action is needed.

If you are in a tailnet on a shared domain:

- [Contact support](https://tailscale.com/contact/support) to request your tailnet to be decomposed.

- If you're the tailnet owner, review the [list of users](https://login.tailscale.com/admin/users) in your
tailnet and [audit logs](https://tailscale.com/kb/1203/audit-logging) for evidence of any suspicious
activity.

- If you're the tailnet owner and don't want to decompose your tailnet, enable
[user](https://tailscale.com/kb/1239/user-approval) and/or [device](https://tailscale.com/kb/1099/device-approval) approval.

If you are in a tailnet on a domain that was wrongfully decomposed, [contact
support](https://tailscale.com/contact/support) to reset your tailnet.

#### Timeline

- March 2019: Tailscale started, Google and Azure AD (now Entra) authentication
implemented

- December 2019

- decision to maintain a list of shared domains was made

- first shared domain hardcoded -  `gmail.com` 

- Tailscale launched to a small set of users

- November 2020: [Node sharing](https://tailscale.com/kb/1084/sharing) released

- January 2021: the hardcoded list of shared domains moved into a database
table, tools created for the support team to decompose new shared domains

- June 2021: GitHub authentication added

- March 2023: Custom OIDC authentication added

- April 2023: Passkey authentication added

- April 2023: Apple authentication added

- May 2023: [External user invites](https://tailscale.com/kb/1271/invite-any-user) added

- This was primarily the point at which creating a tailnet for email domains
stopped being necessary. Multiple users could join a shared tailnet by
an invitation to access each other's nodes, even on personal accounts from
shared domains.

- May 2025:

- May 22nd: Reddit user posted about an unexpected member of their tailnet

- May 22nd: User approval enabled by default for new tailnets

- May 23rd-27th: 130 shared domain tailnets identified and decomposed

Description: Insecure non-constant time comparison in DERP server mesh authentication

#### What happened?

Tailscale's [DERP (Designated Encrypted Relay for Packets) servers](https://tailscale.com/kb/1232/derp-servers) provide connectivity between Tailscale nodes in the event that they cannot mutually communicate due to network restrictions. DERP servers deployed in the same region communicate using a private mesh API to coordinate client connections amongst themselves. These private mesh connections authenticate using a pre-shared secret key.

The DERP servers previously used an insecure non-constant time comparison when verifying the mesh authentication secret. This would have allowed an attacker to discover the mesh secret by performing a side channel timing attack.

The issue was present since the introduction of DERP meshing and patched on May 21, 2025. We have updated all Tailscale-managed DERP servers and rotated their mesh secrets.

#### Who was affected?

All Tailscale-operated DERP servers and Tailscale users who operate their own custom DERP servers with more than one server per region.

#### What was the impact?

An attacker who discovered the mesh key could not see any plaintext traffic between nodes, since all traffic is end-to-end encrypted.

An attacker with mesh access would have been able to enumerate all peers connected to a DERP server, including their WireGuard public key and their source IP address and port.

An attacker with mesh access would have been able to perform a denial-of-service attack (DoS attack), prohibiting a node’s keys on any DERP servers by forcing disconnects of meshed DERP servers by using the [ClosePeer](https://pkg.go.dev/tailscale.com/derp#Client.ClosePeer) API.

We have no evidence to indicate any abuse of this issue.

#### What do I need to do?

If you operate your own custom DERP servers in a mesh setup, you should update to the latest version and rotate any mesh keys that were previously in use.

Description: Privilege escalation in proxy-to-grafana via header spoofing

#### What happened?

The Tailscale [Grafana proxy](https://tailscale.com/kb/1523/grafana) is a HTTP reverse proxy for Grafana that annotates requests with  `X-Webauth-*`  headers bearing the requesting user's [whois](https://tailscale.com/kb/1080/cli#whois)-based Tailscale identity.

The Grafana proxy is intended to be used in combination with [Grafana's session-based authentication](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/auth-proxy/#login-token-and-session-cookie) using cookies issued in response to requests made to  `/login`  to authenticate subsequent requests to other endpoints.

When configured to use session-based authentication, Grafana's  `/api/`  routes will continue to accept  `X-Webauth-*`  headers for authentication. Previous versions of the Grafana proxy did not strip these  `X-Webauth-*`  headers from API requests allowing them to be forged by a malicious tailnet node.

The issue was present since the initial release of the Grafana proxy, and was patched on May 15th, 2025. The Grafana proxy now strips  `X-Webauth-*`  headers from all incoming requests.

#### Who was affected?

Tailnets using Grafana in combination with the Grafana proxy to authenticate users.

#### What was the impact?

Grafana instances protected by the Grafana proxy would have been vulnerable to privilege escalation via HTTP request header forgery from members of their tailnet.

#### What do I need to do?

Update to the latest Grafana proxy by running  `go install tailscale.com/cmd/proxy-to-grafana@latest` 

#### Credits

Thanks to Yeongrok Gim for reporting this issue.

Description: Potential for continued admin console access past inactivity timeout

#### What happened?

The [admin console session timeout](https://tailscale.com/kb/1461/admin-console-session-timeout) works by recording tailnet-specific activity timestamps on login and from browser requests triggered by user activity. Previously the admin console also erroneously considered the act of switching between multiple tailnets to be a login and recorded a fresh timestamp for the user in the destination tailnet while switching.

For tailnets whose users were also [members of other tailnets](https://tailscale.com/kb/1271/invite-any-user) with less strict inactivity timeouts, these users may have been able to continue their access to the admin console for longer than expected if they switched between tailnets and did not time out of the less restrictive tailnet.

The issue was present since inactivity timeout was initially released in August 2024, and was fixed in production on March 7th, 2025. A user who switches to a tailnet in which their session has already expired will be logged out and redirected to the login page.

#### Who was affected?

Tailnets with admin console session timeout configurations and users who are members of other tailnets with less strict session timeout configurations.

#### What was the impact?

Users of tailnets with strict admin console session timeouts may have been able to continue their access to the admin console past expected timeouts by switching to and from other tailnets in the admin console whose console configurations were less strict.

#### What do I need to do?

No action is required.

Description: Potential for Tailscale SSH recording failures

#### What happened?

Tailscale [SSH recording](https://tailscale.com/kb/1246/tailscale-ssh-session-recording) deployments that enforce SSH recording
using  `enforceRecorder`  could fail to record session activity in several
situations.

##### Failure to write to the storage backend

If  `tsrecorder`  instances were unable to write to their configured storage, SSH
sessions would be allowed to execute for a few seconds (typically under one or
two) while the first output bytes failed to write.

A  `tsrecorder`  instance can fail to write to its configured storage for many
reasons, including:

- Misconfigured IAM permissions when using S3 for storage.

- Misconfigured file permissions when using the local filesystem for storage.

- Insufficient free space when using the local filesystem for storage.

 `tsrecorder`  now exercises the full set of required storage actions on startup.

##### Unreachable tsrecorder after a session is established

If  `tsrecorder`  instances became unreachable after a session had started, the
SSH session would take several minutes to terminate. This could happen when
 `tsrecorder`  went offline or when ACLs were updated to restrict access to
 `tsrecorder`  nodes.

The Tailscale client now detects  `tsrecorder`  unreachability within 30 seconds
and terminates the connection.

#### Who was affected?

Users of Tailscale SSH recording with  `enforceRecorder`  option and with
 `tsrecorder`  and Tailscale client versions prior to 1.78.0.

#### What was the impact?

Users connecting over [Tailscale SSH](https://tailscale.com/kb/1193/tailscale-ssh) to nodes that enforce session
recording via  `enforceRecorder`  ACL flags would have been able to execute
commands briefly before having their access terminated due to recording
failures.

#### What do I need to do?

Update  `tsrecorder`  instances and Tailscale clients to version 1.78.0 or later.

Description: Tailscale Funnel abused for phishing

#### What happened?

A malicious user abused [Tailscale Funnel](https://tailscale.com/kb/1223/funnel) to host a phishing page
targeting Facebook users. This user created multiple free Tailscale accounts to
use as an obfuscation/anonymity proxy for their VPS instance hosting the
phishing page.

We received the first report about a phishing page on September 23rd, 2024, and
took down the Funnel page the same day. We received the second report on October
1st, 2024, for the same phishing page on a different Tailscale account. We took
down the second page, added detection for new similar pages, and repeatedly
shut down new attacker accounts as they were created. After a few more
attempts, the attacker stopped creating new accounts.

#### Who was affected?

232 unique IP addresses accessed the attacker's Funnel nodes. Of those, 87 IP addresses made more
than one request, suggesting a possible phishing form submission.

#### What was the impact?

Some Facebook users could have been phished for their credentials. Since
Tailscale Funnel proxies can only see encrypted TLS traffic, we cannot confirm
whether anyone was successfully phished.

#### What do I need to do?

Don't use Tailscale Funnel for phishing.

Description: SCIM group name disclosure via the ACL editor

#### What happened?

The [ACL editor](https://tailscale.com/kb/1338/acl-edit) in the admin console did not check [SCIM](https://tailscale.com/kb/1290/user-group-provisioning)
group names in the ACL rules against the tailnet name. This allowed tailnet A
to use SCIM groups from tailnet B in their ACL rules. A malicious user in
tailnet A could not gain access to target tailnet B this way. However, they
could use the fact that ACLs get saved without warnings to learn about valid
SCIM group names in other tailnets.

This issue was fixed on July 19th, 2024. A user trying to save ACLs with SCIM
group names from other tailnets will always receive a warning that these groups
do not exist, even if they do exist in other tailnets.

#### Who was affected?

None of the existing tailnets' ACLs appear to use SCIM group names from other
tailnets maliciously. A handful of customers used the wrong SCIM group names
from their production tailnets in their test tailnets by accident.

#### What was the impact?

A malicious user could learn about SCIM group names used in other tailnets.

#### What do I need to do?

No action is required.

Description: Accidental ACL edits due to browser caching

#### What happened?

When switching tailnets in the admin console, an [Admin](https://tailscale.com/kb/1138/user-roles#admin) user
could overwrite the [ACLs](https://tailscale.com/kb/1018/acls) of one tailnet with pending changes to ACLs
from another tailnet.

When a user has unsaved ACL changes in the admin console, those changes are
cached in browser storage. If this user is a member of multiple tailnets,
tailnet A and tailnet B, and is editing ACLs for tailnet A, using the tailnet
switcher in the top-right corner of the page would not clear the cached ACL
changes correctly. In some rare cases, saving ACLs of tailnet B after the
switch would use the cached ACL contents from tailnet A.

A user can be an Admin in multiple tailnets when they use GitHub to log in, and are a member of GitHub organizations, or the user is [invited](https://tailscale.com/kb/1271/invite-any-user) to another tailnet and granted the Admin role.

Tailnet switching in the admin console was added on May 22nd, 2023. We fixed
this bug on July 17th, 2024.

#### Who was affected?

Any user who is an Admin in multiple tailnets and edited ACLs in the admin
console between May 22, 2023 and July 17th, 2024 could trigger this bug after
switching the active tailnet.

#### What was the impact?

An Admin user could overwrite the ACLs of one tailnet with ACLs from another
tailnet.

#### What do I need to do?

If you are an Admin of multiple tailnets using the same login name, review the
ACLs in your tailnets for correctness.

Description: Potential for API credential disclosure over plaintext HTTP

#### What happened?

The [Tailscale API](https://tailscale.com/kb/1101/api) is primarily accessible over TLS-encrypted HTTP at
 `api.tailscale.com` . It also has a limited plaintext HTTP handler to serve HTTP
to HTTPS redirects.

Browsers that connect over plaintext HTTP do not send cookies marked as  `Secure` 
to prevent them from being disclosed to network intermediaries.

However, API clients that connect using plaintext HTTP and send requests
with authentication tokens in headers have no such protections to prevent
disclosure.

Before June 26, 2024, the Tailscale API did not reject credentialed plaintext
API requests and instead served them HTTP 302 redirects as it would to browsers.
Typical HTTP client libraries handle redirects transparently, and consequently, the user
would not necessarily know their credentials had been exposed.

Starting on June 26, 2024, the Tailscale API now returns errors for all plaintext
HTTP requests that include credentials. Additionally, the Tailscale API now
automatically revokes API keys that it observes sent over HTTP and notifies
Tailnet security owners of this action.

#### Who was affected?

Any Tailscale API client that connected over plaintext HTTP using credentials
before June 26, 2024.

#### What was the impact?

API clients that connected over plaintext HTTP before June 26, 2024 would have
exposed their credentials to network intermediaries, risking them to theft and
replay.

#### What do I need to do?

No action is needed at this time.

#### Credits

Thanks to [Joachim Viide](https://jviide.iki.fi/) for reporting this issue.

Description: Partial loss of audit and network flow logs

##### What happened?

An integer overflow in our logs processing service led to some customer logs
to be non-deterministically dropped with a probability of 14%.
The overflow condition first exhibited on June 7th, 2024 at 20:45 UTC and
was detected and resolved by June 14th, 2024 at 00:40 UTC.

##### Who was affected?

All tailnets that rely on audit and network flow logs have been affected.

##### What was the impact?

The 14% chance of dropped log entries affects storing of logs such as
[configuration audit logs](https://tailscale.com/kb/1203/audit-logging) and
[network flow logs](https://tailscale.com/kb/1219/network-flow-logs).
While logs can be retrieved for the timeframe that the overflow bug was active,
some fraction of the entries may be missing.

##### What do I need to do?

No action is needed at this time.

We fixed the bug, added additional error checking, and
deployed both to the logs processing service.

Description: Incorrect DNS resolution with split DNS on macOS and iOS

##### What happened?

On Tailscale macOS and iOS clients with split DNS configurations (like [App
Connectors](https://tailscale.com/kb/1281/app-connectors) or [Restricted
Nameservers](https://tailscale.com/kb/1054/dns#nameservers)), lookups of bare tailnet node names
could in rare cases return incorrect answers. For example, if a node  `mynode` 
and an App Connector for  `*.example.com`  exist on a tailnet, DNS lookups for
 `mynode`  could return the answer for  `mynode.example.com`  instead of the local
tailnet IP. This mis-configuration is intermittent, and most often triggers for
a few seconds when switching device networks (for example from Wi-Fi to a phone
hotspot).

We fixed this bug in client version 1.68.0, and notified the security contacts
of potentially affected tailnets over email.

##### Who was affected?

All tailnets that use App Connectors or Restricted Domains, and have macOS or
iOS nodes could have been affected.

This bug is usually intermittently-triggered when switching networks in our
experience. Only lookups of bare domains, like  `mynode`  but not
 `mynode.mytailnet.ts.net` , are at risk.

Note that not all split DNS domains are dangerous. Only domains where an
attacker can choose their FQDN to match a node name, and controls the
destination to receive non-TLS traffic could be abused.

We are not aware of any active exploitation of this vulnerability.

##### What was the impact?

For a split DNS domain  `example.com` , an attacker with control over
 `mynode.example.com`  can impersonate a non-TLS server running on node  `mynode` 
on the tailnet. This attack is opportunistic and passive - it relies on the
user connecting to  `mynode`  using its bare domain and cannot be forced
remotely.

##### What do I need to do?

Upgrade your macOS and iOS clients to 1.68.0 or later.

Description: Tailnet SSO provider migration impacting invited users

##### What happened?

When tailnets are created, they are associated with an [SSO
provider](https://tailscale.com/kb/1013/sso-providers) such as Google or Microsoft, requiring all members
of the tailnet to authenticate using that provider. In addition, Tailscale also
supports inviting [external users](https://tailscale.com/kb/1271/invite-any-user) to tailnets to allow
sharing with contractors, friends, or other collaborators who may use a
different SSO provider than that of the inviting tailnet to log in to
Tailscale.

Customers with an existing tailnet who wish to use a different SSO provider can
request to migrate via customer support. The internal tool used to perform these
migrations previously migrated the SSO provider for
all members of a tailnet, including those of invited external members.

We fixed this internal tool to migrate direct tailnet members, excluding invited
members on May 20, 2024.

We reverted the erroneous SSO provider changes and notified affected
users on May 23, 2024.

##### Who was affected?

55 users were invited external members of tailnets whose SSO provider was
subsequently migrated prior to May 20, 2024. We have notified the security
contacts for the tailnets where users were affected by this incident.

##### What was the impact?

Users whose SSO providers were erroneously migrated would have been
unable to log in to Tailscale during this time, as their SSO source
would differ from the one on record.

##### What do I need to do?

No action is needed at this time.

Description: Insufficient inbound packet filtering in subnet routers and exit nodes

##### What happened?

In Tailscale versions earlier than 1.66.0, [exit nodes](https://tailscale.com/kb/1103/exit-nodes), [subnet
routers](https://tailscale.com/kb/1019/subnets), and [app connectors](https://tailscale.com/kb/1281/app-connectors), could
allow inbound connections to other tailnet nodes from their local area network
(LAN). This vulnerability only affects Linux exit nodes, subnet routers, and
app connectors in tailnets where [ACLs](https://tailscale.com/kb/1018/acls) allow  `"src": "*"` , such as
with [default ACLs](https://tailscale.com/kb/1192/acl-samples#allow-all-default-acl).

Tailscale version 1.66.0 fixes the vulnerability. Additionally, a server-side
update changes the interpretation of  `"src": "*"`  to mitigate the issue
specifically for exit nodes.

Special thanks to [Hakan Ergan](https://www.linkedin.com/in/hakan-ergan/) for reporting a similar
concern that led us to discover this vulnerability.

##### Who was affected?

This affected the following nodes using Tailscale version 1.65 or earlier:

- Exit nodes on Linux

- Subnet routers on Linux

- App connectors on Linux

- Regular nodes on all platforms connecting to the above nodes

Tailnets with custom ACLs that do not use  `"src": "*"`  or any other value that
includes external IPs were not affected.

We are not aware of any active exploitation of this vulnerability.

##### What was the impact?

Devices outside of the tailnet, but on the same LAN as an exit node, subnet
router, or app connector could connect to ports on tailnet nodes that are
allowed by ACLs.

##### What do I need to do?

Upgrade the following nodes to 1.66.0 or later:

- Subnet routers on Linux

- App connectors on Linux

- Regular nodes on all platforms that use exit nodes [shared from other
tailnets](https://tailscale.com/kb/1084/sharing#sharing--exit-nodes) or [Mullvad exit nodes](https://tailscale.com/kb/1258/mullvad-exit-nodes)

We recommend enabling auto-updates and updating all nodes to the latest
version, but it is not required to mitigate this vulnerability.

A server-side change mitigated this vulnerability for other types of affected
nodes.

##### Technical details

Below, we refer to exit nodes, subnet routers, and app connectors as
packet-forwarding nodes, because the details apply to all of them. Specific
types of packet-forwarding nodes are mentioned explicitly where their behavior
is different.

Before 1.66.0, packets between regular nodes and destination hosts behind
packet-forwarding nodes were filtered based on source/destination IP as
specified in tailnet ACLs. Specifying  `"src": "*"`  in ACLs is equivalent to
 `"src": ["0.0.0.0/0", "::/0"]` , meaning any IP address. This allowed source IPs
outside of the tailnet to send packets to tailnet nodes via a packet-forwarding
node. This could be abused by malicious LAN hosts to connect into the tailnet
using a known tailnet node IP.

The attack only works on a LAN because:

- it relies on next-hop routing, which only works in a LAN

- destination IPs are in the subnet router's approved range, or in the [CGNAT
range](https://tailscale.com/kb/1015/100.x-addresses)  `100.64.0.0/10` , which are not routable over the Internet.

###### Attacks

Here are several attack scenarios.

Packet-forwarding node on an untrusted LAN.

A malicious host  `10.0.0.1`  on the same LAN as the packet-forwarding node
 `10.0.0.2`  could craft packets with destination IP of a tailnet node
 `100.64.0.1`  (using a command like  `ip route add 100.64.0.1/32 via 10.0.0.2 dev eth0` ) and send them to the packet-forwarding node. The packet-forwarding node
would accept them and forward them to the victim node. The victim node would
see a packet from  `10.0.0.1`  and accept it if the tailnet ACLs allow this
source IP.

This scenario is very similar to a legitimate use-case of
[site-to-site](https://tailscale.com/kb/1214/site-to-site) networking, where two subnets are bridged using
Tailscale subnet routers and the flag  `--snat-subnet-routes=false` .

Malicious shared exit node

A malicious exit node  `100.64.0.4`  from tailnet A could craft packets with
destination IP of tailnet B node  `100.64.0.3`  and any source IP other than
 `100.64.0.4` . Due to the built-in [quarantining](https://tailscale.com/kb/1084/sharing#quarantine) of shared
nodes, packets from  `100.64.0.4`  are rejected.

###### Mitigations

We implemented 3 separate mitigations for these attacks.

Redefine  `"src": "*"`  in ACLs

While  `*`  is a convenient shorthand in ACLs, Tailscale users almost never need
to allow connections from any IP. In most cases users intend  `*`  as "all other
nodes in my tailnet". As a mitigation for this vulnerability, we redefined  `*` 
in  `src`  section of ACLs to include:

- all tailnet nodes

- all IPs from approved subnet routes

The inclusion of IPs from approved subnet routes is needed for the site-to-site
networking setup.

For users that need the old semantics of  `*`  we added a new
 `` [autogroup:danger-all](https://tailscale.com/kb/1337/acl-syntax#src), which matches the old definition of  `*` .

Stateful packet filtering on packet-forwarding nodes

On Linux packet-forwarding nodes we added stateful packet filtering. This means
that these nodes keep track of forwarded connections and only allow return
packets for existing outbound connections. Inbound packets that don't belong to
an existing connection are dropped.

Because routing is implemented differently on non-Linux platforms, this
mitigation is only necessary on Linux.

Stateful filtering is enabled by default, except for existing subnet routers
that set  `--snat-subnet-routes=false` . You can disable stateful filtering using
 `tailscale up --stateful-filtering=false` .

Client-side quarantining of shared nodes

[Quarantining](https://tailscale.com/kb/1084/sharing#quarantine) of shared nodes was implemented by a packet
filter sent from the Tailscale control plane. This packet filter instructs
nodes to drop any inbound connections from the source IP of the shared node. To
prevent malicious shared exit nodes from crafting packets with different source
IPs, additional client-side quarantining logic was added. The 1.66.0 and later
clients reject all inbound connections from quarantined nodes, regardless of
their source IP. This is similar to how the ["shields up"](https://tailscale.com/kb/1072/client-preferences#allow-incoming-connections) mode
works within the tailnet.

Description: Unclear network flow logs collection status for alpha testers.

##### What happened?

When [network flow logs](https://tailscale.com/kb/1219/network-flow-logs) first entered private alpha, tailnet admins who were interested in testing out the feature had to request to be manually opted into the alpha testing track. When we subsequently introduced admin console settings for self-serve network flow logs for the public beta launch, these settings were not properly connected to the alpha testing track. As a result, for the small number of tailnets that volunteered for alpha testing, the admin console interface did not show that logs were still being collected as initially requested.

We fixed this bug on April 25, 2024 and the admin console now correctly shows the status of network flow logs for all users.

##### Who was affected?

15 tailnets were opted into network flow log collection through the alpha testing track that did not re-enroll through the admin console. We notified security contacts for the affected tailnets about this bug.

##### What was the impact?

The admin panel did not reflect the correct status for network flow log collection for affected tailnets, and admins of these tailnets may not have realized that network flow logs were still being collected.

##### What do I need to do?

No action is needed at this time.

Description: Bug in SSH check mode with  `checkPeriod`  set to  `0s` .

##### What happened?

[Check mode](https://tailscale.com/kb/1193/tailscale-ssh#configure-tailscale-ssh-with-check-mode) in Tailscale SSH forces an SSH client to periodically
re-authenticate when connecting to SSH servers. The period is configured via
the  `checkPeriod`  attribute in Tailscale ACLs, and defaults to 12 hours.

A bug in ACL parsing interpreted  `"checkPeriod": "0s"`  as unset, and used the
default period of 12 hours instead.

We deployed a fix for the bug in ACL parsing logic on 2024-04-23. SSH clients
in tailnets that set  `"checkPeriod": "0s"`  are now correctly prompted for
re-authentication on every connection.

Note that a special value  `"checkPeriod": "always"`  is the documented
recommended way to achieve this behavior.

We thank [Finch](https://twitter.com/plaidfinch) for reporting this issue.

##### Who was affected?

17 tailnets use Tailscale SSH with  `"action": "check"`  and  `"checkPeriod": "0s"` . We notified security contacts for the affected tailnets about this bug.

##### What was the impact?

SSH clients in the affected tailnets were prompted to re-authenticate every 12
hours, instead of during each connection as intended by the tailnet
administrators.

##### What do I need to do?

No action is needed at this time.

Description: We resolved an information disclosure vulnerability in the
[hello.ts.net](https://tailscale.com/kb/1073/hello) service.

##### What happened?

On January 15 2024, we became aware of a potential information disclosure
vulnerability in the  `hello.ts.net`  service, which could show the identity of a
different Tailscale user when loaded. The  `hello.ts.net`  service receives
identity information and public keys of nodes tied to their IP address. On
November 28 2023, we made a [change](https://tailscale.com/blog/choose-your-ip) to how IPs are assigned to
Tailscale nodes, making them globally non-unique. When the Tailscale service
assigned the same IP to multiple nodes,  `hello.ts.net`  would receive identity
information for one of the nodes at random. We confirmed on January 26 2024
that, if one of the other nodes with that IP loaded  `hello.ts.net` , they would
see another user's name, email, and hostname.

The Tailscale Security Team immediately took  `hello.ts.net`  offline while the
fix was in progress. The issue has been fixed and the  `hello.ts.net`  service
was restored on January 29 2024.

##### Who was affected?

The incident was isolated to 10 users across 9 tailnets who could have had
their information leaked to other Tailscale users. We notified the tailnet
security contacts directly in accordance with our obligations under applicable
data privacy laws. Due to the random nature of the vulnerability, we cannot
confirm that all of those users were indeed affected.

Regular [shared nodes](https://tailscale.com/kb/1084/sharing) always see unique node IPs and were not
vulnerable in a manner similar to  `hello.ts.net` .

##### What was the impact?

A small number of users had their name, email, and hostname potentially exposed
to other Tailscale users that had nodes sharing the same IP.

In addition, the  `hello.ts.net`  service was offline between January 26-29
2024. Several users reported being negatively impacted by this.

##### What do I need to do?

No action is needed at this time.

If you have a dependency on  `hello.ts.net`  as a probing target for Tailscale
connectivity, consider using [a different probing
mechanism](https://tailscale.com/kb/1073/hello#does-hellotsnet-have-a-reliability-guarantee).

Description: On Windows before Tailscale version 1.52 and on Linux before
Tailscale 1.54, the  `tailscale serve`  and  `tailscale funnel`  features allowed
users to serve the contents of directories that their user account could not
access, but which the  `tailscaled`  service process could.

##### What happened?

A user could escalate their own file read access by running, for example,
 `tailscale.exe serve http / C:\` , and then browsing to the local HTTP endpoint.

The issue can also occur on Linux if the local administrator enabled an operator
user ID with  `tailscale up --operator=$USER` , as the  `$USER`  account could
 `serve`  itself files that it could not normally read.

##### Who is affected?

Owners of Windows deployments for which the users of Tailscale nodes do not also
have OS-level administrative access, and owners of Linux deployments where the
administrator enabled non-root  `--operator`  access.

This issue can only be triggered by a local user and cannot be triggered
remotely.

##### What is the impact?

This issue enables local privilege escalation (file read access). Access to
certain system files (such as  `/etc/shadow`  on Linux) can then be used to obtain
full administrative control over the host.

##### What do I need to do?

On Windows 10 and later, upgrade to Tailscale 1.52 ([released 30 October
2023](https://tailscale.com/changelog#2023-10-30-client)) or later, which resolves the issue.

On Windows 7 and 8, upgrade to Tailscale 1.44.3 ([released 8 Jan
2024](https://tailscale.com/changelog#2024-01-08-client)), which resolves the issue.

On Linux, upgrade to 1.54 ([released 15 November 2023](https://tailscale.com/changelog#2023-11-15-client)) or later,
which resolves the issue.

The best practice is to run the latest stable version, which as of this writing
is [1.56.1](https://tailscale.com/changelog#2023-12-15-client). Consider turning on [automatic updates](https://tailscale.com/blog/auto-update-beta).

Use [Tailscale ACLs](https://tailscale.com/kb/1223/funnel) to control the availability of Funnel.

Description: [The OAuth implementation of Google Workspace](https://trufflesecurity.com/blog/google-oauth-is-broken-sort-of/) allows for the creation of Google accounts associated with a given Workspace domain that are not actually controlled by that workspace, e.g. alice+foo@example.com. As a result, these accounts may be used to retain access to systems that use Google Workspace SSO login even after the original account has been deactivated or removed.

##### What happened?

Tailscale uses Google as one of the possible identity providers for creating and joining a tailnet. Users who have emails with the same domain name can automatically sign in using SSO and be added to the corresponding tailnet (unless [user approval](https://tailscale.com/kb/1239/user-approval) is turned on for the tailnet)​​. The OAuth vulnerability reported by Truffle Security means that it is possible for an attacker to create a new personal Google Account that is attached to an alias of their legitimate Workspace account. This new account will not register as being part of the domain's Workspace, and thus cannot be removed by its admins. However, if the attacker then uses the new, spoofed Google Account to log into Tailscale, we would have treated it as a legitimate user in the tailnet. Thus, users could remain connected to a tailnet using this spoofed account even if their primary Workspace account has been disabled, e.g. after employee termination.

We became aware of the vulnerability on 2023-12-21 when its disclosure by Truffle Security was circulated widely. We deployed a remediation that prevents personal Google accounts from logging into tailnets associated with Workspace accounts on 2023-12-21.

##### Who is affected?

Everyone who uses Google Workspace to sign in.

##### What is the impact?

Tailnets that use Google Workspace as their SSO provider may have Tailscale users that do not have a corresponding user in the Google Workspace. Prior to 2023-12-21, this would have made it possible for those users to retain access to Tailscale after their SSO account was deleted. Following the remediation, these users can no longer login to Tailscale.

##### What do I need to do?

Tailscale admins should visit [the Users page of the Tailscale admin console](https://login.tailscale.com/admin/users) and audit the list of users to see if there are unknown addresses that should not be there. Admins can also [export this list of users](https://tailscale.com/kb/1229/export-user-list) as a CSV file to examine offline.

For extra security, you can turn on [user approval](https://tailscale.com/kb/1239/user-approval) for your Tailnet so that every new user of Tailscale has to be manually approved by an admin. Note: this does not mitigate against situations where the attacker is themselves an admin of Tailscale.

Description: Privilege escalation bugs in the Tailscale
Kubernetes operator's API proxy allowed authenticated tailnet clients
to send Kubernetes API requests as the operator's service account.

Tailscale Kubernetes operator version v1.53.37 fixes the issue and
users of the operator who enable the API proxy functionality should
update as described below.

##### What happened?

The Tailscale Kubernetes operator can optionally act as [an API server
proxy](https://tailscale.com/kb/1437/kubernetes-operator-api-server-proxy)
for the cluster's Kubernetes API. This proxy allows authenticated
tailnet users to use their tailnet identity in Kubernetes
authentication and RBAC rules. The API server proxy uses
[impersonation
headers](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation)
to translate tailnet identities to Kubernetes identities.

The operator prior to v1.53.37 has two bugs in the forwarding logic,
which affects different modes of operation:

- In the default proxy mode that applies Tailscale identity to
proxied requests, incorrect header sanitization allowed a request
with a crafted  `Connection`  header to drop the impersonation
headers from the proxied request. This caused the proxied request
to be authenticated as the operator's service account, and inherit
the operator's permissions.

- In the
[no-auth](https://tailscale.com/kb/1437/kubernetes-operator-api-server-proxy#configuring-api-server-proxy-in-noauth-mode)
proxy mode, which does not apply Tailscale identity to forwarded
requests, a specially crafted request could similarly cause the
proxied request to use the operator's identity, with similar
results.

The bug was reported by [Mo Khan](https://github.com/enj) from Microsoft on
2023-11-01, and fixed on the same day.

##### Who is affected?

Tailnets using [the API server
proxy](https://tailscale.com/kb/1437/kubernetes-operator-api-server-proxy)
in Tailscale Kubernetes operator images with the following tags are affected:

-  `unstable-v1.53.20`  or earlier

-  `unstable`  deployed before the tag was updated to 1.53.37, some time
on 2023-11-01.

Operator users running in the default operator configuration are
not affected, as the API proxy is not enabled by default.

##### What is the impact?

Authenticated tailnet users who have access to the operator's API
proxy can make requests to the Kubernetes API with operator
privileges. In the proxy mode that allows the operator to use
impersonation, this can be used for further privilege escalation to
other cluster identities.

External attackers cannot exploit this vulnerability without being
a member of the tailnet.

##### What do I need to do?

Update the Tailscale Kubernetes operator image to version unstable-v1.53.37 or
later.

If you used the official [operator manifest
file](https://github.com/tailscale/tailscale/blob/main/cmd/k8s-operator/deploy/manifests/operator.yaml),
download the new manifest file and run  `kubectl apply -f manifest.yaml` .

If you used the Helm chart, set the
 `` [operatorConfig.image.tag](https://github.com/tailscale/tailscale/blob/ca4c940a4d0ac3274ee91a58e4823afb3c92ae0b/cmd/k8s-operator/deploy/chart/values.yaml#L16)
to  `unstable-v1.53.37`  in the  `values.yaml`  file and run  `helm upgrade <path-to-chart-directory> -n tailscale -f <path-to-values-file>` 

If you wrote your own manifest or Helm chart, update the  `k8s-operator`  image
tag to  `unstable-v1.53.37`  and redeploy it.

Description: Microsoft Defender is flagging Tailscale 1.46.1 as malware.
These classifications are false positives, and we are working with Microsoft to
resolve the situation.

As of 2023-10-27 1:05 AM UTC, we have confirmed that Microsoft have addressed
the false positive, meaning Defender no longer flags Tailscale 1.46.1 as
malware. A rescan of [tailscaled.exe 1.46.1 on VirusTotal](https://www.virustotal.com/gui/file/cfbf0c7ef964198e39f9cc97350626673468d311b8626c6b9bef6c95e40e569b) confirms this.

##### What happened?

Microsoft Defender was flagging Tailscale 1.46.1 as malware. This caused
Defender to quarantine the binaries, meaning they could not run.

We submitted Tailscale 1.46.1 to Microsoft to investigate the false positive,
who then updated Defender to avoid flagging this release as malware at
2023-10-27 1:05 AM UTC.

##### Who is affected?

People using Defender and Tailscale 1.46.1.

##### What is the impact?

Tailscale will not run on affected machines.

##### What do I need to do?

To resolve this issue on your own tailnet, you can take either or both of 2
approaches:

- Update to a newer version of Tailscale. Newer versions are not affected by this problem.

- Create an exception in Microsoft Defender. Microsoft has published [instructions explaining how to do this](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26).

- Update Microsoft Defender.

Description: An issue in the Tailscale client, combined with a behavior
of the UPnP implementations in some routers, could expose all UDP ports of a
node to external networks (usually the internet).

As of 2023-08-22 2:30 AM UTC, we have changed the Tailscale coordination server
to advise nodes to stop using UPnP for port mapping. In some cases this can
degrade NAT traversal and may cause some connections to route through DERP.
This may increase node-to-node latency and decrease throughput. Version 1.48.1
resolves the issue and re-enables port mapping via UPnP.

##### What happened?

Tailscale nodes use UPnP as one of the mechanisms to open UDP port forwarding
in routers to help with NAT traversal. Tailscale picks a node port and an
external router port and requests forwarding between them. On first start
Tailscale requested external port  `0` , which many routers interpret as a
request to pick a random available port. However, some routers interpret this
as a request to listen on all external ports and forward traffic to matching
node ports.

Depending on the router's implementation of UPnP, a node could end up open to
all UDP traffic from external networks. If some processes listen on UDP ports
on the node, this could be used as a vector of attack against other software
running on the node.

Any firewall software running on the node would be able to stop unwanted UDP
packets, if configured to do so.

The bug was discovered and fixed on 2023-08-21, and the fix was published in
the 1.48.1 release.

##### Who is affected?

The only known vulnerable routers are those running the  `miniupnpd`  server,
versions 1.9 (2016) or earlier. Other UPnP server implementations may also be
vulnerable, but Tailscale is not aware of any as of 2023-08-22.

A small percentage of nodes listened on router port  `0`  via UPnP before the
mitigation was deployed. All nodes running vulnerable versions now have UPnP
port mapping disabled.

##### What is the impact?

Any node service listening on UDP ports from any IP could receive traffic from
external networks. This only applies to networks where the router implements
UPnP wildcard port support.

If such a service does not implement authentication and/or authorization,
allows packets to trigger sensitive actions, or has separate
remotely-exploitable vulnerabilities, the node could be compromised by an
attacker.

##### What do I need to do?

UPnP on vulnerable versions was disabled by the coordination server. Update
Tailscale to version 1.48.1 or later to restore NAT traversal using UPnP for
better node connectivity.

We do not recommend disabling UPnP or other port-mapping protocols on your
router. These protocols greatly improve connectivity for Tailscale and other
applications.

Description: An issue in the Tailscale coordination server in device
reauthentication logic caused previously authenticated and tagged devices to
lose their [ACL tags](https://tailscale.com/kb/1068/acl-tags/) upon reauthentication.

##### What happened?

The logic that handles the reauthentication to a new identity on an
already-authenticated device with tags had a bug: instead of updating the
device’s logged-in identity to the newly authenticated user, the device’s
identity became that of the user who originally added it to the tailnet, without
any tags.

The bug was introduced on 2022-10-26, and discovered and remediated on
2023-04-21. The bug was discovered when troubleshooting a user-reported issue.

##### Who is affected?

189 tailnets triggered this bug in the course of normal use of Tailscale, either
directly by explicitly re-authenticating a device, or indirectly by using [fast
user switching](https://tailscale.com/kb/1225/fast-user-switching/) to switch between multiple
tailnets.

We have notified affected organizations where we have [security
contacts](https://tailscale.com/kb/1224/contact-preferences/#setting-the-security-issues-email).

##### What is the impact?

Devices that encountered the bug had their tags removed, which reverted the
device’s identity to that of the user who originally authenticated the device,
or the owner of the auth key that was originally used to authenticate the
device. In either case, this is the user listed as “Creator” in the Machines tab
of the admin panel. Depending on access rules in the tailnet policy file, this
could change the device’s network permissions.

We have analyzed the audit logs for affected tailnets, and found no evidence of
deliberate exploitation. In most instances, device owners noticed the incorrect
outcome of reauthentication, and corrected the device’s state themselves.

##### What do I need to do?

If you were not contacted by Tailscale, no action is required.  If you were
contacted by Tailscale, reapply the desired tags to affected devices in the
admin console, or by reauthenticating the devices. Tailscale has deployed a fix
to the coordination server as of 2023-04-21, and notified affected
organizations.

Description: An issue in the Tailscale coordination server allowed tailnets created by GitHub organizations which were subsequently renamed to be associated with a new GitHub organization with the previous name.

#### What happened?

Tailscale mapped tailnets created by GitHub organizations to their organization name, rather than to their organization ID. This meant that if a GitHub organization was renamed, and the previous name taken over by a new GitHub organization, the existing tailnet would be tied to the new GitHub organization instead of the original one.

#### Who is affected?

Up to 1,305 tailnets created by GitHub organizations may have been affected, if those GitHub organizations were renamed between 2021-06-18 and 2023-03-30 and fully relinquished the old GitHub organization name. Additional tailnets created by GitHub organizations could be verified to definitely not have been renamed in that time period based on organization membership.

No tailnets were definitively found to have been affected. If a tailnet created by a GitHub organization is affected, we can detect this the next time an unauthorized user logs in to the tailnet belonging to the renamed organization and block their access. We will contact the [security contact](https://tailscale.com/kb/1224/contact-preferences/#setting-the-security-issues-email) for that tailnet if that happens.

#### What is the impact?

A renamed GitHub organization may have had their previous tailnet visible to a newly created GitHub organization with the same name.
The new GitHub organization would be aware of the existence of the previous tailnet. Devices added to the new GitHub organization would be aware of the existence and some metadata of previous added devices, including: their host names, their OS and version, when the devices were last connected, and their public IP addresses. They would have been able to connect to these devices if allowed by ACLs. The new GitHub organization would not have had any admin access or be able to see or modify any setting in the admin console.

There is no evidence of this vulnerability being purposefully triggered or exploited.

#### What do I need to do?

No action is required. Tailscale has deployed a fix to the coordination server as of 2023-03-30.

GitHub organizations which were previously renamed and lost access to their tailnet should [contact support](https://tailscale.com/contact/support/). When renaming a GitHub organization, [contact support](https://tailscale.com/contact/support/?type=sso) to migrate the tailnet to the new GitHub organization.

#### Credits

We would like to thank [Thomas Way](https://6f.io/) for reporting this issue.

Reference: [CVE-2023-28436](https://www.cve.org/CVERecord?id=CVE-2023-28436)

Severity: Medium

CVSS vector string: CVSS:3.0/AV:A/AC:L/PR:H/UI:R/S:C/C:H/I:N/A:N

Description: A vulnerability identified in the implementation of Tailscale SSH in FreeBSD allowed commands to be run with a higher privilege group ID than that specified by Tailscale SSH access rules.

Affected platforms: FreeBSD

Patched Tailscale client versions: v1.38.2 or later

#### What happened?

A difference in the behavior of the FreeBSD  `setgroups`  system call from POSIX meant that the Tailscale client running on a FreeBSD-based operating system did not appropriately restrict groups on the host when using Tailscale SSH. When accessing a FreeBSD host over Tailscale SSH, the egid of the tailscaled process was used instead of that of the user specified in Tailscale SSH access rules.

#### Who is affected?

9 tailnets with 22 FreeBSD nodes running Tailscale SSH since Tailscale v1.34 (released on 2022-12-04) may have had Tailscale SSH sessions with a higher privilege group ID than that specified in Tailscale SSH access rules.

We have notified affected organizations where we have [security contacts](https://tailscale.com/kb/1224/contact-preferences/#setting-the-security-issues-email).

#### What is the impact?

Tailscale SSH commands may have been run with a higher privilege group ID than that specified in Tailscale SSH access rules if they met all of the following criteria:

- The destination node was a FreeBSD device with Tailscale SSH enabled;

- Tailscale SSH access rules permitted access for non-root users; and

- A non-interactive SSH session was used.

#### What do I need to do?

If you are running Tailscale on FreeBSD, upgrade to v1.38.2 or later to remediate the issue. Admins of a tailnet can view [FreeBSD nodes with unpatched versions](https://login.tailscale.com/admin/machines?q=version%3A%3C1.38.2+freebsd) in the admin console.

To update the local ports tree in advance of what's available upstream, you can:

-  `cd /usr/ports/security/tailscale` 

- edit the Makefile to set  `PORTVERSION`  to  `1.38.2` 

-  `make makesum` 

-  `make install` 

Tailscale SSH on other platforms is not affected.

#### Credits

We would like to thank [Ryan Belgrave](https://www.linkedin.com/in/rbelgrave/) for reporting this issue.

Description: An issue in the Tailscale coordination server allowed nodes with expired node keys to continue communicating with other nodes in a tailnet.

#### What happened?

There was a flaw in Tailscale’s logic for expiring node keys. If the set of nodes that can connect in a tailnet (the netmap) didn’t have any changes, then expired node keys were not immediately removed from the netmap. The longest delay in removal was 19 days, from 2022-12-20 to 2023-01-09.

#### Who is affected?

All tailnets with nodes whose node keys expired prior to 2023-01-12 may have been affected. Admins of a tailnet can view [nodes with expired node keys](https://login.tailscale.com/admin/machines?q=disabled%3Aexpired) in the admin console.

#### What is the impact?

Connections between nodes could continue after a node key expired, both when the expired node key was the source or when it was the destination of a connection. Connections to nodes with expired node keys would only be possible if they met all of the following criteria:

- The peer node was in the same tailnet as, or shared into a tailnet with the node with the expired node key;

- The peer node and the node with the expired node key were allowed to connect based on the access rules in the tailnet policy file at the time of expiry of the node key;

- The tailnet’s netmap, including access rules, nodes added or removed from the tailnet, or connectivity of nodes in the tailnet did not change since the node key expiry; and

- Tailscale had not deployed a change to the coordination server since the node key expiry.

#### What do I need to do?

No action is required. Tailscale has deployed a fix to the coordination server as of 2023-01-11.

Upgrade clients to v1.36 or later for an additional mitigation. In conjunction with the coordination server fix, this mitigation prevents nodes from connecting to nodes with expired node keys if the Tailscale coordination server is offline or unreachable.

#### Credits

We would like to thank [Derek Ellis](https://me.ellisd.com) and [Alex Eiser](https://www.cranksecurity.com/) for reporting this issue.

Description: An issue in the Tailscale coordination server allowed a malicious individual to share nodes from other tailnets to themselves, if they knew the node ID of the target.

#### What happened?

A bug in Tailscale’s node sharing logic allowed the creation of sharing invitations by unauthorized users. A malicious individual who knew a target node’s database ID could generate and accept a sharing invite for that node without being an admin of the target node’s tailnet.

This was possible for any node in any tailnet, as long as the individual knew the target’s node ID. The node ID is an integer used in the admin panel’s database, and is not related to the node “StableID” that is visible to Tailscale clients. A node’s ID is only visible in the API or admin console, by admins of either the node’s tailnet or a tailnet to which that node has already been shared. IDs are random 64-bit numbers that are not sequential or otherwise easily guessable.

The bug was introduced on 2022-09-14, reported to us on 2023-01-11, and remediated on 2023-01-12.

#### Who is affected?

All tailnets with nodes are affected.

#### What is the impact?

This vulnerability was not triggered or exploited. Analysis of tailnet logs shows that no unauthorized shares were created or accepted while the vulnerability was present, except as part of the proof of concept from the individual who reported the vulnerability.

Admins of a tailnet can review [nodes that are shared out of their tailnet](https://login.tailscale.com/admin/machines?q=shared%3Aout) in the admin console. Sharing invites are logged as [events in configuration audit logs](https://tailscale.com/kb/1203/audit-logging/#events-for-shared-nodes). Admins can also review [invites created and accepted in their configuration audit logs](https://login.tailscale.com/admin/logs?events=%5B%22INVITECREATENODE_SHARE%22%2C%22INVITEACCEPTNODE_SHARE%22%5D) in the admin console.

#### What do I need to do?

No action is required. Tailscale has deployed a fix to the coordination server as of 2023-01-12, and verified that the vulnerability was not exploited.

#### Credits

We would like to thank Benjamin Roberts ([tsujamin](https://github.com/tsujamin)) for reporting this issue.

Reference: [CVE-2022-41925](https://www.cve.org/CVERecord?id=CVE-2022-41925)

Severity: Low

CVSS vector string: CVSS:3.0/AV:A/AC:L/PR:N/UI:R/S:C/C:L/I:N/A:N

Description: A vulnerability identified in the Tailscale client allows a malicious website to access the peer API, which can then be used to access Tailscale environment variables.

Affected platforms: All

Patched Tailscale client versions: v1.32.3 or later, v1.33.257 or later (unstable)

#### What happened?

In the Tailscale client, the peer API was vulnerable to DNS rebinding. This allowed an attacker-controlled website visited by the node to rebind DNS for the peer API to an attacker-controlled DNS server, and then making peer API requests in the client, including accessing the node’s Tailscale environment variables.

#### Who is affected?

All Tailscale clients prior to version v1.32.3 are affected.

#### What is the impact?

An attacker with access to the peer API on a node could use that access to read the node’s environment variables, including any credentials or secrets stored in environment variables. This may include Tailscale authentication keys, which could then be used to add new nodes to the user’s tailnet. The peer API access could also be used to learn of other nodes in the tailnet or send files via Taildrop.

An attacker with access to the peer API who sent a malicious file via Taildrop which was accessed while it was loading could use this to gain access to the local API, and remotely execute code.

There is no evidence of this vulnerability being purposefully triggered or exploited.

#### What do I need to do?

Upgrade to v1.32.3 or later to remediate the issue.

#### Credits

We would like to thank [Emily Trau](https://github.com/emilytrau) and [Jamie McClymont (CyberCX)](https://twitter.com/JJJollyjim) for reporting this issue. Further detail is available in [their blog post](https://emily.id.au/tailscale).

Reference: [CVE-2022-41924](https://www.cve.org/CVERecord?id=CVE-2022-41924)

Severity: Critical

CVSS vector string: CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:H

Description: A vulnerability identified in the Tailscale Windows client allows a malicious website to reconfigure the Tailscale daemon  `tailscaled` , which can then be used to remotely execute code.

Affected platforms: Windows

Patched Tailscale client versions: v1.32.3 or later, v1.33.257 or later (unstable)

#### What happened?

In the Tailscale Windows client, the local API was bound to a local TCP socket, and communicated with the Windows client GUI in cleartext with no Host header verification. This allowed an attacker-controlled website visited by the node to rebind DNS to an attacker-controlled DNS server, and then make local API requests in the client, including changing the coordination server to an attacker-controlled coordination server.

#### Who is affected?

All Windows clients prior to version v1.32.3 are affected.

#### What is the impact?

An attacker-controlled coordination server can send malicious URL responses to the client, including pushing executables or installing an SMB share. These allow the attacker to remotely execute code on the node.

Reviewing all logs confirms this vulnerability was not triggered or exploited.

#### What do I need to do?

If you are running Tailscale on Windows, upgrade to v1.32.3 or later to remediate the issue.

#### Credits

We would like to thank [Emily Trau](https://github.com/emilytrau) and [Jamie McClymont (CyberCX)](https://twitter.com/JJJollyjim) for reporting this issue. Further detail is available in [their blog post](https://emily.id.au/tailscale).

Description: An issue in Tailscale’s implementation of the OAuth authentication flow for GitHub allowed users who authenticate to Tailscale with their GitHub user identity to create a tailnet for a GitHub organization using [SAML authentication](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/about-authentication-with-saml-single-sign-on) in [GitHub Enterprise Cloud](https://docs.github.com/en/get-started/onboarding/getting-started-with-github-enterprise-cloud), where Tailscale is not an [authorized OAuth app](https://docs.github.com/en/enterprise-cloud@latest/authentication/keeping-your-account-and-data-secure/authorizing-oauth-apps) for their organization.

#### What happened?

Tailscale silently ignored a 403 error to the [GitHub API query for organizations for an authenticated user](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/orgs#list-organizations-for-the-authenticated-user) that was returned when a user authenticated to SAML, but the organization had not authorized Tailscale. This only applied to organizations using SAML on GitHub Enterprise Cloud with OAuth app authorization enabled, and where Tailscale was not authorized.

As a result, a user identity could bypass the organization’s OAuth app access restrictions, and create a tailnet for the GitHub organization.

#### Who is affected?

Up to 7 tailnets for GitHub organizations on GitHub Enterprise Cloud which use SAML for authentication may have been created between 2021-06-18 and 2022-06-03 without Tailscale being an authorized OAuth app for their GitHub organization, and could have used Tailscale to connect devices in that organization. An additional 10 tailnets were created with no or only one device, and so could not have used Tailscale to connect between devices.

We have notified the Tailscale admins for the affected organizations who we were able to identify. We do not have a way to notify the GitHub organization owners.

If you’re a GitHub organization owner, you can see if Tailscale is approved for your GitHub organization by going to the organization’s settings page and selecting “Third-party access” from the left-hand navigation. Or, for an organization  `$your-org` , navigate to
 ` `https://github.com/organizations/$your-org/settings/oauth_application_policy
` ` 

#### What is the impact?

A tailnet may have been created for a GitHub organization without their GitHub organization owner’s approval.  In this case, the use of Tailscale and the creation of a tailnet could be perceived as being sanctioned by their organization when it might not have been.

#### What do I need to do?

If you are affected, you will need to re-authenticate to keep using your tailnet. Tailscale has expired all admin console sessions for potentially affected GitHub organizations as of 2022-06-13. As a result, users in a potentially affected tailnet will need to re-authenticate the next time they access the admin console, and will not be able to do so without Tailscale being an authorized OAuth app, which may first require getting approval from their GitHub organization owner. Nodes in a potentially affected tailnet will also need to re-authenticate when their node keys expire. If you’re a GitHub organization owner, you can approve Tailscale as an OAuth app by following GitHub’s instructions for [Approving OAuth Apps for your organization](https://docs.github.com/en/organizations/restricting-access-to-your-organizations-data/approving-oauth-apps-for-your-organization).

Tailscale has deployed a fix to the coordination server as of 2022-06-03, so that no new tailnets can be created without a GitHub organization owner’s approval.

#### Credits

We would like to thank [Aurelia](https://github.com/acuteaura) for reporting the issue. Further detail is available in [their blog post](https://notes.acuteaura.net/posts/github-enterprise-security/).

Description: An issue in the Tailscale coordination server allowed individuals creating a new Tailscale account with a gmail.com email address to join the same tailnet, rather than individual tailnets.

#### What happened?

There was a flaw in Tailscale’s logic for migrating accounts between identity providers, and a new gmail.com shared tailnet was accidentally created. Once created, any user who tried to create a new Tailscale account with a gmail.com email address joined the shared gmail.com tailnet.

#### Who is affected?

A total of 44 users with 59 devices who created accounts for their gmail.com email addresses on 2022-05-11 between 10:56 and 13:12 PT were affected. We have notified affected users.

#### What is the impact?

Six connections between devices belonging to different users were made, but no traffic of concern flowed between them. Four connections were pings, and two connections were UDP traffic on port 27036, likely automated broadcasting by a gaming platform to discover peers to play with. There is no evidence of malicious traffic.

Impacted users could see some metadata about other users and devices from their devices’ clients, including users’ names, devices’ host names, and devices’ Tailscale IP addresses. This information was viewed by at least one user, who reported it to us.

One user, the tailnet Admin, was able to see all users and devices added to the shared gmail.com tailnet. This includes users’ email addresses, names, and when they were last connected; and devices’ host names, their OS and version, when the devices were last connected, and their public IP addresses. This information was viewed by the user, who reported it to us.

#### What do I need to do?

No action is required. Tailscale has deployed a fix to the coordination server as of 2022-05-11 13:12 PT.

New users registering for a Tailscale account with a gmail.com email address will create a tailnet as normal.

#### Credits

We would like to thank [David Swafford](https://www.linkedin.com/in/davidswafford/) and George Constantinides for reporting the issue.

Description: An issue in the Tailscale coordination server allowed individuals using GitHub to authenticate to Tailscale to have their devices join a tailnet associated with an empty GitHub username.

#### What happened?

There was a flaw in Tailscale’s authorization logic for the GitHub identity provider. If a user tried to authenticate to Tailscale using their GitHub identity, and GitHub returned a 500 error, then in some cases, Tailscale interpreted that as authorization for an empty GitHub username, and connected these devices to the tailnet associated with the empty GitHub username.

#### Who is affected?

A total of five devices belonging to four users were affected between 2021-06-15 and 2022-02-04, when the issue was reported and remediated. We have contacted the two users we were able to identify.

You may be affected if you authenticated to Tailscale using a GitHub account, and after authorizing a connection using GitHub, you received a connection error. Without being asked to select which GitHub user or organization tailnet to connect to, your device would have connected to a tailnet.

#### What is the impact?

No device connected to another device in the tailnet. Other than the two devices which belonged to the same user, no two devices in the tailnet had valid node keys at the same time, and so did not and would not have been able to establish connections.

A device’s existence and some metadata was shared with devices added later in time. Devices added later in time were able to see previously added devices, including: their host names, their OS and version, when the devices were last connected, and their public IP addresses.

There is no evidence of this vulnerability being purposefully triggered or exploited.

#### Credits

We would like to thank Marvin Boothby ([boothb](https://github.com/boothb)) for reporting the issue.

## Try Tailscale for  free

[Get started](https://login.tailscale.com/start)Schedule a demo[Contact sales](https://tailscale.com/contact/sales)
