from django.urls import path
from authUser import views

app_name='authUser'

urlpatterns = [
    path('register/',views.registerStudent, name='registerStudent'),
    path('login/',views.userLogin,name='userLogin'),
    path('',views.userLogin,name='userLogin'),
]
