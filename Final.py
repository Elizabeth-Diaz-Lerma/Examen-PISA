#Main
#Parte Barbara
#aqui se guardan los puntajes de cada seccion

puntos_mate = 0
puntos_cien = 0
puntos_esp = 0

def main():
  print('Bienvenido a tu examen prueba')
  print('Se desplegarán ciertos menus a elegir, selecciona la seccion que quieras realizar:')
  print('\nMENU')
  print('\n1. MATEMATICAS')
  print('2. ESPAÑOL ')
  print('3. CIENCIAS')
  print('0. SALIR')
    
  print("\n  SELECCION:")
  puntaje_total = 0
  for veces in range (3):
    op = int(input(" \n Ingresa tu menu a elegir: "))
    
 #variables de puntaje
 #Pregunta Matematicas 
    if (op == 1):
        for veces in range (5):
          pazar = random.choice(banco_mate)
          puntaje_total = mostrar_pregunta_mate(puntaje_total, pazar[0], pazar[1], pazar[2], pazar[3])
          banco_mate.remove(pazar)
          puntos_mate = puntaje_total
        if puntaje_total == 100:
          print("Haz dominado matemáticas")
        elif puntaje_total == 60 or puntaje_total == 80:
          print("Te hace falta un poco de estudio")
        else:
          print("Te hace falta mucha practica en matemáticas")
  #parte de espanol       
    elif(op == 2):
        for filas in range (4):
            if 0 <= filas <=3:
                archivo_G = open('Lectura_gripe.txt', 'r')
                for linea in archivo_G:
                    print(f' {linea}', end = '')
                archivo_G.close()

            elif 4 <= filas <=7 :
                archivo_P = open('Lectura_pies_secos.txt', 'r')
                for linea in archivo_P:
                    print(f' {linea}', end = '')
                archivo_P.close()
                
            else: 
                archivo_D = open('Lectura_dientes.txt', 'r')
                for linea in archivo_D:
                    print(f' {linea}', end = '')
                archivo_D.close()
            puntaje_total = mostrar_pregunta_espanol(puntaje_total, p_español[filas][0], p_español[filas][1], p_español[filas][2], p_español[filas][3], p_español[filas][4], p_español[filas][5], p_español[filas][6])
            puntos_esp = puntaje_total
        if puntaje_total == 100:
          print("Haz dominado español")
        elif puntaje_total == 75:
          print("Te hace falta un poco de estudio")
        else:
          print("Te hace falta mucha practica en español")
  #parte de ciencias        
    elif (op == 3):
        for veces in range (5):
            pazar = random.choice(banco_ciencias)
            puntaje_total = mostrar_pregunta_ciencias(puntaje_total, pazar[0], pazar[1], pazar[2], pazar[3])
            banco_ciencias.remove(pazar)
            puntos_cien = puntaje_total
        if puntaje_total == 100:
          print("Haz dominado ciencias")
        elif puntaje_total == 60 or puntaje_total == 80:
          print("Te hace falta un poco de estudio")
        else:
          print("Te hace falta mucha practica en ciencias")
        
    elif (op == 0):
        print("\nSALIDA")
        print("¡Hasta luego!")
        quit()
    
    else:
        print("Opción inválida")
  return puntos_mate, puntos_esp, puntos_cien
    
 #Preguntas de español
 #Parte Elizabeth 
def mostrar_pregunta_espanol(ptotal, preg, opc1, opc2, opc3, opc4, correcta, puntaje):
    print (preg)
    print (opc1, opc2, opc3, opc4)
    resp_usuario = input ('Teclea tu respuesta: ')
    if resp_usuario== correcta:
        ptotal = ptotal + puntaje
    return ptotal
    

