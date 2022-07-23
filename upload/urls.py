from django.urls import path
from upload import views


app_name='upload'

urlpatterns = [

    path('', views.material_list, name='material_list'),
    path('upload_story/', views.upload_material, name='upload_material'),

]
