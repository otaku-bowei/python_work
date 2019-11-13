import sys

def readFile(File = 'Bayes.csv'):
    filename = File
    fo = open(filename)
    ls = []
    for line in fo:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    fo.close()
    return ls

def getJudgeP(dataSet):
    ls = [example[-1] for example in dataSet]
    dic = {}
    for example in ls:
        if example not in dic.keys():
            dic[example] = 0
        dic[example] += 1
    return dic #返回结果的特征种类以及各个种类的个数

def selectResult(dataSet , result):#根据需要的结果截取出结果一样的数据集
    ls = []
    for example in dataSet:
        if example[-1] == result:
            ls.append(example)
    return ls

def getP(dataSet , attributeIndex , value , result):#获取某个结果对应某个特征的概率
    ls = selectResult(dataSet , result)
    count = 0.0
    for example in ls:
        if example[attributeIndex] == value:
            count += 1
    P = count / len(ls)
    return P

def preview(conditionSet , dataSet):#根据条件和数据集的概率得出结果
    dic = getJudgeP(dataSet)
    sum = 0
    for key in dic:
        sum += dic[key]
    #求得总和
    result = ""
    flagP = 0.0
    for key in dic:#扫描比较看哪个结果的概率最大
        P = dic[key] / sum
        index = 0
        for value in  conditionSet:#扫描数据集得出结果概率
            P *= getP(dataSet , index , value , key )
            index += 1
        if P > flagP:
            flagP = P
            result = key
    return result

def main():
    dataSet = readFile()
    conditionLs = []
    while len(conditionLs) != 1:
        string = input()
        conditionLs = string.split(",")
        print("the result is : ")
        print( preview(conditionLs , dataSet))


if __name__ == '__main__':
    main()  # 创造示列数据
