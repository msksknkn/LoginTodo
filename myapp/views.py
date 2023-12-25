from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.views import LogoutView as BaseLogout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from .forms import SignUpForm, LoginForm
from django.views.generic import (ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from .models import CustomUser, Todo

# Create your views here.


class IndexView(TemplateView):
    template_name = "myapp/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # ログインしている場合、Homeにリダイレクト
            return redirect(reverse_lazy('myapp:home'))
        return super().dispatch(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "tasks"
    template_name = "myapp/home.html"
    login_url = "myapp:index"

    def get_success_url(self):
        return reverse('report:detail', kwargs={'pk': self.object.id})

    def get_queryset(self):
        current_user = self.request.user.username
        print(self.request.user.username)
        user_data = CustomUser.objects.get(
            username=current_user)
        if user_data:
            print(user_data)
            queryset = Todo.objects.filter(
                Q(user_name=user_data)).all()
            queryset = queryset.order_by("deadline")
        return queryset


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "myapp/login.html"
    success_url = reverse_lazy("myapp:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return response


class LoginView(BaseLogin):
    form_class = LoginForm
    template_name = "myapp/signin.html"
    success_url = reverse_lazy("myapp:home")


class LogoutView(BaseLogout):
    next_page = "myapp/index.html"


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "smallthing"
    template_name = "myapp/datail.html"


class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("myapp:home")
    template_name = "myapp/form.html"


class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    template_name = "myapp/form.html"
    success_url = reverse_lazy("myapp:home")


class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("myapp:home")
