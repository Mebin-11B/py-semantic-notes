---
title: "Time Machine-style Backups with rsync (2018)"
url: https://samuelhewitt.com/blog/2018-06-05-time-machine-style-backups-with-rsync
clipped: 2026-06-17 01:50:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Time Machine-style Backups with rsync (2018)](https://samuelhewitt.com/blog/2018-06-05-time-machine-style-backups-with-rsync)

## Digest Summary
The article presents a method for creating Time‑Machine‑style incremental backups with rsync. A shell script generates a timestamp (`date "+%Y-%m-%dT%H-%M-%S"`), defines `USER`, `SOURCEDIR`, and `TARGETDIR`, then runs:

```
rsync -avPh --delete --link-dest=$TARGETDIR/current \
      $SOURCEDIR/$USER/ $TARGETDIR/$USER-$TIMESTAMP \
      > /var/log/rsync/$TIMESTAMP.log 2>&1
```

If rsync exits successfully, the script replaces the `current` symlink with the new snapshot (`ln -s $TARGETDIR/$USER-$TIMESTAMP $TARGETDIR/current`); on failure it renames the incomplete directory to `failed‑$USER‑$TIMESTAMP`. The `--link-dest` option creates hard links to unchanged files, so each snapshot stores only new or modified data, conserving space. A cron entry runs the script daily at 5 AM. The author notes that before deleting old snapshots a fresh full backup should be taken, and credits Mike Rubel for influencing the solution.

## Discussion Summary
The discussion emphasizes backup strategies, noting that while hard‑link based scripts are simple and appealing, many users now favor more robust solutions such as Borg, restic, or kopia for reliable backups, and Syncthing for mirroring. References to earlier implementations and tools like rsnapshot illustrate the evolution of the approach. There is interest in macOS‑specific automation using launchd and FSEvents, and some suggest replacing hard‑link methods with direct rsync copies or Syncthing transfers for external or remote storage.

---

## Full Article

Posted on 05 Jun 2018 

Data Hoarding 101
-----------------

I have digital backups of data, especially of my photos, going back almost a decade (Iâm not that old) but itâs only recently that I got into creating time-snapshots of my backups, after I mistakenly deleted a bunch of (non-crucial) personal files with a stray `rsync --delete` on a directory I had not backed-up.

My home server used be [compatible with macOSâs Time Machine](https://samuelhewitt.com/blog/2015-09-12-debian-linux-server-mac-os-time-machine-backups-how-to) and when I kept most things on my Mac that was useful, but I changed my data hoarding habits and that solution started to not be the optimal one.

Time Based Snapshots Using rsync
--------------------------------

`rsync` has got to be one of my favourite and most used utilities. I use it constantly to transfer files between machine on my local network (and remote ones) but Iâve discovered itâs very useful as a backup tool. The following is a short script that uses `rsync` to create snapshots of the my data directory to another directory (they are mount points on two different drives):

```
#!/bin/sh

TIMESTAMP=`date "+%Y-%m-%dT%H-%M-%S"`
USER=user
SOURCEDIR=/var/data/backups
TARGETDIR=/var/redundancy

# Create new backup using rsync and output to log
rsync -avPh --delete --link-dest=$TARGETDIR/current $SOURCEDIR/$USER/ $TARGETDIR/$USER-$TIMESTAMP > /var/log/rsync/$TIMESTAMP.log 2>&1

# check exit status to see if backup failed
if [ "$?" = 0 ]; then
    # Remove link to current backup
    rm -f $TARGETDIR/current
    # Create link to the newest backup
    ln -s $TARGETDIR/$USER-$TIMESTAMP $TARGETDIR/current
else
    # Rename directory if failed
    mv $TARGETDIR/$USER-$TIMESTAMP $TARGETDIR/failed-$USER-$TIMESTAMP
fi
```

Essentially this script creates incremental copies of backups for a given user on the system by comparing any changes to that userâs data directory (`$SOURCEDIR`) with the current backup (`$TARGETDIR`) and making a new snapshot of any changes with the date.

Now all that remains is to save this script somewhere and create a `cron` job to run it on an automatic interval:

```
# daily at 5am
0 5 * * * bash /usr/local/bin/rsync-time-machine
```

### Hard Links

This method uses rsyncâs `--link-dest` option to create [hard-links](https://en.wikipedia.org/wiki/Hard_link) so that isnât duplicative of file data (the contents are only stored once, so you donât use twice as much) and you can delete snapshots at will. (The links do still take up some space but itâs relatively insignificant.)

> Be careful when deleting old snapshots. A new full backup of should be made before further incremental ones.
> I have to give a shoutout to Mike Rubel whose [post](http://www.mikerubel.org/computers/rsync_snapshots/) was helpful in coming up with this solution.