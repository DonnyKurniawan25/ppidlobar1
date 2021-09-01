from django.http import request
from django.shortcuts import render, redirect
from django.template import context
from django.template.context import Context
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect

from django.core.paginator import EmptyPage, Paginator

#untuk membuat query
from django.db.models import Count, OuterRef, Subquery


def error_404_view(request, exception):
    return render(request, 'ppid/404.html')

# Create your views here.
def data_type(request):
    return render(request, 'ppid/data_type.html')

def data_opd(request, pk):
    
    #Filter Data Berdasar dinas
    dataopd = Data.objects.filter(dinas_id = pk)

    #Count data
    dip = Data.objects.all()
    dip_count = dip.count()
 
    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)
    dip_show = Dinas.objects.filter(id = pk).annotate(jumlah=subQry)

    context = {
        'dataopd':dataopd,
        'dip':dip,
        'dip_show':dip_show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/data_opd.html', context)
    
class DIPdetail(DetailView):
    model = Data
    template_name = 'ppid/detail-dip.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context1 = self.get_context_data(object = self.object)
        ip = get_client_ip(self.request)
        print(ip)
        if IpModel.objects.filter(ip=ip).exists():
            print("Ip already")
            post_id = request.GET.get('post-id')
            print(post_id)
            post = Data.objects.get(pk=post_id)
            post.read.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            post_id = request.GET.get('post_id')
            post = Data.objects.get(pk=post_id)
            post.read.add(IpModel.objects.get(ip=ip))
        
        return self.render_to_response(context1)

    def get_context_data(self, **kwargs):
        subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
        opd_count = Dinas.objects.all().annotate(jumlah=subQry)
        dip = Data.objects.all()
        dip_count = dip.count()

        dip_1 = Data.objects.filter(type_data = '2')
        dip1_count = dip_1.count()

        dip_2 = Data.objects.filter(type_data = '3')
        dip2_count = dip_2.count()

        dip_3 = Data.objects.filter(type_data = '4')
        dip3_count = dip_3.count()

        context =  super().get_context_data(**kwargs)

        context['opd_count'] = opd_count
        context['dip_count'] = dip_count
        context['dip1_count'] = dip1_count
        context['dip2_count'] = dip2_count
        context['dip3_count'] = dip3_count
        return context

class DIPdownload(DetailView):
    model = Data
    template_name = 'ppid/download-file.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object = self.object)
        ip =get_client_ip(self.request)
        print(ip)
        if IpModel.objects.filter(ip=ip).exists():
            print("Ip already")
            post_id = request.GET.get('post-id')
            print(post_id)
            post = Data.objects.get(pk=post_id)
            post.download.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            post_id = request.GET.get('post_id')
            post = Data.objects.get(pk=post_id)
            post.download.add(IpModel.objects.get(ip=ip))
        
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):

        subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
        opd_count = Dinas.objects.all().annotate(jumlah=subQry)
        dip = Data.objects.all()
        dip_count = dip.count()

        dip_1 = Data.objects.filter(type_data = '2')
        dip1_count = dip_1.count()

        dip_2 = Data.objects.filter(type_data = '3')
        dip2_count = dip_2.count()

        dip_3 = Data.objects.filter(type_data = '4')
        dip3_count = dip_3.count()

        context =  super().get_context_data(**kwargs)

        context['opd_count'] = opd_count
        context['dip_count'] = dip_count
        context['dip1_count'] = dip1_count
        context['dip2_count'] = dip2_count
        context['dip3_count'] = dip3_count
        return context
     
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    show = Data.objects.all()[:5]
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
    }
    return render(request, 'ppid/index.html', context)

def addreas(request):
    show = Data.objects.filter(title__icontains='alamat')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/addreas.html', context)

def visimisi(request):
    show = Data.objects.filter(title__icontains='misi')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/visimisi.html', context)

def structure(request):
    show = Data.objects.filter(title__icontains='struktur')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/structure.html', context)

def tupoksi(request):
    show = Data.objects.filter(title__icontains='tupoksi')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/tupoksi.html',context)

def profile(request):
    show = Data.objects.filter(title__icontains='profil')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/profile.html', context)

def opd(request):
    show = Data.objects.filter(title__icontains='profil')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/opd.html', context)

def profileppid(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request,'ppid/profile-ppid.html', context) 

