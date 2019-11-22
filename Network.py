class Network:
    __layers: list
    __weights: list

    def __init__(self, structure: list):
        self.__layers = []
        for layer in structure:
            self.__layers.append(list(0 for i in range(len(layer))))

    def getLayers(self):
        return self.__layers

    def getWeights(self):
        return self.__weights

