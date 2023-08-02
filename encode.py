import datetime

from Cryptodome.Cipher import AES
import os
import hashlib
import base64
import time

"""def bytes_ljust(byte_string:bytes, width, fill_byte = b'\0'):
    if len(byte_string) >= width:
        return byte_string
    padding = width - len(byte_string)
    addbytes = fill_byte * padding
    print(addbytes)
    print(byte_string)
    print('addbytes:', type(addbytes))
    print('byte_string:', type(byte_string))
    return byte_string + addbytes
"""


def b64decode(base64Info: bytes):
    try:
        return base64.b64decode(base64Info)
    except Exception as e:
        print("异常：", e)


def b64encode(data: bytes):
    try:
        tmpBase64 = base64.b64encode(data)
        return tmpBase64
    except Exception as e:
        print("异常：", e)


def aesen(key: bytes, data: bytes):
    if len(key) <= 16:
        key = key.ljust(16, b"\0")
    else:
        key = key.ljust(16 * (len(key) // 16 + 1), b"\0")
    if len(data) == 0:
        return b""

    data = data.ljust(16 * (len(data) // 16 + 1), b"\0")
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)


def remove_bytes_from_file(file_path, num_bytes, writecon, output):
    temp_file_path = output

    with open(file_path, "rb") as src_file, open(temp_file_path, "wb") as dest_file:
        src_file.seek(num_bytes)
        buffer_size = 8192  # 8KB 缓冲区大小
        dest_file.write(writecon)
        while True:
            buffer = src_file.read(buffer_size)
            if not buffer:
                break
            dest_file.write(buffer)

    # 将临时文件替换为原始文件


def verify(data, password, endata):
    password = password.encode("utf-8")
    if len(password) <= 16:
        key = password.ljust(16, b"\0")
    else:
        key = password.ljust(16 * (len(password) // 16 + 1), b"\0")
    cipher = AES.new(key, AES.MODE_ECB)
    data2 = cipher.decrypt(endata)
    data2 = data2.rstrip(b"\0")
    if data2 == data:
        return True
    else:
        return False


def encodefile(filename, password, encodelen=1024, outputfile=None):
    sttime = time.time()
    filename = filename.replace("/", "\\")
    if not os.path.isfile(filename):
        return {
            "filename": filename,
            "status": "error",
            "newfile": None,
            "reason": "file not found",
        }
    data = b""
    with open(filename, "rb") as f:
        data = f.read(encodelen)
    newdata = aesen(password.encode("utf-8"), data)
    if outputfile is None:
        outputfile = (
            os.path.dirname(filename)
            + "\\"
            + b64encode(
                aesen(
                    password.encode("utf-8"), os.path.basename(filename).encode("utf-8")
                )
            ).decode("utf-8")
            + ".enc"
        )
        if not verify(
            os.path.basename(filename).encode("utf-8"),
            password,
            aesen(password.encode("utf-8"), os.path.basename(filename).encode("utf-8")),
        ):
            endtime = time.time()
            endtime = endtime - sttime
            endtime = datetime.timedelta(seconds=endtime)
            return {
                "filename": filename,
                "status": "error",
                "newfile": None,
                "reason": "对文件名加密时验证错误",
                "time": str(endtime),
            }
    if verify(data, password, newdata):
        h1 = hashlib.md5()
        h1.update(password.encode("utf-8"))
        md5 = h1.hexdigest()
        length = str(len(newdata)).encode("utf-8")
        if len(length) <= 8:
            length = length.ljust(8, b"\0")
        wrd = bytes(md5, encoding="utf-8") + length + newdata
        try:
            remove_bytes_from_file(filename, encodelen, wrd, outputfile)
            os.remove(filename)
            endtime = time.time()
            endtime = endtime - sttime
            endtime = datetime.timedelta(seconds=endtime)
            return {
                "filename": filename,
                "status": "ok",
                "newfile": outputfile,
                "time": str(endtime),
                "reason": "None",
            }
        except BaseException as e:
            endtime = time.time()
            endtime = endtime - sttime
            endtime = datetime.timedelta(seconds=endtime)
            return {
                "filename": filename,
                "status": "error",
                "newfile": None,
                "reason": e,
                "time": str(endtime),
            }

    else:
        endtime = time.time()
        endtime = endtime - sttime
        endtime = datetime.timedelta(seconds=endtime)
        return {
            "filename": filename,
            "status": "error",
            "newfile": None,
            "reason": "对数据加密时验证错误",
            "time": str(endtime),
        }
