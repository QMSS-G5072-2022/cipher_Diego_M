from cipher_dm3760 import cipher_dm3760
import pytest
    
def test_cipher_function_1a():
    example = 'Hello'
    expected = 'Khoor'
    actual = cipher(example, 3)
    assert actual == expected
