#! /usr/bin/python3
# -*- coding: utf-8 -*-

import argparse

import requests

import json


def parse_args():
    parser = argparse.ArgumentParser(description='添加摄像机模拟器')

    parser.add_argument('--device_id', help='设备的id', type=str, required=True)
    parser.add_argument('--rtsp_stream', help='视频流', type=str, required=True)
    parser.add_argument('--park_server_ip', help='园区的ip', type=str, required=True)
    parser.add_argument('--park_server_port', help='园区的port', type=int, default=9812)

    args = parser.parse_args()

    return args.device_id, args.park_server_ip, args.park_server_port, args.rtsp_stream


def login(server_ip, server_port):
    login_url = "https://{}:{}/login".format(server_ip, server_port)
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        "password": "7f3fa48ca885678134842fa7456f3ece53a97f843b610185d900ac4e467c7490",
        "username": "partner"
    }
    response = requests.post(login_url, data=json.dumps(body), headers=headers, verify=False)
    return response.json()['result']


def main():
    device_id, park_server_ip, park_server_port, rtsp_stream= parse_args()


    token = login(park_server_ip, park_server_port)

    device_url = "https://{}:{}/devices".format(park_server_ip,park_server_port)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    body = {
        "device_list": [
            {
                "device_id": device_id,
                "device_meta": {
                    "device_name": "name of {}".format(device_id),
                    "direction_type": 0,
                    "enable": True,
                    "location":"123",
                    "ip": rtsp_stream,
                    "type": "9",
                    "video_definition_type": "1"
                }
            }
        ]
    }
    response = requests.post(device_url, json=body, headers=headers, verify=False)
    print(response.json())


if __name__ == '__main__':
    main()