p_español = [['\n ¿Cuál de las siguientes afirmaciones describe una característica del programa de inmunización de ACOL contra la gripe?\n',
    ' a) Se darán clases de ejercicio físico durante el invierno.\n' ,
    'b) La vacunación se llevará a cabo durante las horas de trabajo.\n' ,
    'c) Se ofrecerá un pequeño bono a los participantes.\n',
    'd) Un médico pondrá las inyecciones \n',
    'b',
    25], ['\n Esta hoja informativa sugiere que si uno quiere protegerse del virus de la gripe, la inyección de una vacuna de la gripe es...\n',
    'a) Más eficaz que el ejercicio y una dieta saludable, pero más arriesgada.\n' ,
    'b) Una buena idea, pero no un sustituto del ejercicio y la dieta saludable.\n' ,
    'c) Tan eficaz como el ejercicio y una dieta saludable y menos problemática.\n',
    'd) No es necesaria si se hace ejercicio y se sigue una dieta sana.\n',
    'b',
    25], ['\n Según la hoja informativa, ¿cuál de estos empleados de la empresa debería contactar con Raquel?\n',
    'a) Ramón, del almacén, que no quiere vacunarse porque prefiere confiar en su sistema inmunológico natural.\n' ,
    'b) Julia, de ventas, que quiere saber si el programa de vacunación es obligatorio.\n' ,
    'c) Alicia, de recepción, que querría vacunarse este invierno pero dará a luz dentro de dos meses.\n',
    'd) Miguel, de contabilidad, al que le gustaría vacunarse pero tiene que salir de viaje la semana del 17 de mayo. \n',
    'd',
    25], ['\n Podemos hablar sobre el contenido de un escrito (lo que dice). Podemos hablar sobre su estilo (el modo en el que se presenta). Raquel quería que esta hoja informativa tuviera un estilo cordial y que animase a vacunarse. ¿Crees que lo consiguió?\n',
    'a) No, no funciona. \n' ,
    'b) Sí, el estilo es relajado e informal Utiliza sus propios términos (“relajado”, “informal”) para valorar uno de los aspectos mencionados en el enunciado de la pregunta.\n' ,
    'c) No, porque una parte de la información no es correcta. Alicia, de recepción, que querría vacunarse este invierno pero dará a luz dentro de dos meses.\n',
    'd) Sí, las ilustraciones animan a la vacunación y el estilo de la nota también es aceptable.\n',
    'b',
    25],['\n ¿Qué intenta demostrar el autor en este texto? \n',
    'a) Que la calidad de muchas zapatillas deportivas ha mejorado mucho.\n' ,
    'b) Que es mejor no jugar al fútbol si eres menor de 12 años.\n' ,
    'c) Que los jóvenes sufren cada vez más lesiones debido a su baja forma física.\n',
    'd) Que es muy importante para los deportistas jóvenes calzar unas buenas zapatillas deportivas.\n',
    'd',
    25],['\n Según el artículo, ¿por qué no deberían ser demasiado rígidas las zapatillas deportivas? \n',
    'a) Impiden que puedas correr fácilmente.\n' ,
    'b) Para evitar lesiones.\n' ,
    'c) No pueden sujetar el pie.\n',
    'd) Porque necesita apoyar el pie y el tobillo.\n',
    'a',
    25],['\n Fíjate en esta frase que está casi al final del artículo. Aquí se presenta en dos partes: “Para evitar molestias menores, pero dolorosas, como ampollas, grietas o “pie de atleta” (infección por hongos)” (primera parte). “el calzado debe permitir la evaporación del sudor y evitar que penetre la humedad exterior” (segunda parte). ¿Cuál es la relación entre la primera y la segunda parte de la frase? La segunda parte…\n',
    'a) Contradice la primera parte.\n' ,
    'b) Repite la primera parte.\n' ,
    'c) Describe el problema planteado en la primera parte.\n',
    'd) Describe la solución al problema planteado en la primera parte. \n',
    'd',
    25], ['\n Una parte del artículo afirma: “Un buen calzado deportivo debe cumplir cuatro requisitos.” ¿Cuáles son esos requisitos?\n',
    'a) Hacer frente a las desigualdades del terreno.\n' ,
    'b) Mantener el pie caliente y seco.\n' ,
    'c) Tienen que proteger tu pie de los golpes.\n',
    'd) Sujetar el pie.\n',
    'c',
    25],['\n ¿De qué trata el artículo? \n',
    'a) De la mejor manera de cepillarse los dientes.\n' ,
    'b) Del mejor tipo de cepillo de dientes a utilizar.\n' ,
    'c) De la importancia de una buena dentadura.\n',
    'd) De la manera en que las distintas personas se cepillan los dientes.\n',
    'a',
    25], ['\n ¿Qué recomiendan los investigadores británicos? \n',
    'a) Cepillarse los dientes tanto como sea posible. \n' ,
    'b) No intentar cepillarse la lengua. \n' ,
    'c) No cepillarse los dientes demasiado fuerte.\n',
    'd) De la manera en que las distintas personas se cepillan los dientes.\n',
    'c',
    25],['\n Según Bente Hansen, ¿por qué debes cepillarte la lengua? \n',
    'a) Para que no te olvides. \n' ,
    'b) Para eliminar las bacterias y por tanto evitar que tengas mal aliento.\n' ,
    'c) Para quitar los restos de comida.\n',
    'd) Para eliminar la placa dental.\n',
    'b',
    25], ['\n ¿Por qué se menciona un bolígrafo en el texto? \n',
    'a) Para ayudarte a comprender cómo se sujeta un cepillo de dientes.\n' ,
    'b) Porque comienzas por una esquina tanto con el bolígrafo como con el cepillo de dientes.\n' ,
    'c) Para mostrarte que puedes cepillarte los dientes de muchas formas diferentes.\n',
    'd) Porque debes tomarte el cepillo de dientes tan en serio como la escritura.\n',
    'b',
    25],['\n ¿Cuál es el nivel actual de profundidad del lago Chad?\n',
    'a) Alrededor de los dos metros. \n' ,
    'b) Alrededor de los quince metros.\n' ,
    'c) Alrededor de los cincuenta metros\n',
    'd) Ha desaparecido por completo.\n',
    'a',
    25],['\n ¿Cuál es la fecha de comienzo del gráfico en la figura 1? \n',
    'a) 10.000 a.C. \n' ,
    'b) 20.000 a.C. \n' ,
    'c) 11.000 a.C.\n',
    'd) 8.000 a.C. \n',
    'c',
    25],['\n La desaparición en el arte rupestre sahariano del rinoceronte, el hipopótamo y el uro ocurrió... \n',
    'a) A principios de la última era glacial.\n' ,
    'b) A mediados del período en el que el lago Chad alcanzó su máximo nivel.\n' ,
    'c) Después de que el nivel del lago Chad hubiera descendido durante más de mil años.\n',
    'd) A principios de un período continuo de sequía.\n',
    'c',
    25]]
