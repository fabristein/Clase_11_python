# Clase 11 Python — Evaluador de Notas con Flask + PostgreSQL + MinIO

Aplicación web construida con Flask que evalúa notas de alumnos, persiste los registros en PostgreSQL y utiliza MinIO como almacenamiento de objetos. Todo el stack corre dentro de contenedores Docker.

---

## Requisitos previos

- Git
- Python 3.10+
- Docker y Docker Compose

---

## 0. Instalar Docker y Docker Compose

### En Linux (Ubuntu / Debian)

Docker Compose viene incluido como plugin oficial de Docker desde la versión moderna del engine. No es necesario instalarlo por separado.

**Paso 1 — Agregar la clave GPG oficial de Docker y el repositorio apt:**

## A. Actualizar el índice de paquetes locales e instalar las dependencias de transporte criptográfico
```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
```

## B. Crear el directorio seguro para los llaveros GPG si no existiese en el host
```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

## C. Descargar la clave GPG oficial de Docker e importarla en formato.asc (estándar moderno no depreciado)
```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

## D. Registrar de manera dinámica el repositorio oficial estable según la arquitectura del procesador del sistema
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

## E. Sincronizar de nuevo el gestor de paquetes con el repositorio oficial recién registrado
```bash
sudo apt update
```

## F. Instalar los binarios estables del motor, la CLI, el runtime y los plugins de Buildx y Compose v2

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## G. Verificar la instalación:

```bash
sudo systemctl status docker
sudo docker run hello-world
docker compose version
```

> Si Docker no está corriendo, iniciarlo manualmente: `sudo systemctl start docker`

> **Opcional:** Para ejecutar Docker sin `sudo`, agregá tu usuario al grupo `docker` y reiniciá sesión:
> ```bash
> sudo usermod -aG docker $USER
> ```

---

### En Windows

En Windows la forma oficial y recomendada es instalar **Docker Desktop**, que incluye el motor de Docker, Docker Compose y una interfaz gráfica.

#### Requisitos del sistema

- Windows 10 64-bit (versión 22H2 o superior) o Windows 11 64-bit
- Mínimo 8 GB de RAM
- Virtualización habilitada en BIOS/UEFI
- WSL 2 habilitado (se instala automáticamente junto con Docker Desktop)

#### Opción A: Instalar con winget (recomendado, desde PowerShell o CMD)

```powershell
winget install -e --id Docker.DockerDesktop
```

Una vez instalado, reiniciá el sistema y abrí **Docker Desktop** desde el menú inicio. Esperá a que el motor arranque (ícono de ballena en la barra de tareas).

#### Opción B: Instalación manual (descarga del instalador)

