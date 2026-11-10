---
title: "Ed25519-CLI – command-line interface for the Ed25519 signature system"
url: https://lib25519.cr.yp.to/ed25519-cli.html
clipped: 2026-06-17 02:04:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Ed25519-CLI – command-line interface for the Ed25519 signature system](https://lib25519.cr.yp.to/ed25519-cli.html)

## Digest Summary
The lib25519 package implements X25519 encryption and Ed25519 signatures, providing command‑line tools for Ed25519 operations. **ed25519-keypair** generates a random secret key and the matching public key, outputting the public key on file descriptor 5 and the secret key on descriptor 9. **ed25519-sign** reads a secret key from descriptor 8, reads a message from stdin, signs it, and writes the signed message to stdout. **ed25519-open** reads a public key from descriptor 4, reads a signed message from stdin, verifies the signature, and outputs the original message to stdout. Each tool returns exit status 0 on success and non‑zero on failure; a status 100 from ed25519-open indicates an invalid signature, producing no output. The utilities are designed for use in shell scripts or via foreign‑function interfaces, with separate X25519 tools documented elsewhere. (Reference: x25519-cli(1), lib25519(3)).

## Discussion Summary
The discussion highlights confusion over the tools’ inconsistent use of numbered file descriptors, prompting calls for more intuitive designs such as adopting OpenSSH for broader cryptographic support. Concerns are raised about the potential for credential‑stealing malware given the code’s public hosting, and the overall impression is that the utilities occupy an awkward, risky middle ground that many view as poorly engineered and prone to user error.

---

## Full Article

lib25519: Ed CLI

### NAME

ed25519-cli - command-line interface for the lib25519 implementation of the Ed25519 signature system

### SYNOPSIS

Key generation:

```
ed25519-keypair 5>publickey 9>secretkey
```

Signature generation:

```
ed25519-sign 8<secretkey <message >signedmessage
```

Signature verification and message recovery:

```
ed25519-open 4<publickey <signedmessage >message
```

### DESCRIPTION

lib25519 is an implementation
of the X25519 encryption system
and the Ed25519 signature system.
The command-line interface for lib25519
provides three Ed25519 tools,
documented here,
and two X25519 tools,
documented separately.

Each tool exits nonzero on failure (e.g., running out of memory), 0 on success.

These tools allow lib25519
to be easily used from shell scripts.
Other languages can also use lib25519 via these tools,
but languages typically have good support for FFI
and can use the C interface directly.

### KEY GENERATION

Alice runs the `ed25519-keypair` command.
This command randomly generates
Alice's secret key and Alice's corresponding public key.
It writes the public key to file descriptor 5,
and then writes the secret key to file descriptor 9.

### SIGNATURE GENERATION

Alice runs the `ed25519-sign` command.
This command reads Alice's secret key from file descriptor 8.
It then reads a message (into memory) from standard input (file descriptor 0).
It signs the message using Alice's secret key,
and then writes the signed message to standard output (file descriptor 1).

### SIGNATURE VERIFICATION AND MESSAGE RECOVERY

Bob runs the `ed25519-open` command.
This command reads Alice's public key from file descriptor 4.
It then reads a signed message (into memory) from standard input (file descriptor 0).
It verifies the signed message using Alice's public key,
and then writes the verified message to standard output (file descriptor 1).

For `ed25519-open`,
exit code 100 specifically indicates an invalid signature;
retrying on the same input will then always fail.
In this case, `ed25519-open` produces an empty output.

### SEE ALSO

**x25519-cli**(1), **lib25519**(3)

---

**Version:**
This is version 2024.02.18 of the "Ed CLI" web page.