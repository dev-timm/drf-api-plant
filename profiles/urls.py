from django.urls import path
from profiles import views 

urlpatterns = [
    path('profiles/', views.UserProfileList.as_view()),
    path('profiles/<int:pk>/', views.UserProfileDetail.as_view()),
]