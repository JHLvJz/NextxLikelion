from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
# Create your views here.

class AddNewView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'AddNew.html'
    success_url = reverse_lazy('home')

class AddNewSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'AddNewSubject.html'
    success_url = reverse_lazy('home')

def home(request):
    subjects = Subject.objects.all
    majors = Major.objects.all()
    return render(request, 'home.html', {'subjects': subjects, 'majors':majors})

def major(request, major_pk):
    major = Major.objects.get(pk = major_pk)
    subjectgroup = Subject.objects.filter(major=major_pk)

    return render(request, 'MajorDetail.html', {
        'major': major,
        'subjects': subjectgroup,
    })


    #원래코드//
    # subject = Subject.objects.all()
    # educationMajor = Subject.objects.filter(major__name="교육학과")
    # return render(request, 'education.html', {'educationMajor': educationMajor})
    #참고해보기//
    # delSubject = Subject.objects.get(pk=subject_pk)
class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')
    
class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def DeleteMajorView(request, major_pk):
    major = Major.objects.get(pk=major_pk)
    major.delete()
    return redirect('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

