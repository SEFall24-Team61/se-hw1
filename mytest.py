from fileForTest import func

def test_fail():
    assert func(3) == 5

def test_pass():
    assert func(3) == 4
