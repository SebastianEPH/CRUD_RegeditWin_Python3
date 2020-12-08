from winreg import *

import binascii

aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
aKey = OpenKey(aReg, r"hey")

for i in range(1024):

    try:
        name,value,type = EnumValue(aKey,i)
        print(value)
        print("\n")
    except EnvironmentError:
        break

CloseKey(aKey)