from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView,UpdateView,DetailView,RedirectView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from forms import RegistrationForm

from models import Item,Variant,UserActionLog

from utils import send_log_signal

"""Item Views """

class ItemCreationView(CreateView):
    model = Item
    template_name = "Item_views/create.html"
    success_url = reverse_lazy("homepage")
    fields = ['product_code','product_name']

    def post(self, request, **kwargs):
        request.POST = request.POST
        usr = User.objects.get(id=1)

        message = "Created Item "+request.POST['product_name']
        UserActionLog.objects.create(user_id=usr,user_action="Created Item",log_msg=message,)

        send_log_signal("Created Item")

        return super(ItemCreationView, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ItemCreationView,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context

class ItemEditView(UpdateView):
    model = Item
    template_name = "Item_views/edit.html"
    success_url = reverse_lazy("homepage")
    fields = ['product_code','product_name']

    def post(self, request, **kwargs):
        request.POST = request.POST
        obj = self.get_object()
        changed = {}
        for key in obj.__dict__.keys():
            if key in request.POST.keys():
                if request.POST[key] != obj.__dict__[key]:
                    changed[key] = request.POST[key]
        usr = User.objects.get(id=1)

        message = ""
        for key in changed.keys():
            message+= key +" changed to "+changed[key]+".";

        UserActionLog.objects.create(user_id=usr,user_action="Updated Item",log_msg=message,)

        send_log_signal("Updated Item "+message)

        return super(ItemEditView, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ItemEditView,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_views/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context

"""Variant Views """

class VariantCreationView(CreateView):
    model = Variant
    template_name = "Item_views/create.html"
    success_url = reverse_lazy("homepage")
    fields = ['item_code','cost','quantity','color']

    def post(self, request, **kwargs):
        request.POST = request.POST
        usr = User.objects.get(id=1)

        message = "Created Variant "
        UserActionLog.objects.create(user_id=usr,user_action="Created Variant",log_msg=message,)

        send_log_signal("Updated Product")

        return super(VariantCreationView, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VariantCreationView,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context


class VariantEditView(UpdateView):
    model = Variant
    template_name = "Item_views/edit.html"
    success_url = reverse_lazy("homepage")
    fields = ['item_code','cost','quantity','color']

    def post(self, request, **kwargs):
        request.POST = request.POST
        obj = self.get_object()
        changed = {}
        print(obj.__dict__)
        print request.POST
        for key in obj.__dict__.keys():
            if key in request.POST.keys():
                if str(request.POST[key]) != str(obj.__dict__[key]):
                    print request.POST[key],obj.__dict__[key],request.POST[key]!=obj.__dict__[key]
                    changed[key] = request.POST[key]
        usr = User.objects.get(id=1)

        message = ""
        for key in changed.keys():
            message+= key +" changed to "+changed[key]+".";

        UserActionLog.objects.create(user_id=usr,user_action="Updated Variant",log_msg=message,)

        send_log_signal("Updated Product "+message)

        return super(VariantEditView, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VariantEditView,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context


class VariantDetailView(DetailView):
    model = Variant
    template_name = "variant_views/detail.html"

    def get_context_data(self, **kwargs):
        context = super(VariantDetailView,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context


"""Misc Views """

class UserLogView(ListView):
    model = UserActionLog
    template_name = "app_views/detail.html"

    def get_context_data(self, **kwargs):
        context = super(UserLogView,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context

class HomePage(ListView):
    template_name = "app_views/list.html"
    model = Variant

    def get_context_data(self, **kwargs):
        context = super(HomePage,self).get_context_data(**kwargs)
        context['logs'] = UserActionLog.objects.all().order_by('-time')[:10]
        return context


""" User Account Views """

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "account_views/register.html"
    success_url = reverse_lazy('login')


class LoginView(FormView):
    template_name = "account_views/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)