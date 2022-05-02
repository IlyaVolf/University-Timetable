# возвращаем то, что удалили
from entities.GeneratedClass import GeneratedClass


def test0(a):
    return a


# это мб породить штраф из-за ценелесообразности выбора аудитории, ибо аудитория лекционная
def test1(a):
    return GeneratedClass(
        a.faculty,
        a.edProgram,
        a.specialization,
        a.subject,
        a.semester,
        a.teacher,
        a.typeOfClass,
        "1156",
        a.groups,
        a.day,
        a.classNumber
    )


# такой аудитории нет => ничего не добавится
def test2(a):
    return GeneratedClass(
        a.faculty,
        a.edProgram,
        a.specialization,
        a.subject,
        a.semester,
        a.teacher,
        a.typeOfClass,
        "999",
        a.groups,
        a.day,
        a.classNumber
    )


# такой специализации нет => ничего не добавится
def test3(a):
    return GeneratedClass(
        a.faculty,
        a.edProgram,
        "bloggeromania",
        a.subject,
        a.semester,
        a.teacher,
        a.typeOfClass,
        "999",
        a.groups,
        a.day,
        a.classNumber
    )


# такой специализации нет => ничего не добавится
def test4(a):
    return GeneratedClass(
        a.faculty,
        a.edProgram,
        "Computer Science and Systems Engineering",
        "Interface design",
        5,
        "Derzho Marina Anatolievna",
        "lec",
        "1156",
        "[19213,19214]",
        6,
        4
    )
