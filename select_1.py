import os
import re
import time
import datetime


with open("PGAs_email.txt", "w") as w:
    w.write("sta      PGA_Z   PGA_X   PGA_Y   PGA_3D  PGA_H  triID        evtID\n")
    print("sta      PGA_Z  PGA_X   PGA_Y   PGA_3D   PGA_H  triID        evtID")
    folder_path = "230425_110033-QSIS_alert-trigger"
    file_extension = r"\d+_\d+.eml"
    file_paths = [
        os.path.join(folder_path, file)  # 將文件夾路徑和文件名合併為一個完整的路徑
        for file in os.listdir(folder_path)  # 函數返回一個列表，其中包含指定目錄中的所有文件和文件夾
        if re.match(file_extension, file)  # 以指定的文件名才會被包含到列表中
        # if file.endswith(file_extension)  # 以指定的擴展名結尾的文件才會被包含到列表中
    ]
    # read evenlist
    with open("eventlist.txt", "r") as ef:
        elines = ef.read().split("\n")
        eleng = len(elines)
        # read target_file
        for file_path in file_paths:
            with open(file_path, "r") as f:
                tlines = f.read()

            # Time
            regex = re.compile(r"Event time: (\w*-\w*-\w*\s*\w*:\w*:\w*.\w*)")  # 正則式
            utime = regex.search(tlines).group(1)
            datetime_format = datetime.datetime.strptime(
                utime, "%Y-%m-%d %H:%M:%S.%f"
            )  # 儲存成時間格式
            tritime_stamp = datetime.datetime.timestamp(datetime_format)  # 轉成時間戳
            # station
            regex = re.compile(r"station: (\w*)")  # 正則式
            stname = regex.search(tlines).group(1)
            # PGA
            regex = re.compile(r"PGA 3D: (\d*.\d*)")  # 正則式
            pga30 = float(regex.search(tlines).group(1))

            regex = re.compile(r"PGA horizontal: (\d*.\d*)")  # 正則式
            pgah = float(regex.search(tlines).group(1))

            regex = re.compile(r"PGA_X: (\d*.\d*)")  # 正則式
            pgax = float(regex.search(tlines).group(1))

            regex = re.compile(r"PGA_Y: (\d*.\d*)")  # 正則式
            pgay = float(regex.search(tlines).group(1))

            regex = re.compile(r"PGA_Z: (\d*.\d*)")  # 正則式
            pgaz = float(regex.search(tlines).group(1))

            # evenlist translate
            for i in range(0, eleng - 1):
                esp = elines[i].split()  # 索引從0開始，所以要減1
                eutime = esp[0] + " " + esp[1]
                edatetime_format = datetime.datetime.strptime(
                    eutime, "%Y/%m/%d %H:%M:%S.%f"
                )  # 時間格式
                etime_stamp = datetime.datetime.timestamp(edatetime_format)  # 轉成時間戳
                etime = float(edatetime_format.strftime("%Y%m%d%H%M%S"))  # float(先轉成字串)

                if ((etime_stamp - tritime_stamp) ** 2) ** 0.5 <= 120:
                    w.write(
                        stname
                        + " "
                        + "{:7.2f}".format(pgaz)
                        + " "
                        + "{:7.2f}".format(pgax)
                        + " "
                        + "{:7.2f}".format(pgay)
                        + " "
                        + "{:7.2f}".format(pga30)
                        + " "
                        + "{:7.2f}".format(pgah)
                        + " "
                        + "{:12.0f}".format(tritime_stamp)
                        + " "
                        + "{:12.0f}".format(etime_stamp)
                        + "  "
                        + "{:19.0f}\n".format(etime)
                    )
    print(
        stname
        + " "
        + "{:7.2f}".format(pga30)
        + " "
        + "{:7.2f}".format(pgah)
        + " "
        + "{:7.2f}".format(pgax)
        + " "
        + "{:7.2f}".format(pgay)
        + " "
        + "{:7.2f}".format(pgaz)
        + " "
        + "{:12.0f}".format(tritime_stamp)
        + " "
        + "{:12.0f}".format(etime_stamp)
        + "  "
        + "{:19.2f}\n".format(etime)
    )
