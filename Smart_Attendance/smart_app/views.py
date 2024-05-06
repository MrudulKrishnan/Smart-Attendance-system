from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse


# Create your views here.


# /////////////////////////////ADMIN/////////////
from smart_app.models import *


def log(request):
    return render(request, "login_index.html")


def logout(request):
    auth.logout(request)
    return render(request, "login_index.html")


def login_action(request):
    username1 = request.POST['username']
    password1 = request.POST['password']
    ob = Login.objects.get(Username=username1, Password=password1)
    try:
        if ob.Type == 'admin':
            auth_obj = auth.authenticate(username="admin", password="admin")
            if auth_obj is not None:
                auth.login(request, auth_obj)
            return HttpResponse('''<script>alert("welcome ");window.location="/admin_home"</script>''')
        elif ob.Type == 'college':
            auth_obj = auth.authenticate(username="admin", password="admin")
            if auth_obj is not None:
                auth.login(request, auth_obj)
            request.session['college_lid'] = ob.id
            return HttpResponse('''<script>alert("welcome ");window.location="/college_home"</script>''')
        elif ob.Type == 'staff':
            auth_obj = auth.authenticate(username="admin", password="admin")
            if auth_obj is not None:
                auth.login(request, auth_obj)
            request.session['staff_lid'] = ob.id
            return HttpResponse('''<script>alert("welcome ");window.location="/staff_home"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid user");window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("invalid user");window.location="/"</script>''')


@login_required(login_url='/')
def admin_home(request):
    return render(request, "admin/admin_home.html")


@login_required(login_url='/')
def addcamera(request):
    return render(request, "admin/add_camera.html")


@login_required(login_url='/')
def addcamera_add(request):
    name = request.POST['textfield']
    no = request.POST['textfield3']

    oa = Camera()
    oa.name = name
    oa.no = no
    oa.save()
    return HttpResponse('''<script>alert("Added ");window.location="/addcamera#about"</script>''')


@login_required(login_url='/')
def add_camera_add(request):
    return render(request, "admin/add_camera_add.html")


@login_required(login_url='/')
def add_college(request):
    return render(request, "admin/add_college.html")


@login_required(login_url='/')
def add_college_action(request):
    name = request.POST['textfield']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']
    username = request.POST['textfield8']
    password = request.POST['textfield2']

    ob = Login()
    ob.Username = username
    ob.Password = password
    ob.Type = 'college'
    ob.save()

    ob1 = College()
    ob1.LOGIN = ob
    ob1.name = name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.phone = phone
    ob1.email = email
    ob1.save()
    return HttpResponse('''<script>alert("Added ");window.location="/manage_college#about"</script>''')


@login_required(login_url='/')
def feedback(request):
    fb_obj = Feedback.objects.all()
    return render(request, "admin/feedback.html", {'fb_obj': fb_obj})


@login_required(login_url='/')
def manage_college(request):
    college_obj = College.objects.all()
    return render(request, "admin/manage_college.html", {'college_obj': college_obj})


@login_required(login_url='/')
def edit_college(request, college_id):
    request.session['college_id'] = college_id
    college_obj = College.objects.get(LOGIN=college_id)
    return render(request, "admin/edit COLLEGE.html", {'college_obj': college_obj})


@login_required(login_url='/')
def edit_college_action(request):
    ob1 = College.objects.get(LOGIN=request.session['college_id'])
    name = request.POST['textfield']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']

    ob1.name = name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.phone = phone
    ob1.email = email
    ob1.save()
    return HttpResponse('''<script>alert("college updated ");window.location="/manage_college#about"</script>''')


@login_required(login_url='/')
def delete_college(request, college_id):
    clg_obj = College.objects.get(LOGIN=college_id)
    clg_obj.delete()
    return HttpResponse('''<script>alert("college deleted ");window.location="/manage_college#about"</script>''')


@login_required(login_url='/')
def sendnoti(request):
    return render(request, "admin/send_notific2.html")


@login_required(login_url='/')
def send_notification(request):
    noti_obj = Notification.objects.all()
    return render(request, "admin/send_notification.html", {'noti_obj': noti_obj})


