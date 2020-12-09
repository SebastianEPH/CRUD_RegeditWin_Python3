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


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request


</details>
<details>
  <summary>📚 Set value DWORD</summary>


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request


</details>
<details>
  <summary>📚 Set value QWORD</summary>


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request


</details>
<details>
  <summary>📚 Set value Multi-String</summary>


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request


</details>
<details>
  <summary>📚 Set value Expandable-String</summary>


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request


</details>
<details>
  <summary>📚 Delete Value</summary>


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request

</details>
<details>
  <summary>📚 Read Value</summary>


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request


</details>