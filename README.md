# WinRegistry CRUD

* __Developed by:__ `SebastianEPH`
* __Product name:__ `WinRegistry CRUD`
* __Type software:__ `Library`
* __File version:__ `1.0`
* __State:__ `Finish`
* __Plataform:__ `Only Windows 7, 8.1, 10`
* __Programming language:__ `Python 3.9`
* __Licence:__ `MIT`
* __IDE or text editor:__ `PyCharm`
* __Documentation date:__ `08-12-2020`
* __Description:__ `Biblioteca que permite, leer, crear, eliminar llaves y valores del registro de Windows`


## Ejemplos de Uso
<details>
  <summary><b>Create Key</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\Adobe'
nameKey = 'config'
k = WinRegistry(path)
k.create_key(nameKey)
````
### Antes 

![](https://imgur.com/xD2S6Gn.png)

### Despues 
![](https://imgur.com/4XutaWN.png)

</details>
<details>
  <summary><b>Delete Key</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\Adobe'
nameKey = 'config'
k = WinRegistry(path)
k.delete_key(nameKey)
````
### Antes 
![](https://imgur.com/4XutaWN.png)

### Despues 
![](https://imgur.com/xD2S6Gn.png)

</details>

<details>
  <summary><b>Set value String</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = 'config'
value = "soy un valor String"
k = WinRegistry(path)
k.set_value_String(nameValue, value)
````
### Antes 
![](https://imgur.com/8GSRnC8.png)

### Despues 
![](https://imgur.com/ZHZ0YmQ.png)

</details>
<details>
  <summary><b>Set value Binary</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = 'Typebinary'
value = b'v\x00l\x00c\x00.\x00e\x00x\x00e\x00\x00\x00\x00'
k = WinRegistry(path)
k.set_value_Binary(nameValue, value)
````
### Antes 
![](https://imgur.com/sCNJaNh.png)

### Despues 
![](https://imgur.com/ywd6yvK.png)

![](https://imgur.com/GMdOtNj.png)

</details>
<details>
  <summary><b>Set value DWORD</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = 'TypeDWORD'
value = 45
k = WinRegistry(path)
k.set_value_DWORD(nameValue, value)
````
### Antes 
![](https://imgur.com/sCNJaNh.png)

### Despues 
![](https://imgur.com/lFnLHzp.png)

</details>
<details>
  <summary><b>Set value QWORD</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = 'TypeQWORD'
value = 45545454545
k = WinRegistry(path)
k.set_value_QWORD(nameValue, value)
````
### Antes 
![](https://imgur.com/sCNJaNh.png)

### Despues 
![](https://imgur.com/IYz3D2A.png)

</details>
<details>
  <summary><b>Set value Multi-String</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = 'TypeMultiString'
value = ['linea 1', 'linea 2', 'linea fin']
k = WinRegistry(path)
k.set_value_MultiString(nameValue, value)
````
### Antes 
![](https://imgur.com/sCNJaNh.png)

### Despues 
![](https://imgur.com/VeT5cns.png)
![](https://imgur.com/cv7NzKt.png)

</details>
<details>
  <summary><b>Set value Expandable-String</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = 'TypeExpandableString'
value = "texto largo..."
k = WinRegistry(path)
k.set_value_ExpandableString(nameValue, value)
````
### Antes 
![](https://imgur.com/8GSRnC8.png)

### Despues 
![](https://imgur.com/pmowP4n.png)

</details>
<details>
  <summary><b>Delete Value</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = "name"
k = WinRegistry(path)
k.delete_value(nameValue)
````

</details>
<details>
  <summary><b>Read Value</b></summary>

## Código de ejemplo

````py
path = r'Computer\HKEY_CURRENT_USER\SOFTWARE\test'
nameValue = "name"
k = WinRegistry(path)
print(k.read_value(nameValue))
````
</details>

___

## Versión de esta lib pero en en C# .net
### Windows Registry Tools C# || [ link del repositorio](https://github.com/SebastianEPH/WindowsRegistryTools_Library)

