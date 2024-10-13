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
