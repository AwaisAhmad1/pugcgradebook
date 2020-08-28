from django import forms
from django.forms import ChoiceField
from accounts.models import Courses, SessionYearModel, Subjects, Students

class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    roll_number = forms.CharField(label="Roll Number", max_length=20, widget=forms.TextInput(attrs={"class": "form-control",}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control","id":"fname"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "autocomplete":"off"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete":"off"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    course_list = []
    courses = Courses.objects.all()
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    session_list = []
    sessions = SessionYearModel.objects.all()
    for session in sessions:
        small_session = (session.id, str(session.session_start_year) + "  TO  " + str(session.session_end_year))
        session_list.append(small_session)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )
    course = forms.ChoiceField(label="Course",choices=course_list, widget=forms.Select(attrs={"class": "form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", widget=forms.Select(attrs={"class": "form-control"}), choices=session_list)



class EditStudentForm(forms.Form):
    roll_number = forms.CharField(label="Roll Number", max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    course_list = []
    courses = Courses.objects.all()
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    session_list = []
    sessions = SessionYearModel.objects.all()
    for session in sessions:
        small_session = (session.id, str(session.session_start_year)+"  TO  "+str(session.session_end_year))
        session_list.append(small_session)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )
    course = forms.ChoiceField(label="Course",choices=course_list, widget=forms.Select(attrs={"class": "form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", widget=forms.Select(attrs={"class": "form-control"}), choices=session_list)

class EditResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.staff_id=kwargs.pop("staff_id")
        super(EditResultForm,self).__init__(*args,**kwargs)
        subject_list=[]
        try:
            subjects=Subjects.objects.filter(staff_id=self.staff_id)
            for subject in subjects:
                subject_single=(subject.id,subject.subject_name)
                subject_list.append(subject_single)
        except:
            subject_list=[]
        self.fields['subject_id'].choices=subject_list

    session_list=[]
    try:
        sessions=SessionYearModel.objects.all()
        for session in sessions:
            session_single=(session.id,str(session.session_start_year)+" TO "+str(session.session_end_year))
            session_list.append(session_single)
    except:
        session_list=[]

    subject_id=forms.ChoiceField(label="Subject",widget=forms.Select(attrs={"class":"form-control"}))
    session_ids=forms.ChoiceField(label="Session Year",choices=session_list,widget=forms.Select(attrs={"class":"form-control"}))
    student_ids=ChoiceNoValidation(label="Student",widget=forms.Select(attrs={"class":"form-control"}))
    mid_term=forms.CharField(label="Mid Term",widget=forms.TextInput(attrs={"class":"form-control"}))
    final_term=forms.CharField(label="Final Term",widget=forms.TextInput(attrs={"class":"form-control"}))
    sessional_marks = forms.CharField(label="Sessional Marks", widget=forms.TextInput(attrs={"class": "form-control"}))