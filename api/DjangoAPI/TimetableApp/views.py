from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TimetableApp.models import Auditories, Constraints, EducationalPrograms, Faculties, GeneratedEntities, GeneratedSchedule,  Groups, Subjects, Teachers, entries
from TimetableApp.serializers import AuditorySerializer, ConstraintsSerializer, EducationalProgramsSerializer, EntriesSerializer, FacultiesSerializer, GeneratedEntitiesSerializer, GeneratedScheduleSerializer, GroupsSerializer, SubjectsSerializer, TeachersSerializer

# Create your views here.




@csrf_exempt
def auditoryApi(request, idd=0):
    if request.method=='GET':
        auditories = Auditories.objects.all()
        auditories_serializer=AuditorySerializer(auditories, many=True)
        return JsonResponse(auditories_serializer.data, safe=False)
    elif request.method=='POST':
        auditory_data=JSONParser().parse(request)
        auditories_serializer=AuditorySerializer(data=auditory_data)
        if auditories_serializer.is_valid():
            auditories_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        auditory_data=JSONParser().parse(request)
        auditory=Auditories.objects.get(id=auditory_data['id'])
        auditories_serializer=AuditorySerializer(auditory,data=auditory_data)
        if auditories_serializer.is_valid():
            auditories_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        auditory=Auditories.objects.get(id=idd)
        auditory.delete()
        return JsonResponse("Deleted Successfully", safe=False)

def constraintsApi(request, idd=0):
    if request.method=='GET':
        constraints = Constraints.objects.all()
        constraints_serializer=ConstraintsSerializer(constraints, many=True)
        return JsonResponse(constraints_serializer.data, safe=False)
    elif request.method=='POST':
        constraints_data=JSONParser().parse(request)
        constraints_serializer=ConstraintsSerializer(data=constraints_data)
        if constraints_serializer.is_valid():
            constraints_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        constraints_data=JSONParser().parse(request)
        constraints=Constraints.objects.get(id=constraints_data['id'])
        constraints_serializer=ConstraintsSerializer(constraints,data=constraints_data)
        if constraints_serializer.is_valid():
            constraints_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        constraints=Constraints.objects.get(id=idd)
        constraints.delete()
        return JsonResponse("Deleted Successfully", safe=False)

def epApi(request, idd=0):
    if request.method=='GET':
        ep = EducationalPrograms.objects.all()
        ep_serializer=EducationalProgramsSerializer(ep, many=True)
        return JsonResponse(ep.data, safe=False)
    elif request.method=='POST':
        ep_data=JSONParser().parse(request)
        ep_serializer=EducationalProgramsSerializer(data=ep_data)
        if ep_serializer.is_valid():
            ep_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        ep_data=JSONParser().parse(request)
        ep=Constraints.objects.get(id=ep_data['id'])
        ep_serializer=EducationalProgramsSerializer(ep,data=ep_data)
        if ep_serializer.is_valid():
            ep_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        ep=EducationalPrograms.objects.get(id=idd)
        ep.delete()
        return JsonResponse("Deleted Successfully", safe=False)

def facultiesApi(request, idd=0):
    if request.method=='GET':
        faculties = Faculties.objects.all()
        faculties_serializer=FacultiesSerializer(faculties, many=True)
        return JsonResponse(faculties.data, safe=False)
    elif request.method=='POST':
        faculties_data=JSONParser().parse(request)
        faculties_serializer=FacultiesSerializer(data=faculties_data)
        if faculties_serializer.is_valid():
            faculties_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        faculties_data=JSONParser().parse(request)
        faculties=Faculties.objects.get(id=faculties_data['id'])
        faculties_serializer=FacultiesSerializer(faculties,data=faculties_data)
        if faculties_serializer.is_valid():
            faculties_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        faculties=Faculties.objects.get(id=idd)
        faculties.delete()
        return JsonResponse("Deleted Successfully", safe=False)

def geApi(request, idd=0):
    if request.method=='GET':
        ge = GeneratedEntities.objects.all()
        ge_serializer=GeneratedEntitiesSerializer(ge, many=True)
        return JsonResponse(ep.data, safe=False)
    elif request.method=='POST':
        ge_data=JSONParser().parse(request)
        ge_serializer=GeneratedEntitiesSerializer(data=ge_data)
        if ge_serializer.is_valid():
            ge_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        ge_data=JSONParser().parse(request)
        ge=GeneratedEntities.objects.get(id=ge_data['id'])
        ge_serializer=GeneratedEntitiesSerializer(ge,data=ge_data)
        if ge_serializer.is_valid():
            ge_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        ge=GeneratedEntities.objects.get(id=idd)
        ge.delete()
        return JsonResponse("Deleted Successfully", safe=False)

