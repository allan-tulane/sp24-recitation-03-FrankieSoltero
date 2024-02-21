from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3*4
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(5)) == 5*5
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(7)) == 7*7
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10
    assert quadratic_multiply(BinaryNumber(100), BinaryNumber(100)) == 100*100
    assert quadratic_multiply(BinaryNumber(1000), BinaryNumber(1000)) == 1000*1000