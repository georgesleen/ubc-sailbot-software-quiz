from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_basic2():
    assert bound_to_180(135) == 135


def test_bound_intervals1():
    assert bound_to_180(-180) == -180
    assert bound_to_180(180) == -180


def test_bound_out_one_revolution():
    assert bound_to_180(200) == -160
    assert bound_to_180(-200) == 160


def test_bound_out_multiple_revolutions():
    assert bound_to_180(760) == 40
    assert bound_to_180(-1100) == -20


def test_bound_intervals2():
    assert bound_to_180(-720 - 180) == -180
    assert bound_to_180(360 + 180) == -180


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_basic2():
    assert is_angle_between(0, -1, -2)
    assert not is_angle_between(0, 2, 1)


def test_between_docstring_definition():
    assert is_angle_between(0, 45, 90)
    assert not is_angle_between(45, 90, 270)


def test_between_multiple_revolutions():
    assert is_angle_between(90, -180 - 45, 180 + 360)
    assert is_angle_between(-90, 180, 135 + 720)
    assert not is_angle_between(45, 180, 135 + 360)


def test_between_ambiguous_no_reflex_case():
    # With no larger angle, I argue there is no reflex angle
    # and thus this ambiguous case should resolve to true
    # (if the docstring is not to be updated)
    assert is_angle_between(0, 90, 180)
    assert is_angle_between(0, -90, 180)
    assert is_angle_between(0, 90, -180)


def test_between_angle_on_bounds():
    assert not is_angle_between(0, 0, 90)
    assert not is_angle_between(0, 180, 180)
