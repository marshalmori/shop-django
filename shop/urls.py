from django.urls import path

from . import views

app_name = 'shop'

# <app_name: name>
# shop:index
# shop:single_course

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course')
]