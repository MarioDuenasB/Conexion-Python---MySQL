import mysql.connector

bd = mysql.connector.connect(user ='mario', password ='12345678', 
    database ='mascotas')

cursor = bd.cursor()

while True:
    print('1.- Agregar dueno')
    print('2.- Mostrar duenos')
    print('0.- SALIR')
    op = input()
    
    if op == '1':
        nombre= input('nombre: ')
        domicilio= input('domicilio: ')
        apellido= input('apellido: ')
        telefono= input('telefono: ')
        email= input('email: ')
        foto= input('foto: ')

        consulta = "INSERT INTO dueno (Nombre, Domicilio, Apellido, Telefono, Email, Foto) VALUES (%s, %s, %s, %s, %s, %s)"

        cursor.execute(consulta, (nombre, domicilio, apellido, telefono, email, foto))
        bd.commit()
        if cursor.rowcount:
            print('Se agrego un dueno')
        else:
            print('ERROR')

    elif op == '2':
        consulta = "SELECT * FROM dueno"
        
        cursor.execute(consulta)

        for row in cursor.fetchall():
            print('Id: ', row[0])
            print('Nombre: ', row[1])
            print('Domicilio: ', row[2])
            print('Apellido: ', row[3])
            print('Telefono: ', row[4])
            print('Email: ', row[5])
            print('Foto: ', row[6])

    elif op == '0':
        break