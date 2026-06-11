from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect,redirect
from django.db import connection
import os
from django.conf import setting
# import cv2
import numpy as np
from tensorflow.keras.models import load_model
from  datetime import date 
from datetime import datetime
now = date.today()
today1=date.today()
import datetime
today_date = datetime.date.today()
today = today_date.strftime("%Y-%m-%d")
import datetime
tdate=datetime.date.today()
today=tdate.strftime("%Y-%m-%d")
todaym=tdate.strftime("%m")
import datetime
tdate=datetime.date.today()
today=tdate.strftime("%Y-%m-%d")
todaym=tdate.strftime("%m")


def svreport(request):
    return render(request,'svreport.html',{'today':today})

def svreportaction(request):
    cursor=connection.cursor()
    fdate=request.GET['fdate']
    ldate=request.GET['ldate']
    
    s1 = "SELECT * FROM emotion INNER JOIN head ON emotion.hid = head.hid WHERE emotion.date BETWEEN '%s' AND '%s' group by date"% (fdate, ldate)
    cursor.execute(s1)
    print(s1)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'eid':row[0],'hid':row[1],'emotion':row[2],'date':row[3],'hname':row[6]}
        use.append(q)
    return render(request,'svreport1.html',{'use':use})
def surveyReport(request):
    return render(request,'surveyReport.html',{'today':today})

def surveyReportAct(request):
    cursor=connection.cursor()
    fdate=request.GET['fdate']
    ldate=request.GET['ldate']
    
    s1="select * from survey inner join head on survey.empid=head.hid  where survey.sdate between '%s' and '%s'"% (fdate,ldate)
    cursor.execute(s1)
    print(s1)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'sid':row[0],'empid':row[1],'attr':row[2],'stress':row[3],'sdate':row[4],'hname':row[8]}
        use.append(q)
    return render(request,'surveyReport1.html',{'use':use})
def hsurveyReport(request):
    return render(request,'hsurveyReport.html')
def hsurveyReportAct(request):
    cursor = connection.cursor()
    fdate = request.GET['fdate']
    ldate = request.GET['ldate']
    
    # Get the department name of the logged-in head
    s_department = "SELECT dname FROM head WHERE hid='%s'" % (request.session['uid'])
    cursor.execute(s_department)
    department = cursor.fetchone()[0]
    
    # Retrieve all employees in the same department as the logged-in head
    s_employees = "SELECT hid, fname, lname FROM head WHERE dname='%s' AND etype='emp'" % (department)
    cursor.execute(s_employees)
    employee_data = cursor.fetchall()
    
    # Fetch survey data for each employee within the specified date range
    all_employee_details = []
    for emp_id, fname, lname in employee_data:
        s_survey = "SELECT survey.*, head.fname AS emp_fname, head.lname AS emp_lname FROM survey INNER JOIN head ON survey.empid=head.hid WHERE survey.empid='%s' AND survey.sdate BETWEEN '%s' AND '%s'" % (emp_id, fdate, ldate)
        cursor.execute(s_survey)
        survey_results = cursor.fetchall()
        
        # Append survey results to the list
        for row in survey_results:
            all_employee_details.append({
                'sid': row[0],
                'empid': row[1],
                'attr': row[2],
                'stress': row[3],
                'sdate': row[4],
                'emp_fname': row[6],
                'emp_lname': row[5],
            })
    
    return render(request, 'hsurveyReport1.html', {'use': all_employee_details})


def hsvreport(request):
    return render(request,'hsvreport.html')
def hsvreportAct(request):
    cursor = connection.cursor()
    fdate = request.GET['fdate']
    ldate = request.GET['ldate']
    
    # Get the department name of the logged-in head
    s_department = "SELECT dname FROM head WHERE hid='%s'" % (request.session['uid'])
    cursor.execute(s_department)
    department = cursor.fetchone()[0]
    
    # Retrieve all employees in the same department as the logged-in head
    s_employees = "SELECT hid, fname, lname FROM head WHERE dname='%s' AND etype='emp'" % (department)
    cursor.execute(s_employees)
    employee_data = cursor.fetchall()
    
    # Fetch emotion data for each employee within the specified date range
    all_employee_emotions = []
    for emp_id, fname, lname in employee_data:
        s_emotion = "SELECT emotion.*, head.fname AS emp_fname, head.lname AS emp_lname FROM emotion INNER JOIN head ON emotion.hid=head.hid WHERE emotion.hid='%s' AND emotion.date BETWEEN '%s' AND '%s' group by date" % (emp_id, fdate, ldate)
        cursor.execute(s_emotion)
        emotion_results = cursor.fetchall()
        
        # Append emotion results to the list
        for row in emotion_results:
            all_employee_emotions.append({
                'eid': row[0],
                'hid': row[1],
                'emotion': row[2],
                'date': row[3],
                'emp_fname': row[4],
                'emp_lname': row[5],
            })
    
    return render(request, 'hsvreport1.html', {'use': all_employee_emotions})


