from django.urls import path
from . import views
urlpatterns = [

    path("", views.log),
    path("admin_home", views.admin_home, name="admin_home"),
    path("addcamera", views.addcamera),
    path("add_college", views.add_college, name="add_college"),
    path("add_college_action", views.add_college_action, name="add_college_action"),
    path("feedback", views.feedback),
    path("manage_college", views.manage_college, name="manage_college"),
    path('edit_college/<int:college_id>', views.edit_college, name="edit_college"),
    path('edit_college_action', views.edit_college_action, name="edit_college_action"),
    path('delete_college/<int:college_id>', views.delete_college, name="delete_college"),
    path("sendnoti", views.sendnoti, name="sendnoti"),
    path("delete_notification/<int:notification_id>", views.delete_notification, name="delete_notification"),
    path("send_notification", views.send_notification, name="send_notification"),
    path("view_rating", views.view_rating, name="view_rating"),
    path('rating_search', views.rating_search, name="rating_search"),
    path("view_complaint", views.view_complaint, name="view_complaint"),
    path("login_action", views.login_action),
    path("add_camera_add", views.add_camera_add),
    path("addcamera_add", views.addcamera_add),
    path("sendnoti_post", views.sendnoti_post),
    path("reply/<int:reply_id>", views.reply, name="reply"),
    path("reply_action", views.reply_action, name="reply_action"),
    path("logout", views.logout, name="logout"),

    # ///////////////////////COLLEGE////////////////

    path("college_home", views.college_home, name="college_home"),
    path("manage_staff", views.manage_staff, name="manage_staff"),
    path("add_staff", views.add_staff, name="add_staff"),
    path("add_staff_action", views.add_staff_action, name="add_staff_action"),
    path('edit_staff/<int:staff_id>', views.edit_staff, name="edit_staff"),
    path('edit_staff_action', views.edit_staff_action, name="edit_staff_action"),
    path('delete_staff/<int:staff_id>', views.delete_staff, name="delete_staff"),
    path("add_rating", views.add_rating, name="add_rating"),
    path('add_rating_action_clg', views.add_rating_action_clg, name="add_rating_action_clg"),
    path("view_notification", views.view_notification, name="view_notification"),
    path("add_department", views.add_department, name="add_department"),
    path("delete_department/<int:department_id>", views.delete_department, name="delete_department"),
    path("add_dep_2", views.add_dep_2, name="add_dep_2"),
    path('view_attendance_college', views.view_attendance_college, name="view_attendance_college"),
    path('view_attendance_college_action', views.view_attendance_college_action, name="view_attendance_college_action"),
    path("add_department_post", views.add_department_post),
    path("sendfeedback_college", views.sendfeedback_college),
    path("sendfeedback_college_send", views.sendfeedback_college_send),
    path("sent_rating", views.sent_rating),


    # //////////////////////staff//////////////////

    path("staff_home", views.staff_home, name="staff_home"),
    path("add_rating_staff", views.add_rating_staff, name="add_rating_staff"),
    path('add_rating_action', views.add_rating_action, name="add_rating_action"),
    path("add_student", views.add_student, name="add_student"),
    path("add_student_action", views.add_student_action, name="add_student_action"),
    path('update_student/<int:student_id>', views.update_student, name="update_student"),
    path('update_student_action', views.update_student_action, name="update_student_action"),
    path('delete_student/<int:student_id>', views.delete_student, name="delete_student"),
    path("manage_student", views.manage_student, name="manage_student"),
    path('view_attendance', views.view_attendance, name="view_attendance"),
    path('search_attendance_action', views.search_attendance_action, name="search_attendance_action"),
    path('search_attendance_date', views.search_attendance_date, name="search_attendance_date"),
    path("sendfeedback", views.sendfeedback),
    path("sendfeedback_post", views.sendfeedback_post),
    path("manage_camera", views.manage_camera, name="manage_camera"),
    path("search_college", views.search_college, name="search_college"),
    path("add_camera", views.add_camera, name="add_camera"),
    path("add_camera_action", views.add_camera_action, name="add_camera_action"),
    path("delete_camera/<int:cam_id>", views.delete_camera, name="delete_camera"),
    # path("view_emotions", views.view_emotions, name="view_emotions"),


    # /////////////////////////////////STUDENT////////////////////////////////


    path('login_code', views.login_code, name="login_code"),
    path('view_attendance_student', views.view_attendance_student, name="view_attendance_student"),
    path('view_complaint_reply', views.view_complaint_reply, name="view_complaint_reply"),
    path('send_complaint', views.send_complaint, name="send_complaint"),
    path('send_feedback', views.send_feedback, name="send_feedback"),
    path('send_rating', views.send_rating, name="send_rating"),


]

