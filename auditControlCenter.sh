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
}

function auditPort() {
    lsof -Pn -i4 | grep -v "CLOSE" | tail -n +2 | awk '{print $1, $2, $8, $9}' >> log/portAudit.log
}

function runProcessAudit() {
    python processAudit.py
}

function runWindowAudit() {
    python windowAudit.py &
    echo $! > save_window_audit_pid.txt
}

function runChromeTabAudit() {
    python chromeTabAudit.py &
    echo $! > save_chrome_audit_pid.txt
}

function runChromeTabCountAudit() {
    python chromeTabCountAudit.py 
}

function runFileWatcherAudit() {
    sudo unbuffer opensnoop -v -n Preview | tee -a log/preview.log &
    echo $! > save_preview_pid.txt
    sudo unbuffer opensnoop -v -n TextEdit | tee -a log/textedit.log &
    echo $! > save_textedit_pid.txt
}

function cleanUp() {
    echo "Ctrl-C caught...performing clean up"
    kill -9 `cat save_keylog_heartbeat_pid.txt`
    kill -9 `cat save_keylog_sleep_pid.txt`
    kill -9 `cat save_window_audit_pid.txt`
    kill -9 `cat save_chrome_audit_pid.txt`
    kill -9 `cat save_keylog_pid.txt`
    kill -9 `cat save_sleep_pid.txt`
    kill -9 `cat save_preview_pid.txt`
    kill -9 `cat save_textedit_pid.txt`
    sudo pkill -f opensnoop
    rm save_preview_pid.txt
    rm save_textedit_pid.txt
    rm save_window_audit_pid.txt
    rm save_chrome_audit_pid.txt
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
runFileWatcherAudit

while true;
do
    runProcessAudit;
    auditPort;
    runChromeTabCountAudit;
    current_date_time="`date +%Y-%m-%d-%H:%M:%S`";
    echo "\n---5min KeyLogger milestone--- $current_date_time" >> log/keyStroke.log;
    echo "\n---5min Port Audit milestone--- $current_date_time" >> log/portAudit.log;
    echo "\n---5min Window Audit milestone--- $current_date_time" >> log/windowAudit.log;
    echo "\n---5min Chrome Tab Audit milestone--- $current_date_time" >> log/chromeTab.log;
    echo "\n---5min Chrome Tab Count Audit milestone--- $current_date_time" >> log/chromeTabCount.log;
    echo "\n---5min Preview Audit milestone--- $current_date_time" >> log/preview.log;
    echo "\n---5min TextEdit Audit milestone--- $current_date_time" >> log/textedit.log; 
    echo "Audit Completed for $current_date_time";
    sleep 300 &
    sleep_pid=$!
    echo $sleep_pid > save_sleep_pid.txt
    wait $sleep_pid
done

