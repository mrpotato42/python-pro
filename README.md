# 🤖 Discord Info Bot

Un bot de Discord desarrollado con **discord.py** que responde a comandos de prefijo para brindar información útil sobre el servidor y el estado del bot.

---

## 📋 Descripción

**Discord Info Bot** es un bot de Discord creado en Python utilizando la biblioteca `discord.py`. Su propósito es interactuar con los usuarios de un servidor respondiendo a comandos específicos, proporcionando información del servidor y verificando que el bot esté funcionando correctamente.

El bot fue desarrollado como proyecto práctico para el curso **Python Pro**, aprovechando las funciones integradas de la biblioteca `discord.py` como el sistema de comandos (`commands.Bot`), los `Embeds` y los `Intents`.

---

## ⚙️ Funciones

### `/info`
Muestra un **Embed** con información del servidor actual:
- 👤 **Miembro**: nombre del usuario que ejecutó el comando.
- 📢 **Canal**: nombre del canal donde se ejecutó el comando.
- 🔎 Pie de página indicando que el bot fue creado con `discord.py`.

### `/health`
Verifica el estado del bot:
- ✅ Si el bot está listo, responde con un saludo personalizado al usuario que usó el comando.
- ❌ Si ocurre algún problema, notifica al usuario con un mensaje de error.

---

## 🚀 Cómo ejecutar el bot

### 1. Clonar el repositorio

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
venv\Scripts\activate   # En Windows
```

```bash
python3 -m venv venv
source venv/bin/activate   # En Linux/Mac
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar el token
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```
DISCORD=tu_token_aqui
```
> ⚠️ Este proyecto ya cuenta con un token, el cual puedes encontrar en el archivo `.env`, si no existe, crealo y agregue su propio token.

### 5. Invitar el bot a tu servidor

Puedes invitar el bot usando el siguiente enlace de autorización:
[Invitar Bot a Discord](https://discord.com/oauth2/authorize?client_id=1507119801217056869&permissions=4399120394304&scope=bot)

### 6. Ejecutar el bot
```bash
python discord_bot.py
```

## 📦 Dependencias

Las dependencias del proyecto se encuentran en el archivo `requirements.txt`. Las principales son:

| Librería | Descripción |
|---|---|
| `discord.py` | Framework principal para crear bots de Discord |
| `python-dotenv` | Carga variables de entorno desde el archivo `.env` |

---

## 📁 Estructura del proyecto

```
Python-Pro/
│
├── discord_bot.py      # Archivo principal del bot
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Este archivo
└── .env                # Variables de entorno (no incluido en el repositorio)
```

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **discord.py** — Biblioteca principal del proyecto
- **python-dotenv** — Manejo seguro de credenciales

---
