# Advent of Code 2023
# Gabriel Teuchert

import numpy as np


class mapReader:

    calibrationData = []
    calibrationResult = 0
    digimons = []
    pokemons = []
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def __init__(self, path=None):
        self.dataPath = path
        self.readCalibrationData()
        self.digimonCatcher()
        self.calibrationResult = self.calculateResult()

    def readCalibrationData(self):
        data = []
        with open(self.dataPath) as textData:
            for line in textData:
                data.append(line.strip())
        self.calibrationData = data
        return self.calibrationData

    def digimonCatcher(self):
        digits = []
        for index, line in enumerate(self.calibrationData):
            firstDigit = []
            secondDigit = []
            digitBuffer = []
            element = list(line)
            for character in element:
                if character.isdigit() is True:
                    if len(firstDigit) == 0:
                        firstDigit.append(character)
                    else:
                        digitBuffer.append(character)
            if len(digitBuffer) == 0:
                digit = firstDigit + firstDigit
                digits.append(''.join(digit))
            elif len(digitBuffer) != 0:
                secondDigit.append(digitBuffer.pop(-1))
                digit = firstDigit + secondDigit
                digits.append(''.join(digit))
            else:
                digits[index] = float(0)
            self.digimons = list(map(int, digits))
        return digits

    def calculateResult(self):
        result = 0
        if len(self.digimons) != 0:
            for digit in self.digimons:
                result += int(digit)
        else:
            for digit in self.pokemons:
                result += int(digit)
        self.calibrationResult = result
        return result

    def pokemonCatcher(self):
        pokemon = np.zeros(2)
        result = []
        for dataIndex, string in enumerate(self.calibrationData):
            # Check for digits
            for digit in self.digits:
                if digit in string:
                    pokemon = dataIndex, int(digit)
                    result.append(pokemon)
            # Check for spelled numbers
            for index, spelled_num in enumerate(self.spelled_numbers):
                if spelled_num in string:
                    pokemon = dataIndex, int(index)+1
                    result.append(pokemon)
        self.pokemons = result
        return pokemon


if __name__ == '__main__':
    mR = mapReader(path='src/calibrationData.txt')
    print('Calibration Data = {0}'.format(mR.calibrationResult))
