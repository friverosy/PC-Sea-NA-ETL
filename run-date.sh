#! /bin/bash
python /mnt/resource/script/cron.py --date $(date +%F) 2>&1 >> /home/tzu/na-cron-logs/daily_$(date --iso-8601=seconds).log
