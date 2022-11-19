



from django.urls import path
from app import views



urlpatterns = [
    path('', views.index, name='home'),
    path('weekly_task', views.weekly_task, name='weekly-task'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('<int:id>', views.updateTodo, name='update'),
]
