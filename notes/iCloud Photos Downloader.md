---
title: "iCloud Photos Downloader"
url: https://github.com/icloud-photos-downloader/icloud_photos_downloader
clipped: 2026-06-17 02:00:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [iCloud Photos Downloader](https://github.com/icloud-photos-downloader/icloud_photos_downloader)

## Digest Summary
The repository icloud-photos-downloader/icloud_photos_downloader hosts a command‑line utility for downloading photos from Apple iCloud. The project’s README (or landing page) references three visual assets: “Quality Checks,” indicating automated testing or code‑quality verification; “Build and Package,” denoting the build pipeline that compiles and packages the tool for distribution; and “MIT License,” specifying that the software is released under the permissive MIT open‑source license. No additional functional details, usage instructions, or code excerpts are present in the provided text.

## Discussion Summary
Comments reveal widespread frustration with Apple Photos’ limited export options, hidden “optimize” settings, and proprietary formats that make full backups difficult, prompting many users to seek third‑party or self‑hosted solutions. Numerous tools—including open‑source scripts, Docker containers, Parachute, Immich, and the author’s own backup app—are cited as effective ways to download, preserve metadata, and organize large iCloud libraries while reducing reliance on Apple’s storage fees. Opinions are generally positive about these alternatives, though users note occasional authentication hassles, performance issues, and the need for ongoing maintenance. Overall sentiment is critical of Apple’s native workflow but hopeful about community‑driven backup methods.

---

## Full Article

* A command-line tool to download all your iCloud photos.
* Works on Linux, Windows, and macOS; laptop, desktop, and NAS
* Available as an executable for direct downloading and through package managers/ecosystems ([Docker](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#docker), [PyPI](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#pypi), [AUR](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#aur), [npm](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#npm))
* Developed and maintained by volunteers (we are always looking for [help](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/master/CONTRIBUTING.md)).

See [Documentation](https://icloud-photos-downloader.github.io/icloud_photos_downloader/) for more details. Also, check [Issues](https://github.com/icloud-photos-downloader/icloud_photos_downloader/issues)

We aim to release new versions once a week (Friday), if there is something worth delivering.

To make iCloud Photo Downloader work, ensure the iCloud account is configured with the following settings, otherwise Apple Servers will return an ACCESS\_DENIED error:

* **Enable Access iCloud Data on the Web:** On your iPhone / iPad, enable `Settings > Apple ID > iCloud > Access iCloud Data on the Web`
* **Disable Advanced Data Protection:** On your iPhone /iPad disable `Settings > Apple ID > iCloud > Advanced Data Protection`

There are three ways to run `icloudpd`:

1. Download executable for your platform from the GitHub [Release](https://github.com/icloud-photos-downloader/icloud_photos_downloader/releases/tag/v1.32.3) and run it
2. Use package manager to install, update, and, in some cases, run ([Docker](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#docker), [PyPI](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#pypi), [AUR](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#aur), [npm](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html#npm))
3. Build and run from the source

See [Documentation](https://icloud-photos-downloader.github.io/icloud_photos_downloader/install.html) for more details

* Three modes of operation:
  + **Copy** - download new photos from iCloud (default mode)
  + **Sync** - download new photos from iCloud and delete local files that were removed in iCloud (`--auto-delete` option)
  + **Move** - download new photos from iCloud and delete photos in iCloud (`--keep-icloud-recent-days` option)
* Support for Live Photos (image and video as separate files) and RAW images (including RAW+JPEG)
* Automatic de-duplication of photos with the same name
* One time download and an option to monitor for iCloud changes continuously (`--watch-with-interval` option)
* Optimizations for incremental runs (`--until-found` and `--recent` options)
* Photo metadata (EXIF) updates (`--set-exif-datetime` option)
* ... and many more (use `--help` option to get full list)

Some changes are added to the experimental mode before they graduate into the main package. [Details](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/master/EXPERIMENTAL.md)

To keep your iCloud photo collection synchronized to your local system:

```
icloudpd --directory /data --username my@email.address --watch-with-interval 3600
```

Important

It is `icloudpd`, not `icloud` executable

Tip

Synchronization logic can be adjusted with command-line parameters. Run `icloudpd --help` to get full list.

To independently create and authorize a session (and complete 2SA/2FA validation if needed) on your local system:

```
icloudpd --username my@email.address --password my_password --auth-only
```

Tip

This feature can also be used to check and verify that the session is still authenticated.

Want to contribute to iCloud Photos Downloader? Awesome! Check out the [contributing guidelines](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/master/CONTRIBUTING.md) to get involved.