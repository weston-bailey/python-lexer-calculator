from unittest import TestCase, main
from lib.type_check import is_float, is_int

class TestTypeCheck(TestCase):
    def test_is_float(self):
        print("is_float:")
        f = 3.1415
        i = 3

        print(f"\t{f} is a type {type(f)}, should return {True}")
        self.assertTrue(is_float(f))

        print(f"\t{i} is a type {type(i)}, should return {True}")
        self.assertTrue(is_float(i))


    def test_is_int(self):
        print("is_int:")
        f = 2.7182
        i = 2

        print(f"\t{f} is a type {type(f)}, should return {True}")
        self.assertTrue(is_int(f))

        print(f"\t{i} is a type {type(i)}, should return {True}")
        self.assertTrue(is_int(i))

if __name__ == "main":
    main()