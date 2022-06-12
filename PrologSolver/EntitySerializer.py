from entities.Teacher import Teacher

def serialiseTeacher(teacher : Teacher):
    return {
        'id': teacher.id,
        'name': teacher.name,
        'daysCanWork': teacher.daysCanWork,
        'daysWantWork': teacher.daysWantWork,
        'weight': teacher.weight
    }