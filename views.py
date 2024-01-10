from django.shortcuts import render
from .forms import InputForm
from .models import Member
from members.models import Member
from members.serializers import MemberSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
#from members.permissions import IsOwnerOrReadOnly

def members(request):
    context={}
    context['form']=InputForm()
    return render(request, "data.html", context)

def print(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('roll_no') and request.POST.get('city'):
            post=Member()
            post.firstname= request.POST.get('firstname')
            post.lastname= request.POST.get('lastname')
            post.roll_no= request.POST.get('roll_no')
            post.city= request.POST.get('city')
            post.save()

            return render(request, 'insert.html')
        else:
            return render(request,'data.html')
        
class UserList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserDetail(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]