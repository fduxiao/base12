import unittest
import numpy as np
from base12 import b12encode, b12decode


class TestEncodingDecoding(unittest.TestCase):

    def test_encoding_decoding(self):
        r = np.random.bytes(np.random.randint(5, 10))
        r1 = b12encode(r)
        r2 = b12decode(r1)
        r3 = b12encode(r2)
        self.assertEqual(r, r2)
        self.assertEqual(r1, r3)


if __name__ == '__main__':
    unittest.main()
