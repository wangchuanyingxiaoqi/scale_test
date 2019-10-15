#!/usr/bin/env bash

if [[ $# < 3 ]];then
    echo "Usage: ${0} <--rtsp_stream> <mock_video_num> <--park_server_ip>"
    exit 1
fi

rtsp_stream=$1
mock_video_num=$2
park_server_ip=$3

for i in `seq 1 $mock_video_num`;
do
    echo $i
  ./add_mock_video.py --device_id mock_video_${i} --rtsp_stream ${rtsp_stream}  --park_server_ip ${park_server_ip}
done
