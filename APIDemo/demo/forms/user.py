from django.utils.decorators import method_decorator
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from demo.models.user import User
from demo.forms import form_decorators


class UserAddForm(forms.ModelForm):
    """
    User Add Form
    """

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'nickname',
            'email',
            'telephone',
            'sex',
        )
        widgets = {
            'username':
            forms.TextInput(attrs={'class': 'form-control'}),
            'password':
            forms.PasswordInput(attrs={'class': 'form-control'}),
            'nickname':
            forms.TextInput(attrs={'class': 'form-control'}),
            'email':
            forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone':
            forms.TextInput(attrs={'class': 'form-control'}),
            'sex':
            forms.Select(
                choices=((u'男', u'男'), (u'女', u'女')),
                attrs={'class': 'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):
    """
    User Add Form
    """

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'nickname',
            'email',
            'telephone',
            'sex',
        )
        widgets = {
            'username':
            forms.TextInput(attrs={'class': 'form-control'}),
            'password':
            forms.PasswordInput(attrs={'class': 'form-control'}),
            'nickname':
            forms.TextInput(attrs={'class': 'form-control'}),
            'email':
            forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone':
            forms.TextInput(attrs={'class': 'form-control'}),
            'sex':
            forms.Select(
                choices=((u'男', u'男'), (u'女', u'女')),
                attrs={'class': 'form-control'}),
        }


class UserRegisterForm(forms.ModelForm):
    """
    User Register Form
    """

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'nickname',
            'email',
            'telephone',
            'sex',
        )
        widgets = {
            'username':
            forms.TextInput(attrs={'class': 'form-control'}),
            'password':
            forms.PasswordInput(attrs={'class': 'form-control'}),
            'nickname':
            forms.TextInput(attrs={'class': 'form-control'}),
            'email':
            forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone':
            forms.TextInput(attrs={'class': 'form-control'}),
            'sex':
            forms.Select(
                choices=((u'男', u'男'), (u'女', u'女')),
                attrs={'class': 'form-control'}),
        }


@method_decorator(form_decorators, name='dispatch')
class UserCreate(SuccessMessageMixin, CreateView):
    template_name = 'demo/user/add.html'
    form_class = UserAddForm
    success_url = reverse_lazy('app:user:list')
    success_message = "用户%(nickname)s添加成功"


# @method_decorator(form_decorators, name='dispatch')
class UserRegister(SuccessMessageMixin, CreateView):
    template_name = 'user/add.html'
    # template_name = 'user/register.html'
    form_class = UserRegisterForm
    # success_url = reverse_lazy('/')
    success_url = '/'
    # success_message = "用户%(nickname)s注册成功"


@method_decorator(form_decorators, name='dispatch')
class UserUpdate(SuccessMessageMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'demo/user/edit.html'
    success_url = reverse_lazy('app:user:list')
    success_message = "用户%(nickname)s更新成功"

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs.get('pk'))


@method_decorator(form_decorators, name='dispatch')
class UserDelete(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'demo/user/delete.html'
    success_url = reverse_lazy('app:user:list')
    success_message = "用户%(nickname)s删除成功"
