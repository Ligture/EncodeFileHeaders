import datetime
import time

from Cryptodome.Cipher import AES
import os
import hashlib
import base64


def decodefile(filename, password, decodefilename: bool = True):
    sttime = time.time()
    if len(password) <= 16:
        passwordnew = password.encode("utf-8").ljust(16, b"\0")
    else:
        passwordnew = password.encode("utf-8").ljust(16 * (len(password) // 16 + 1), b"\0")

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
            'time': str(endtime)
        }

    with open(filename, "rb") as f:
        md5 = f.read(32)
        length = int(f.read(8).rstrip(b"\0").decode("utf-8"))
        m1 = hashlib.md5()
        m1.update(password.encode("utf-8"))
        md5_check = m1.hexdigest()
        print(md5_check)
        if md5_check != md5.decode("utf-8"):
            endtime = time.time()
            endtime = endtime - sttime
            endtime = datetime.timedelta(seconds=endtime)
            return {
                "filename": filename,
                "status": "error",
                "newfile": None,
                "reason": "md5 check failed",
                'time': str(endtime)
            }
        else:
            data = f.read(length)
            cipher = AES.new(passwordnew, AES.MODE_ECB)
            newdata = cipher.decrypt(data).rstrip(b'\0')
            if decodefilename:
                newfile = cipher.decrypt(
                    base64.b64decode(os.path.basename(filename).replace(".enc", ""))
                ).rstrip(b'\0')
                print(newfile)
                newfile = os.path.dirname(filename) + "\\" + newfile.decode("utf-8")
            with open(newfile, 'wb') as nf:
                nf.write(newdata)
                buffersize = 8192 #缓冲读取
                while True:
                    buffer = f.read(buffersize)
                    if not buffer:
                        break
                    nf.write(buffer)
            endtime = time.time()
            endtime = endtime - sttime
            endtime = datetime.timedelta(seconds=endtime)
            return {
                "filename": filename,
                "status": "ok",
                "newfile": newfile,
                "reason": None,
                'time': str(endtime)
            }

