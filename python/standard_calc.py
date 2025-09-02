FULL_REVOLUTION_DEGREES: int = 360
HALF_REVOLUTION_DEGREES: int = 180


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
    bounded_angle = (
        angle + HALF_REVOLUTION_DEGREES
    ) % FULL_REVOLUTION_DEGREES - HALF_REVOLUTION_DEGREES
    return bounded_angle


def is_angle_between(
    first_angle: float, middle_angle: float, second_angle: float
) -> bool:
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
    first_angle = bound_to_180(first_angle)
    middle_angle = bound_to_180(middle_angle)
    second_angle = bound_to_180(second_angle)

    if (middle_angle == first_angle) or (middle_angle == second_angle):
        # Ambiguous case where the angle compared is on one of the existing angles
        # I have chosen to return false when this occurs
        return False
    elif abs(first_angle - second_angle) == HALF_REVOLUTION_DEGREES:
        # Ambiguous case where there the "reflex" angle is the same size
        # I choose to return true when it exists between either angle
        return True
    else:
        angular_sweep = bound_to_180(second_angle - first_angle)
        middle_relative_position = bound_to_180(middle_angle - first_angle)

        if angular_sweep > 0:
            # Arc sweeps counter-clockwise
            return 0 < middle_relative_position < angular_sweep
        else:
            # Arc sweeps clockwise
            return 0 > middle_relative_position > angular_sweep
