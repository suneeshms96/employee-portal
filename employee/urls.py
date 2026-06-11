"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employeeapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('index/',index,name="index"),
    path('login/',login,name="login"),
    path('loginadmin/',loginadmin,name="loginadmin"),
    path('adminhome/',adminhome,name="adminhome"),
    path('adddept/',adddept,name="adddept"),
    path('deptadd/',deptadd,name="deptadd"),
    path('viewdept/',viewdept,name="viewdept"),
    path('deptheadassign/',deptheadassign,name="deptheadassign"),
    path('headassign/',headassign,name="headassign"),
    path('depthome/',depthome,name="depthome"),
    path('viewheads/',viewheads,name="viewheads"),
    path('headdelete/',headdelete,name="headdelete"),
    path('headupdate/',headupdate,name="headupdate"),
    # path('updatehead/',updatehead,name="updatehead"),
    path('headregupdate/',headregupdate,name="headregupdate"),
    path('workassign/',workassign,name="workassign"),
    path('assign/',assign,name="assign"),
    path('viewwork/',viewwork,name="viewwork"),
    path('workdelete/',workdelete,name="workdelete"),
    path('workupdate/',workupdate,name="workupdate"),
    path('workregupdate/',workregupdate,name="workregupdate"),
    path('employees/',employees,name="employees"),
    path('employeesassign/',employeesassign,name="employeesassign"),
    path('viewemp/',viewemp,name="viewemp"),
    path('empdelete/',empdelete,name="empdelete"),
    path('empupdate/',empupdate,name="empupdate"),
    path('updateemp/',updateemp,name="updateemp"),
    path('allocatedwork/',allocatedwork,name="allocatedwork"),
    path('task/',task,name="task"),
    path('assigntask/',assigntask,name="assigntask"),
    path('assignedstaff/',assignedstaff,name="assignedstaff"),
    # path('assignedtasks/',assignedtasks,name="assignedtasks"),
    path('emphome/',emphome,name="emphome"),
    path('viewmytask/',viewmytask,name="viewmytask"),
    path('statusm/',statusm,name="statusm"),
    path('statush/',statush,name="statush"),
    path('questionair/',questionair,name="questionair"),
    path('stressdet/',stressdet,name="stressdet"),
    path('detection/',detection,name="detection"),
    path('logout/',logout,name="logout"),

    path('result/',result,name="result"),
    path('predict/',predict,name="predict"),
    path('dpract/',dpract,name="dpract"),
    path('vanalysis/',vanalysis,name="vanalysis"),
    path('svreport/',svreport,name="svreport"),
    path('svreportaction/',svreportaction,name="svreportaction"),
    path('surveyReport/',surveyReport,name="surveyReport"),
    path('surveyReportAct/',surveyReportAct,name="surveyReportAct"),
    path('hsvreport/',hsvreport,name="hsvreport"),
    path('hsvreportAct/',hsvreportAct,name="hsvreportAct"),
    path('hsurveyReport/',hsurveyReport,name="hsurveyReport"),
    path('hsurveyReportAct/',hsurveyReportAct,name="hsurveyReportAct"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=staticfiles_urlpatterns()
