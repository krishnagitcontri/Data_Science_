# @author: 22000214 - Abhiraj Chaudhuri
# @description: Program No. 5. Given this nested dictionary grab the word "hello".
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

def find_hello(d):
    target_word = d["kl"][3]["tricky"][3]["target"][3]
    return target_word

d = {"kl": [1,2,3,{"tricky": ["oh", "man", "inception", {"target": [1, 2, 3, "hello"]}]}]}
result = find_hello(d)
print(result)

# output: hello