def gschApi(request, idd=0):
    if request.method=='GET':
        gsch = GeneratedSchedule.objects.all()
        gsch_serializer=GeneratedScheduleSerializer(gsch, many=True)
        return JsonResponse(gsch.data, safe=False)
    elif request.method=='POST':
        gsch_data=JSONParser().parse(request)
        gsch_serializer=GeneratedScheduleSerializer(data=gsch_data)
        if gsch_serializer.is_valid():
            gsch_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        gsch_data=JSONParser().parse(request)
        gsch=GeneratedScheduleSerializer.objects.get(id=gsch_data['id'])
        gsch_serializer=GeneratedScheduleSerializer(gsch,data=gsch_data)
        if gsch_serializer.is_valid():
            gsch_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        gsch=GeneratedEntities.objects.get(id=idd)
        gsch.delete()
        return JsonResponse("Deleted Successfully", safe=False)

def groupsApi(request, idd=0):
    if request.method=='GET':
        groups = Groups.objects.all()
        groups_serializer=GroupsSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)
    elif request.method=='POST':
        group_data=JSONParser().parse(request)
        groups_serializer=GroupsSerializer(data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        group_data=JSONParser().parse(request)
        group=Groups.objects.get(id=group_data['id'])
        groups_serializer=GroupsSerializer(group,data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        group=Groups.objects.get(id=idd)
        group.delete()
        return JsonResponse("Deleted Successfully", safe=False)


def subjApi(request, idd=0):
    if request.method=='GET':
        gsch = Subjects.objects.all()
        gsch_serializer=SubjectsSerializer(gsch, many=True)
        return JsonResponse(gsch.data, safe=False)
    elif request.method=='POST':
        gsch_data=JSONParser().parse(request)
        gsch_serializer=SubjectsSerializer(data=gsch_data)
        if gsch_serializer.is_valid():
            gsch_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        gsch_data=JSONParser().parse(request)
        gsch=SubjectsSerializer.objects.get(id=gsch_data['id'])
        gsch_serializer=SubjectsSerializer(gsch,data=gsch_data)
        if gsch_serializer.is_valid():
            gsch_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        gsch=Subjects.objects.get(id=idd)
        gsch.delete()
        return JsonResponse("Deleted Successfully", safe=False)


def tchApi(request, idd=0):
    if request.method=='GET':
        groups = Teachers.objects.all()
        groups_serializer=TeachersSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)
    elif request.method=='POST':
        group_data=JSONParser().parse(request)
        groups_serializer=TeachersSerializer(data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        group_data=JSONParser().parse(request)
        group=Groups.objects.get(id=group_data['id'])
        groups_serializer=TeachersSerializer(group,data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        group=Teachers.objects.get(id=idd)
        group.delete()
        return JsonResponse("Deleted Successfully", safe=False)


def entriesApi(request, idd=0):
    if request.method=='GET':
        groups = entries.objects.all()
        groups_serializer=EntriesSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)
    elif request.method=='POST':
        group_data=JSONParser().parse(request)
        groups_serializer=EntriesSerializer(data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        group_data=JSONParser().parse(request)
        group=entries.objects.get(id=group_data['id'])
        groups_serializer=EntriesSerializer(group,data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        group=entries.objects.get(id=idd)
        group.delete()
        return JsonResponse("Deleted Successfully", safe=False)

'''
@csrf_exempt
def groupApi(request, id=0):
    if request.method=='GET':
        groups = Group.objects.all()
        groups_serializer=GroupSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)
    elif request.method=='POST':
        group_data=JSONParser().parse(request)
        groups_serializer=GroupSerializer(data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        group_data=JSONParser().parse(request)
        group=Group.objects.get(GroupId=group_data['GroupId'])
        groups_serializer=GroupSerializer(group,data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        group=Group.objects.get(GroupId=id)
        group.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def teacherApi(request, id=0):
    if request.method=='GET':
        teachers = Teacher.objects.all()
        teachers_serializer=TeacherSerializer(teachers, many=True)
        return JsonResponse(teachers_serializer.data, safe=False)
    elif request.method=='POST':
        teacher_data=JSONParser().parse(request)
        teachers_serializer=TeacherSerializer(data=teacher_data)
        if teachers_serializer.is_valid():
            teachers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        teacher_data=JSONParser().parse(request)
        teacher=Teacher.objects.get(TeacherId=teacher_data['TeacherId'])
        teachers_serializer=TeacherSerializer(teacher,data=teacher_data)
        if teachers_serializer.is_valid():
            teachers_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        teacher=Teacher.objects.get(TeacherId=id)
        teacher.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def classroomApi(request, id=0):
    if request.method=='GET':
        classrooms = Classroom.objects.all()
        classrooms_serializer=ClassroomSerializer(classrooms, many=True)
        return JsonResponse(classrooms_serializer.data, safe=False)
    elif request.method=='POST':
        classroom_data=JSONParser().parse(request)
        classrooms_serializer=ClassroomSerializer(data=classroom_data)
        if classrooms_serializer.is_valid():
            classrooms_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        classroom_data=JSONParser().parse(request)
        classroom=Classroom.objects.get(ClassroomId=classroom_data['ClassroomId'])
        classrooms_serializer=ClassroomSerializer(classroom,data=classroom_data)
        if classrooms_serializer.is_valid():
            classrooms_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        classroom=Classroom.objects.get(ClassroomId=id)
        classroom.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def departmentApi(request, idd=0):
    if request.method=='GET':
        departments = Department.objects.all()
        departments_serializer=DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=idd)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
'''