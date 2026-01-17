from fairsharer.fair_sharer import fair_sharer

# Test-Datei für die fair_sharer Funktion

def test_eine_iteration():
    """Testet das Beispiel aus der Aufgabenstellung mit einer Iteration."""
    ergebnis = fair_sharer([0, 1000, 800, 0], 1)
    erwartet = [100, 800, 900, 0]
    assert ergebnis == erwartet


def test_zwei_iterationen():
    """Testet das Beispiel aus der Aufgabenstellung mit zwei Iterationen."""
    ergebnis = fair_sharer([0, 1000, 800, 0], 2)
    erwartet = [100, 890, 720, 90]
    assert ergebnis == erwartet


def test_zirkulaere_nachbarn():
    """Testet ob das erste und letzte Element korrekt als Nachbarn behandelt werden."""
    ergebnis = fair_sharer([1000, 0, 0, 0], 1)
    erwartet = [800, 100, 0, 100]
    assert ergebnis == erwartet