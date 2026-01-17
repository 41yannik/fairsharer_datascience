from fairsharer.fair_sharer import fair_sharer


def test_fair_sharer_one_iteration():
    """Test mit einer Iteration."""
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert result == [100, 800, 900, 0]


def test_fair_sharer_two_iterations():
    """Test mit zwei Iterationen."""
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert result == [100, 890, 720, 90]


def test_fair_sharer_circular():
    """Test ob zirkuläre Nachbarn funktionieren."""
    result = fair_sharer([1000, 0, 0, 0], 1)
    assert result == [800, 100, 0, 100]