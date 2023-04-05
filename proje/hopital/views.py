from django.shortcuts import render,get_object_or_404,redirect
from .models import Patient
from faker import Faker
from .form import PatientForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



f = Faker()

# Create your views here.
def list_patients(request):

    '''for i in range(10):
        Patient(None,f.name(),f.date(),).save()
        '''

    all_patients = Patient.objects.all()
    p = Paginator(all_patients, 5)
    page = request.GET.get('page',1)
    try:
        patients = p.page(page)
    except PageNotAnInteger:
        patients = p.page(1)
    except EmptyPage:
        patients = p.page(p.num_pages)
    return render(request,'patients.html',{'patients': patients})

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_patients')
    else:
            form = PatientForm()
            return render(request, 'create_patient.html',{'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('list_patients')

def update_patient(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('list_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'update_patient.html',{'form': form, 'patient':patient})

def search(request):
    query = request.GET.get('keyword')
    patients = Patient.objects.filter(nom__contains=query)
    return render(request,'patients.html',{'patients': patients})