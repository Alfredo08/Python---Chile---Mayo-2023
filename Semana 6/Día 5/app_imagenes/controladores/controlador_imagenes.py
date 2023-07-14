from app_imagenes.modelos.modelo_imagen import Imagen
from flask import render_template, redirect, request
from app_imagenes import app, FOLDER_IMAGENES
from werkzeug.utils import secure_filename
import os

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif']

@app.route( '/', methods = ['GET'] )
def inicio():
    return render_template( 'index.html' )

@app.route( '/muestra/imagen/<string:ruta>', methods = ['GET'] )
def desplegar_imagen( ruta ):
    return render_template( 'muestra_imagen.html', ruta = ruta )

@app.route( '/agregar/imagen', methods = ['POST'] )
def crear_imagen():
    if 'imagen' not in request.files:
        return redirect( '/' )
    else:
        nueva_imagen = request.files['imagen']
        
        if nueva_imagen and allowed_file( nueva_imagen.filename ):
            nombre_archivo = secure_filename( nueva_imagen.filename )
            nueva_imagen.save( os.path.join(FOLDER_IMAGENES, nombre_archivo ) )

            data = {
                "ruta_imagen" : f'/imagenes/{nombre_archivo}'
            }
            Imagen.agrega_uno( data )
            return redirect( f'/muestra/imagen/{nombre_archivo}' )