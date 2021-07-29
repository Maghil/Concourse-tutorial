from sub import Sub

def test_sub_two():
    s=Sub()
    assert s.sub_two(3,5) == -2

def test_sub_three():
    s=Sub()
    assert s.sub_three(3,5,1) == -3    