import os
import re
import time

print("sta  PGA_3D  PGA_h  PGA_X  PGA_Y  PGA_Z  evtID")
folder_path = "230425_110033-QSIS_alert-trigger"
file_extension = ".eml"
file_paths = [
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.endswith(file_extension)
]
for file_path in file_paths:
    print(file_path)
    # read target_file
    with open(file_path, "r") as f:
        tlines = f.read()
        # Time
    regex = re.compile(r"Event time: (\w*-\w*-\w*\s*\w*:\w*:\w*.\w*)")  # 正則式
    utime = regex.search(tlines).group(1)

    # 儲存成時間格式

    datetime_format = time.strptime(utime, "%Y-%m-%d %H:%M:%S.%f")
    time_stamp = int(time.mktime(datetime_format))  # 轉成時間戳
    print(time_stamp)
    # station
    regex = re.compile(r"station: (\w*)")  # 正則式
    stname = regex.search(tlines).group(1)
    # PGA
    regex = re.compile(r"PGA 3D: (\d*.\d*)")  # 正則式
    pga30 = regex.search(tlines).group(1)

    regex = re.compile(r"PGA horizontal: (\d*.\d*)")  # 正則式
    pgah = regex.search(tlines).group(1)

    regex = re.compile(r"PGA_X: (\d*.\d*)")  # 正則式
    pgax = regex.search(tlines).group(1)

    regex = re.compile(r"PGA_Y: (\d*.\d*)")  # 正則式
    pgay = regex.search(tlines).group(1)

    regex = re.compile(r"PGA_Z: (\d*.\d*)")  # 正則式
    pgaz = regex.search(tlines).group(1)

    print(
        stname
        + " "
        + pga30
        + " "
        + pgah
        + " "
        + pgax
        + " "
        + pgay
        + " "
        + pgaz
        + " "
        + str(time_stamp)
    )

    # evenlist
    with open("eventlist.txt", "r") as f:
        elines = f.readlines()
        esp = elines[186 - 1].split()  # 索引從0開始，所以要減1
        eutime = esp[0] + " " + esp[1]

    edatetime_format = time.strptime(eutime, "%Y/%m/%d %H:%M:%S.%f")
    etime_stamp = int(time.mktime(edatetime_format))  # 轉成時間戳
