# @author: 22000214 - Abhiraj Chaudhuri
# @description: Program No. 4. Given this nested list, use indexing to grab the word "hello”
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

def find_string(lst):
    for i in lst:
        if type(i) == list:
            result = find_string(i)
            if result:
                return result
        elif type(i) == str:
            return i

lst = [1, 2, [3, 4], [5, [100, 200, ["hello"]], 23, 11], 1, 7]
print(find_string(lst))

# output: hello
