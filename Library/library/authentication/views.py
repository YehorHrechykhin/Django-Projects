from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import CustomUser
from .forms import RegistrationForm, LoginUserForm
from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate


class Profile(ListView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user_info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_queryset(self):
        user = CustomUser.objects.get(pk=self.kwargs['id'])
        return user


class RegistrationUser(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        form.save()
        user = authenticate(email=form.cleaned_data.get('email'),
                            password=form.cleaned_data.get('password'),
                            first_name=form.cleaned_data.get('first_name'),
                            middle_name=form.cleaned_data.get('middle_name'),
                            last_name=form.cleaned_data.get('last_name'))
        current_user = CustomUser.get_by_email(email=form.cleaned_data.get('email'))
        if self.request.POST.get('role'):
            current_user.role = 1
            current_user.is_staff = True
        else:
            current_user.role = 0
        if self.request.POST.get('superuser'):
            current_user.is_superuser = True
        current_user.save()

        login(self.request, current_user)
        return redirect('profile', current_user.pk)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'id': self.request.user.pk})


def logout_user(request):
    logout(request)
    return redirect('login')


class AllUsers(ListView):
    model = CustomUser
    template_name = 'list_of_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        users = CustomUser.objects.exclude(email=self.request.user.email)
        return users

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


