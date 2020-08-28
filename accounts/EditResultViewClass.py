from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from accounts.forms import EditResultForm
from accounts.models import Students, Subjects, StudentResult


class EditResultViewClass(View):
    def get(self,request,*args,**kwargs):
        staff_id=request.user.id
        edit_result_form=EditResultForm(staff_id=staff_id)
        return render(request,"staff_template/edit_student_result.html",{"form":edit_result_form})

    def post(self,request,*args,**kwargs):
        form=EditResultForm(staff_id=request.user.id,data=request.POST)
        if form.is_valid():
            student_admin_id = form.cleaned_data['student_ids']
            mid_term = form.cleaned_data['mid_term']
            final_term = form.cleaned_data['final_term']
            sessional_marks = form.cleaned_data['sessional_marks']
            subject_id = form.cleaned_data['subject_id']

            student_obj = Students.objects.get(admin=student_admin_id)
            subject_obj = Subjects.objects.get(id=subject_id)
            result=StudentResult.objects.get(subject_id=subject_obj,student_id=student_obj)
            result.subject_mid_term=mid_term
            result.subject_final_term=final_term
            result.subject_sessional_marks = sessional_marks
            result.save()
            messages.success(request, "Successfully Updated Result")
            return HttpResponseRedirect(reverse("edit_student_result"))
        else:
            messages.error(request, "Failed to Update Result")
            form=EditResultForm(request.POST,staff_id=request.user.id)
            return render(request,"staff_template/edit_student_result.html",{"form":form})