import _pickle as pickle
import numpy as np
import scipy as sp
import pandas as pd
#model = pickle.load (open ('E:/Projects/2026/employee (10)/employee/employeeapp/model.pkl','rb'))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model.pkl')
model = pickle.load(open(model_path, 'rb'


def predict(request):
	"""
    For rendering results on HTML GUI
    """
	Age = request.GET["Age"]
	BusinessTravel = request.GET['BusinessTravel']
	DailyRate = request.GET['Daily Rate']
	Department = request.GET['Department']
	DistanceFromHome = request.GET["Distance From Home"]
	Education = request.GET["Education"]
	EducationField = request.GET['education_field']
	EnvironmentSatisfaction = request.GET["Environment Satisfaction"]
	Gender = request.GET['Gender']
	HourlyRate = request.GET["Hourly Rate"]
	JobInvolvement = request.GET["Environment Satisfaction"]
	JobLevel = request.GET["Job Level"]
	JobRole = request.GET['Job Role']
	JobSatisfaction = request.GET["Job Satisfaction"]
	MaritalStatus = request.GET['Marital Status']
	MonthlyIncome = request.GET["Monthly Income"]
	NumCompaniesWorked = request.GET["Number of Companies Worked in"]
	OverTime = request.GET['Over Time']
	PerformanceRating = request.GET["Performance Rating"]
	RelationshipSatisfaction = request.GET["Relationship Satisfaction"]
	StockOptionLevel = request.GET["Stock Option Level"]
	TotalWorkingYears = request.GET["Total Working Years"]
	TrainingTimesLastYear = request.GET["Training Times Last Year"]
	WorkLifeBalance = request.GET["Work Life Balance"]
	YearsAtCompany = request.GET["Years At Company"]
	YearsInCurrentRole = request.GET["Years In Current Role"]
	YearsSinceLastPromotion = request.GET["Years Since Last Promotion"]
	YearsWithCurrManager = request.GET["Years With Curr Manager"]

	dict = {
        'Age': int (Age),
        'BusinessTravel': str (BusinessTravel),
        'DailyRate': int (DailyRate),
        'Department': Department,
        'DistanceFromHome': int (DistanceFromHome),
        'Education': Education,
        'EducationField': str (EducationField),
        'EnvironmentSatisfaction': int (EnvironmentSatisfaction),
        'Gender': str (Gender),
        'HourlyRate': int (HourlyRate),
        'JobInvolvement': int (JobInvolvement),
        'JobLevel': int (JobLevel),
        'JobRole': JobRole,
        'JobSatisfaction': int (JobSatisfaction),
        'MaritalStatus': str (MaritalStatus),
        'MonthlyIncome': int (MonthlyIncome),
        'NumCompaniesWorked': int (NumCompaniesWorked),
        'OverTime': str (OverTime),
        'PerGETanceRating': int (PerformanceRating),
        'RelationshipSatisfaction': int (RelationshipSatisfaction),
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': int (TotalWorkingYears),
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': int (WorkLifeBalance),
        'YearsAtCompany': int (YearsAtCompany),
        'YearsInCurrentRole': int (YearsInCurrentRole),
        'YearsSinceLastPromotion': int (YearsSinceLastPromotion),
        'YearsWithCurrManager': int (YearsWithCurrManager)
    }
	df = pd.DataFrame ([dict])
	df['Total_Satisfaction'] = (df['EnvironmentSatisfaction'] +
                                df['JobInvolvement'] +
                                df['JobSatisfaction'] +
                                df['RelationshipSatisfaction'] +
                                df['WorkLifeBalance']) / 5
	
	# Drop Columns
	df.drop (
        ['EnvironmentSatisfaction','JobInvolvement','JobSatisfaction','RelationshipSatisfaction','WorkLifeBalance'],
        axis=1,inplace=True)

	# Convert Total satisfaction into boolean
	df['Total_Satisfaction_bool'] = df['Total_Satisfaction'].apply (lambda x: 1 if x >= 2.8 else 0)
	df.drop ('Total_Satisfaction',axis=1,inplace=True)
	
	# It can be observed that the rate of attrition of employees below age of 35 is high
	df['Age_bool'] = df['Age'].apply (lambda x: 1 if x < 35 else 0)
	df.drop ('Age',axis=1,inplace=True)
	
	# It can be observed that the employees are more likey the drop the job if dailyRate less than 800
	df['DailyRate_bool'] = df['DailyRate'].apply (lambda x: 1 if x < 800 else 0)
	df.drop ('DailyRate',axis=1,inplace=True)
	
	# Employees working at R&D Department have higher attrition rate
	df['Department_bool'] = df['Department'].apply (lambda x: 1 if x == 'Research & Development' else 0)
	df.drop ('Department',axis=1,inplace=True)
	
	# Rate of attrition of employees is high if DistanceFromHome > 10
	df['DistanceFromHome_bool'] = df['DistanceFromHome'].apply (lambda x: 1 if x > 10 else 0)
	df.drop ('DistanceFromHome',axis=1,inplace=True)
	
	# Employees are more likey to drop the job if the employee is working as Laboratory Technician
	df['JobRole_bool'] = df['JobRole'].apply (lambda x: 1 if x == 'Laboratory Technician' else 0)
	df.drop ('JobRole',axis=1,inplace=True)
	
	# Employees are more likey to the drop the job if the employee's hourly rate < 65
	df['HourlyRate_bool'] = df['HourlyRate'].apply (lambda x: 1 if x < 65 else 0)
	df.drop ('HourlyRate',axis=1,inplace=True)
	
	# Employees are more likey to the drop the job if the employee's MonthlyIncome < 4000
	df['MonthlyIncome_bool'] = df['MonthlyIncome'].apply (lambda x: 1 if x < 4000 else 0)
	df.drop ('MonthlyIncome',axis=1,inplace=True)

	# Rate of attrition of employees is high if NumCompaniesWorked < 3
	df['NumCompaniesWorked_bool'] = df['NumCompaniesWorked'].apply (lambda x: 1 if x > 3 else 0)
	df.drop ('NumCompaniesWorked',axis=1,inplace=True)

	# Employees are more likey to the drop the job if the employee's TotalWorkingYears < 8
	df['TotalWorkingYears_bool'] = df['TotalWorkingYears'].apply (lambda x: 1 if x < 8 else 0)
	df.drop ('TotalWorkingYears',axis=1,inplace=True)
	
	# Employees are more likey to the drop the job if the employee's YearsAtCompany < 3
	df['YearsAtCompany_bool'] = df['YearsAtCompany'].apply (lambda x: 1 if x < 3 else 0)
	df.drop ('YearsAtCompany',axis=1,inplace=True)
	
	# Employees are more likey to the drop the job if the employee's YearsInCurrentRole < 3
	df['YearsInCurrentRole_bool'] = df['YearsInCurrentRole'].apply (lambda x: 1 if x < 3 else 0)
	df.drop ('YearsInCurrentRole',axis=1,inplace=True)
	
	# Employees are more likely to the drop the job if the employee's YearsSinceLastPromotion < 1
	df['YearsSinceLastPromotion_bool'] = df['YearsSinceLastPromotion'].apply (lambda x: 1 if x < 1 else 0)
	df.drop ('YearsSinceLastPromotion',axis=1,inplace=True)
	
	# Employees are more likely to the drop the job if the employee's YearsWithCurrManager < 1
	df['YearsWithCurrManager_bool'] = df['YearsWithCurrManager'].apply (lambda x: 1 if x < 1 else 0)
	df.drop ('YearsWithCurrManager',axis=1,inplace=True)
	# Convert Categorical to Numerical
	# Buisness Travel
	if BusinessTravel == 'Rarely':
		df['BusinessTravel_Rarely'] = 1
		df['BusinessTravel_Frequently'] = 0
		df['BusinessTravel_No_Travel'] = 0
	elif BusinessTravel == 'Frequently':
		df['BusinessTravel_Rarely'] = 0
		df['BusinessTravel_Frequently'] = 1
		df['BusinessTravel_No_Travel'] = 0
	else:
		df['BusinessTravel_Rarely'] = 0
		df['BusinessTravel_Frequently'] = 0
		df['BusinessTravel_No_Travel'] = 1
	df.drop ('BusinessTravel',axis=1,inplace=True)

    # Education
	if Education == 1:
		df['Education_1'] = 1
		df['Education_2'] = 0
		df['Education_3'] = 0
		df['Education_4'] = 0
		df['Education_5'] = 0
	elif Education == 2:
		df['Education_1'] = 0
		df['Education_2'] = 1
		df['Education_3'] = 0
		df['Education_4'] = 0
		df['Education_5'] = 0
	elif Education == 3:
		df['Education_1'] = 0
		df['Education_2'] = 0
		df['Education_3'] = 1
		df['Education_4'] = 0
		df['Education_5'] = 0
	elif Education == 4:
		df['Education_1'] = 0
		df['Education_2'] = 0
		df['Education_3'] = 0
		df['Education_4'] = 1
		df['Education_5'] = 0
	else:
		df['Education_1'] = 0
		df['Education_2'] = 0
		df['Education_3'] = 0
		df['Education_4'] = 0
		df['Education_5'] = 1
	df.drop ('Education',axis=1,inplace=True)

    # EducationField
	if EducationField == 'Life Sciences':
		df['EducationField_Life_Sciences'] = 1
		df['EducationField_Medical'] = 0
		df['EducationField_Marketing'] = 0
		df['EducationField_Technical_Degree'] = 0
		df['Education_Human_Resources'] = 0
		df['Education_Other'] = 0
	elif EducationField == 'Medical':
		df['EducationField_Life_Sciences'] = 0
		df['EducationField_Medical'] = 1
		df['EducationField_Marketing'] = 0
		df['EducationField_Technical_Degree'] = 0
		df['Education_Human_Resources'] = 0
		df['Education_Other'] = 0
	elif EducationField == 'Marketing':
		df['EducationField_Life_Sciences'] = 0
		df['EducationField_Medical'] = 0
		df['EducationField_Marketing'] = 1
		df['EducationField_Technical_Degree'] = 0
		df['Education_Human_Resources'] = 0
		df['Education_Other'] = 0
	elif EducationField == 'Technical Degree':
		df['EducationField_Life_Sciences'] = 0
		df['EducationField_Medical'] = 0
		df['EducationField_Marketing'] = 0
		df['EducationField_Technical_Degree'] = 1
		df['Education_Human_Resources'] = 0
		df['Education_Other'] = 0
	elif EducationField == 'Human Resources':
		df['EducationField_Life_Sciences'] = 0
		df['EducationField_Medical'] = 0
		df['EducationField_Marketing'] = 0
		df['EducationField_Technical_Degree'] = 0
		df['Education_Human_Resources'] = 1
		df['Education_Other'] = 0
	else:
		df['EducationField_Life_Sciences'] = 0
		df['EducationField_Medical'] = 0
		df['EducationField_Marketing'] = 0
		df['EducationField_Technical_Degree'] = 0
		df['Education_Human_Resources'] = 1
		df['Education_Other'] = 1
	df.drop ('EducationField',axis=1,inplace=True)

	# Gender
	if Gender == 'Male':
		df['Gender_Male'] = 1
		df['Gender_Female'] = 0
	else:
		df['Gender_Male'] = 0
		df['Gender_Female'] = 1
	df.drop ('Gender',axis=1,inplace=True)

	# Marital Status
	if MaritalStatus == 'Married':
		df['MaritalStatus_Married'] = 1
		df['MaritalStatus_Single'] = 0
		df['MaritalStatus_Divorced'] = 0
	elif MaritalStatus == 'Single':
		df['MaritalStatus_Married'] = 0
		df['MaritalStatus_Single'] = 1
		df['MaritalStatus_Divorced'] = 0
	else:
		df['MaritalStatus_Married'] = 0
		df['MaritalStatus_Single'] = 0
		df['MaritalStatus_Divorced'] = 1
	df.drop ('MaritalStatus',axis=1,inplace=True)
	
	if OverTime == 'Yes':
		df['OverTime_Yes'] = 1
		df['OverTime_No'] = 0
	else:
		df['OverTime_Yes'] = 0
		df['OverTime_No'] = 1
	df.drop ('OverTime',axis=1,inplace=True)

    # Stock Option Level
	if StockOptionLevel == 0:
		df['StockOptionLevel_0'] = 1
		df['StockOptionLevel_1'] = 0
		df['StockOptionLevel_2'] = 0
		df['StockOptionLevel_3'] = 0
	elif StockOptionLevel == 1:
		df['StockOptionLevel_0'] = 0
		df['StockOptionLevel_1'] = 1
		df['StockOptionLevel_2'] = 0
		df['StockOptionLevel_3'] = 0
	elif StockOptionLevel == 2:
		df['StockOptionLevel_0'] = 0
		df['StockOptionLevel_1'] = 0
		df['StockOptionLevel_2'] = 1
		df['StockOptionLevel_3'] = 0
	else:
		df['StockOptionLevel_0'] = 0
		df['StockOptionLevel_1'] = 0
		df['StockOptionLevel_2'] = 0
		df['StockOptionLevel_3'] = 1
	df.drop ('StockOptionLevel',axis=1,inplace=True)
	# Training Time Last Year
	if TrainingTimesLastYear == 0:
		df['TrainingTimesLastYear_0'] = 1
		df['TrainingTimesLastYear_1'] = 0
		df['TrainingTimesLastYear_2'] = 0
		df['TrainingTimesLastYear_3'] = 0
		df['TrainingTimesLastYear_4'] = 0
		df['TrainingTimesLastYear_5'] = 0
		df['TrainingTimesLastYear_6'] = 0
	elif TrainingTimesLastYear == 1:
		df['TrainingTimesLastYear_0'] = 0
		df['TrainingTimesLastYear_1'] = 1
		df['TrainingTimesLastYear_2'] = 0
		df['TrainingTimesLastYear_3'] = 0
		df['TrainingTimesLastYear_4'] = 0
		df['TrainingTimesLastYear_5'] = 0
		df['TrainingTimesLastYear_6'] = 0
	elif TrainingTimesLastYear == 2:
		df['TrainingTimesLastYear_0'] = 0
		df['TrainingTimesLastYear_1'] = 0
		df['TrainingTimesLastYear_2'] = 1
		df['TrainingTimesLastYear_3'] = 0
		df['TrainingTimesLastYear_4'] = 0
		df['TrainingTimesLastYear_5'] = 0
		df['TrainingTimesLastYear_6'] = 0
	elif TrainingTimesLastYear == 3:
		df['TrainingTimesLastYear_0'] = 0
		df['TrainingTimesLastYear_1'] = 0
		df['TrainingTimesLastYear_2'] = 0
		df['TrainingTimesLastYear_3'] = 1
		df['TrainingTimesLastYear_4'] = 0
		df['TrainingTimesLastYear_5'] = 0
		df['TrainingTimesLastYear_6'] = 0
	elif TrainingTimesLastYear == 4:
		df['TrainingTimesLastYear_0'] = 0
		df['TrainingTimesLastYear_1'] = 0
		df['TrainingTimesLastYear_2'] = 0
		df['TrainingTimesLastYear_3'] = 0
		df['TrainingTimesLastYear_4'] = 1
		df['TrainingTimesLastYear_5'] = 0
		df['TrainingTimesLastYear_6'] = 0
	elif TrainingTimesLastYear == 5:
		df['TrainingTimesLastYear_0'] = 0
		df['TrainingTimesLastYear_1'] = 0
		df['TrainingTimesLastYear_2'] = 0
		df['TrainingTimesLastYear_3'] = 0
		df['TrainingTimesLastYear_4'] = 0
		df['TrainingTimesLastYear_5'] = 1
		df['TrainingTimesLastYear_6'] = 0
	else:
		df['TrainingTimesLastYear_0'] = 0
		df['TrainingTimesLastYear_1'] = 0
		df['TrainingTimesLastYear_2'] = 0
		df['TrainingTimesLastYear_3'] = 0
		df['TrainingTimesLastYear_4'] = 0
		df['TrainingTimesLastYear_5'] = 0
		df['TrainingTimesLastYear_6'] = 1
	df.drop ('TrainingTimesLastYear',axis=1,inplace=True)
	prediction = model.predict (df)
	pt=""
	if prediction == 0:
		pt='Might Not Leave'
		
	else:
		pt='Might Leave'
		
	cur=connection.cursor()
	at=""
	s="select * from survey where empid='%s' and month=%s"%(request.session['uid'],todaym)
	cur.execute(s)
	if(cur.rowcount>0):
		rs=cur.fetchall()
		for r in rs:
			at=r[2]
		if(at == 'Nil'):
			cur.execute("update survey set attr='%s' where empid='%s' and month=%s"%(pt,request.session['uid'],todaym))
			msg="<script>alert('Done');window.location='/emphome/';</script>"
			return HttpResponse(msg)
	else:
		cur.execute("insert into survey (empid,attr,stress,sdate,month) values('%s','%s','Nil','%s','%s')"%(request.session['uid'],pt,today,todaym))
		return render (request,'emphome.html')

def vanalysis(request):
    cur = connection.cursor()
    list = []
    id = request.GET['id']
    print(id)
    s = "select * from survey where empid='%s' order by sid desc" % (request.GET['id'])
    cur.execute(s)
    rs = cur.fetchall()
    for row in rs:
        w = {'srid': row[0], 'empcode': row[1], 'attr': row[2], 'depr': row[3], 'sdate': row[4]}
        list.append(w)
    return render(request, 'vanalysis.html', {'list': list})

def dpract(request):
	cur=connection.cursor()
	q1=int(request.GET['Q1'])
	q2=int(request.GET['Q2'])
	q3=int(request.GET['Q3'])
	q4=int(request.GET['Q4'])
	q5=int(request.GET['Q5'])
	q6=int(request.GET['Q6'])
	q7=int(request.GET['Q7'])
	q8=int(request.GET['Q8'])
	q9=int(request.GET['Q9'])
	q10=int(request.GET['Q10'])

	q11=int(request.GET['Q11'])
	q12=int(request.GET['Q12'])
	q13=int(request.GET['Q13'])
	q14=int(request.GET['Q14'])
	q15=int(request.GET['Q15'])
	q16=int(request.GET['Q16'])
	q17=int(request.GET['Q17'])
	q18=int(request.GET['Q18'])
	q19=int(request.GET['Q19'])
	q20=int(request.GET['Q20'])
	dpr=q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20
	print(dpr)
	depr=""
	if(dpr>=0 and dpr<=10):
		depr="Normal"
	elif(dpr>=11 and dpr<=16):
		depr="Mild Mood Disturbance"
	elif(dpr>=17 and dpr<=20):
		depr="Borderline Clinical Depression"
	elif(dpr>=21 and dpr<=30):
		depr="Moderate Depression"
	elif(dpr>=31 and dpr<=40):
		depr="Severe Depression"
	elif(dpr>=41):
		depr="Extreme Depression"

	dp=""
	s="select * from survey where empid='%s' and month=%s"%(request.session['uid'],todaym)
	print(s)
	cur.execute(s)
	if(cur.rowcount>0):
		rs=cur.fetchall()
		for r in rs:
			dp=r[3]
			print(dp)
		if(dp == 'Nil'):
			cur.execute("update survey set stress='%s' where empid='%s' and month=%s"%(depr,request.session['uid'],todaym))
			msg="<script>alert('Done');window.location='/emphome/';</script>"
			return HttpResponse(msg)
	else:
		cur.execute("insert into survey (empis,attr,stress,sdate,month) values('%s','Nil','%s','%s','%s')"%(request.session['uid'],depr,today,todaym))
		return render (request,'emphome.html')

def result(request):
    return render(request,'result.html')
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginadmin(request):
    cursor=connection.cursor()
    p=request.GET['username']
    q=request.GET['password']
    sql4="select * from login where uname='%s' and upass='%s'"%(p,q)
    cursor.execute(sql4)
    if(cursor.rowcount) > 0:
        result1=cursor.fetchall()
        for row in result1:
            request.session['uid']=row[1]
            request.session['uname']=row[2]
            request.session['upass']=row[3]
            request.session['utype']=row[4]
        if(request.session['utype']=='admin'):
            return render(request,'adminhome.html')  
        
        elif(request.session['utype']=='head'):
            return render(request,'depthome.html')

        elif(request.session['utype']=='emp'):
            return render(request,'emphome.html')
        
    else:
        msg="<script>alert('invalid username and password');window.location='/login/';</script>"
    return HttpResponse(msg)   

def adddept(request):
    return render(request,'adddept.html')

def deptadd(request):
    cursor=connection.cursor()
    dn=request.GET['dname']
    sql="insert into dept(dname)values('%s')"%(dn)
    cursor.execute(sql)
    result=cursor.fetchall()
    msg="<script>alert('successfully added');window.location='/adddept/';</script>"
    return HttpResponse(msg)


def viewdept(request):
    cursor=connection.cursor()
    s="select * from dept"
    cursor.execute(s)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'dname':row[1]}
        use.append(q)
    return render(request,'viewdept.html',{'use':use})

def deptheadassign(request):
    dname=request.GET['dname']
    return render(request,'deptheadassign.html',{'dname':dname,'today':today})

def headassign(request):
    cursor=connection.cursor()
    dn=request.GET['dname']
    fn=request.GET['fname']
    ln=request.GET['lname']
    ad=request.GET['address']
    gn=request.GET['gender']
    ph=request.GET['phone']
    ds=request.GET['desig']
    ex=request.GET['exp']
    qu=request.GET['qual']
    dob=request.GET['dob']
    doj=request.GET['doj']
    un=request.GET['username']
    pas=request.GET['password']
    today = date.today()
    birthdate = datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 18:
        sql="insert into head(dname,fname,lname,address,gender,phone,desig,exp,qual,dob,doj,username,etype)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','head')"%(dn,fn,ln,ad,gn,ph,ds,ex,qu,dob,doj,un)
        cursor.execute(sql)
        ut='head'
        sql2="select max(hid) as hid from head"
        cursor.execute(sql2)
        result=cursor.fetchall()
        for r in result:
            sql3="insert into login(uid,uname,upass,utype)values('%s','%s','%s','%s')"%(r[0],un,pas,ut)
            cursor.execute(sql3)
        msg="<script>alert('successfully added');window.location='/viewheads/';</script>"
        return HttpResponse(msg)
    else:
         msg="<script>alert('Employee age must be greater than 18');window.location='/viewdept/';</script>"
         return HttpResponse(msg)

def depthome(request):
    return render(request,'depthome.html')

def adminhome(request):
    return render(request,'adminhome.html')

def viewheads(request):
    cursor=connection.cursor()
    s="select * from head"
    cursor.execute(s)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'hid':row[0],'dname':row[1],'fname':row[2],'lname':row[3],'address':row[4],'phone':row[5],'gender':row[6],'desig':row[7],'exp':row[8],'qual':row[9],'dob':row[10],'doj':row[11],'etype':row[13]}
        use.append(q)
    return render(request,'viewheads.html',{'use':use})

