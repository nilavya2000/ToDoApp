from django.urls import path
from .views import taskList, taskDetail, taskCreate, taskUpdate, taskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', taskList.as_view(), name='tasks'),
    path('task/<int:pk>', taskDetail.as_view(), name='task'),
    path('taskCreate/', taskCreate.as_view(), name='taskCreate'),
    path('taskUpdate/<int:pk>', taskUpdate.as_view(), name='taskUpdate'),
    path('taskDelete/<int:pk>', taskDelete.as_view(), name='taskDelete'),
]
