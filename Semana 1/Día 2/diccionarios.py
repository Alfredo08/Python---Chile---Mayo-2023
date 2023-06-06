
""" js
let estudiante = {
    nombre : "Alex",
    apellido : "Gonzalez",
    edad : 25
};

console.log( estudiante.apellido );
"""

estudiante = {
    'nombre' : 'Alex',
    'apellido' : 'Gonzalez',
    'edad' : 25,
    'diplomas' : ['Yellow belt', 'Black belt']
}

print( estudiante['apellido'] )
estudiante['nombre'] = 'Alejandro'
estudiante['calificacion'] = 9.7

estudiante.pop( 'edad' )

print( estudiante )
print( estudiante['diplomas'][1] )