def headdelete(request):
    cursor=connection.cursor()
    delid=request.GET['id']
    s="delete from head where hid='%s'"%(delid)
    cursor.execute(s)
    msg="<script>alert('successfully deleteded');window.location='/viewheads/';</script>"
    return HttpResponse(msg)

def headupdate(request):
    cursor=connection.cursor()
    upid=request.GET['cid']
    dname=request.GET['dname']
    s="select * from head where hid='%s'"%(upid)
    cursor.execute(s)
    rs=cursor.fetchall()
    tk=[]
    for row in rs:
        q={'hid':row[0],'dname':row[1],'fname':row[2],'lname':row[3],'address':row[4],'phone':row[5],'gender':row[6],'desig':row[7],'exp':row[8],'qual':row[9],'dob':row[10],'doj':row[11]}
        tk.append(q)
    return render(request,'updatehead.html',{'tk':tk,'upid':upid, 'dname':dname})

# def updatehead(request):
#     return render(request,'updatehead.html')

from django.db import connection
from django.http import HttpResponse

def headregupdate(request):
    cursor = connection.cursor()
    hid = request.GET['id']
    dn = request.GET['dname']
    fn = request.GET['fname']
    ln = request.GET['lname']
    ad = request.GET['address']
    ph = request.GET['phone']
    gn = request.GET['gender']
    ds = request.GET['desig']
    ex = request.GET['exp']
    qu = request.GET['qual']
    dob = request.GET['dob']
    doj = request.GET['doj']

    s = "UPDATE head SET fname='%s', lname='%s', address='%s', phone='%s', gender='%s', desig='%s', exp='%s', qual='%s', dob='%s', doj='%s' WHERE hid='%s'" % (fn, ln, ad, ph, gn, ds, ex, qu, dob, doj, hid)
    cursor.execute(s)

    msg = "<script>alert('Successfully updated'); window.location='/viewheads/';</script>"
    return HttpResponse(msg)

