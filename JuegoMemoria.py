from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
numTaps = 0
cartasDescubiertas = 0
fin = False

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    "Se utilizan las variables globales"
    global numTaps 
    global cartasDescubiertas
    global fin

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
    else:
        hide[spot] = False  
        hide[mark] = False
        state['mark'] = None
        cartasDescubiertas += 1 #Se aumenta el numero de cartas descubiertas
    
    "Aumenta el numero de clic"
    numTaps += 1
    print("Veces que se ha hecho click: ", numTaps)
    print("Pares de cartas encontradas: ", cartasDescubiertas)
    print("")
    "Si todas las cartas han sido descubiertas se imprime un mensaje en consola y la variable fin se marca True"
    if (cartasDescubiertas == 32):
        print("HAS GANADO!!")
        fin = True

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        "Se da un color de valor absoluto"
        valcolor = tiles[mark] * 0.125
        r = 0
        g = 0
        b = 0
        "Segun los 4 tipo de transicion se cambian los colores RGB"
        #Rojo -> Amarillo
        if(valcolor<=1):
            r = 1
            g = valcolor % 1
            b = 0
        #Amarillo -> Verde
        elif(valcolor<=2):
            r = 1 - valcolor % 1
            g = 1
            b = 0
        #Verde -> Verde/Azul
        elif(valcolor<=3):
            r = 0
            g = 1
            b = valcolor % 1
        #Verde/Azul -> Azul
        else:
            r = 0
            g = 1 - valcolor % 1
            b = 1
        goto(x+25, y+10)    #Centrado del texto
        color(r,g,b)    #Se aplica RGB
        write(tiles[mark], align='center', font=('Arial', 15, 'bold'))
    
    "Si 'fin' es verdadero el juego finaliza"
    if (fin):
        return

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()