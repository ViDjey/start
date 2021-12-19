import yrdif


class TestKvadryp:
    def test_ur__1_7_8(self):
        assert yrdif.kvadryp(-1, 7, 8) == (-1.0, 8.0)

    def test_ur_4_4_1(self):
        assert yrdif.kvadryp(4, 4, 1) == -0.5
        
    def test_ur_2_2_1(self):
        assert yrdif.kvadryp(2, 2, 1) == ((-0.49999999999999994+0.5j), (-0.5-0.5j))