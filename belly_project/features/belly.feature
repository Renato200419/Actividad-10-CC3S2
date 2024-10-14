# language: es

Característica: Característica del Estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir

  Escenario: Esperar usando minutos en inglés
    Dado que he comido 40 pepinos
    Cuando espero "4 hours"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir

  Escenario: Manejar una cantidad no válida de pepinos (cantidad negativa)
    Dado que he comido -5 pepinos
    Entonces debería ocurrir un error de cantidad negativa

  Escenario: Manejar una cantidad no válida de pepinos (cantidad extremadamente alta)
    Dado que he comido 150 pepinos
    Entonces debería ocurrir un error de cantidad extremadamente alta

@grandes-cantidades
  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

@complejos
  Escenario: Manejar tiempos complejos
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

@ejercicio_8
Escenario: Comer muchos pepinos y esperar el tiempo suficiente
   Dado que he comido 15 pepinos
   Cuando espero 2 horas
   Entonces mi estómago debería gruñir

  @critico
  Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @critico
  Escenario: Comer pocos pepinos y no esperar suficiente tiempo
    Dado que he comido 5 pepinos
    Cuando espero 1 hora
    Entonces mi estómago no debería gruñir

  @pepinos-restantes
  Escenario: Saber cuántos pepinos he comido y cuántos quedan
    Dado que he comido 15 pepinos
    Y tengo un total de 20 pepinos
    Entonces deberían quedar 5 pepinos

  @estomago-gruñendo
  Escenario: Verificar que el estómago gruñe después de comer suficientes pepinos y esperar el tiempo correcto
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir
