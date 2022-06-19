class Teacher:
    def __init__(self, id, name, daysCanWork,
                 daysWantWork, weight):
        self.id = id
        self.name = name
        self.shortName = shortenName(name)
        self.daysCanWork = daysCanWork
        self.daysCanWorkStr = daysToWorkBeautify(daysCanWork)
        self.daysWantWork = daysWantWork
        self.daysWantWorkStr = daysToWorkBeautify(daysWantWork)
        self.weight = weight

def shortenName(name):
    token = name.split(" ")
    if len(token) == 3:
        return token[0] + token[1][0] + ". " + token[2][0] + "."
    return token[0] + token[1][0] + "."

def daysToWorkBeautify(daysToWork):
    mapp = {1: "Mon", 2: "Tue", 3: "Wen", 4: "Thu", 5: "Fri", 6: "Sat"}
    
    daysToWork = daysToWork[1:-1].replace("],[", "];[")
    tokens = daysToWork.split(";")
    string = ""
    for day in range(1,7):
        token = tokens[day-1]
        token = token[1:-1]
        classes = token.split(",")
        string = string + mapp[day] + ": " 
        for i in range(1,8):
            flag = False
            for clazz in classes:
                if clazz != "":
                    if int(clazz) == i:
                        flag = True
                        string = string + "" + clazz
                        if (i != 7):
                            string = string = string + ","

        string = string + "; "

    print(string)
    return string