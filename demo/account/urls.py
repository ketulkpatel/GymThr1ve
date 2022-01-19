from django.urls import path
from account import views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name="login"),
    path('viewprofile/', views.ViewProfileView.as_view(), name="viewprofile"),
    path('editprofile/', views.EditProfileView.as_view(), name="editprofile"),
    path('saveprofile/', views.SaveProfileView.as_view(), name="saveprofile"),
    path('register/', views.RegisterView.as_view(), name="register"),
    

]
