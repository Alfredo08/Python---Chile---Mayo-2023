from app_imagenes.config.mysqlconnection import connectToMySQL
from app_imagenes import BASE_DATOS

class Imagen:
    def __init__( self, data ):
        self.id = data['id']
        self.ruta_imagen = data['ruta_imagen']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
    
    @classmethod
    def agrega_uno( cls, data ):
        query = """
                INSERT INTO imagenes( ruta_imagen )
                VALUES ( %(ruta_imagen)s );
                """
        return connectToMySQL( BASE_DATOS ).query_db( query, data )
