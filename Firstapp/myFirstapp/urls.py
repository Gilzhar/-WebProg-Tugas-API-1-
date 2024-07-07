from django.urls import path
from myFirstapp import views
from myFirstapp import views_api

app_name = 'myFirstapp'
urlpatterns = [

    path('', views.readStudent, name='read-data-student'),
    path('create/', views.createStudent, name='create-data-student'),
    path('update/', views.updateStudent, name='update-data-student'),
    path('delete/', views.deleteStudent, name='delete-data-student'),

     #punya untuk course
    path('',views.readCourse, name='read-data-course'),
    path('create/', views.createCourse, name='create-data-course'),
    path('update/', views.updateCourse, name='update-data-course'),
    path('delete/', views.deleteCourse, name='delete-data-course'),

]