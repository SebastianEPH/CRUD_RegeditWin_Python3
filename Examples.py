# Create in Python 3.8.5
# Import Library
import winreg

# Global variables
from msilib.schema import File
path = ""

############### SET VALUE EX ################
def setValueEx(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
    name_value = "Valor"
    value = "soy un valor"
    # Create value
    winreg.SetValueEx(opened_key, name_value, 0, winreg.REG_EXPAND_SZ, value)


############### SET VALUE ################
def setValue(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    name_value = "Valor"  # not use name value // (default)
    value = "soy un valor"
    # Create value
    winreg.SetValue(winreg.HKEY_CURRENT_USER, key, winreg.REG_SZ, value)


############### DELETE VALUE ################
def deleteValue(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
    name_value = "Valor"
    # Create value
    winreg.DeleteValue(opened_key, name_value)


############### DELETE KEY ################
def deleteKey(self):
    # This method can not delete keys with subkeys.
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, path)


############### DELETE KEY  ################
def deleteKeyEx(self):
    # This method can not delete keys with subkeys.
    winreg.DeleteKeyEx(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)


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

    def __format_afterPath(self):
        afterPath = self.afterPath
        if afterPath != "":
            return afterPath + "\\"
        else:
            return afterPath

    def __createvalue(self, type, nameValue, value):
        self.create_key('')
        opened_key = winreg.OpenKey(self.HKEY, self.afterPath, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(opened_key, nameValue, 0, type, value)
        opened_key.Close()

    def create_key(self, keyName):
        winreg.CreateKeyEx(self.HKEY, self.__format_afterPath() + keyName, 0, winreg.KEY_ALL_ACCESS)

    def delete_key(self, keyName):
        winreg.DeleteKeyEx(self.HKEY, self.__format_afterPath() + keyName, winreg.KEY_ALL_ACCESS, 0)

    def read_value(self, nameValue):
        pass

    def create_value_String(self, nameValue, value):
        self.__createvalue(winreg.REG_SZ, nameValue, value)

    def create_value_Binary(self, nameValue, value):
        pass

    def create_value_DWORD(self, nameValue, value):
        pass

    def create_value_QWORD(self, nameValue, value):
        pass

    def create_value_MultiString(self, nameValue, value):
        pass

    def create_value_ExpandableString(self, nameValue, value):
        pass

    def delete_value(self, nameValue):
        pass

#hhh = winreg.HKEY_CURRENT_USER
#winreg.CreateKeyEx(hhh, "hola\ho", 0, winreg.KEY_ALL_ACCESS)


path3 = "Computer\HKEY_CURRENT_USER\hey"
h = WinRegistry(path3)
h.create_value_String('namevalue', 'soy valor')
"""
nameValue  = "soy el nombre"
setValue()
print(nameValue)
print(value)
print(self.HKEY)
print(self.afterPath)

opened_key = winreg.OpenKey(self.HKEY, self.afterPath, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
# Create value
winreg.SetValueEx(opened_key, nameValue, 0, winreg.REG_EXPAND_SZ, value)
#opened_key.Close()


def saveKey():
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
    name_value = "Valor"
    # Create value
    file = open("file.txt", "w")  # Read file
    #winreg.LoadKey(opened_key, name_value, file)
    winreg.SaveKey(opened_key, file.name)
    """

# Read Documentation:
#
