"""
run the main app
"""
from .harmonic_resonance import Harmonic_resonance


def run() -> None:
    reply = Harmonic_resonance().run()
    print(reply)
