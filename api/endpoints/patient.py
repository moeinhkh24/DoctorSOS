from django.urls import path
from api.views import PatientListView, PatientRetrieveUpdateDestroyApiView

app_name = 'patient'

urlpatterns= [
    path('', PatientListView.as_view(),name = 'patient'),
    path('<uuid:pk>/', PatientRetrieveUpdateDestroyApiView.as_view() ,name='patient_detail')
]
