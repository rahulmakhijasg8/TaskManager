from django.urls import path
from .views import RedirectView, TaskViewset, AdminMailSend
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('tasks', TaskViewset, basename='task')

urlpatterns = [
    path('login/', RedirectView),
    path('emailsend/',AdminMailSend.as_view())
]

urlpatterns = urlpatterns + router.urls