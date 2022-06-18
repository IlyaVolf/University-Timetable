class Teacher:
    def __init__(self, id, name, daysCanWork,
                 daysWantWork, weight):
        self.id = id
        self.name = name
        self.shortName = shortenName(name)
        self.daysCanWork = daysCanWork
        self.daysWantWork = daysWantWork
        self.weight = weight

def shortenName(name):
    token = name.split(" ")
    if len(token) is 3:
        return token[0] + token[1][0] + ". " + token[2][0] + "."
    return token[0] + token[1][0] + "."
