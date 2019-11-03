
from homework_shujuwajue3 import read_Apriori, remove_null, getData, showTuple, Apriori_one, Apriori_tow, Apriori_three, Apriori_four


ls = []
ls = read_Apriori()
ls = remove_null(ls)
data = getData(ls)
Apriori_one(data)#******得出相关联的项集情况
Apriori_tow(data)#******计算关联度


