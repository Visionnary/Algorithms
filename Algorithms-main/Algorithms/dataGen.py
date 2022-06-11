import random
import string


class Droid:
    def __init__(self, code, model):
        self.code = code
        self.model = model

    def __str__(self):
        return "(code: " + str(self.code) + ", " + "model: " + str(self.model) + ")"

    def __repr__(self):
        return str(self)


def generateData(size):
    newList = []
    for i in range(size):
        code = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
        model = round(random.random() * size)
        newDroid = Droid(code, model)
        newList.append(newDroid)
    return newList


