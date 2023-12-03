# Advent of Code 2023
# Gabriel Teuchert

import numpy as np
import re


class mapReader:

    calibrationData = []
    calibration = 0
    digimons = []

    def __init__(self, path=None):
        self.dataPath = path
        self.readCalibrationData()
        self.calibrationDigits = self.digimonCatcher()
        self.calculateResult()

    def readCalibrationData(self):
        data = []
        with open(self.dataPath) as textData:
            for line in textData:
                data.append(line.strip())
        self.calibrationData = data
        return self.calibrationData

    def digimonCatcher(self):
        digits = []
        firstDigit = []
        secondDigit = []
        digitBuffer = []
        for index, line in enumerate(self.calibrationData):
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
                firstDigit = []
                secondDigit = []
                digitBuffer = []
            elif len(digitBuffer) != 0:
                secondDigit.append(digitBuffer.pop(-1))
                digit = firstDigit + secondDigit
                digits.append(''.join(digit))
                firstDigit = []
                secondDigit = []
                digitBuffer = []
            else:
                digits[index] = float(0)
        return digits

    def calculateResult(self):
        result = 0
        for digit in self.calibrationDigits:
            result += int(digit)
        self.calibration = result
        return result


if __name__ == '__main__':
    mR = mapReader(path='src/calibrationData.txt')
    print('Calibration Data = {0}'.format(mR.calibration))
