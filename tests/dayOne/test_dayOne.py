# Gabriel Teuchert

import unittest
from main import mapReader as mR


test_calibrationData = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
test_digimon = [12, 38, 12345, 7]
test_digits = [12, 38, 15, 77]
test_resultDigimon = 142
test_resultPokemon = 281
test_pokemon = [29, 83, 13, 24, 42, 14, 76]


class test_classDayOne(unittest.TestCase):

    def test_Reader(self):
        calibrationData = mR(path="exampleInput.txt")
        self.assertEquals(calibrationData.readCalibrationData(), test_calibrationData, 'The reading went wrong')

    def test_DigimonCatcher(self):
        digimons = mR(path="exampleInput.txt")
        self.assertEquals(digimons.digimons, test_digits, 'The Digimons are escalating')

    def test_result(self):
        calibration = mR(path="exampleInput.txt")
        self.assertEquals(calibration.calculateResult(), test_resultDigimon, 'Result is incorrect')

    def test_PokemonCatcher(self):
        pokemon = mR(path="exampleInput2.txt")
        self.assertEquals(pokemon.calculateResult(), test_resultPokemon, 'You gotta catch`em all!!')


if __name__ == "__main__":
    unittest.main()
