# Primero se debe instalar el paquete yt-dlp con el comando: pip install yt-dlp
# Ejecucion de scripts en windows Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Luego, se puede ejecutar el script con el comando: python download.py

import yt_dlp

def descargar_video(url, ruta_destino="."):
    try:
        opciones = {
            'outtmpl': f'{ruta_destino}/%(title)s.%(ext)s',  # Guardar con título original
            'format': 'best'  # Descargar el mejor formato disponible (sin combinar)
        }
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("¡Descarga completada!")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    url_video = input("Ingresa la URL del video de YouTube: ")
    ruta = input("Ingresa la ruta de destino (deja en blanco para el directorio actual): ") or "."
    descargar_video(url_video, ruta)
