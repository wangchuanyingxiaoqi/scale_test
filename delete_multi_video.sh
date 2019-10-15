#!/usr/bin/env bash

if [[ $# < 2 ]];then
    echo "Usage: ${0}  <park_ip> <mock_video_mum>"
    exit 1
fi


park_server_ip=$1
mock_video_mum=$2

for i in `seq 1 $mock_video_mum`;
do
  ./delete_mock_camera.py --device_id mock_video_${i}   --park_server_ip ${park_server_ip}
done

