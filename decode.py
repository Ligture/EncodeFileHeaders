import datetime
import time
from Cryptodome.Util.Padding import unpad
from Cryptodome.Cipher import AES
import os
import hashlib
import base64

global md5
md5 = b""
global length
length = 0


def decodefile(filename, password, decodefilename: bool = True):
    sttime = time.time()
    if len(password) <= 16:
        passwordnew = password.encode("utf-8").ljust(16, b"\0")
    else:
        passwordnew = password.encode("utf-8").ljust(
            16 * (len(password) // 16 + 1), b"\0"
        )

    filename = filename.replace("/", "\\")
    if not os.path.isfile(filename):
        endtime = time.time()
        endtime = endtime - sttime
        endtime = datetime.timedelta(seconds=endtime)
        return {
            "filename": filename,
            "status": "error",
            "newfile": None,
            "reason": "file not found",
            "time": str(endtime),
        }

    if os.path.splitext(filename)[-1] != ".enc":
        endtime = time.time()
        endtime = endtime - sttime
        endtime = datetime.timedelta(seconds=endtime)

        return {
            "filename": filename,
            "status": "error",
            "newfile": None,
            "reason": "文件未被加密",
            "time": str(endtime),
        }

    f1 = open(filename, "rb")
    md5 = f1.read(32)
    length = int(f1.read(8).rstrip(b"\0").decode("utf-8"))

    m1 = hashlib.md5()
    m1.update(password.encode("utf-8"))
    md5_check = m1.hexdigest()
    print(md5_check)
    if md5_check != md5.decode("utf-8"):
        endtime = time.time()
        endtime = endtime - sttime
        endtime = datetime.timedelta(seconds=endtime)
        f1.close()
        return {
            "filename": filename,
            "status": "error",
            "newfile": None,
            "reason": "密码错误",
            "time": str(endtime),
        }
    else:


        data = f1.read(length)

        cipher = AES.new(passwordnew, AES.MODE_ECB)
        print(data)
        newdata = cipher.decrypt(data)
        print(newdata)
        newdata = unpad(newdata, AES.block_size, 'pkcs7')
        if decodefilename:
            newfile = cipher.decrypt(
                base64.b64decode(
                    os.path.basename(filename).replace(".enc", "").replace("-", "/")
                )
            )
            newfile = unpad(newfile, AES.block_size, 'pkcs7')
            print(newfile)
            newfile = os.path.dirname(filename) + "\\" + newfile.decode("utf-8")
        with open(newfile, "wb") as nf:
            nf.write(newdata)
            buffersize = 8192  # 缓冲读取


            while True:
                buffer = f1.read(buffersize)

                if not buffer:
                    break
                nf.write(buffer)
        f1.close()
        endtime = time.time()
        endtime = endtime - sttime
        endtime = datetime.timedelta(seconds=endtime)
        os.remove(filename)
        return {
            "filename": filename,
            "status": "ok",
            "newfile": newfile,
            "reason": None,
            "time": str(endtime),
        }
