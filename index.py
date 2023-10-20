#Ejercicio1
story="""Hace dos décadas, Javier, un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA, a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad."""
longitud=len(story)
print("La longitud es ",longitud)

#Ejercicio2
year = 2025 
years_left = 2045 
total_years = years_left - year
print("Number of years left:", total_years)

#Ejercicio3
year = 2025 
years_left = 2045 
total_years = years_left - year
total_days=total_years*365
print("Los dias que quedan son:" ,total_days,"dias") 

#Ejercicio4
text="""Hace dos décadas, Javier, un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA , a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad.""" 
story=False
if "IA" in text:
 story=True
if story: 
 print("Contiene la palabra IA")
else:
 print("No contiene la palabra IA")

#Ejercicio5
text="""Hace dos décadas, Javier, un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA , a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad.""" 
texto=text.split()
lista=list(texto)
print("Las diez primeras palabras son: ",lista[:10])

#Ejercicio6
text="""Hace dos décadas, Javier, un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA , a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad.""" 
texto=text.split()
lista=list(texto)
print("Las diez ultimas palabras son: ",lista[-10:])

#Ejercicio7
text="""Hace dos décadas, Javier, un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA , a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad.""" 
texto=text.split()
lista=list(texto)
print("Las palabas son: ",lista[10:20])

#Ejercicio8
text="""Hace dos décadas, Javier , un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA , a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad.""" 
texto=text.split()
palabra= "Javier"
javier_count= text.count(palabra)
print("Esta repetida",javier_count,"veces")

#Ejercicio9
text="""Hace dos décadas,Javier , un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA , a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad.""" 
texto=text.replace("Javier", "Pepito")
print(texto)

#Ejercicio10
text="""Hace dos décadas,Javier , un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA , a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.
Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad.""" 
texto=list(text)
texto=text.split()
print(texto[::-1])

#Ejercicio10

