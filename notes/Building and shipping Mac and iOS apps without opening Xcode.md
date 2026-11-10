---
title: "Building and shipping Mac and iOS apps without opening Xcode"
url: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/
clipped: 2026-08-31 12:22:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Building and shipping Mac and iOS apps without opening Xcode](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/)

## Digest Summary
Xcode must be installed, but all building, signing and notarizing can be run from the shell using the tools bundled inside Xcode.app: xcodebuild, notarytool, stapler and devicectl. First set the command‑line toolchain to Xcode ( sudo xcode-select –s /Applications/Xcode.app/Contents/Developer ). Perform one‑time GUI actions: log in with a paid Apple Developer account, create a **Developer ID Application** certificate (installed in the login keychain), and store a notarization credential with `xcrun notarytool store-credentials ` using an app‑specific password. Install **XcodeGen** (Homebrew or GitHub) and keep only a `project.yml` in source; the `.xcodeproj` folder is regenerated on each build. Add a `Local.xcconfig` containing `DEVELOPMENT_TEAM` and `BUNDLE_PREFIX` and exclude it from git.  

A single script (e.g., `scripts/release.sh`) automates the full pipeline:  

1. Regenerate the project with xcodegen.  
2. Archive via xcodebuild ‑‑archivePath.  
3. Export a Developer ID‑signed app using an ExportOptions.plist.  
4. Zip and submit to Apple with notarytool ‑‑wait.  
5. Staple the notarization ticket using stapler.  
6. Verify with spctl and copy the app to /Applications.  

After the initial setup, builds and deployments are completely headless.

---

## Full Article

Lately, Iâve heard several Apple related podcasters talk about how bad Xcode is, and how Apple needs to make vibe-coding Mac and iOS apps better by making Xcode less inscrutable. Theyâre not wrong, but also I donât understand why theyâre even opening Xcode in the first place. With a little bit of pre-work, you can vibe code Mac and iOS apps to your heartâs content without looking at Xcode anymore.

And if youâre ever in doubt about how to make any of the following work, point Claude Code or your LLM coding tool of choice to this blog post, and let it figure it out. Thatâs literally its job, figuring out things you donât want to have to.

## TL;DR

- Xcode.app must be installed, but it never has to be open.  `xcodebuild` ,  `notarytool` ,  `stapler` , and  `devicectl`  all live inside Xcode and run fine from a shell.

- A few one-time steps do need the GUI (or an interactive terminal): sign into your Apple ID, create a Developer ID certificate, store a notarization password. After that, builds and deploys are fully headless.

- The Mac app ships via one script â  `scripts/release.sh`  â which you write once. It runs the whole chain: archive â Developer ID sign â notarize â staple â install to  `/Applications` .

- Signing is certificate-and-keychain based. The signing key lives in the login keychain;  `xcodebuild`  finds it automatically. No secrets in the repo.

The one-time setup is the only part with any friction, so letâs get it out of the way first.

## Install Xcode

You do have to have Xcode installed, thereâs no getting around that, because build depends on tools that live inside Xcode.app.

Once Xcode is installed, make sure itâs the selected command line toolchain, and not  `/Library/Developer/CommandLineTools` . If the output of the check is  `/Applications/Xcode.app/Contents/Developer` , youâre in good shape:
 ` `â¯ xcode-select -p
/Applications/Xcode.app/Contents/Developer` ` 

If it DOES return the path for the standalone CommandLineTools instead, point it to Xcode.
 ` `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer` ` 

NOTE: The name âCommand Line Toolsâ can be confusing.

This is because thereâs a standalone Command Line Tools package, available with  `xcode-select --install` , which is the  `/Library/Developer/CommandLineTools`  version. This contains clang and git, but not the iOS SDK, notarytool, devicectl, and other items needed for full app development.

The complete toolchain is inside Xcode.app, at  `/Applications/Xcode.app/Developer` , and it has everything you need. If you have Xcode installed, you donât need the standalone Command Line Tools.

## Install XcodeGen