def visimisippid(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/visimisi-ppid.html', context)

def structureppid(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/structure-ppid.html', context)

def authorityppid(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/authority-ppid.html',context)

def noticeppid(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/notice-ppid.html', context)

def complaint(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/complaint.html', context)

def contact(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/contact.html', context)

def DIP(request):
    
    dip = Data.objects.all()
    dip_count = dip.count()
 
    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)
    
    p = Paginator(dip, 10)

    page_num = request.GET.get('page',1)

    try:
        dip = p.page(page_num)
    except EmptyPage:
        dip = p.page(1)


    context = {
        'dip':dip,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd':opd,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/DIP.html', context)

def mekanisme(request):
    return render(request, 'ppid/mekanisme.html')

def disputeresolution(request):
    return render(request, 'ppid/dispute-resolution.html')

def search(request):
    dip = Data.objects.all()
    dip_count = dip.count()
 
    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)
    
    if request.method == "POST":
        searched = request.POST['searched']

        datas = Data.objects.filter(title__icontains=searched)

        return render(request, 'ppid/search.html',{'searched':searched, 'datas':datas,'dip':dip,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,})
    else:
        return render(request, 'ppid/search.html')

def berkala(request):

     #Filter Data Berdasar dinas
    dataopd = Data.objects.filter(type_data = '2',)

    #Count data
    dip = Data.objects.all()
    dip_count = dip.count()
 
    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(dataopd, 10)

    page_num = request.GET.get('page',1)

    try:
        dataopd = p.page(page_num)
    except EmptyPage:
        dataopd = p.page(1)

    context = {
        'dataopd':dataopd,
        'dataopd':dataopd,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/berkala.html', context)

def sertamerta(request):

     #Filter Data Berdasar dinas
    dataopd = Data.objects.filter(type_data = '3',)

    #Count data
    dip = Data.objects.all()
    dip_count = dip.count()
 
    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(dataopd, 10)

    page_num = request.GET.get('page',1)

    try:
        dataopd = p.page(page_num)
    except EmptyPage:
        dataopd = p.page(1)

    context = {
        'dataopd':dataopd,
        'dataopd':dataopd,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/sertamerta.html', context)

def setiapsaat(request):

     #Filter Data Berdasar dinas
    dataopd = Data.objects.filter(type_data = '4',)

    #Count data
    dip = Data.objects.all()
    dip_count = dip.count()
 
    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(dataopd, 10)

    page_num = request.GET.get('page',1)

    try:
        dataopd = p.page(page_num)
    except EmptyPage:
        dataopd = p.page(1)

    context = {
        'dataopd':dataopd,
        'dataopd':dataopd,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/setiapsaat.html', context)

def rulespermohonan(request):
    show = Data.objects.filter(title__icontains='tata cara')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/rulespermohonan.html', context)
    
def standarharga(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/standarharga.html', context)

def permintaandata(request):
    show = Form_information.objects.all()

    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/permintaandata.html', context)

def form_request(request):
    show = Form_information.objects.all()

    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formrequest')

    context = {
        'form':form,
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/form_request.html', context)
    
def rulessengketa(request):
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    context = {
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/rulessengketa.html', context)

def pengajuankeberatan(request):
    show = Data.objects.filter(title__icontains='keberatan')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/pengajuankeberatan.html', context)

def laporan(request):
    show = Data.objects.filter(title__icontains='laporan') 
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
   
    return render(request, 'ppid/laporan.html', context)

def sop(request):
    show = Data.objects.filter(title__icontains='sop') 
    
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/sop.html', context)

def regulasi(request):
    show = Data.objects.filter(title__icontains='undang') 
    
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/regulasi.html', context)

def kegiatan(request):
    show = Data.objects.filter(title__icontains='kegiatan')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/kegiatan.html', context)

def agenda(request):
    show = Data.objects.filter(title__icontains='agenda')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/agenda.html', context)

def hakmasyarakat(request):
    show = Data.objects.filter(title__icontains='masyarakat')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/hakmasyarakat.html', context)

def akuntabilitas(request):
    show = Data.objects.filter(title__icontains='akuntabilitas')
    dip = Data.objects.all()
    dip_count = dip.count()

    dip_1 = Data.objects.filter(type_data = '2')
    dip1_count = dip_1.count()

    dip_2 = Data.objects.filter(type_data = '3')
    dip2_count = dip_2.count()

    dip_3 = Data.objects.filter(type_data = '4')
    dip3_count = dip_3.count()

    subQry = Subquery(Data.objects.filter(dinas_id = OuterRef('id')).values('dinas_id').annotate(jml=Count('id')).values('jml'))
    opd_count = Dinas.objects.all().annotate(jumlah=subQry)

    p = Paginator(show, 10)

    page_num = request.GET.get('page',1)

    try:
        show = p.page(page_num)
    except EmptyPage:
        show = p.page(1)

    context = {
        'show':show,
        'dip_count':dip_count,
        'dip3_count':dip3_count,
        'dip2_count':dip2_count,
        'dip1_count':dip1_count,
        'opd_count':opd_count,
    }
    return render(request, 'ppid/akuntabilitas.html', context)