@login_required(login_url='/')
def sendnoti_post(request):
    notification = request.POST['textarea']
    oc = Notification()
    oc.notification = notification
    oc.date = datetime.today()
    oc.save()
    return HttpResponse('''<script>alert("Notification sent ");window.location="/send_notification#about"</script>''')


@login_required(login_url='/')
def delete_notification(request, notification_id):
    notification_obj = Notification.objects.get(id=notification_id)
    notification_obj.delete()
    return HttpResponse('''<script>alert("Notification deleted ");window.location="/send_notification#about"</script>''')


@login_required(login_url='/')
def reply(request, reply_id):
    request.session['reply_id'] = reply_id
    return render(request,"admin/reply.html")


@login_required(login_url='/')
def reply_action(request):
    reply1 = request.POST['textarea']
    comp_obj = Complaint.objects.get(id=request.session['reply_id'])
    comp_obj.reply = reply1
    comp_obj.save()
    return HttpResponse('''<script>alert("Reply sent ");window.location="/viewcomplaint#about"</script>''')


@login_required(login_url='/')
def view_rating(request):
    rating_obj = Rating.objects.all()
    return render(request, "admin/view_rating.html", {'rating_obj': rating_obj})


@login_required(login_url='/')
def rating_search(request):
    type = request.POST['select']
    rating_obj = Rating.objects.filter(LOGIN__Type=type)
    return render(request, "admin/view_rating.html", {'rating_obj': rating_obj})


@login_required(login_url='/')
def view_complaint(request):
    comp_obj = Complaint.objects.all()
    return render(request, "admin/view_complaint.html", {'comp_obj': comp_obj})


@login_required(login_url='/')
def complaint_reply(request):
    reply1 = request.POST['textarea']
    od = Complaint()
    od.reply = reply1
    od.date = datetime.today()
    od.save()
    return HttpResponse('''<script>alert("Reply sent ");window.location="/view_complaint#about"</script>''')


@login_required(login_url='/')
def add_department(request):
    department_obj = Department.objects.all()
    return render(request, "admin/add_department.html", {'department_obj': department_obj})


@login_required(login_url='/')
def add_dep_2(request):
    return render(request, "admin/add_dep_2.html")


@login_required(login_url='/')
def add_department_post(request):
    departments = request.POST['textfield']
    ob = Department()
    ob.department = departments
    ob.save()
    return HttpResponse('''<script>alert("Department Added ");window.location="/add_department#about"</script>''')


@login_required(login_url='/')
def delete_department(request, department_id):
    department_obj = Department.objects.get(id=department_id)
    department_obj.delete()
    return HttpResponse('''<script>alert("Department Deleted ");window.location="/add_department#about"</script>''')

# /////////////////////////////college/////////////


@login_required(login_url='/')
def college_home(request):
    return render(request, "college/college_home.html")


@login_required(login_url='/')
def manage_staff(request):
    staff_obj = Staff.objects.all()
    return render(request, "college/manage_staff.html", {'staff_obj': staff_obj})


@login_required(login_url='/')
def add_staff(request):
    department_obj = Department.objects.all()
    return render(request, "college/add_staff.html", {'department_obj': department_obj})


