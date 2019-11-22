class DataItem:
    __input: list
    __output: list

    def __init__(self, input, output):
        self.__input = input
        self.__output = output

    def getInput(self):
        return self.__input

    def getOutput(self):
        return self.__output

    @staticmethod
    def createDataSet(inputs, outputs):
        if len(inputs) != len(outputs):
            raise Exception('length of inputs and outputs are not equals')
        dataSet = []
        for i in range(len(inputs)):
            dataItem = DataItem(inputs[i], outputs[i])
            dataSet.append(dataItem)
        return dataSet