def workassign(request):
    dn=request.GET['dn']
    return render(request,'workassign.html',{'dn':dn,'today':today})
  
def assign(request):
    cursor=connection.cursor()
    dn=request.GET['dn']
    pn=request.GET['pname']
    de=request.GET['descrip']
    do=request.GET['dos']
    sql4="insert into works(dname,pname,descrip,dos,status) values ('%s','%s','%s','%s','pending')"%(dn,pn,de,do)
    cursor.execute(sql4)
    msg="<script>alert('successfully added');window.location='/viewwork/';</script>"
    return HttpResponse(msg)

def viewwork(request):
    cursor=connection.cursor()
    s="select * from works"
    cursor.execute(s)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'pcode':row[0],'dname':row[1],'pname':row[2],'descrip':row[3],'dos':row[4],'status':row[5]}
        use.append(q)
    return render(request,'viewwork.html',{'use':use}) 

def workdelete(request):
    cursor=connection.cursor()
    delid=request.GET['id']
    s="delete from works where pcode='%s'"%(delid)
    cursor.execute(s)
    msg="<script>alert('successfully deleteded');window.location='/viewwork/';</script>"
    return HttpResponse(msg)

def workupdate(request):
    cursor=connection.cursor()
    upid=request.GET['id']
    s="select * from works where pcode='%s'"%(upid)
    cursor.execute(s)
    rs=cursor.fetchall()
    tk=[]
    for row in rs:
        q={'pcode':row[0],'pname':row[2],'descrip':row[3],'dos':datetime.strftime(row[4],'%Y-%m-%d')}
        tk.append(q)
    return render(request,'updatework.html',{'tk':tk})

