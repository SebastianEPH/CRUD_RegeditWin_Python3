# Create in Python 3.8.5
# Import Library
import winreg

# Global variables
from msilib.schema import File

sub_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\"
key = "Run"
path = sub_path + key


def createKey(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # sub_path can be empty
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)


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
        self.alferPath = path
        self.HKEY = ""
        self.ID = 0
        id = 0
        listHKEY = {
            'CLASSES_ROOT': [
                r'HKEY_CLASSES_ROOT'],
            'CURRENT_USER': [
                r'HKEY_CURRENT_USER'],
            'LOCAL_MACHINE': [
                r'HKEY_LOCAL_MACHINE'],
            'USERS': [
                r'HKEY_USERS'],
            'CURRENT_CONFIG': [
                r'HKEY_CURRENT_CONFIG']
        }
        for sub in listHKEY:
            for s in listHKEY[sub]:
                id = id + 1
                index = self.alferPath.find(s)  # getting boot index
                if index != -1:  # Only if it was successful
                    self.HKEY = s   # get HKEY
                    self.ID = id    # get id
                    index = index + len(s)+1    # Index cut
                    end = len(self.alferPath)   # End cut
                    self.alferPath = self.alferPath[index:end]   # cut path

    def create_key(self, keyName):
        pass
    def delete_key(self, keyName):
        pass
    def read_value(self, nameValue):
        pass
    def create_value_String(self, nameValue, value):
        pass
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

path3 ="Computer\HKEY_LOCAL_MACHINE\Console"
h = WinRegistry(path3)
#h.get_HKEY_and_formatPath()
print(h.HKEY)
print(h.alferPath)
print(h.ID)


"""
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
# https://docs.python.org/3/library/winreg.html