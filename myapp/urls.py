from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('signup/', views.SignUpView.as_view(), name="login"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('signin/', views.LoginView.as_view(), name="signin"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path("detail/<int:pk>", views.TodoDetail.as_view(), name="detail"),
    path("create/", views.TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", views.TodoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.TodoDelete.as_view(), name="delete"),
]
