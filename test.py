tablero = [4,4,4,0,4,4,0,4,4,4,4,4,4,0]
jugadas_posibles = [0,1,2,3,4,5]
print(type(jugadas_posibles))
print(len(jugadas_posibles))

print('posibles jugadas: {}'.format(jugadas_posibles))
# Borramos las jugadas que estan vacias
for x in jugadas_posibles:
    print('halp')
    print('x: {}'.format(x))
    print('Valor en Tablero: {}'.format(tablero[x]))

    if tablero[x] == 0:
        print('si es 0')
        jugadas_posibles.remove(x)

print(jugadas_posibles)