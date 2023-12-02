# Advent of Code 2023
# Gabriel Teuchert

import numpy as np


class mapReader:

    calibrationData = []
    digimons = []

    def __init__(self, path=None):
        self.dataPath = path
        self.readCalibrationData()
        self.calibration = int(sum(self.digimonCatcher()))

    def readCalibrationData(self):
        data = []
        with open(self.dataPath) as textData:
            for line in textData:
                data.append(line.strip())
        self.calibrationData = data
        return self.calibrationData

    def digimonCatcher(self):
        digits = np.zeros(len(self.calibrationData))
        firstDigit = []
        secondDigit = []
        digitBuffer = []
        for index, line in enumerate(self.calibrationData):
            digimons = ''.join((digimon if digimon in '0123456789' else ' ') for digimon in line)
            listOfNumbers = digimons.split()
            for element in listOfNumbers:
                if len(firstDigit) == 0:
                    firstDigit.append(element)
                else:
                    digitBuffer.append(element)
            if len(digitBuffer) == 0:
                digit = firstDigit + firstDigit
                digits[index] = float(''.join(digit))
                firstDigit = []
                secondDigit = []
                digitBuffer = []
            elif len(digitBuffer) != 0:
                secondDigit.append(digitBuffer.pop(-1))
                digit = firstDigit + secondDigit
                digits[index] = float(''.join(digit))
                firstDigit = []
                secondDigit = []
                digitBuffer = []
            else:
                digits[index] = float(0)

        return digits


if __name__ == '__main__':
    mR = mapReader(path='src/calibrationData.txt')
    print('Calibration Data = {0}'.format(mR.calibration))
