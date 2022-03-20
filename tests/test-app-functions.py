from src.app import calculate_daily_return


def test_positve_return():
    assert calculate_daily_return(349, 360) > 0
    assert calculate_daily_return(349, 360) == 3.15


def test_negative_return():
    assert calculate_daily_return(349, 340) < 0
    assert calculate_daily_return(349, 340) == -2.58


def test_zero_return():
    assert calculate_daily_return(349, 349) == 0
