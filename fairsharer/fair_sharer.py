def fair_sharer(values, num_iterations, share=0.1):
    """
    Verteilt Werte über mehrere Iterationen um.
    
    In jeder Iteration gibt der höchste Wert einen Anteil (share)
    an beide Nachbarn ab. Das erste und letzte Element sind
    ebenfalls Nachbarn (zirkulär).
    
    Beispiele:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Parameter:
        values: Liste mit Werten
        num_iterations: Anzahl der Durchläufe
        share: Anteil der abgegeben wird (Standard: 0.1 = 10%)
    
    Rückgabe:
        Liste mit neu verteilten Werten
    """
    # Kopie erstellen, damit Original nicht verändert wird
    ergebnis = list(values)
    
    # Hauptschleife: so oft wiederholen wie gewünscht
    for i in range(num_iterations):
        # Höchsten Wert und dessen Position finden
        hoechster_wert = max(ergebnis)
        position = ergebnis.index(hoechster_wert)
        
        # Berechnen wie viel abgegeben wird
        abgabe = hoechster_wert * share
        
        # Vom höchsten Wert abziehen (2x, weil links und rechts)
        ergebnis[position] = ergebnis[position] - (2 * abgabe)
        
        # An linken Nachbarn geben
        # Modulo sorgt dafür, dass nach Index 0 der letzte Index kommt
        links = (position - 1) % len(ergebnis)
        ergebnis[links] = ergebnis[links] + abgabe
        
        # An rechten Nachbarn geben
        # Modulo sorgt dafür, dass nach dem letzten Index wieder 0 kommt
        rechts = (position + 1) % len(ergebnis)
        ergebnis[rechts] = ergebnis[rechts] + abgabe
    
    return ergebnis