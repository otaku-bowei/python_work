from math import log
import operator

def calcShannonEnt(dataSet):  # 计算数据的熵(entropy)
    numEntries=len(dataSet)  # 数据条数
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1] # 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1  # 统计有多少个类以及每个类的数量
    shannonEnt=0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries # 计算单个类的熵值
        shannonEnt-=prob*log(prob,2) # 累加每个类的熵值
    return shannonEnt


def readFile(file_name="C4.5.csv"):
    fname = file_name
    fo = open(fname)
    ls = []
    for line in fo:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    fo.close()
    return ls

def createDataSet1():    # 创造示例数据
    dataSet = readFile()
    labels = ["[=性别=]" , "[=学生干部=]" , "[=综合成绩=]" , "[=毕业论文=]"]
    return dataSet,labels

def splitDataSet(dataSet,axis,value): # 按某个特征分类后的数据
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec =featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):  # 选择最优的分类特征
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)  # 原始的熵
    bestGainRatio = 0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:#某属性中的每个特征
            subDataSet = splitDataSet(dataSet,i,value)
            prob =len(subDataSet)/float(len(dataSet))
            newEntropy +=prob*calcShannonEnt(subDataSet)  # 按特征分类后的熵
        infoGain = baseEntropy - newEntropy  # 原始熵与按特征分类后的熵的差值

        # //C4.5添加：{
        sliptDict = {}
        slipt_Info = 0.0
        for key in featList:
            if key not in sliptDict.keys():
                sliptDict[key] = 0
            sliptDict[key] += 1
        for key in sliptDict:
            prob = sliptDict[key] / float(len(featList))
            slipt_Info -= prob*log(prob,2)
        if slipt_Info == 0:#当该数=0时，是剩下一个特征
            bestFeature = i
            break
        gainRatio = infoGain / slipt_Info

        # }
        if (gainRatio>bestGainRatio):   # 若按某特征划分后，熵值减少的最大，则此特征为最优分类特征
            bestGainRatio=gainRatio
            bestFeature = i
    return bestFeature

def majorityCnt(classList):    #按分类后类别数量排序，比如：最后分类为2男1女，则判定为男；
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):

    classList=[example[-1] for example in dataSet]

    #2样本同属于一类
    if classList.count(classList[0])==len(classList):
        return classList[0]
    # #3某个属性只剩下最后一条时，返回结果
    # if len(classList) == 1:
    #     return classList[0]
    #7样本子集为0
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    #4计算信息增益率，选择测试属性
    bestFeat=chooseBestFeatureToSplit(dataSet) #选择最优特征
    #5取测试属性
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}} #分类结果以字典形式保存
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    #7继续分裂
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


if __name__=='__main__':
    dataSet, labels=createDataSet1()  # 创造示列数据
    print(createTree(dataSet, labels))  # 输出决策树模型结果
