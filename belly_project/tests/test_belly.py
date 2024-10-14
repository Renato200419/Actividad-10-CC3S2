import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from belly import Belly

def test_grunir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_restantes(20) == 5, "Se esperaban 5 pepinos restantes."
