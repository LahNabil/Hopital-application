from django.shortcuts import render,get_object_or_404,redirect
from .models import Patient
from faker import Faker
from .form import PatientForm



f = Faker()

# Create your views here.
def list_patients(request):

    '''for i in range(10):
        Patient(None,f.name(),f.date(),).save()
        '''

    patients = Patient.objects.all()
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

