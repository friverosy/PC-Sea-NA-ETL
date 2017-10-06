#! /bin/bash
/usr/bin/mongodump --db nav-dev --out /mnt/resource/backup/nav-dev-dump-$(date +'%Y-%m-%dT%H_%M_%S')