@login_required(login_url='/')
def add_staff_action(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    department = request.POST['select']
    age = request.POST['textfield9']
    phone = request.POST['textfield4']
    pin = request.POST['textfield5']
    email = request.POST['textfield6']
    username = request.POST['textfield7']
    password = request.POST['textfield8']

    login_obj = Login()
    login_obj.Username = username
    login_obj.Password = password
    login_obj.Type = 'staff'
    login_obj.save()

    staff_obj = Staff()
    staff_obj.name = name
    staff_obj.place = place
    staff_obj.post = post
    staff_obj.DEPARTMENT_ID = Department.objects.get(id=department)
    staff_obj.COLLEGE = College.objects.get(LOGIN_id=request.session['college_lid'])
    staff_obj.age = age
    staff_obj.phone = phone
    staff_obj.pin = pin
    staff_obj.email = email
    staff_obj.LOGIN = login_obj
    staff_obj.save()
    return HttpResponse('''<script>alert("Added ");window.location="/manage_staff#about"</script>''')


@login_required(login_url='/')
def edit_staff(request, staff_id):
    request.session['staff_id'] = staff_id
    department_obj = Department.objects.all()
    staff_obj = Staff.objects.get(id=staff_id)
    return render(request, "college/edit_staff.html", {'department_obj': department_obj, 'staff_obj': staff_obj})


@login_required(login_url='/')
def edit_staff_action(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    department = request.POST['select']
    age = request.POST['textfield9']
    phone = request.POST['textfield4']
    pin = request.POST['textfield5']
    email = request.POST['textfield6']
    staff_obj = Staff.objects.get(id=request.session['staff_id'])
    staff_obj.name = name
    staff_obj.place = place
    staff_obj.post = post
    staff_obj.department = department
    staff_obj.age = age
    staff_obj.phone = phone
    staff_obj.pin = pin
    staff_obj.email = email
    staff_obj.save()
    return HttpResponse('''<script>alert("Updated");window.location="/manage_staff#about"</script>''')


@login_required(login_url='/')
def delete_staff(request, staff_id):
    staff_obj = Staff.objects.get(id=staff_id)
    staff_obj.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_staff#about"</script>''')


@login_required(login_url='/')
def add_rating(request):
    return render(request, "college/add_rating.html")


@login_required(login_url='/')
def add_rating_action_clg(request):
    rating = request.POST['select']
    review = request.POST['review']
    ob = Rating()
    ob.LOGIN = Login.objects.get(id=request.session['college_lid'])
    ob.rating = rating
    ob.review = review
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("THANKYOU FOR YOUR RATING ");window.location="/college_home#about"</script>''')


@login_required(login_url='/')
def sendfeedback_college(request):
    return render(request, "college/send_feedback.html")


@login_required(login_url='/')
def sendfeedback_college_send(request):
    feedback = request.POST['textarea']
    ob = Feedback()
    ob.LOGIN = Login.objects.get(id=request.session['college_lid'])
    ob.feedback = feedback
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("FEEDBACK SENT ");window.location="/college_home#about"</script>''')


@login_required(login_url='/')
def view_notification(request):
    notification_obj = Notification.objects.all()
    return render(request, "college/view_notification.html", {'notification_obj': notification_obj})


@login_required(login_url='/')
def view_attendance_college(request):
    college_obj = College.objects.get(LOGIN=request.session['college_lid'])
    student_obj = Student.objects.filter(COLLEGE_id=college_obj.id)
    department_obj = Department.objects.all()
    return render(request, "college/search_student_attendance_college.html", {'student_obj': student_obj, 'department_obj': department_obj})


@login_required(login_url='/')
def view_attendance_college_action(request):
    student_name = request.POST['student']
    department = request.POST['department']
    attendance_obj = Attendance.objects.filter(STUDENT_ID__first_name__startswith=student_name, STUDENT_ID__DEPARTMENT=department)
    return render(request, "college/view_attendance_college.html", {'attendance_obj': attendance_obj})


#//////////////////////////STAFF////////////////////


@login_required(login_url='/')
def staff_home(request):
    return render(request, "staff/staff_home.html")


@login_required(login_url='/')
def add_rating_staff(request):
    return render(request, "staff/add_rating_staff.html")


@login_required(login_url='/')
def add_rating_action(request):
    rating = request.POST['select']
    review = request.POST['review']
    ob = Rating()
    ob.LOGIN = Login.objects.get(id=request.session['staff_lid'])
    ob.rating = rating
    ob.review = review
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("THANKYOU FOR YOUR RATING ");window.location="/staff_home#about"</script>''')


@login_required(login_url='/')
def sent_rating(request):
    rating = request.POST['select']
    ob = Rating()
    ob.LOGIN = Login.objects.get(id=request.session['staff_lid'])
    ob.rating = rating
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("THANKYOU FOR YOUR RATING ");window.location="/staff_home#about"</script>''')


@login_required(login_url='/')
def manage_student(request):
    student_obj = Student.objects.all()
    return render(request, "staff/manage_student.html", {'student_obj': student_obj})


