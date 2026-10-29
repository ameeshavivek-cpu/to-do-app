from django.urls import path

from todo_app import views

urlpatterns = [
path('add_subject',views.add_subject,name='add_subject'),
path('content_view',views.content_view,name='content_view'),
path('delete_data/<int:id>/',views.delete_data,name='delete_data'),
path('update_data/<int:id>/',views.update_data,name='update_data'),
path('',views.index,name='index'),
path('dashboard1',views.dashboard1,name='dashboard1'),
]