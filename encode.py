from Cryptodome.Cipher import AES
import os
import hashlib


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
    data = b""
    with open(filename, "rb") as f:
        data = f.read(encodelen)
    newdata = aesen(password.encode("utf-8"), data)
    if outputfile is None:
        outputfile = (
            os.path.dirname(filename)
            + "\\"
            + aesen(
                password.encode("utf-8"), os.path.basename(filename).encode("utf-8")
            )
            + ".enc"
        )
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
            return {"filename": filename, "status": "ok", "newfile": outputfile}
        except BaseException as e:
            return {"filename": filename, "status": "error", "newfile": None, 'reason': e}


    else:
        return {"filename": filename, "status": "error", "newfile": None, 'reason': '验证错误'}