1. Descargá el instalador desde la página oficial: [https://docs.docker.com/desktop/release-notes/](https://docs.docker.com/desktop/release-notes/)
2. Ejecutá `Docker Desktop Installer.exe` y seguí el asistente.
3. Al instalar, asegurate de que la opción **"Use WSL 2 instead of Hyper-V"** esté seleccionada.
4. Reiniciá el sistema al finalizar.

**Verificar la instalación (en PowerShell o CMD):**

```powershell
docker --version
docker compose version
docker run hello-world
```

---

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <DIRECTORIO_DEL_PROYECTO>
```

---

## 2. Crear y activar el entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> En Windows usar: `.venv\Scripts\activate`

---

## 3. Instalar dependencias de Python(una vez activado el entorno virtual)

```bash
pip install flask

pip install flask-sqlalchemy

pip install python-dotenv

pip install psycopg2-binary

o 

pip install flask flask-sqlalchemy python-dotenv psycopg2-binary
```

### Generar el archivo `requirements.txt`

```bash
pip freeze > requirements.txt
```

---

## 4. Configurar las variables de entorno

Copiar el archivo de ejemplo y completar los valores:

```bash
cp .env-example .env
```

Editar `.env` con los datos del entorno:

```env
# Configuración de la Base de Datos
DB_USER=admin
DB_PASSWORD=123
DB_HOST=db
DB_PORT=5432
DB_NAME=evaluador_db

# URL de conexión que usará SQLAlchemy
DATABASE_URL=postgresql://admin:123@db:5432/evaluador_db

# MinIO config
MINIO_ROOT_USER=admin
MINIO_ROOT_PASSWORD=123
MINIO_BROWSER_REDIRECT_URL=https://your-domain.ngrok-free.dev
```

---

## 5. Exponer MinIO con Ngrok (acceso externo)

**Ngrok** es una herramienta que crea un túnel seguro entre internet y un puerto de tu máquina local. Te da una URL pública (con HTTPS) que redirige el tráfico a tu servicio, sin necesidad de configurar el router ni abrir puertos. Es ideal para compartir o acceder a servicios locales desde cualquier lugar.

### 1. crear cuenta en Ngrok(tiene cuenta gratuita)

[https://ngrok.com/](https://ngrok.com/)

### 2. Instalar Ngrok

**Snap** es un sistema de paquetes de Linux desarrollado por Canonical (Ubuntu) que permite instalar aplicaciones de forma aislada y con actualizaciones automáticas. Muchas distribuciones lo traen desactivado por defecto; los pasos a continuación lo habilitan.

Primero, habilitar Snap (si está bloqueado en el sistema):

```bash
sudo mv /etc/apt/preferences.d/nosnap.pref /etc/apt/preferences.d/nosnap.bak
sudo apt update
sudo apt install snapd
```

> **Importante:** Cerrá sesión o reiniciá el ordenador para que el sistema reconozca los nuevos comandos de Snap.

Luego instalar Ngrok y autenticarlo con tu token:

```bash
sudo snap install ngrok
ngrok config add-authtoken TU_TOKEN_AQUÍ
```
> El token lo encontrás en [https://dashboard.ngrok.com/](https://dashboard.ngrok.com/) → *Your Authtoken*.

---

### 3. Exponer el puerto de MinIO Console

MinIO sirve la interfaz gráfica en el puerto `9001`. Para exponerlo al exterior, ejecutá:

```bash
ngrok http 9001
```

La terminal quedará "bloqueada" mostrando el estado del túnel. Buscá la línea `Forwarding` y copiá la URL segura (`https://`):

```
Forwarding  https://a1b2-c3d4-e5f6.ngrok-free.app -> http://localhost:9001
```

> **Nota:** No cierres esa terminal. Si cerrás Ngrok, el túnel se destruye y la URL deja de funcionar. Abrí una nueva pestaña para seguir trabajando con Docker.

Una vez que tenés la URL, actualizá `MINIO_BROWSER_REDIRECT_URL` en tu `.env`:

```env
MINIO_BROWSER_REDIRECT_URL=https://a1b2-c3d4-e5f6.ngrok-free.app
```

---

### 4. Usar tu Dev Domain estático (recomendado)

Ngrok asigna automáticamente un **Dev Domain** gratuito y permanente al crear la cuenta. No vence ni cambia aunque reinicies la consola.

#### Paso A: Encontrar tu dominio asignado

1. Entrá al panel de [Ngrok Dashboard](https://dashboard.ngrok.com/).
2. En el menú lateral izquierdo, ir a **Universal Gateway** → **Domains** (en algunas cuentas figura como *Cloud Edge* → *Domains*).
3. Copiá el dominio estático asignado. Suele tener una estructura como `nombre-aleatorio.ngrok-free.dev`.

#### Paso B: Lanzar el túnel con la URL fija

Usá el flag `--url` para fijar el dominio:

```bash
ngrok http 9001 --url=tu-dominio-aleatorio.ngrok-free.dev
```

Por ejemplo:

```bash
ngrok http 9001 --url=tu-dominio.ngrok-free.dev
```

A partir de ahora el túnel siempre usará ese enlace exacto.

#### Paso B.1 (Opcional): Lanzar el túnel con política de acceso

Para proteger el acceso a la consola de MinIO podés agregar el flag `--traffic-policy-file` apuntando al archivo `policy.yaml` incluido en el proyecto:

```bash
ngrok http 9001 --url=tu-dominio.ngrok-free.dev --traffic-policy-file policy.yaml
```

**¿Qué hace `policy.yaml`?**

El archivo define dos reglas que Ngrok aplica a cada petición HTTP entrante antes de llegar a MinIO:

1. **Autenticación OAuth con Google** — redirige al usuario a Google para que inicie sesión con su cuenta.
2. **Control de acceso por dominio/email** — una vez autenticado, verifica el email del usuario. Si el email **no** termina en `@gmail.com` (o el dominio que configures), la petición es denegada con un error 403.

Esto significa que solo las cuentas de Google con el dominio autorizado podrán ver la consola de MinIO desde la URL pública. Para restringir a un dominio de organización en lugar de `@gmail.com`, editá esta línea en `policy.yaml`:

```yaml
- "!actions.ngrok.oauth.identity.email.endsWith('@gmail.com')"
```

Reemplazando `@gmail.com` por el dominio deseado, por ejemplo `@miempresa.com`.

#### Paso C: Actualizar `.env` con el dominio fijo

```env
MINIO_BROWSER_REDIRECT_URL=https://tu-dominio-aleatorio.ngrok-free.dev
```

Luego reiniciá los contenedores para que tomen el nuevo valor:

```bash
docker compose --env-file .env up --build
```

---

## 6. Levantar los contenedores Docker

```bash
docker compose --env-file .env up --build
```

Este comando construye la imagen de la app Flask e inicia los cuatro servicios:

| Servicio  | Descripción                         |
|-----------|-------------------------------------|
| `web`     | Aplicación Flask                    |
| `db`      | Base de datos PostgreSQL 15         |
| `adminer` | Gestor visual de base de datos      |
| `minio`   | Almacenamiento de objetos (S3-like) |

---

## 7. Verificar que los contenedores funcionan

Una vez que todos los servicios están corriendo, acceder a las siguientes rutas en el navegador:

| Servicio          | URL                                         |
|-------------------|---------------------------------------------|
| Flask (app)       | [http://localhost:5000](http://localhost:5000) |
| Adminer (DB GUI)  | [http://localhost:8080](http://localhost:8080) |
| MinIO Console     | [http://localhost:9001](http://localhost:9001) |
| MinIO API         | [http://localhost:9000](http://localhost:9000) |

### Credenciales de Adminer

- **Sistema:** PostgreSQL
- **Servidor:** `db`
- **Usuario:** valor de `DB_USER` en `.env`
- **Contraseña:** valor de `DB_PASSWORD` en `.env`
- **Base de datos:** valor de `DB_NAME` en `.env`

### Credenciales de MinIO Console

- **Usuario:** valor de `MINIO_ROOT_USER` en `.env`
- **Contraseña:** valor de `MINIO_ROOT_PASSWORD` en `.env`

---


## 8. Detener los contenedores

```bash
docker compose down
```

Para eliminar también los volúmenes de datos persistentes:

```bash
docker compose down -v
```