from datetime import datetime

def workregupdate(request):
    cursor=connection.cursor()
    pc=request.GET['id']
    pn=request.GET['pname']
    de=request.GET['descrip']
    do=request.GET['dos']
    s="update works set pname='%s',descrip='%s',dos='%s' where pcode ='%s'" %(pn,de,do,pc)
    cursor.execute(s)
    msg="<script>alert('successfully updated');window.location='/viewwork/';</script>"
    return HttpResponse(msg)

def employees(request):
    cursor=connection.cursor()
    s="select dname from head where hid='%s'"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    dname=""
    for row in rs:
        dname=row[0]
    return render(request,'employees.html',{'dname':dname,'today':today})
    
    
def employeesassign(request):
    cursor=connection.cursor()
    dn=request.GET['dname']
    fn=request.GET['fname']
    ln=request.GET['lname']
    ad=request.GET['address']
    gn=request.GET['gender']
    ph=request.GET['phone']
    ds=request.GET['desig']
    ex=request.GET['exp']
    qu=request.GET['qual']
    dob=request.GET['dob']
    doj=request.GET['doj']
    un=request.GET['username']
    pas=request.GET['password']
    today = date.today()
    birthdate = datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 18:
        sql="insert into head(dname,fname,lname,address,gender,phone,desig,exp,qual,dob,doj,username,etype)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','emp')"%(dn,fn,ln,ad,gn,ph,ds,ex,qu,dob,doj,un)
        cursor.execute(sql)
        ut='emp'
        sql2="select max(hid) as hid from head"
        cursor.execute(sql2)
        result=cursor.fetchall()
        for r in result:
            sql3="insert into login(uid,uname,upass,utype)values('%s','%s','%s','%s')"%(r[0],un,pas,ut)
            cursor.execute(sql3)
        msg="<script>alert('successfully added');window.location='/viewemp/';</script>"
        return HttpResponse(msg)
    else:
         msg="<script>alert('Employee age must be greater than 18');window.location='/employees/';</script>"
         return HttpResponse(msg)

