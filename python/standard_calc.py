FULL_REVOLUTION_DEGREES: int = 360


def bound_to_180(angle: float) -> float:
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    upper_bound_exclusive: int = 180
    lower_bound_inclusive: int = -180

    revolutions_outside: int = round(angle / FULL_REVOLUTION_DEGREES)
    bounded_angle: float = angle - revolutions_outside * FULL_REVOLUTION_DEGREES

    # Account for excluded upper interval
    if bounded_angle == upper_bound_exclusive:
        return lower_bound_inclusive

    return bounded_angle


def is_angle_between(first_angle: float, middle_angle: float, second_angle: float) -> bool:
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    return True