@login_required(login_url='/')
def add_student(request):
    ob = Department.objects.all()
    return render(request, "staff/add_student.html", {'val': ob})


@login_required(login_url='/')
def add_student_action(request):
    firstname = request.POST['textfield']
    lastname = request.POST['textfield10']
    place = request.POST['place']
    post = request.POST['textfield3']
    pin = request.POST['textfield2']
    phone = request.POST['textfield4']
    email = request.POST['textfield5']
    photo = request.FILES['photo']
    fss = FileSystemStorage()
    photo_file = fss.save(photo.name, photo)
    dept = request.POST['select']
    username = request.POST['textfield6']
    password = request.POST['textfield7']

    login_obj = Login()
    login_obj.Username = username
    login_obj.Password = password
    login_obj.Type = 'student'
    login_obj.save()

    student_obj = Student()
    student_obj.first_name = firstname
    student_obj.last_name = lastname
    student_obj.place = place
    student_obj.post = post
    student_obj.pin = pin
    student_obj.phone = phone
    student_obj.email = email
    student_obj.photo = photo_file
    student_obj.LOGIN = login_obj
    staff_obj = Staff.objects.get(LOGIN_id=request.session['staff_lid'])
    student_obj.COLLEGE = staff_obj.COLLEGE
    student_obj.DEPARTMENT = Department.objects.get(id=dept)
    student_obj.save()

    return HttpResponse('''<script>alert("Added ");window.location="/manage_student#about"</script>''')


@login_required(login_url='/')
def update_student(request, student_id):
    request.session['student_id'] = student_id
    student_obj = Student.objects.get(id=student_id)
    ob = Department.objects.all()
    return render(request, "staff/update_student.html", {'val': ob, 'student_obj': student_obj})


@login_required(login_url='/')
def update_student_action(request):
    student_obj = Student.objects.get(id=request.session['student_id'])
    firstname = request.POST['textfield']
    lastname = request.POST['textfield10']
    place = request.POST['place']
    post = request.POST['textfield3']
    pin = request.POST['textfield2']
    phone = request.POST['textfield4']
    email = request.POST['textfield5']
    dept = request.POST['select']

    student_obj.first_name = firstname
    student_obj.last_name = lastname
    student_obj.place = place
    student_obj.post = post
    student_obj.pin = pin
    student_obj.phone = phone
    student_obj.department = dept
    student_obj.email = email
    staff_obj = Staff.objects.get(LOGIN_id=request.session['staff_lid'])
    student_obj.COLLEGE = staff_obj.COLLEGE
    student_obj.DEPARTMENT = Department.objects.get(id=dept)
    student_obj.save()
    return HttpResponse('''<script>alert("Updated ");window.location="/manage_student#about"</script>''')


@login_required(login_url='/')
def delete_student(request, student_id):
    student_obj = Student.objects.get(id=student_id)
    student_obj.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location="/manage_student#about"</script>''')


@login_required(login_url='/')
def view_attendance(request):
    staff_obj = Staff.objects.get(LOGIN=request.session['staff_lid'])
    student_obj = Student.objects.filter(COLLEGE_id=staff_obj.COLLEGE.id, DEPARTMENT=staff_obj.DEPARTMENT_ID)
    return render(request, "staff/search_student_attendance.html", {'student_obj': student_obj})


@login_required(login_url='/')
def search_attendance_action(request):
    student_name = request.POST['select']
    attendance_obj = Attendance.objects.filter(STUDENT_ID__first_name__startswith=student_name)
    return render(request, "staff/view_attendance_staff.html", {'attendance_obj': attendance_obj})


@login_required(login_url='/')
def search_attendance_date(request):
    student_name = request.POST['select']
    date = request.POST['Date']
    attendance_obj = Attendance.objects.filter(STUDENT_ID__first_name__startswith=student_name, Date=date)
    return render(request, "staff/view_attendance_staff.html", {'attendance_obj': attendance_obj})


@login_required(login_url='/')
def sendfeedback(request):
    return render(request, "staff/send_feedback.html")


@login_required(login_url='/')
def sendfeedback_post(request):
    feedback = request.POST['textarea']
    ob = Feedback()
    ob.LOGIN = Login.objects.get(id=request.session['staff_lid'])
    ob.feedback = feedback
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("FEEDBACK SENT ");window.location="/staff_home#about"</script>''')


