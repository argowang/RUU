#!/bin/sh
function startKeyLogger() {
    keylogger keyStroke.txt &
    # make sure the process is terminated later
    echo $! > save_keylog_pid.txt
}

function runProcessAudit() {
    python /Users/mrdoggie/Desktop/Project/RUU/processAudit.py
}

function runWindowAudit() {
    python /Users/mrdoggie/Desktop/Project/RUU/windowAudit.py &
    echo $! > save_window_audit_pid.txt
}

function runChromeTabAudit() {
    python /Users/mrdoggie/Desktop/Project/RUU/chromeTabAudit.py &
    echo $! > save_chrome_audit_pid.txt
}

function cleanUp() {
    echo "Ctrl-C caught...performing clean up"
    kill -9 `cat save_window_audit_pid.txt`
    kill -9 `cat save_chrome_audit_pid.txt`
    kill -9 `cat save_keylog_pid.txt`
    kill -9 `cat save_sleep_pid.txt`
    rm save_window_audit_pid.txt
    rm save_chrome_audit_pid.txt
    rm save_keylog_pid.txt
    rm save_sleep_pid.txt
    exit 2
}

trap cleanUp SIGINT

runWindowAudit;
runChromeTabAudit;
startKeyLogger

while true;
do
    runProcessAudit;
    current_date_time="`date +%Y-%m-%d-%H:%M:%S`";
    echo "\n---5min KeyLogger milestone--- $current_date_time" >> keyStroke.txt;
    echo "\n---5min Window Audit milestone--- $current_date_time" >> windowSensor.txt;
    echo "\n---5min Chrome Tab Audit milestone--- $current_date_time" >> appSensor.txt;
    echo "Audit Completed for $current_date_time";
    sleep 300 &
    sleep_pid=$!
    echo $sleep_pid > save_sleep_pid.txt
    wait $sleep_pid
done