def viewemp(request):
    cursor=connection.cursor()
    s="SELECT * FROM head WHERE dname=(SELECT dname from head WHERE hid='%s')AND etype='emp'"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'hid':row[0],'dname':row[1],'fname':row[2],'lname':row[3],'address':row[4],'phone':row[5],'gender':row[6],'desig':row[7],'exp':row[8],'qual':row[9],'dob':row[10],'doj':row[11]}
        use.append(q)
    return render(request,'viewemp.html',{'use':use})

def empdelete(request):
    cursor=connection.cursor()
    delid=request.GET['id']
    s="delete from head where hid='%s'"%(delid)
    cursor.execute(s)
    msg="<script>alert('successfully deleteded');window.location='/viewemp/';</script>"
    return HttpResponse(msg)

def updateemp(request):
    cursor=connection.cursor()
    hid=request.GET['id']
    fn=request.GET['fname']
    ln=request.GET['lname']
    ad=request.GET['address']
    ph=request.GET['phone']
    gn=request.GET['gender']
    ds=request.GET['desig']
    ex=request.GET['exp']
    qu=request.GET['qual']
    dob=request.GET['dob']
    doj=request.GET['doj']
    s="update head set fname='%s',lname='%s',address='%s',phone='%s',gender='%s',desig='%s',exp='%s',qual='%s',dob='%s',doj='%s'where hid ='%s'" %(fn,ln,ad,ph,gn,ds,ex,qu,dob,doj,hid)
    cursor.execute(s)
    msg="<script>alert('successfully updated');window.location='/viewemp/';</script>"
    return HttpResponse(msg)

