#! /bin/bash
python /mnt/resource/apps/pc-sea-na-backend/script/manifest_harvester.py --date $(date +%F) 2>&1 >> /mnt/resource/logs/na-cron-logs/update_$(date --iso-8601=seconds).log
new_date=$(date -d "+1 day" +%F)
#echo "new:${new_date}"
python /mnt/resource/apps/pc-sea-na-backend/script/manifest_harvester.py --date $(date -d "+1 day" +%F)  2>&1 >> /mnt/resource/logs/na-cron-logs/update_one_day_ahead_$(date --iso-8601=seconds).log
