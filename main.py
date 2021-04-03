import csv
with open('Listado_alumnos(csv).csv') as csvfile:
    alumnos = csv.reader(csvfile,delimiter=';')
    for row in alumnos:
        print('usuario: '+row[1].split('@')[0]+' correo: '+row[1]+' pass: '+row[1].split('@')[0] )
