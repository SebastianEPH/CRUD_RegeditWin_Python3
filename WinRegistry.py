# Create in Python 3.8.5
# Import Library
import winreg

class WinRegistry:
    def __init__(self, path):
        self.afterPath = path
        self.HKEY = None
        self.__listHKEY = [
            'HKEY_CLASSES_ROOT',
            'HKEY_CURRENT_USER',
            'HKEY_LOCAL_MACHINE',
            'HKEY_DYN_DATA',
            'HKEY_PERFORMANCE_DATA',
            'HKEY_USERS',
            'HKEY_CURRENT_CONFIG']

        for hkey in self.__listHKEY:
            index = self.afterPath.find(hkey)  # getting boot index
            if index != -1:  # Only if it was successful
                if str(hkey) == 'HKEY_CLASSES_ROOT':
                    self.HKEY = winreg.HKEY_CLASSES_ROOT
                elif str(hkey) == 'HKEY_CURRENT_USER':
                    self.HKEY = winreg.HKEY_CURRENT_USER
                elif str(hkey) == 'HKEY_LOCAL_MACHINE':
                    self.HKEY = winreg.HKEY_LOCAL_MACHINE
                elif str(hkey) == 'HKEY_DYN_DATA':
                    self.HKEY = winreg.HKEY_DYN_DATA
                elif str(hkey) == 'HKEY_PERFORMANCE_DATA':
                    self.HKEY = winreg.HKEY_PERFORMANCE_DATA
                elif str(hkey) == 'HKEY_USERS':
                    self.HKEY = winreg.HKEY_CLASSES_ROOT
                elif str(hkey) == 'HKEY_CURRENT_CONFIG':
                    self.HKEY = winreg.HKEY_CURRENT_CONFIG
                else:
                    print('Error path invalido')
                index = index + len(hkey) + 1  # Index cut
                end = len(self.afterPath)  # End cut
                self.afterPath = self.afterPath[index:end]  # cut path

    def __format_after_path(self):
        afterPath = self.afterPath
        if afterPath != "":
            return afterPath + "\\"
        else:
            return afterPath

    def __create_value(self, type, nameValue, value):
        self.create_key('')
        opened_key = winreg.OpenKey(self.HKEY, self.afterPath, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(opened_key, nameValue, 0, type, value)
        opened_key.Close()

    def create_key(self, keyName):
        winreg.CreateKeyEx(self.HKEY, self.__format_after_path() + keyName, 0, winreg.KEY_ALL_ACCESS)

    def delete_key(self, keyName):
        try:
            winreg.DeleteKeyEx(self.HKEY, self.__format_after_path() + keyName, winreg.KEY_ALL_ACCESS, 0)
        except:
            pass

    def read_value(self, nameValue):
        # Open key
        opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.afterPath, 0,winreg.KEY_ALL_ACCESS)  # Error if key is emply
        # Create value
        f = winreg.QueryValueEx(opened_key, nameValue)
        print(f)

    def set_value_String(self, nameValue, value):
        self.__create_value(winreg.REG_SZ, nameValue, value)

    def set_value_Binary(self, nameValue, value):
        self.__create_value(winreg.REG_BINARY, nameValue, value)

    def set_value_DWORD(self, nameValue, value):
        self.__create_value(winreg.REG_DWORD, nameValue, value)

    def set_value_QWORD(self, nameValue, value):
        self.__create_value(winreg.REG_QWORD, nameValue, value)

    def set_value_MultiString(self, nameValue, value):
        self.__create_value(winreg.REG_MULTI_SZ, nameValue, value)

    def set_value_ExpandableString(self, nameValue, value):
        self.__create_value(winreg.REG_EXPAND_SZ, nameValue, value)

    def delete_value(self, nameValue):
        try:
            # Open key
            opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.afterPath, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
            # Create value
            winreg.DeleteValue(opened_key, nameValue)
        except:
            pass


path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = 'config'
value = "soy un valor String"
k = WinRegistry(path)
k.set_value_String(nameValue, value)


# hhh = winreg.HKEY_CURRENT_USER
# winreg.CreateKeyEx(hhh, "hola\ho", 0, winreg.KEY_ALL_ACCESS)


#path3 = "Computer\HKEY_CURRENT_USER\hey"
#h = WinRegistry(path3)
#https://stackoverflow.com/questions/27534005/how-to-read-reg-binary-type-values-in-string-format-from-registry-in-python
#g = b'v\x00l\x00c\x00.\x00e\x00x\x00e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x85\x00\x00\x00\x10\x03\x00\x00<\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\xa4\x00\x00\x00i\x03\x00\x00\x84\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
#h.set_value_Binary('namevaluedd', g)
#h.read_value('asd')


