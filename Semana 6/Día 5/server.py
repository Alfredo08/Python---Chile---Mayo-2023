from app_imagenes.controladores import controlador_imagenes
from app_imagenes import app

if __name__ == "__main__":
    app.run( debug = True, port = 5001 )