while true;
do
    python /Users/mrdoggie/Desktop/Project/RUU/processAudit.py;
    current_date_time="`date +%Y-%m-%d-%H:%M:%S`";
    echo "Audit Completed for $current_date_time"
    sleep 300;
done
