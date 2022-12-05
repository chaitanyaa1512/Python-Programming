def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    if len(data1) == len(data2):
        for i in range(len(data1)):
          if data1[i] not in data2 or data2[i] not in data1 or data1[i] == data2[i]:
            return False
        return True
    else:
        return False   
    

if __name__ == '__main__':
    print(check_anagram("eat","tea"))