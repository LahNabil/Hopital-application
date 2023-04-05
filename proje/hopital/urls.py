from django.urls import path
from .views import list_patients,create_patient,delete_patient

urlpatterns = [
    path('patients/', list_patients, name='list_patients'),
    path('create/', create_patient, name='create_patient'),
    path('delete/<int:pk>', delete_patient, name='delete_patient'),

]
