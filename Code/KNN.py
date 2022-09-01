from copy import deepcopy
from random import shuffle
from numpy import sqrt

class indiv:
    def __init__(self, label="unknown", values=None):
        self.label = label
        self.values = deepcopy(values)

class knn:
    def __init__(self, train=None, test=None):
        self.train = deepcopy(train)
        self.test = deepcopy(test)
        self.result = None
        self.matConfusion = None
        self.err = 0
    def distance(self, i):
        dist = []
        elem = self.test[i]
        for x in self.train:
            scareDist = 0
            k = 0
            for y in elem.values:
                scareDist += (y - x.values[k])**2
                k += 1
            dist.append([sqrt(scareDist), x.label])
            dist.sort()
        return dist
    def solve(self, k=10):
        result = []
        allDist = []
        classes = [{} for i in range(len(self.test))]
        for i in range(len(self.test)):
            allDist.append(self.distance(i))
        for x in range(len(self.test)):
            for y in range(k):
                tempdist = allDist[x][y][1]
                tempclass = list(classes[x].keys())
                if allDist[x][y][1] not in list(classes[x].keys()):
                    classes[x][allDist[x][y][1]] = 1
                else:
                    classes[x][allDist[x][y][1]] += 1
        #Calcul des resultats
        for i in range(len(test)):
            result.append(max(classes[i], key=lambda key: classes[i][key]))
        #Matrice de confusion
        conf = [[0 for i in range(2)] for j in range(2)]
        dicLabel = {'0': 0, '1': 1}
        for i in range(len(test)):
            x = dicLabel[result[i]]
            y = dicLabel[test[i].label]
            conf[x][y] += 1
        self.result = result
        self.matConfusion = conf
    def export(self, filename="pariente_ortega_groupeG.txt"):
        if self.result:
            f = open(filename, 'w')
            for line in self.result:
                f.write(line + "\n")
            f.close()
    def error(self):
        tot = len(self.test)
        correct = 0
        if self.matConfusion:
            for x in range(len(self.matConfusion)):
                for y in range(len(self.matConfusion)):
                    if x==y:
                        correct += self.matConfusion[x][y]
        self.err = 1-(correct/tot)
    def __str__(self):
        res = ""
        if self.matConfusion:
            for i in self.matConfusion:
                for j in i:
                    res += f"{j} "
                res += "\n"
        if self.err != 0:
            res += "\n" + "Error: " + str(round(self.err*100, 2)) + "%"
        return res

def LoadData(filename="mergeData.txt"):
    data = []
    f = open(filename)
    allRaw = f.readlines()
    f.close()
    for elem in allRaw:
        splitted = elem.split(";")
        label = splitted[10].strip()
        values = [float(x) for x in splitted[:len(splitted)-1]]
        individu = indiv(label, values)
        data.append(individu)
    return data
def LoadTrainTest(filenameTrain="data.txt", filenameTest="finalTest.txt"):
    train = []
    test = []
    fTrain = open(filenameTrain)
    rawTrain = fTrain.readlines()
    fTrain.close()
    fTest = open(filenameTest)
    rawTest = fTest.readlines()
    fTest.close()
    for elem in rawTrain:
        splitted = elem.split(";")
        label = splitted[10].strip()
        values = [float(x) for x in splitted[:len(splitted)-1]]
        individu = indiv(label, values)
        train.append(individu)
    for elem in rawTest:
        splitted = elem.split(";")
        values = [float(x) for x in splitted]
        individu = indiv(label, values)
        test.append(individu)
    return train, test
def MergeRes(filenameTest="finalTest.txt", filenameRes="pariente_ortega_groupeG.txt"):
    train = []
    test = []
    final = []
    fTest = open(filenameTest)
    rawTest = fTest.readlines()
    fTest.close()
    fRes = open(filenameRes)
    rawRes = fRes.readlines()
    fRes.close()
    k=0
    for line in rawTest:
        final.append(line.rstrip('\n') + ";" + rawRes[k])
        k += 1
    f = open("finalMerged.txt", 'w')
    for line in final:
        f.write(line)
    f.close()
def Splitter(allData):
    train = []
    test = []
    shuffle(allData)
    k = 0
    for x in allData:
        if k % 3 == 0:
            test.append(x)
        else:
            train.append(x)
        k+=1
    return train, test

if __name__ == '__main__':
    action = "test"
    if action == "train":
        data = LoadData("preTest.txt")
        train, test = Splitter(data)
        problem = knn(train, test)
        problem.solve()
        problem.error()
        problem.export()
        print(problem)
    elif action == "merge":
        MergeRes()
        print("Merge terminé")
    elif action == "test":
        train, test = LoadTrainTest()
        problem = knn(train, test)
        problem.solve()
        problem.export()
        MergeRes()
        print("Test terminé")