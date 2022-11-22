# d={101:'Chay', 102: 'Joey', 103: 'Chan'}
# x=d.get(104)
# x=d.keys()
# x=d.values()
# x=d.items()
# print(x)
# for key, value in d.items():
#     print(key)
#     print(value)
#     print(d.get(key))
# # x=d.pop(104)
# # x=d.popitem()
# # print(x)
# # print(d)

# x=d.setdefault(105,'Pooh')
# x=d.update({105:'Pooh'})
# print(x)
# print(d)

# lst=[101,102,103,104,105]
# x=dict.fromkeys(lst, None)
# print(x)


#ASSIGNMENT -04 Dictionary Incorrect Function

def find_correct(word_dict):
    correct,almost,wrong=0,0,0
    for key,value in word_dict.items():
        if key == value:
            correct=correct+1
        else:
            if len(key)!=len(value):
                wrong=wrong+1
                continue
            incorrect=0
            for i in range(min([len(key),len(value)])):
                if key[i] != value[i]:
                    incorrect=incorrect+1
                    if incorrect>2:
                        wrong=wrong+1
                        break
            if incorrect<=2:
                almost=almost+1
    return [correct, almost, wrong]
                    
                    
                    

word_dict={"PICK": "PIC", "RAMEN": "RAMAN", "MAN": "MAN", "WENT": "VENT", "CARTOON": "CARTON"}
print(find_correct(word_dict))