def manage_camera(request):
    college_obj = College.objects.all()
    camera_obj = Camera.objects.all()
    return render(request, "admin/manage_camera.html", {'camera_obj': camera_obj, 'college_obj': college_obj})


def search_college(request):
    college_obj = College.objects.all()
    college_id = request.POST['college']
    camera_obj = Camera.objects.filter(COLLEGE_id=college_id)
    return render(request, "admin/manage_camera.html", {'college_obj': college_obj, 'camera_obj': camera_obj})


def add_camera(request):
    college_obj = College.objects.all()
    department_obj = Department.objects.all()
    return render(request, "admin/add_camera.html", {'college_obj': college_obj, 'department_obj': department_obj})


def add_camera_action(request):
    college_id = request.POST['college']
    department_id = request.POST['department']
    camera_no = request.POST['CameraNo']
    camera_obj = Camera()
    camera_obj.COLLEGE = College.objects.get(id=college_id)
    camera_obj.DEPARTMENT = Department.objects.get(id=department_id)
    camera_obj.camera = camera_no
    camera_obj.date = datetime.now().today()
    camera_obj.save()
    return HttpResponse('''<script>alert("Camera added");window.location="/manage_camera#about"</script>''')


def delete_camera(request, cam_id):
    cam_obj = Camera.objects.get(id=cam_id)
    cam_obj.delete()
    return HttpResponse('''<script>alert("Camera deleted");window.location="/manage_camera#about"</script>''')

# @login_required(login_url='/')
# def view_emotions(request):
#     return render(request, )


    #////////////////////////////////WEBSERVICE/////////////////////////////////
    #/////////////////////////////////STUDENT///////////////////////////////////


def login_code(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        login_obj = Login.objects.get(Username=username, Password=password)
        if login_obj is None:
            data = {"task": "invalid"}
            return JsonResponse(data)
        elif login_obj.Type == "student":
            request.session['worker_id'] = login_obj.id
            data = {"task": "worker", "id": login_obj.id}
            return JsonResponse(data)
    except Exception as e:
        print(e)
        data = {"task": "invalid"}
        return JsonResponse(data)


def view_attendance_student(request):
    login_id = request.POST['lid']
    total = 0
    prog_obj = Attendance.objects.filter(STUDENT_ID__LOGIN=login_id)
    for i in prog_obj:
        total = int(i.Attendance)+total

    attendance = (total/len(prog_obj))*100
    print("____________________ atten,  max, totA", attendance, len(prog_obj), total)
    data = {'Attendance': attendance}
    r = json.dumps(data)
    return HttpResponse(r)


def send_complaint(request):
    complaints = request.POST["complaint"]
    student_id = request.POST["lid"]
    reply1 = "waiting"
    complaint_obj = Complaint()
    complaint_obj.complaint = complaints
    complaint_obj.date = datetime.now().strftime("%d/%m/%y")
    complaint_obj.reply = reply1
    complaint_obj.STUDENT = Student.objects.get(LOGIN=student_id)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)


def view_complaint_reply(request):
    student_id = request.POST['lid']
    complaint_obj = Complaint.objects.filter(STUDENT__LOGIN=student_id)
    data = []
    for i in complaint_obj:
        row = {'Complaint': i.complaint, 'Reply': i.reply, 'Date': str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def send_feedback(request):
    feedback = request.POST["Feedback"]
    student_id = request.POST["lid"]
    feedback_obj = Feedback()
    feedback_obj.feedback = feedback
    feedback_obj.date = datetime.now()
    feedback_obj.LOGIN = Login.objects.get(id=student_id)
    feedback_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)


def send_rating(request):
    rating = request.POST["Rating"]
    review = request.POST["Review"]
    lid = request.POST["lid"]
    rating_obj = Rating()
    rating_obj.rating = rating
    rating_obj.date = datetime.now()
    rating_obj.review = review
    rating_obj.LOGIN = Login.objects.get(id=lid)
    rating_obj.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)





