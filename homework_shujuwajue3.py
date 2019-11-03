from pymining import itemmining, assocrules, perftesting, seqmining



def read_Apriori(file_name="Apriori.csv"):
    fname = file_name
    fo = open(fname)
    ls = []
    for line in fo:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    fo.close()
    return ls

#将二次列表中的空值去掉
def remove_null(ls):
    for i in ls:
        index = 0
        for j in range(len(i)):
            if i[j] == "":
                del i[j:]
                break
    return ls

def getData(ls):
    tuple_ = ()
    data_tuple = (())
    for i in range(len(ls)):
        tuple_= tuple(ls[i])
        data_tuple = data_tuple + (tuple_,)
    return data_tuple



def showTuple(data_tuple):
    for i in range(len(data_tuple)):
        print(data_tuple[i])

def Apriori_one(data_tuple):
    relim = itemmining.get_relim_input(data_tuple)
    report = itemmining.relim(relim, min_support=100)# //最小关联度
    print(report)


def Apriori_tow(data_tuple):
    transactions = data_tuple
    relim_input = itemmining.get_relim_input(transactions)
    item_sets = itemmining.relim(relim_input, min_support=100)
    rules = assocrules.mine_assoc_rules(item_sets, min_support=100, min_confidence=0.5)
    print(rules)



def Apriori_three(data_tuple):
    transactions = perftesting.get_default_transactions()
    relim_input = itemmining.get_relim_input(transactions)
    item_sets = itemmining.relim(relim_input, min_support=50)#////最小关联度
    rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.5)
    print(rules)

def Apriori_four(data_tuple):
    seqs = ('caabc', 'abcb', 'cabc', 'abbca')
    freq_seqs = seqmining.freq_seq_enum(seqs, 2)
    print( sorted(freq_seqs) )