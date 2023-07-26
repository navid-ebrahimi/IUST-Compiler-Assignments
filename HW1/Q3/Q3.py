dic = {}


find_num = 0
while(True):
    try:
        line = input().split(' ')
        if (line[0] == "Add"):
            dic[line[4]] = f"{line[1]} {line[2]} {line[3]}"
            print(f"User {line[4]} added successfully")
            myKeys = list(dic.keys())
            myKeys.sort()
            dic = {i: dic[i] for i in myKeys}
        elif (line[0] == "Find"):
            find_num+=1
            flag = 0
            num_find = 0
            for keys, value in dic.items():
                if (num_find == 10):
                    break
                if (keys.startswith(line[1])):
                    num_find+=1
                    flag+=1
                    detail = value.split(' ')
                    print(f"{find_num} {detail[0]} {detail[1]} {detail[2]} {keys}")
            if (flag == 0):
                print(f"{find_num} No user found")
            # print(dic[int(line[1])])
    except EOFError:
        break


