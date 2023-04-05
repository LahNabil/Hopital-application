from django.urls import path
from .views import list_patients,create_patient,delete_patient,update_patient,search

urlpatterns = [
    path('patients/', list_patients, name='list_patients'),
    path('create/', create_patient, name='create_patient'),
    path('search/', search, name='search'),
    path('delete/<int:pk>', delete_patient, name='delete_patient'),
    path('update/<int:pk>', update_patient, name='update_patient'),

]
