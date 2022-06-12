from DatabaseManager import DatabaseManager

dbManager = DatabaseManager()
teacher = dbManager.getTeacher(1)
print(teacher.name)
dbManager.close()