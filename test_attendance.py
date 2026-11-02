import pytest
from attendance import calculate_attendance


def test_full_attendance():
    assert calculate_attendance(20, 20) == 100.0


def test_partial_attendance():
    result = calculate_attendance(15, 20)
    assert result == 75.0


def test_zero_classes_attended():
    assert calculate_attendance(0, 20) == 0.0


def test_zero_total_raises():
    with pytest.raises(ValueError):
        calculate_attendance(0, 0)


def test_negative_attended_raises():
    with pytest.raises(ValueError):
        calculate_attendance(-1, 20)


def test_attended_exceeds_total_raises():
    with pytest.raises(ValueError):
        calculate_attendance(25, 20)


@pytest.mark.parametrize("attended,total,expected", [
    (10, 20, 50.0),
    (18, 20, 90.0),
    (1, 4, 25.0),
    (3, 3, 100.0),
])
def test_parametrized_attendance(attended, total, expected):
    assert calculate_attendance(attended, total) == expected