# Preguntas de Mate
#Parte de Joaquin
import random #Libreria
def mostrar_pregunta_mate(ptotal, preg, opc, correcta, puntaje):
    print (preg)
    print (opc)
    #numPregunta == 
    resp_usuario = input ('Tecela tu respuesta: ')
    if resp_usuario == correcta:
        ptotal = ptotal + puntaje

    
    return ptotal

banco_mate = [ ['\n Mei-Ling se enteró de que el tipo de cambio entre el dólar de Singapur y el rand sudafricano era de: 1 SGD = 4,2 ZAR Mei-Ling cambió 3.000 dólares de Singapur en rands sudafricanos con este tipo de cambio. ¿Cuánto dinero recibió Mei-Ling en rands sudafricanos?',
                     'a) 12,000\t b) 9,600\t c) 12,600\t d) 10,000', 'a', 20],
                ['\n Al volver a Singapur, tres meses después, a Mei-Ling le quedaban 3.900 ZAR. Los cambió en dólares de Singapur, dándose cuenta de que el tipo de cambio había cambiado a: 1 SGD = 4,0 ZAR ¿Cuánto dinero recibió en dólares de Singapur?',
                     'a) 1050\t b) 975\t c) 1195\t d) 875', 'b', 20],
               ['\n Normalmente, una pareja de pingüinos pone dos huevos al año. Por lo general, el polluelo del mayor de los dos huevos es el único que sobrevive. En el caso de los pingüinos de penacho amarillo, el primer huevo pesa aproximadamente 78 g y el segundo huevo pesa aproximadamente 110 g. Aproximadamente, ¿en qué porcentaje es más pesado el segundo huevo que el primer huevo? ',
                     'a) 29%\t b) 32%\t c) 41%\t d) 45%', 'c', 20],
               ['\n Jean se pregunta cómo evolucionará en los próximos años el tamaño de una colonia de pingüinos. Para determinarlo elabora las siguientes hipótesis: • A comienzos de año, la colonia consta de 10.000 pingüinos (5.000 parejas). • Cada pareja de pingüinos cría un polluelo todos los años por primavera. • A finales de año, el 20% de los pingüinos (adultos y polluelos) morirá. Al final del primer año, ¿cuántos pingüinos (adultos y polluelos) hay en la colonia?  ',
                     'a) 1200\t b) 1400\t c) 1100\t d) 1300', 'c', 20],
               ['\n Jean establece la hipótesis de que la colonia seguirá creciendo de la siguiente manera: • Al comienzo de cada año, la colonia consta del mismo número de pingüinos machos y hembras que forman parejas. • Cada pareja de pingüinos cría un polluelo todos los años por primavera. • Al final de cada año, el 20% de los pingüinos (adultos y polluelos) morirá. • Los pingüinos de un año de edad también criarán polluelos. Según las anteriores hipótesis, ¿cuál de las siguientes fórmulas expresa el número total de pingüinos, P, después de 7 años? ',
                     'a)  P = 10.000 x (1,5 x 0,2)7 \t b)  P = 10.000 x (1,2 x 0,8)7\n c) P = 10.000 x (1,2 x 0,2)7\t d) P = 10.000 x (1,5 x 0,8)7 ', 'd', 20],
               ['\n La subida al Monte Fuji sólo está abierta al público desde el 1 de julio hasta el 27 de agosto de cada año. Alrededor de unas 200.000 personas suben al Monte Fuji durante este periodo de tiempo. Como media, ¿alrededor de cuántas personas suben al Monte Fuji cada día?',
                     'a) 340\t b) 710\t c) 3.400\t d) 7.10', 'c', 20],
               ['\n La ruta del Gotemba, que lleva a la cima del Monte Fuji, tiene unos 9 kilómetros (km) de longitud. Los senderistas tienen que estar de vuelta de la caminata de 18 km a las 20:00 h. Toshi calcula que puede ascender la montaña caminado a 1,5 kilómetros por hora, como media, y descenderla al doble de velocidad. Estas velocidades tienen en cuenta las paradas para comer y descansar. Según las velocidades estimadas por Toshi, ¿a qué hora puede, como muy tarde, iniciar su caminata de modo que pueda estar de vuelta a las 20:00 h? ',
                     'a) 11:00\t b) 13:00\t c) 9:00\t d) 14:00', 'a', 20],
               ['\n Toshi llevó un podómetro para contar los pasos durante su recorrido por la ruta del Gotemba. El podómetro mostró que dio 22.500 pasos en la ascensión. Calcula la longitud media del paso de Toshi en su ascensión de 9 km por la ruta del Gotemba. Expresa tu respuesta en centímetros (cm). ',
                     'a) 0.4\t b) 40\t c) 80\t d) 0.8', 'b', 20],
               ['\n Durante un trayecto, Elena hizo 4 km durante los 10 primeros minutos y luego 2 km durante los 5 minutos siguientes. ¿Cuál de las siguientes afirmaciones es la correcta? ',
                     'a)  La velocidad media de Elena fue mayor durante los 10 primeros minutos que durante los 5 minutos siguientes.\n b) La velocidad media de Elena fue la misma durante los 15 primeros minutos que durante los 5 minutos siguientes.\n c) La velocidad media de Elena fue menor durante los 10 primeros minutos que durante los 5 minutos siguientes.\n d) La velocidad media de Elena fue la misma durante los 10 primeros minutos que durante los 5 minutos siguientes. ', 'd', 20],
                    ['\n Elena recorrió 6 km hasta la casa de su tía. El velocímetro marcó una velocidad media de 18 km/h para todo el trayecto. ¿Cuál de las siguientes afirmaciones es la correcta? ',
                     'a) Elena le llevó 20 minutos llegar a casa de su tía.\n b) Elena le llevó 30 minutos llegar a casa de su tía.\n c) Elena le llevó 3 horas llegar a casa de su tía.\n d) Elena le llevó 1.5 horas llegar a casa de su tía.', 'b', 20]]
