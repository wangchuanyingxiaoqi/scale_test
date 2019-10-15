#! /usr/bin/python3
# -*- coding: utf-8 -*-

import argparse

import requests


def parse_args():
    parser = argparse.ArgumentParser(description='删除摄像机模拟器')

    parser.add_argument('--device_id', help='设备的id，不填写则删除第一个设备', type=str)
    parser.add_argument('--park_server_ip', help='园区的ip', type=str, required=True)
    parser.add_argument('--park_server_port', help='园区的port', type=int, default=9812)

    args = parser.parse_args()

    return args.device_id, args.park_server_ip, args.park_server_port


def login(server_ip, server_port):
    login_url = "https://{}:{}/login".format(server_ip, server_port)
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        "password": "7f3fa48ca885678134842fa7456f3ece53a97f843b610185d900ac4e467c7490",
        "username": "partner"
    }
    response = requests.post(login_url, json=body, headers=headers, verify=False)
    return response.json()['result']


def get_one_device(park_server_ip, park_server_port, token):
    url = "https://{}:{}/devices".format(park_server_ip, park_server_port)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    params = {
        'page': 0,
        'size': 1
    }
    response = requests.get(url, params=params, headers=headers, verify=False)
    return response.json()['result'][0]['device_id']


def main():
    device_id, park_server_ip, park_server_port = parse_args()

    token = login(park_server_ip, park_server_port)

    if device_id is None:
        device_id = get_one_device(park_server_ip, park_server_port, token)

    device_url = "https://{}:{}/devices/{}".format(park_server_ip, park_server_port, device_id)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = requests.delete(device_url, headers=headers, verify=False)
    print('delete device: {}'.format(device_id))
    print(response.json())


if __name__ == '__main__':
    main()
