with open(r'html_file.html', "r") as f:
    page = f.read()
page = page.replace('\n', '')
page = page.replace('  ', '')
type = ""
i = 0
flag = True
while(i != len(page)):
    if (page[i] == '<' and page[i+1] != '/'):
        type = "OPENING_TAG: "
    elif (page[i] == '<' and page[i + 1] == '/'):
        type = "CLOSING_TAG: "
        i+=1
    elif ( page[i] == ' ' and flag):
        if ( type != ""):
            print(type)
            type = ""
        type = "ATTRIBUTE: "
    elif (page[i] == '"' and page[i-1] == '='):
        flag = False
        type += ' VALUE: '
    elif (page[i] == '"'):
        flag = True
        if ( type != ""):
            print(type)
            type = ""
        pass
    elif (page[i] == "="):
        pass
    elif (page[i] == ">" and page[i-1] != '"'):
        print(type)
        type = ""
    else:
        type += page[i]
    i+=1