# def empupdate(request):
#     return render(request,'empupdate.html')

def empupdate(request):
    cursor=connection.cursor()
    upid=request.GET['id']
    s="select * from head where hid='%s'"%(upid)
    cursor.execute(s)
    rs=cursor.fetchall()
    tk=[]
    for row in rs:
        q={'hid':row[0],'fname':row[2],'lname':row[3],'address':row[4],'phone':row[5],'gender':row[6],'desig':row[7],'exp':row[8],'qual':row[9],'dob':row[10],'doj':row[11]}
        tk.append(q)
    return render(request,'empupdate.html',{'tk':tk})

def allocatedwork(request):
    cursor=connection.cursor()
    s="SELECT * FROM works WHERE dname=(SELECT dname from head where hid='%s')"%(request.session['uid'])
    cursor.execute(s)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'pcode':row[0],'dname':row[1],'pname':row[2],'descrip':row[3],'dos':row[4],'status':row[5]}
        use.append(q)
    return render(request,'allocatedwork.html',{'use':use})

def task(request):
    cursor=connection.cursor()
    pc=request.GET['id']
    m="SELECT * FROM head WHERE dname=(SELECT dname from head WHERE hid='%s')and hid NOT in(SELECT hid from task WHERE tid IN(SELECT tid FROM task WHERE pcode='%s'))AND etype='emp'"%(request.session['uid'],pc)
    cursor.execute(m)
    rs1=cursor.fetchall()
    cr=[]
    for row in rs1:
        sql={'hid':row[0],'dname':row[1],'fname':row[2],'lname':row[3],'address':row[4],'phone':row[5],'gender':row[6],'desig':row[7],'exp':row[8],'qual':row[9],'dob':row[10],'doj':row[11],'etype':row[13]}
        cr.append(sql)
    s="select * from task where pcode='%s'"%(pc)
    cursor.execute(s)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        s1="select fname from head  where hid='%s'" % (row[6])
        cursor.execute(s1)
        rsw=cursor.fetchall()
        if(cursor.rowcount>0):
            for m in rsw:
                q={'tid':row[0],'pcode':row[1],'tname':row[2],'details':row[3],'ldate':row[4],'status':row[5],'fname':m[0]}
                use.append(q)
        else:
            q={'tid':row[0],'pcode':row[1],'tname':row[2],'details':row[3],'ldate':row[4],'status':row[5],'hid':row[6]}
            use.append(q)
    return render(request,'task.html',{'pc':pc,'use':use,'cr':cr,'today':today})


def assigntask(request):
    cursor=connection.cursor()
    pc=request.GET['pcode']
    tn=request.GET['tname']
    de=request.GET['details']
    ld=request.GET['ldate']
    # st=request.GET['status']
    sql="insert into task(pcode,tname,details,ldate,status)values('%s','%s','%s','%s','pending')"%(pc,tn,de,ld)
    cursor.execute(sql)
    result=cursor.fetchall()
    msg="<script>alert('successfully added');window.location='/allocatedwork/';</script>"
    return HttpResponse(msg)

def assignedstaff(request):
    cursor=connection.cursor()
    tid=request.GET['tid']
    hid=request.GET['hid']
    pc=request.GET['id']
    print(tid)
    # sql4="insert into task_assign(tid,hid) values ('%s','%s')"%(dn,pn)
    # cursor.execute(sql4)
    s="update task set hid='%s' where tid ='%s'" %(hid,tid)
    cursor.execute(s)
    msg="<script>alert('successfully added');window.location='/task?id="+pc+"';</script>"
    return HttpResponse(msg)


# def assignedtasks(request):
#     cursor=connection.cursor()
#     s="SELECT * FROM task_assign INNER JOIN task on task_assign.tid=task.tid INNER JOIN head on task_assign.hid=head.hid where task_assign.hid='%s'"%(request.session['uid'])
#     print(s)
#     cursor.execute(s)
#     rs=cursor.fetchall()
#     use=[]
#     for row in rs:
#         q={'aid':row[0],'tid':row[1],'hid':row[2],'fname':row[11],'dname':row[10],'tname':row[5],'details':row[6],'ldate':row[7],'status':row[8]}
#         use.append(q)
#     return render(request,'assignedtasks.html',{'use':use})

