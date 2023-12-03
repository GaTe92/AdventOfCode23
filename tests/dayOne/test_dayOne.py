# Gabriel Teuchert

import unittest
from main import mapReader as mR


test_calibrationData = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
test_digimon = [12, 38, 12345, 7]
test_digits = [12, 38, 15, 77]
test_result = 142


class test_classDayOne(unittest.TestCase):

    def testReader(self):
        calibrationData = mR(path="exampleInput.txt")
        self.assertEquals(calibrationData.readCalibrationData(), test_calibrationData, 'The reading went wrong')

    def test_DigimonCatcher(self):
        digimons = mR(path="exampleInput.txt")
        self.assertEquals(digimons.digimonCatcher().tolist(), test_digits, 'The Digimons are escalating')

    def test_result(self):
        calibration = mR(path="exampleInput.txt")
        self.assertEquals(calibration.calculateResult(), test_result, 'Result is incorrect')


if __name__ == "__main__":
    unittest.main()
