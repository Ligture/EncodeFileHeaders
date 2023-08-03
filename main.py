import encode
import decode
#retur = encode.encodefile('F:\\xposed\\system\\lib\\libxposed_art.so', '12345')
retur = decode.decodefile(r"F:\xposed\system\lib\FPJpA8QrFXUBwD2ZGSs1lw==.enc", '123456')
print(retur)