#!/bin/sh
function startKeyLogger() {
    keyloggerHeartBeat &
    echo $! > save_keylog_heartbeat_pid.txt
    keylogger ./log/keyStroke.log &
    # make sure the process is terminated later
    echo $! > save_keylog_pid.txt
}

function keyloggerHeartBeat() {
    while true;
    do
        echo "\n***5s KeyLogger Milestone***" >> log/keyStroke.log
        sleep 5 &
        keylog_sleep_pid=$!
        echo $keylog_sleep_pid > save_keylog_sleep_pid.txt
        wait $keylog_sleep_pid
    done
function auditPort() {
    lsof -Pn -i4 | grep -v "CLOSE" | tail -n +2 | awk '{print $1, $2, $8, $9}' >> log/portAudit.log
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

function runChromeTabCountAudit() {
    python /Users/mrdoggie/Desktop/Project/RUU/chromeTabCountAudit.py &
    echo $! > save_chrometab_audit_pid.txt
}

function runFileWatcherAudit() {
    cd ~/dev/IDS_HW2/filewatcher/filewatcher/
    make
    sudo ./bin/filewatcher -f .pdf -f .txt -f .jpg -f .png -f .jpeg -f .doc >> fileAudit.log

}

function cleanUp() {
    echo "Ctrl-C caught...performing clean up"
    kill -9 `cat save_keylog_heartbeat_pid.txt`
    kill -9 `cat save_keylog_sleep_pid.txt`
    kill -9 `cat save_window_audit_pid.txt`
    kill -9 `cat save_chrome_audit_pid.txt`
    kill -9 `cat save_chrometab_audit_pid.txt`
    kill -9 `cat save_keylog_pid.txt`
    kill -9 `cat save_sleep_pid.txt`
    rm save_window_audit_pid.txt
    rm save_chrome_audit_pid.txt
    rm save_chrometab_audit_pid.txt
    rm save_keylog_heartbeat_pid.txt
    rm save_keylog_sleep_pid.txt
    rm save_keylog_pid.txt
    rm save_sleep_pid.txt
    exit 2
}

trap cleanUp SIGINT

mkdir -p log/
runWindowAudit;
runChromeTabAudit;
startKeyLogger

while true;
do
    runProcessAudit;
    auditPort;
    current_date_time="`date +%Y-%m-%d-%H:%M:%S`";
    echo "\n---5min KeyLogger milestone--- $current_date_time" >> log/keyStroke.log;
    echo "\n---5min Port Audit milestone--- $current_date_time" >> log/portAudit.log;
    echo "\n---5min Window Audit milestone--- $current_date_time" >> log/windowAudit.log;
    echo "\n---5min Chrome Tab Audit milestone--- $current_date_time" >> log/chromeTab.log;
    echo "\n---5min Chrome Tab Count Audit milestone--- $current_date_time" >> log/chromeTabCount.log;
    echo "Audit Completed for $current_date_time";
    sleep 300 &
    sleep_pid=$!
    echo $sleep_pid > save_sleep_pid.txt
    wait $sleep_pid
done
