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
