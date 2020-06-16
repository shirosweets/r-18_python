# r-18_python

Realice el análisis, diseño y codificación de un algoritmo que solicite el sueldo de un trabajador, los años de antigüedad que lleva en la empresa y el estamento al que pertenece (1: Obrero, 2: Administrativo y 3: Directivo). Considere que al trabajador se le entrega un bono según las siguientes reglas:

•	Trabajadores con hasta 3 años de antigüedad bono igual al 15% del sueldo.

•	Trabajadores con hasta 6 años de antigüedad bono igual al 20% del sueldo para Obreros y Administrativos, y 25% del sueldo para Directivos.

•	Trabajadores con más de 6 años de antigüedad bono igual al 30% del sueldo para Obreros, 35% del sueldo para Administrativos y 40% del sueldo para Directivos.

Además del bono que le corresponde al trabajador, el algoritmo debe mostrar el monto a descontar por salud que es de un 7% del sueldo, el monto a descontar por previsión que es de un 10% del sueldo y el monto final que se le debe pagar (sueldo líquido) considerando los descuentos anteriores y el bono que se le entrega (el monto del bono que se le entrega está libre de todo descuento).

-------------------------------------------------------------------------------------------------------------------
### 1) Enunciado: ¿Qué hace el programa?
El programa solicita 3 datos (sueldo, años de servicios y estamento) que los utiliza para descontar salud y previsión al trabajador, según su estamento y años de servicio, al sueldo del mismo. También muestra el bono que debe recibir, y este se suma al sueldo
### 2) Análisis: ¿? Entrada, Algoritmo, Salida
Entrada: sueldo, años de servicio y estamento.
Algoritmo:
Salida: bono, descuento por salud, descuento por previsión y sueldo final.
### 3) Diseño: ¿Cómo lo implementaría?
Solicito 3 datos que serían el sueldo, años de servicio y estamento del trabajador. Creo 2 variables para guardar los descuentos y los asigno. Creo el bono, que se le asigna el valor según los años de servicio y estamento. Al sueldo le resto los descuentos y le sumo el bono. Finalmente, muestro los datos del bono, descuentos y el sueldo final.
### 4) Implementación y prueba (Codificar el diseño en python).  [Enviar el programa ya probado que compila]
-------------------------------------------------------------------------------------------------------------------
