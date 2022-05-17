from django.urls import re_path as url
from TimetableApp import views


urlpatterns=[
    url(r'^auditory$', views.auditoryApi),
    url(r'^auditory/([0-9]+)$', views.auditoryApi),

    url(r'^constraints$', views.constraintsApi),
    url(r'^constraints/([0-9]+)$', views.constraintsApi),

    url(r'^ep$', views.epApi),
    url(r'^ep/([0-9]+)$', views.epApi),

    url(r'^faculties$', views.facultiesApi),
    url(r'^faculties/([0-9]+)$', views.facultiesApi),

    url(r'^ge$', views.geApi),
    url(r'^ge/([0-9]+)$', views.geApi),

    url(r'^gsch$', views.gschApi),
    url(r'^gsch/([0-9]+)$', views.gschApi),

    url(r'^groups$', views.groupsApi),
    url(r'^groups/([0-9]+)$', views.groupsApi),

    url(r'^subj$', views.subjApi),
    url(r'^subj/([0-9]+)$', views.subjApi),

    
    url(r'^tch$', views.tchApi),
    url(r'^tch/([0-9]+)$', views.tchApi),

    
    url(r'^entries$', views.entriesApi),
    url(r'^entries/([0-9]+)$', views.entriesApi)

]

''' url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),

    url(r'^teacher$', views.teacherApi),
    url(r'^teacher/([0-9]+)$', views.teacherApi),

    url(r'^group$', views.groupApi),
    url(r'^group/([0-9]+)$', views.groupApi),

    url(r'^classroom$', views.classroomApi),
    url(r'^classroom/([0-9]+)$', views.classroomApi)'''