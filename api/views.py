from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from rest_framework.exceptions import  PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.core.mail import send_mail
# Create your views here.


def RedirectView(request):
        return redirect('/accounts/google/login')
    

class TaskViewset(ModelViewSet):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]
    queryset = None
    
    def get_queryset(self):
        self.queryset = Task.objects.filter(user=self.request.user).all()
        return super().get_queryset()
    
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied({
                'detail': 'Authentication required. Please log in using google, click on the below url.',
                'login_url': 'http://127.0.0.1:8000/api/login/'  # Provide your custom login URL here
            })
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    


class AdminMailSend(generics.GenericAPIView):
     from .serializers import AdminMailSendSerializer
     permission_classes = [IsAuthenticated, IsAdminUser]
     serializer_class = AdminMailSendSerializer
    
     def get(self, request):
        return Response({'Message':'Please enter the mail below to send the registration link.'})
     def post(self, request):
         serializer = self.get_serializer(data=request.data)
         if serializer.is_valid():
             message = f'Hi {serializer.validated_data['email']}, please register to aur application using this link http://127.0.0.1:8000/api/tasks/'
             
             send_mail('Registration link for sign in',message,'rahulmakhijals7@gmail.com',[serializer.validated_data['email']])
             return Response({'message':'Email sent successfully'})
         return Response({'message':'entered data in incorrect format'})