Xcode and its command line tools arenât enough to generate and manage Xcode projects automatically. For that, youâre going to need [XcodeGen](https://xcodegen.com/). You can [download it from Github](https://github.com/yonaskolb/XcodeGen) or install it using homebrew:
 ` `brew install xcodegen` ` 

Long story short, Xcode projects are actually folders that macOS makes appear as files, and they contain everything about your project needed to create and compile your app. Xcode constantly modifies the files and file references constantly, and it creates issues for git repositories.

Xcodegen creates a project.yml (YAML) file with all your project settings, and then on every build, it recreates the entire .xcodeproj folder using that project.yml file. Only the YAML file has to be committed to git, and the whole .xcodeproj can be ignored from gitâs perspective.

## Configure Xcode, Once

You do need to setup Xcode initially in order to never have to look at it again.

### Xcode License and Additional Components

First, either accept its license and install its additional components, or do it through the command line:
 ` `sudo xcodebuild -license accept
sudo xcodebuild -runFirstLaunch` ` 

### Setup Your Apple Developer Account in Xcode

Next, open Xcode, click on Settings â Accounts and click on + to add your account.

NOTE: You have to have a paid Apple Developer account in order to distribute and notarize your apps.

And you will want them notarized in order to install them on you Mac and iOS devices and not have the OSes decided theyâre malware and delete them.

### Create a Developer ID Application Certificate

Once thatâs done, create a Developer ID Application certificate (Settings â Accounts â your Apple ID â Manage Certificatesâ¦ â + â Developer ID Application), which creates a cert for signing the shipped .app bundle.

Please note that a Developer ID Application certificate and your Apple Development certificate are two separate things.

The Apple Development identity is for building and running on your own devices â pushing to your iPhone, local debugging. The Developer ID Application identity is for the notarized  `.app`  that survives Gatekeeper and runs on someone elseâs Mac. The release script wants that second one.

Creating the certificate in Xcode installs both the certificate and its private key into your login keychain. That private key is what actually does the signing, and it cannot be re-downloaded â so donât delete it, and back up your keychain.

When in doubt, ask your LLM of choice about them and have it help you get set up. Itâs the one thatâs going to be using Xcode for you anyway.

And finally,

### Store a Notarization Credential â Once, in Terminal

Notarization uploads your signed app to Apple for a malware scan.  `notarytool`  authenticates using a stored keychain profile that you create once, interactively â it prompts for an app-specific password, and thereâs no way around the prompt:
 ` `
xcrun notarytool store-credentials App-Name \
  --apple-id "[[email protected]](https://scottwillsey.com/cdn-cgi/l/email-protection)" --team-id YOUR-TEAM-ID
# paste an app-specific password when prompted
` ` 

A few things worth knowing here:

- Name the profile after the app. Donât borrow another appâs profile â itâll work on your machine and then silently break on someone elseâs.

- The app-specific password is not your Apple ID password. Generate one at [appleid.apple.com](https://appleid.apple.com) â Sign-In & Security â App-Specific Passwords.

- These passwords go stale silently whenever you change your Apple ID password. A  `401 invalid credentials`  out of notarization almost always means âgo make a fresh app-specific password,â not âyour setup is broken.â

Confirm itâs stored:
 ` `xcrun notarytool history --keychain-profile App-Name` ` 

Side topic here, I store my app-specific passwords in a 1Password vault that Claude Code has access to. That way whenever Iâm creating a new app, I can tell IT to create the notarization credential for me, and it knows to check its 1Password vault for the password. The whole point of using the LLM in the first place is to avoid doing things manually that you donât want to do.

### Setup a Local.xconfig File and Add It to .gitignore

Real signing needs your team ID and bundle prefix, and I put those in a Local.xconfig file:
 ` `cp Local.xcconfig.example Local.xcconfig
# then edit Local.xcconfig to set:
#   BUNDLE_PREFIX     = your.real.prefix
#   DEVELOPMENT_TEAM  = YOUR-TEAM-ID` ` 

Again, if in doubt, ask Claude Code or your LLM of choice to create this for you.

## Set up the Agent Tools

### Create the Deploy Script

Deployment on my apps is handled via a script called  `release.sh`  that lives in a  `scripts`  folder inside the repo. Without it, I donât have an automated build pipeline.

I had Claude Code create mine: I told Claude, more or less: I want to archive, Developer ID-sign, notarize, staple, and install this app to /Applications without ever opening Xcode. Write me a script that does the whole chain and fails loudly if any step breaks.

It didnât need me to explain the pipeline, because the pipeline isnât a secret â archive with  `xcodebuild` , export with  `-exportArchive`  and an  `ExportOptions.plist` , submit with  `notarytool --wait` , attach the ticket with  `stapler` , check with  `spctl` . Thatâs the documented, conventional way to ship a Developer ID Mac app, and the model knows it. What it needed from me was the project-specific stuff: the scheme name, the team ID, what to call the notary profile, where to install the result.

Then it wrote a first draft, we ran it, it broke, and we fixed it. That loop is not a failure mode, itâs just the process. I always look at AI workflows as works in progress, but it doesnât take long before you can stop tweaking things and just start working.

This is the actual script from one of my app repos:
 ` `#!/usr/bin/env bash
# scripts/release.sh â produce a Developer ID-signed, notarized MY-APP-NAME.app and
# install it to /Applications.
#
# Requires (one-time): Xcode signed into your Apple ID, the paid Developer
# Program, and a notarytool credential profile. Defaults to the "MY-APP-NAME"
# profile; override with MY-APP-NAME_NOTARY_PROFILE=<name>.
#
# Usage: ./scripts/release.sh

set -euo pipefail

PROJECT="MY-APP-NAME.xcodeproj"
SCHEME="MY-APP-NAME-macOS"
APP_NAME="MY-APP-NAME"
TEAM_ID="YOURTEAMID"
NOTARY_PROFILE="${MY-APP-NAME_NOTARY_PROFILE:-MY-APP-NAME}"

BUILD_DIR="build"
ARCHIVE_PATH="$BUILD_DIR/$APP_NAME.xcarchive"
EXPORT_PATH="$BUILD_DIR/Export"
APP_PATH="$EXPORT_PATH/$APP_NAME.app"
INSTALL_DIR="/Applications"
LSREGISTER="/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister"

cd "$(dirname "$0")/.."

step() { printf "\n\033[1;36mâ¸ %s\033[0m\n" "$*"; }
fail() { printf "\n\033[1;31mâ %s\033[0m\n" "$*" >&2; exit 1; }

step "Pre-flight"
command -v xcodegen >/dev/null || fail "xcodegen not installed (brew install xcodegen)."
if ! xcrun notarytool history --keychain-profile "$NOTARY_PROFILE" >/dev/null 2>&1; then
  fail "notarytool profile '$NOTARY_PROFILE' missing. Create it with xcrun notarytool store-credentials."
fi

step "Regenerating project"
xcodegen generate

rm -rf "$BUILD_DIR"; mkdir -p "$BUILD_DIR"

step "Archiving (Release)"
xcodebuild -project "$PROJECT" -scheme "$SCHEME" -configuration Release \
  -derivedDataPath "$BUILD_DIR/derived" -archivePath "$ARCHIVE_PATH" \
  -allowProvisioningUpdates archive

step "Exporting Developer ID-signed app"
cat > "$BUILD_DIR/ExportOptions.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>method</key><string>developer-id</string>
  <key>teamID</key><string>$TEAM_ID</string>
  <key>signingStyle</key><string>automatic</string>
</dict></plist>
EOF
xcodebuild -exportArchive -archivePath "$ARCHIVE_PATH" -exportPath "$EXPORT_PATH" \
  -exportOptionsPlist "$BUILD_DIR/ExportOptions.plist" -allowProvisioningUpdates
[ -d "$APP_PATH" ] || fail "Exported app not found at $APP_PATH."

step "Notarizing (submitting to Apple, may take a few minutes)"
ditto -c -k --keepParent "$APP_PATH" "$BUILD_DIR/notarize.zip"
xcrun notarytool submit "$BUILD_DIR/notarize.zip" --keychain-profile "$NOTARY_PROFILE" --wait

step "Stapling ticket"
xcrun stapler staple "$APP_PATH"

step "Verifying Gatekeeper acceptance"
spctl -a -vvv -t exec "$APP_PATH"

step "Installing to $INSTALL_DIR/$APP_NAME.app"
pkill -x "$APP_NAME" 2>/dev/null || true
rm -rf "$INSTALL_DIR/$APP_NAME.app"
cp -R "$APP_PATH" "$INSTALL_DIR/"
[ -x "$LSREGISTER" ] && "$LSREGISTER" -f "$INSTALL_DIR/$APP_NAME.app" >/dev/null 2>&1 || true

step "Verifying installed bundle"
xcrun stapler validate "$INSTALL_DIR/$APP_NAME.app"
spctl -a -vvv -t exec "$INSTALL_DIR/$APP_NAME.app"
printf "\n\033[1;32mâ %s notarized, stapled, installed.\033[0m\n" "$APP_NAME"` ` 

It looks more complicated than it is, but it is a series of steps that youâd have to know need performed. Again, this is why you talk to your LLM, tell it what you want, and have it help build your workflow.

Some things to note:

 `set -euo pipefail`  halts the script on any failing command immediately instead of blundering forward. Thereâs no half-finished state that looks like success.

 `cd "$(dirname "$0")/.."`  means the script hops to the repo root regardless of where you invoked it from, so  `./scripts/release.sh`  works whether youâre in the repo root or three directories down.

The pre-flight block checks that  `xcodegen`  exists and that the notary profile is actually stored before spending five minutes on an archive thatâs doomed to fail at step five.

And the last two steps re-verify the installed bundle, not just the exported one. Belt and suspenders, but Iâve had a copy step silently mangle a bundle before and Iâd rather find out from the script than from Gatekeeper three days later when it deletes my app for me.

### Create CLAUDE.md or AGENTS.md

 `release.sh`  gives you a one-command deploy.  `CLAUDE.md`  (or  `AGENTS.md`  for basically every other model under the sun) is what makes the agent actually use it without being told every single time.

I had Claude create my CLAUDE.md itself after going back and forth about the build process. Now whenever I create a new app, I tell it to reference the repo for one of my other apps and use the same methodology.
 ` `## Build commands

```bash
# Regenerate the Xcode project after changing project.yml or adding source files
xcodegen generate

# Unit tests (YOUR-APP-NAMEKit only; fast, no Xcode build required)
swift test

# macOS app
xcodebuild -project YOUR-APP-NAME.xcodeproj -scheme YOUR-APP-NAME-macOS \
    -destination 'platform=macOS' CODE_SIGNING_ALLOWED=NO build
```

## Release (Developer ID + notarization)

```bash
./scripts/release.sh   # archive â Developer ID export â notarize â staple â install
```

The `xcodebuild` commands above use `CODE_SIGNING_ALLOWED=NO`, which produces an
**ad-hoc** build: fine for CI and quick local checks, but Gatekeeper rejects it
and the iCloud KVS / App Group entitlements don't bind (no team prefix). For a
real menu-bar build that survives quarantine and lets iCloud sync work, use
`scripts/release.sh`. It signs with Developer ID, notarizes via the `YOUR-APP-NAME`
notarytool keychain profile, staples the ticket, and installs to
`/Applications/YOUR-APP-NAME.app`.` ` 

## Thatâs It

And thatâs the whole one-time setup. From here on, nothing needs a mouse.

## How the build actually runs â no GUI in the loop

Everything below is plain command-line invocation. Xcode.app never launches; these tools live inside it but run standalone. This is exactly what Claude Code executes through its shell.

### Fast, Unsigned Checks

For âdoes it compile / do the tests pass,â you donât need signing at all:
 ` `# Unit tests â pure SPM, no Xcode build at all
swift test

# Compile the macOS app (ad-hoc, unsigned â fine for CI/local sanity)
xcodebuild -project TZed.xcodeproj -scheme TZed-macOS \
    -destination 'platform=macOS' CODE_SIGNING_ALLOWED=NO build

# Compile the iOS app + widget extension for the simulator
xcodebuild -project TZed.xcodeproj -scheme TZed-iOS \
    -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build` ` 

 `CODE_SIGNING_ALLOWED=NO`  gives you an ad-hoc build: it compiles and runs in a simulator, but Gatekeeper rejects it and entitlements like iCloud KVS and App Group donât bind. Thatâs the fast inner loop.

### The Mac Release Pipeline

One command does the entire shippable chain â the script from Part two:
 ` `./scripts/release.sh` ` 

Archive, Developer ID export, notarize, staple, verify, install. If any step fails it stops and tells you which one broke. Need a different notary profile? Override it:  `TZED_NOTARY_PROFILE=<name> ./scripts/release.sh` .

### Deploying to a Real iPhone, Headless

iOS has no notarization step â thatâs a Mac-distribution concept. Getting a build onto a connected iPhone is  `xcodebuild`  plus  `devicectl` , both inside Xcodeâs toolchain:
 ` `# Build & sign for a real device (uses the Apple Development cert + provisioning)
xcodebuild -project TZed.xcodeproj -scheme TZed-iOS \
    -destination 'generic/platform=iOS' \
    -allowProvisioningUpdates \
    -derivedDataPath build/ios archive -archivePath build/TZed-iOS.xcarchive

# Install the built .app onto the connected device by its UDID
xcrun devicectl device install app \
    --device <DEVICE-UDID> build/ios/â¦/TZed.app` ` 

 `devicectl list devices`  lists connected and paired devices with their UDIDs. Device builds sign with the Apple Development identity (not Developer ID) plus a development provisioning profile, which  `-allowProvisioningUpdates`  fetches for you.

## How code signing works when thereâs no GUI

If youâve only ever signed apps by ticking a box in Xcode, itâs worth understanding whatâs actually going on under there, because none of it needs the GUI at build time.

The private key does the signing. When you created that Developer ID Application certificate, Apple issued a certificate and your Mac generated a matching private key, both landing in your login keychain.  `codesign`  (which  `xcodebuild`  calls) uses the private key to sign the binary; the certificate â which chains up to Appleâs root â gets embedded so anyone can verify it.

Automatic signing picks the identity for you. The release script uses  `signingStyle: automatic` , so  `xcodebuild`  selects the right identity by team ID and pulls any needed provisioning profile from Apple on the fly. No profiles checked into the repo.

Entitlements bind at sign time. Each target has a  `.entitlements`  file (sandbox, network client, iCloud KVS, App Group). These only take effect when the app is signed with a real team identity, which is the other reason ad-hoc builds canât ship: the iCloud and App-Group entitlements quietly donât bind without the team prefix, and you get to spend an hour wondering why your key-value store is empty.

Notarization isnât signing. Signing proves who built the app. Notarization is a separate step where Apple scans the signed app for malware and issues a ticket; stapling attaches that ticket so Gatekeeper trusts the app offline. For a hidden-UI menu bar app ( `LSUIElement` ), notarization is what keeps XProtect from flagging it.

The secrets never touch git. The signing private key lives in the login keychain. The notarization app-specific password lives in the notarytool keychain profile. Neither ever gets written into the repo.

You can verify any signed build by hand:
 ` `codesign -dv --verbose=4 /Applications/TZed.app   # who signed it, with what cert
spctl -a -vvv -t exec   /Applications/TZed.app     # would Gatekeeper allow it?
stapler validate        /Applications/TZed.app     # is the notarization ticket attached?` ` 

## What the agent actually uses

Thereâs no magic here. Claude Code drives all of this through a plain, non-interactive shell â thereâs no special âbuildâ MCP server or plugin doing something clever. Itâs  `xcodebuild` ,  `xcrun notarytool` ,  `xcrun stapler` ,  `spctl` ,  `codesign` ,  `devicectl` ,  `xcodegen` , and  `swift` . Standard CLI tools, the same ones weâd use ourselves.

The glue is the  `CLAUDE.md`  from Part two. It tells the agent the notary-profile convention, the two build paths, and that shipping means  `release.sh` . The result is Claude just runs the thing, without me re-explaining it every session.

The one step that stays interactive is  `notarytool store-credentials` , and thatâs a choice rather than a limitation: you could pass  `--password`  and script it, but that means putting an app-specific password in your shell history. Type it once by hand, let the keychain or 1Password hold it, and everything downstream is automated.

## Why Xcode never needs to be open

Put the GUI workflow next to the headless one and the whole thing just lines up:
JOBGUI WAYHEADLESS WAY
Generate projectXcode manages  `.xcodeproj`  `xcodegen generate`  from  `project.yml` 
BuildâB / Run button `xcodebuild â¦ build` 
ArchiveProduct â Archive `xcodebuild â¦ archive` 
Export signed appOrganizer â Distribute `xcodebuild -exportArchive` 
NotarizeOrganizer upload `xcrun notarytool submit --wait` 
Staple(automatic in Organizer) `xcrun stapler staple` 
Install to /Applicationsdrag-and-drop `cp -R`  +  `lsregister` 
Deploy to iPhoneRun on device `xcodebuild archive`  +  `devicectl device install` 

The GUI is only ever needed for that one-time credential setup. After that, the entire lifecycle is scriptable, which is exactly what  `release.sh`  finalizes, and exactly why the agent can own it end to end while I go do something more interesting than watching a progress bar.

If you want to try it yourself, the order is: install Xcode and xcodegen, do the credential setup, then sit down with Claude and build your own  `release.sh`  and  `CLAUDE.md` . That last part is the actual work, and itâs an hour or two at most. After that, âship a new buildâ becomes one sentence. After the first app setup, Claude Code can copy the same setup to apply to future apps.
