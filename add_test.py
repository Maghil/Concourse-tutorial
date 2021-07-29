from add import Add

def test_add():
    s=Add()
    assert s.add_two(3,5) == 8

def test_sub_three():
    s=Add()
    assert s.add_three(3,5,1) == 9