from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)

"""admin.site.register(Admin),
admin.site.register(Staffs),
admin.site.register(Courses),
admin.site.register(Subjects),
admin.site.register(Students),
admin.site.register(Attendance),
admin.site.register(AttendanceReport),
admin.site.register(LeaveReportStudent),
admin.site.register(LeaveReportStaff),"""
