from django.urls import path
from members import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/print/',views.print, name='print'),
    path('memberslist/', views.UserList.as_view()),
    path('memberslist/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
   