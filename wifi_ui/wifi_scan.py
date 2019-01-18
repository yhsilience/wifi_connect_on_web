import os

import time


def get_wifi_list():
    time.sleep(1)
    result = get_result()
    os.system("nmcli dev wifi > wifi_list")  # scan wifi and save as file
    fs_r = open("wifi_list", "r+")
    fs_w = open("wifi_result", "w+")
    for line in fs_r.readlines():
        item = line.split()
        if "SSID" in item:
            continue
        if "--" in item:
            continue
        fs_w.write(line)
    fs_w.close()
    fs_w.close()
    return result


def get_essid():
    essid_list = []
    fs = open("wifi_result", "r+")
    for line in fs.readlines():
        item = line.split()
        if item[0] == "*":
            essid_list.append(item[1])
        else:
            essid_list.append(item[0])

    fs.close()
    print(essid_list)
    return essid_list


def get_single():
    single_list = []
    fs = open("wifi_result", "r+")
    for line in fs.readlines():
        item = line.split()
        if item[0] == "*":
            single_list.append(item[6])
        else:
            single_list.append(item[5])

    fs.close()
    return single_list


def connect_wifi(essid,passwd):
    str_cmd = "sudo nmcli dev wifi connect %s password %s" %(essid, passwd)
    os.system(str_cmd)


def get_result():
    fs_r = os.popen("nmcli dev status")
    for line in fs_r.readlines():
        item = line.split()
        if item[1] == "wifi":
            if item[2] =="connected":
                return item[3]
            else:
                print("connetc  failed")
                return -1

# get_wifi_list()
# list_essid = get_essid()
# list_single = get_single()
# print list_essid[0]
# print list_single[0]
# connect_wifi(list_essid[0], "20180102")

