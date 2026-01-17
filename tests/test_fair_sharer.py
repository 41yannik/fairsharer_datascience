# Test-Datei für die fair_sharer Funktion
from fairsharer.fair_sharer import fair_sharer


def test_fair_sharer():
    """Testet die Beispiele aus der Aufgabenstellung."""
    # Test mit einer Iteration
    ergebnis1 = fair_sharer([0, 1000, 800, 0], 1)
    assert ergebnis1 == [100, 800, 900, 0]
    
    # Test mit zwei Iterationen
    ergebnis2 = fair_sharer([0, 1000, 800, 0], 2)
    assert ergebnis2 == [100, 890, 720, 90]


def test_fair_sharer_zirkulaer():
    """Testet ob das erste und letzte Element Nachbarn sind."""
    ergebnis = fair_sharer([1000, 0, 0, 0], 1)
    assert ergebnis == [800, 100, 0, 100]