#Preguntas ciencias
#Parte de Marcelo
import random 
#Libreria
def mostrar_pregunta_ciencias(ptotal, preg, opc, correcta, puntaje):
    print (preg)
    print (opc)
    resp_usuario = input ('Tecela tu respuesta: ')
    if resp_usuario== correcta:
        ptotal = ptotal + puntaje
    return ptotal

banco_ciencias = [
    [
        '\nEl humo del tabaco se inhala en los pulmones. El alquitrán del humo se deposita en los pulmones y les impide funcionar de forma adecuada. ¿Cuál de las siguientes funciones es propia del pulmón?',
        'a) Bombear sangre oxigenada a todas las partes del cuerpo.\t b) Transferir el oxígeno del aire que respiras a la sangre.\n c) Purificar la sangre reduciendo a cero su contenido en dióxido de carbono. \t d) Transformar las moléculas de dióxido de carbono en moléculas de oxígeno.', 'b', 20
    ],
    [
        '\n¿Cuál es el papel de las bacterias en la aparición de la caries dental?',
        'a) Las bacterias producen esmalte. \t b) Las bacterias producen azúcar.\n c) Las bacterias producen minerales.\t d) Las bacterias producen ácido.', 'd', 20
    ],
    [
        '\nEn el estrato de caliza del Gran Cañón se encuentran muchos fósiles de animales marinos, como almejas, peces y corales. ¿Qué sucedió hace millones de años para que aparezcan estos fósiles en este estrato?  ',
        'a) Antiguamente los habitantes transportaban alimentos marinos desde el océano a esta área. \t b) En otro tiempo, los océanos eran más violentos, y olas gigantes arrastraban criaturas marinas hacia el interior. \n c) En esa época, la zona estaba cubierta por un océano que más tarde se retiró. \t d) Algunos animales marinos vivieron una vez sobre la tierra antes de emigrar al mar.', 'c', 20
    ],
    [
        '\n¿Qué frase explica por qué hay día y noche en la Tierra? ',
        'a) La Tierra gira alrededor de su eje.\t b) El Sol gira alrededor de su eje.\n c) El eje de la Tierra está inclinado. \t d) La Tierra gira alrededor del Sol.', 'a', 20
    ],
    [
        '\nUn autobús circula por un tramo recto de carretera. Raimundo, el conductor del autobús, tiene un vaso de agua sobre el panel de mandos. De repente, Raimundo tiene que frenar violentamente. ¿Qué es más probable que le ocurra al agua del vaso inmediatamente después de que Raimundo frene violentamente?',
        'a) El agua permanecerá horizontal.  \t b)  El agua se derramará por el lado en dirección al movimiento \n c) El agua se derramará por el lado opuesto al movimiento\t d) El agua se derramará, pero no sabes porque lado lo hará. ',
        'b', 20
    ],
    [
        '\nPara beber durante el día, Pedro tiene una taza con café caliente, a unos 90 ºC de temperatura, y una taza con agua mineral fría, a unos 5 ºC de temperatura. Las tazas son del mismo material y tamaño, y el volumen contenido en cada taza es el mismo. Pedro deja las tazas en una habitación donde la temperatura es de unos 20 ºC. ¿Cuáles serán probablemente las temperaturas del café y del agua mineral después de 10 minutos?',
        'a) 70 ºC y 10 ºC. \t b) 90 ºC y 5 ºC. \t c) 70 ºC y 25 ºC. \t d) 20 ºC y 20 ºC.', 'a', 20
    ],
    [
        '\nAceites y ceras son sustancias que se mezclan bien entre sí. El agua no se mezcla con los aceites, y las ceras no son solubles en agua. Si se vuelca mucha agua dentro de la mezcla de la barra de labios cuando se está calentando, ¿qué ocurrirá con mayor probabilidad? ',
        'a) Se producirá una mezcla más cremosa y blanda. \t b) La mezcla se hará más dura. \n c) La mezcla apenas cambiará. \t d) Grumos grasos de la mezcla flotarán sobre el agua.', 'd', 20
    ],
    [
        '\nUna astilla de mármol tiene una masa de 2,0 gramos antes de ser sumergida en vinagre durante toda una noche. Al día siguiente, la astilla se extrae y se seca. ¿Cuál será la masa de la astilla de mármol seca? ',
        'a) Menos de 2,0 gramos. \t b) Exactamente 2,0 gramos.\t c) Entre 2,0 y 2,4 gramos. \t d) Más de 2,4 gramos.', 'a', 20
    ],
    [
        '\n¿Por qué se pueden observar más estrellas en el campo que en las ciudades donde vive la mayoría de la gente?',
        'a)  La luna es más luminosa en las ciudades y amortigua la luz de muchas estrellas. \n b) Hay más polvo que refleja la luz en el aire del campo que en el aire de la ciudad. \n c) La luminosidad de las luces de la ciudad dificulta la visibilidad de las estrellas. \n d) El aire de la ciudad es más caliente por el calor que emiten los coches, las máquinas y las casas.',
        'c', 20
    ],
    [
        '\nA igual velocidad del viento, si los aerogeneradores están situados a mayor altitud, giran con mayor lentitud. Entre las razones siguientes, ¿cuál es la que mejor explica por qué las palas de los aerogeneradores giran más despacio en los lugares situados a mayor altitud, a igual velocidad del viento? ',
        'a)El aire es menos denso cuando aumenta la altitud. \n b) La temperatura es más baja cuando aumenta la altitud. \n c) La gravedad disminuye cuando aumenta la altitud. \n d) Llueve más a menudo cuando aumenta la altitud.',
        'a', 20
    ]]

nombre = input('Nombre: ')
edad = int(input('Edad: '))
if 15 <= edad <= 16:
  puntos_mate, puntos_esp, puntos_cien = main ()
  archivo = open('datos.txt', 'w')
  archivo.write(f'Estimado {nombre},\nTu edad es {edad}\nGracias por haber tomado tu pre-prueba PISA, a continuación se mostraran tus resultados\n')
  archivo.write(f' Tu puntaje en español fue de\t{puntos_esp} \n Tu puntaje en matemáticas fue de\t{puntos_mate}\n Tu puntaje en ciencias fue de\t{puntos_cien}\n')
  promedio = (puntos_mate+puntos_esp+puntos_cien)/3
  archivo.write (f'Tu promedio fue de {promedio}')
  archivo.close()

#Cambiando el modo del archivo
  archivo = open('datos.txt', 'r')
  print (archivo.read())
  archivo.close()
else:
  print('No cumples con la edad necesaria para tomar la prueba')
  quit()