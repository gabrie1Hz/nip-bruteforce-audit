# Fuerza Bruta en Panel de Login Institucional

Este script realiza un ataque de fuerza bruta contra un panel de login vulnerable de una institución educativa. Está diseñado para pruebas de auditoría y análisis de fallos en sistemas de autenticación, y permite automatizar el envío de NIPs desde un archivo `.txt`. Además, utiliza **Burp Suite** como proxy para inspeccionar las solicitudes HTTP.

> ⚠️ **Nota:** Este script debe ser usado únicamente con fines educativos o en auditorías éticas donde se tenga permiso explícito para probar la seguridad del sistema. **No lo utilices en sistemas sin autorización.**

## Características
- Automatiza el envío de NIPs para un número de control específico.
- Redirige las solicitudes a través de **Burp Suite** para inspeccionar y depurar.
- Añade un delay de 10 segundos entre intentos para evitar saturar el servidor.
- Maneja errores comunes como fallos en la conexión o respuestas HTTP no esperadas.

---

## Requisitos

1. **Python 3.7 o superior** instalado en tu sistema.
2. Módulos de Python requeridos:
   - `requests`
3. **Burp Suite** configurado como proxy:
   - Proxy escuchando en `127.0.0.1:8080`.
   - Certificado SSL de Burp Suite instalado (si trabajas con HTTPS).

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/fuerza-bruta-institucional.git
   cd fuerza-bruta-institucional
