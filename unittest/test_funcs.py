from basic_funcs import is_even_or_odd, calc_mean, find_max

def test_is_even_or_odd():
    assert True == is_even_or_odd(2)
    assert False == is_even_or_odd(3)
    assert True == is_even_or_odd(0)

def test_calc_mean():
    assert 3 == calc_mean([3])
    assert None == calc_mean([])
    assert 2.5 == calc_mean([1,2,3,4])

def test_find_max():
    assert None == find_max([])
    assert 7 == find_max([-1, 2, 5, 7])
    assert -3 == find_max([-3])