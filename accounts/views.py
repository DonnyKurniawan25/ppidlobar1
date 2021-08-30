from ppid.models import Dinas
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator

# membuat akses login dan logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
import logging
import os
logger = logging.getLogger(__name__)

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username atau Password Salah")
    
    context = {

    }
    return render(request, 'registration/login.html', context)

@login_required(login_url="/accounts/login/")
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/accounts/login/")
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = { 
        'form':form
    }
    return render(request, 'registration/register.html', context)

@login_required(login_url="/accounts/login/")
def dashboard(request):
    show =  models.Data.objects.filter(user=request.user.id)[:5]
    # context['instansi'] = instansi.objects.filter(site_id=siteID)[:1]


    dip = models.Data.objects.filter(user=request.user.id)
    dip_count = dip.count()

    dip_1 = models.Data.objects.filter(type_data = '2', user=request.user.id)
    dip1_count = dip_1.count()

    dip_2 = models.Data.objects.filter(type_data = '3', user=request.user.id)
    dip2_count = dip_2.count()

    dip_3 = models.Data.objects.filter(type_data = '4', user=request.user.id)
    dip3_count = dip_3.count()

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count
    }
    return render(request, 'account/index.html', context)

@login_required(login_url="/accounts/login/")
def data_ppid(request):
    data = models.Data.objects.filter(user=request.user.id)

    dip = models.Data.objects.filter(user=request.user.id)
    dip_count = dip.count()

    dip_1 = models.Data.objects.filter(type_data = '2', user=request.user.id)
    dip1_count = dip_1.count()

    dip_2 = models.Data.objects.filter(type_data = '3', user=request.user.id)
    dip2_count = dip_2.count()

    dip_3 = models.Data.objects.filter(type_data = '4', user=request.user.id)
    dip3_count = dip_3.count()

    context = {
        'data':data,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count
    }
    return render(request, 'account/data_ppid.html', context)

@login_required(login_url="/accounts/login/")
def create_data(request):
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            
            qry = models.Dinas.objects.filter(user_id = request.user.id).values_list("id", flat=True)

            obj.dinas_id = qry[0]
 
            obj.user_id = request.user.id
            obj.save()
            
            return redirect('datappid')

    context = {
        'form':form
    }
    return render(request, "account/create_data.html", context)

@login_required(login_url="/accounts/login/")
def update_data(request, pk):

    data = models.Data.objects.get(id=pk)
    form = DataForm(instance = data)

    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES, instance = data)
        if len(request.FILES) != 0:
            if len(data.file) > 0:
                os.remove(data.file.path)
                if form.is_valid():
                    obj = form.save(commit=False)
                    
                    qry = models.Dinas.objects.filter(user_id = request.user.id).values_list("id", flat=True)

                    obj.dinas_id = qry[0]
        
                    obj.user_id = request.user.id
                    obj.save()
                    return redirect('datappid')
                    
        if form.is_valid():
            obj = form.save(commit=False)
            
            qry = models.Dinas.objects.filter(user_id = request.user.id).values_list("id", flat=True)

            obj.dinas_id = qry[0]

            obj.user_id = request.user.id
            obj.save()
            return redirect('datappid')
    context = {
        'form':form,
    }
    return render(request, 'account/edit_data.html', context)

@login_required(login_url="/accounts/login/")
def delete_data(request, pk):
    if request.method == "POST":
        data = models.Data.objects.get(id=pk)
        data.delete()
    return redirect('datappid')


@login_required(login_url="/accounts/login/")
def profile(request):
    return render(request, 'account/profile.html')


