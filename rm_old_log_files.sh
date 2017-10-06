#! /bin/bash
/usr/bin/find /mnt/resource/logs/na-cron-logs/* -mtime +20 -exec rm {} \;

