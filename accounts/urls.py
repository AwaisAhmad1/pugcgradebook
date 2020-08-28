from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from PUGCGRADEBOOK import settings
from accounts import StudentViews, StaffViews
from . import views, AdminViews, StaffViews, StudentViews
from django.core.mail import send_mail

from .EditResultViewClass import EditResultViewClass

urlpatterns = [
         #views URP path
        path('accounts/', include('django.contrib.auth.urls')),
        path('',views.ShowLoginPage, name="show_login"),
        path('doLogin',views.doLogin, name="do_login"),
        path('get_user_details',views.GetUserDetials, name="get_user_detail"),
        path('logout_user',views.logout_user, name="logout_user"),
        # Admin URL Path
        path('admin_home',AdminViews.admin_home, name="admin_home"),
        path('add_staff',AdminViews.add_staff, name="add_staff"),
        path('add_staff_save',AdminViews.add_staff_save, name="add_staff_save"),
        path('add_department',AdminViews.add_department, name="add_department"),
        path('add_department_save',AdminViews.add_department_save, name="add_department_save"),
        path('add_program',AdminViews.add_program, name="add_program"),
        path('add_program_save',AdminViews.add_program_save, name="add_program_save"),
        path('add_student',AdminViews.add_student, name="add_student"),
        path('add_student_save',AdminViews.add_student_save, name="add_student_save"),
        path('add_subject',AdminViews.add_subject, name="add_subject"),
        path('add_subject_save',AdminViews.add_subject_save, name="add_subject_save"),
        path('manage_staff',AdminViews.manage_staff, name="manage_staff"),
        path('manage_student',AdminViews.manage_student, name="manage_student"),
        path('manage_department',AdminViews.manage_department, name="manage_department"),
        path('manage_program',AdminViews.manage_program, name="manage_program"),
        path('manage_subject',AdminViews.manage_subject, name="manage_subject"),
        path('edit_staff/<str:staff_id>',AdminViews.edit_staff, name="edit_staff"),
        path('edit_staff_save', AdminViews.edit_staff_save, name="edit_staff_save"),
        path('edit_student/<str:student_id>',AdminViews.edit_student, name="edit_student"),
        path('edit_student_save', AdminViews.edit_student_save, name="edit_student_save"),
        path('edit_subject/<str:subject_id>',AdminViews.edit_subject, name="edit_subject"),
        path('edit_subject_save', AdminViews.edit_subject_save, name="edit_subject_save"),
        path('edit_department/<str:department_id>', AdminViews.edit_department, name="edit_department"),
        path('edit_department_save', AdminViews.edit_department_save, name="edit_department_save"),
        path('edit_program/<str:course_id>', AdminViews.edit_program, name="edit_program"),
        path('edit_program_save', AdminViews.edit_program_save, name="edit_program_save"),
        path('manage_session', AdminViews.manage_session, name="manage_session"),
        path('add_session_save', AdminViews.add_session_save, name="add_session_save"),
        path('check_email_exist',AdminViews.check_email_exist,name="check_email_exist"),
        path('check_username_exist',AdminViews.check_username_exist,name="check_username_exist"),
        path('check_roll_number_exist',AdminViews.check_roll_number_exist,name="check_roll_number_exist"),
        path ('student_feedback_message' , AdminViews.student_feedback_message , name="student_feedback_message") ,
        path ('student_feedback_message_replied' , AdminViews.student_feedback_message_replied , name="student_feedback_message_replied") ,
        path ('staff_feedback_message' , AdminViews.staff_feedback_message , name="staff_feedback_message") ,
        path ('staff_feedback_message_replied' , AdminViews.staff_feedback_message_replied ,name="staff_feedback_message_replied") ,
        path('student_leave_view', AdminViews.student_leave_view,name="student_leave_view"),
        path('staff_leave_view', AdminViews.staff_leave_view,name="staff_leave_view"),
        path ('student_approve_leave/<str:leave_id>' , AdminViews.student_approve_leave , name="student_approve_leave") ,
        path ('student_disapprove_leave/<str:leave_id>' , AdminViews.student_disapprove_leave , name="student_disapprove_leave") ,
        path ('staff_disapprove_leave/<str:leave_id>' , AdminViews.staff_disapprove_leave , name="staff_disapprove_leave") ,
        path ('staff_approve_leave/<str:leave_id>' , AdminViews.staff_approve_leave , name="staff_approve_leave") ,
        path('admin_view_attendance', AdminViews.admin_view_attendance,name="admin_view_attendance"),
        path ('admin_get_attendance_dates' , AdminViews.admin_get_attendance_dates , name="admin_get_attendance_dates") ,
        path('admin_get_attendance_student', AdminViews.admin_get_attendance_student,name="admin_get_attendance_student"),
        path('admin_profile', AdminViews.admin_profile,name="admin_profile"),
          path('admin_profile_save', AdminViews.admin_profile_save,name="admin_profile_save"),


        # Staff URL Path
        path('staff_home', StaffViews.staff_home, name="staff_home"),
        path('staff_take_attendance', StaffViews.staff_take_attendance, name="staff_take_attendance"),
        path('staff_update_attendance', StaffViews.staff_update_attendance, name="staff_update_attendance"),
        path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
        path('get_attendance_student', StaffViews.get_attendance_student, name="get_attendance_student"),
        path('save_updateattendance_data', StaffViews.save_updateattendance_data, name="save_updateattendance_data"),
        path('staff_apply_leave', StaffViews.staff_apply_leave, name="staff_apply_leave"),
        path('staff_apply_leave_save', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
        path('staff_feedback', StaffViews.staff_feedback, name="staff_feedback"),
        path('staff_feedback_save', StaffViews.staff_feedback_save, name="staff_feedback_save"),
        path('get_students', StaffViews.get_students, name="get_students"),
        path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
        path ('staff_profile' , StaffViews.staff_profile , name="staff_profile") ,
        path ('staff_profile_save' , StaffViews.staff_profile_save , name="staff_profile_save") ,
        path ('staff_add_result' , StaffViews.staff_add_result , name="staff_add_result") ,
        path('save_student_result', StaffViews.save_student_result, name="save_student_result"),
        path('edit_student_result',EditResultViewClass.as_view(), name="edit_student_result"),
        path('fetch_result_student',StaffViews.fetch_result_student, name="fetch_result_student"),

        # Student URL Path
        path('student_home', StudentViews.student_home, name="student_home"),
        path('student_view_attendance', StudentViews.student_view_attendance, name="student_view_attendance"),
        path('student_view_attendance_post', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
        path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
        path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
        path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
        path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
        path ('student_profile' , StudentViews.student_profile , name="student_profile") ,
        path ('student_profile_save' , StudentViews.student_profile_save , name="student_profile_save") ,
        path('student_view_result',StudentViews.student_view_result,name="student_view_result"),

]
