from django.urls import path
from . import views

urlpatterns = [
    path('initiate-call/', views.InitiateCallView.as_view(), name= 'initiate_call_api'),
    path('call-report/', views.CallReportView.as_view()),
    path('call-update/<int:id>', views.Call_Update_DeleteView.as_view()),
]