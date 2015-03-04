#!/bin/bash

LOG_FILE='all_events.log'
LOG_PATH='logs/'
DATE=`date +%Y-%m-%d`

mv $LOG_PATH$LOG_FILE $LOG_PATH$DATE"_"$LOG_FILE
touch $LOG_PATH$LOG_FILE