import numpy as np
import DataItem
import Network

def generateData(paramsNumber, size) -> list:
    inputs = []
    muArray = list(6 * np.random.rand() - 3 for j in range(paramsNumber))
    sigmaArray = np.ones(paramsNumber)

    for j in range(size):
        tmp = list(np.random.normal(muArray[i], sigmaArray[i]) for i in range(paramsNumber))
        inputs.append(tmp)

    return inputs

# inputs = []
# outputs = []
#
# n = 3
# m = 2
#
# muArray = np.array(list(list(6*np.random.rand() - 3 for j in range(m)) for i in range(n)))
#
# sigmaArray = np.array(list(np.ones(m) for x in range(n)))
#
# data = []
#
# for i in range(n):
#     for n in range(10):
#         tmp = list(np.random.normal(muArray[i][j], sigmaArray[i][j]) for j in range(m))
#         inputs.append(tmp)
#         outputs.append(i)
#
# print(muArray)
# print(sigmaArray)
# print(np.array(inputs))
# print(np.array(outputs))



data = generateData(3, 10)

# print(data)

dataSet = DataItem.DataItem.createDataSet(data, list(1 for i in range(len(data))))

# print(dataSet[1].getInput())

net = Network.Network([3, 4, 3])