def emphome(request):
    return render(request,'emphome.html')

def viewmytask(request):
    cursor=connection.cursor()
    # s="SELECT * FROM task_assign INNER JOIN task on task_assign.tid=task.tid INNER JOIN head on task_assign.hid=head.hid where task_assign.hid='%s'"%(request.session['uid'])
    # cursor.execute(s)
    s1="select * from task where hid= '%s'" % (request.session['uid']) 
    cursor.execute(s1)
    rs=cursor.fetchall()
    use=[]
    for row in rs:
        q={'tid':row[0],'pcode':row[1],'tname':row[2],'details':row[3],'ldate':row[4],'status':row[5]}
        use.append(q)
    return render(request,'viewmytask.html',{'use':use})

def statusm(request):
    cursor=connection.cursor()
    dn=request.GET['tid']
    st=request.GET['status']
    s="update task set status='%s' where tid ='%s'"%(st,dn)
    cursor.execute(s)
    print(s)
    msg="<script>alert('successfully updated');window.location='/viewmytask/';</script>"
    return HttpResponse(msg)

def statush(request):
    cursor=connection.cursor()
    dn=request.GET['pcode']
    st=request.GET['status']
    s="update works set status='%s' where pcode ='%s'"%(st,dn)
    cursor.execute(s)
    print(s)
    msg="<script>alert('successfully updated');window.location='/allocatedwork/';</script>"
    return HttpResponse(msg)

def questionair(request):
    cur=connection.cursor()
    dp=""
    s="select * from survey where empid='%s' and month=%s"%(request.session['uid'],todaym)
    print(s)
    cur.execute(s)
    if(cur.rowcount>0):
        rs=cur.fetchall()
        for r in rs:
            dp=r[2]
            print(dp)
        if(dp != 'Nil'):
             msg="<script>alert('Mental helath survey already attended for this month');window.location='/emphome/'</script>"
             return HttpResponse(msg)
        else:
              return render(request,'questionair.html')
    else:
          return render(request,'questionair.html')

def questions(request):
    cursor=connection.cursor()
    ag=request.GET['age']
    bt=request.GET['businesstravel']
    dr=request.GET['dailyrate']
    sa=request.GET['sales']
    di=request.GET['distance']
    ed=request.GET['edu']
    ef=request.GET['edufield']
    ge=request.GET['gender']
    en=request.GET['environment']
    ho=request.GET['hourly']
    ji=request.GET['jobinvo']
    jl=request.GET['joblevel']
    jr=request.GET['jobrole']
    js=request.GET['jobsat']
    ma=request.GET['martial']
    mo=request.GET['monthlyin']
    nc=request.GET['nocompany']
    ot=request.GET['overtime']
    pe=request.GET['performance']
    re=request.GET['relationship']
    st=request.GET['stock']
    to=request.GET['totalworking']
    wl=request.GET['worklife']
    ya=request.GET['yearsat']
    yi=request.GET['yearsin']
    ys=request.GET['yearssince']
    yw=request.GET['yearswith']
    return render(request,'questionair.html')

def stressdet(request):
    cur=connection.cursor()
    dp=""
    s="select * from survey where empid='%s' and month=%s"%(request.session['uid'],todaym)
    print(s)
    cur.execute(s)
    if(cur.rowcount>0):
        rs=cur.fetchall()
        for r in rs:
            dp=r[3]
            print(dp)
        if(dp != 'Nil'):
             msg="<script>alert('Mental helath survey already attended for this month');window.location='/emphome/'</script>"
             return HttpResponse(msg)
        else:
              return render(request,'stressdet.html')
    else:
          return render(request,'stressdet.html')

def detection(request):
    cursor=connection.cursor()
    qa1=request.GET['question1']
    print(qa1)
    qa2=request.GET['question2']
    qa3=request.GET['question3']
    qa4=request.GET['question4']
    qa5=request.GET['question5']
    qa6=request.GET['question6']
    qa7=request.GET['question7']
    qa8=request.GET['question8']
    qa9=request.GET['question9']
    qa10=request.GET['question10']
    qa11=request.GET['question11']
    qa12=request.GET['question12']
    qa13=request.GET['question13']
    qa14=request.GET['question14']
    qa15=request.GET['question15']
    qa16=request.GET['question16']
    qa17=request.GET['question17']
    qa18=request.GET['question18']
    dpr=int(qa1+qa2+qa3+qa4+qa5+qa6+qa7+qa8+qa9+qa10+qa11+qa12+qa13+qa14+qa15+qa16+qa17+qa18)
    print(dpr)
    dep=""
    if(dpr>=0 and dpr<=9):
        dep="Depression Likely"
    elif(dpr>=10 and dpr<=17):
        dep="Possibiliy Mildly Depressed"
    elif(dpr>=18 and dpr<=21):
        dep="Borderline Depression"
    elif(dpr>=22 and dpr<=35):
        dep="Mild-Moderate Depression"
    elif(dpr>=36 and dpr<=53):
        dep="Moderate_Severe Depression"
    elif(dpr>=54):
        dep="Possibiliy Mildly Depressed"

    cursor.execute("insert into survey(empid,attr,stress,sdate,month)values('%s','Nil','%s','%s','%s')"%(request.session['uid'],dep,today,todaym))
    return render(request,'stressdet.html')

def logout(request):
  try:
    del request.session['uid']
    del request.session['utype']
  except:
    pass
  return HttpResponse("<script>alert('Logged out');window.location='/login/';</script>")





