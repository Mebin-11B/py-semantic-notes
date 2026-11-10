---
title: "Block the “Upgrade to Tahoe” Alerts"
url: https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/
clipped: 2026-06-17 01:38:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Block the “Upgrade to Tahoe” Alerts](https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/)

## Digest Summary
None

## Discussion Summary
The comments convey a broadly negative view of the latest macOS release, describing it as a downgrade that introduces slower, jittery animations, Finder lag, intrusive UI changes, and flaky cross‑device features. Users express frustration with forced updates and regard the “stop‑Tahoe‑update” tools, notification suppression, and downgrade workarounds as essential. While a minority note no noticeable impact on certain hardware or prefer alternative OSes, the dominant sentiment is disappointment with the UI, stability, and perceived loss of user control.

---

## Full Article

Based on some comments on

[my Mastodon post](https://mstdn.social/@rgriff/115911291324085543)

, this only works due to a bug in macOS 15.7.3! The 90 day period isn't supposed to be a rolling date, but 90 days from release date. So it should have no impact…but it does, so I hope Apple doesn't fix the bug.

Although I have to have a machine running macOS Tahoe to support our customers, I personally don't like the look of Liquid Glass, nor do I like some of the functional changes Apple has made in macOS Tahoe.

![](https://robservatory.com/postimages/_onetime/upgrade_tahoe.jpg)So I have macOS Tahoe on my laptop, but I'm keeping my desktop Mac on macOS Sequoia for now. Which means I have the joy of seeing things like this wonderful notification on a regular basis.

Or I did, until I found a way to block them, at least in 90 day chunks. Now when I open System Settings → General → Software Update, I see this:

![](https://robservatory.com/postimages/_onetime/upgrade_status.jpg)

The secret? Using [device management profiles](https://support.apple.com/guide/deployment/intro-to-device-management-profiles-depc0aadd3fe/web), which let you enforce policies on Macs in your organization, even if that "organization" is one Mac on your desk. One of the available policies is the ability to block activities related to major macOS updates for up to 90 days at a time (the max the policy allows), which seems like exactly what I needed.

Not being anywhere near an expert on device profiles, I went looking to see what I could find, and stumbled on the [Stop Tahoe Update project](https://github.com/travisvn/stop-tahoe-update?tab=readme-ov-file). The eventual goals of this project are quite impressive, but what they've done so far is exactly what I needed: A configuration profile that blocks Tahoe update activities for 90 days.

I first tried to get things working by following the Read Me, but it's missing some key steps. After some fumbling about, I managed to get it working by using these modified instructions:

1. Clone the repo and switch to its directory in Terminal; run the two commands as shown in the project's Read Me:

   ```
   $ git clone https://github.com/travisvn/stop-tahoe-update.git
   $ cd stop-tahoe-update
   ```
2. Set all the scripts to executable (not in the instructions):

   ```
   $ chmod 755 ./scripts/*.sh
   ```
3. Create and insert two UUIDs into the profile (not in the instructions). To do this, use your favorite text editor to edit the file named deferral-90days.mobileconfig in the profiles folder. Look for two lines like this:

   ```
   <key>PayloadUUID</key><string>REPLACE-WITH-UUID</string>
   ```

   You need to replace that text with two distinct UUIDs; the easiest way to do that is to run uuidgen twice in Terminal, then copy and paste each UUID, replacing each REPLACE-WITH-UUID text with the UUID. Save the changes and quit the editor, unless you want to make the following optional change...
4. **Optional step:** I didn't want to defer normal updates, just the major OS update, so I changed the Optional (set to your taste) section to look like this:

   ```
   <!-- Optional (set to your taste) -->
         <key>forceDelayedSoftwareUpdates</key><false/>
   ```

   Just to be clear, you need to delete the other lines in this section, leaving just the above as-edited line. [Thanks for the heads-up](https://daringfireball.net/linked/2026/02/27/how-to-block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator#:~:text=I%20have%20one%20small%20clarification), Daring Fireball!

   This way, I'll still get notifications for updates other than the major OS update, in case Apple releases anything further for macOS Sequoia. Remember to save your changes, then quit the editor.
5. Run the script as described in the project's Read Me:

   ```
   ./scripts/install-profile.sh profiles/deferral-90days.mobileconfig
   ```

   When run, you'll see output in Terminal indicating that you're not done yet:

   ```
   Installing profile: profiles/deferral-90days.mobileconfig
   profiles tool no longer supports installs.  Use System Settings Profiles to add configuration profiles.
   Done. You may need to open System Settings → Privacy & Security → Profiles to approve.
   ```

   You'll also get an onscreen alert saying basically the same thing.
6. To finish the installation, open System Settings and click on the *Profile Downloaded* entry in the sidebar. This will take you to a screen showing the profile you just added. Double-click on that profile, and a dialog appears showing the settings; here's how mine looked, reflecting the changes I made to remove minor updates from the policy:

   ![](https://robservatory.com/postimages/_onetime/approve_profile.jpg)

   Click the Install button, which will lead you to Yet Another Dialog; again click Install and you'll finally be done. Quit and relaunch System Settings, and you should see a message like mine at the top of the Software Update panel.

As I've just done all this today, I'm not sure exactly what happens in 90 days. I imagine I may be notified that the policy has expired, or maybe I'll just see a macOS Tahoe update notification. Either way, you can reinstall the policy again by just running the install-profile.sh command again. Alternatively, and to make things much simpler, here's what I've done…

I copied my modified profile (the deferral-90days.mobileconfig file in the Profiles folder) to one of my utility folders, so I could remove the repo as I won't need it any more. Then I looked at the install script, which tries to install the profile using the profiles command, and if that fails, it then opens the profile to install it. In Sequoia, you can't use profiles to install a profile, so only the open part of the command is needed.

Once I figured out I only needed to use the open command, I added a simple alias in my .zshrc configuration file:

```
# Reinstall the no-Tahoe 90 day policy
alias notahoe='open "/path/to/deferral-90days.mobileconfig"; sleep 2; open "x-apple.systempreferences:com.apple.preferences.configurationprofiles"'
```

Now I just have to type notahoe every 90 days, and the profile will be reinstalled, and System Settings will open to the profiles panel, where a few clicks will finish activating the installed profile. We'll see how that goes in April :).

I am *so* much happier now, not being interrupted with the Tahoe update notification, and not having the glaring red "1" on the System Settings icon.