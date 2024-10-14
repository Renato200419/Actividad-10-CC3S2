from behave import given, when, then
import re
import random

# Función para convertir palabras numéricas a números (español e inglés)
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            #Números en español
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5,

            #Números en inglés
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
            "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
            "eighty": 80, "ninety": 90, "half": 0.5
        }
        return numeros.get(palabra.lower(), 0)

@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        cukes = float(cukes)
        context.belly.comer(cukes)
    except ValueError as e:
        context.error_message = str(e)

@given('tengo un total de {total_pepinos} pepinos')
def step_given_total_cukes(context, total_pepinos):
    context.total_pepinos = float(total_pepinos)



@when('espero un tiempo aleatorio entre {min_time} y {max_time} horas')
def step_when_wait_random_time(context, min_time, max_time):
    # Convertimos los tiempos mínimos y máximos
    min_time = float(min_time)
    max_time = float(max_time)

    # Generamos un tiempo aleatorio entre el mínimo y el máximo
    random_time = random.uniform(min_time, max_time)
    print(f"\033[96mTiempo aleatorio generado: {random_time:.2f} horas\033[0m")

    # Esperamos ese tiempo
    context.belly.esperar(random_time)
    


@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    try:
        # Intentamos convertir el tiempo directamente si es un número simple como "10 hours"
        total_time_in_hours = float(time_description)
    except ValueError:
        # Si no es un número simple, aplicamos la lógica actual
        time_description = time_description.strip('"').lower()
        time_description = time_description.replace('y', ' ').replace('and', ' ').replace(',', '')
        time_description = time_description.strip()

    # Manejar casos especiales como 'media hora' o 'half hour'
    if time_description in ['media hora', 'half hour']:
        total_time_in_hours = 0.5
    else:
        # Expresión regular para extraer horas, minutos y segundos  en español e inglés
        # pattern = re.compile(r'(?:(\w+)\s*(?:horas?|hours?))?\s*(?:(\w+)\s*(?:minutos?|minutes?))?\s*(?:(\w+)\s*(?:segundos?|seconds?))?')
        pattern = re.compile(r'(?:(\d+(?:\.\d+)?)\s*(?:horas?|hours?))?\s*(?:(\d+)\s*(?:minutos?|minutes?))?\s*(?:(\d+)\s*(?:segundos?|seconds?))?')
        match = pattern.fullmatch(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = float(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@when('pregunto cuántos pepinos más puedo comer')
def step_when_ask_how_many_more_cukes(context):
    context.pepinos_mas = context.belly.pepinos_mas_puedo_comer()

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería ocurrir un error de cantidad negativa')
def step_then_should_raise_error(context):
    assert context.error_message == "La cantidad de pepinos debe ser positiva.", f"Error esperado no ocurrió, mensaje recibido: {context.error_message}"

@then('debería ocurrir un error de cantidad extremadamente alta')
def step_then_should_raise_high_error(context):
    assert context.error_message == "No puedes comer más de 100 pepinos a la vez.", f"Error esperado no ocurrió, mensaje recibido: {context.error_message}"

@then('deberían quedar {expected_restantes} pepinos')
def step_then_should_have_remaining_cukes(context, expected_restantes):
    expected_restantes = float(expected_restantes)
    restantes = context.belly.pepinos_restantes(context.total_pepinos)
    assert restantes == expected_restantes, f"Se esperaban {expected_restantes} pepinos restantes, pero quedan {restantes}."

@then('debería decirme que puedo comer {expected_pepinos_mas} pepinos más')
def step_then_should_tell_how_many_more(context, expected_pepinos_mas):
    expected_pepinos_mas = int(expected_pepinos_mas)
    assert context.pepinos_mas == expected_pepinos_mas, f"Se esperaban {expected_pepinos_mas} pepinos más, pero el sistema dijo {context.pepinos_mas}."