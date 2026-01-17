def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    
    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.
    
    Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args:
        values: 1D array of values (list or numpy array)
        num_iterations: Integer to set the number of iterations
        share: Fraction to give to each neighbor (default 0.1)
    
    Returns:
        List with redistributed values
    """
    # 1. Kopie der Liste erstellen
    values_new = list(values)
    
    # 2. Wiederhole num_iterations mal
    for _ in range(num_iterations):
        # Finde den Index des höchsten Wertes
        max_index = values_new.index(max(values_new))
        
        # Berechne den Anteil, der abgegeben wird
        amount = values_new[max_index] * share
        
        # Ziehe 2x den Anteil vom höchsten Wert ab (einmal für links, einmal für rechts)
        values_new[max_index] -= 2 * amount
        
        # Gib den Anteil an den linken Nachbarn (mit Modulo für zirkulär)
        left_index = (max_index - 1) % len(values_new)
        values_new[left_index] += amount
        
        # Gib den Anteil an den rechten Nachbarn (mit Modulo für zirkulär)
        right_index = (max_index + 1) % len(values_new)
        values_new[right_index] += amount
    
    return values_new