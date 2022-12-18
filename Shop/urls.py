from django.urls import path
from . import views


app_name = 'Shop'
urlpatterns = [
    path('',views.index , name = 'index'),
    path('create/',views.create , name = 'create'),
    #path('/edit',views.edit , name = 'edit'),
    path('update/<int:id>',views.update , name = 'update'),
    path('delete/<int:id>',views.delete , name = 'delete'),
]
