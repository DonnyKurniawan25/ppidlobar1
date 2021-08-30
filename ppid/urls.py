from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('alamat/', views.addreas, name="addreas"),
    path('visimisi/', views.visimisi, name="visimisi"),
    path('structure/', views.structure, name="structure"),
    path('tupoksi/', views.tupoksi, name="tupoksi"),
    path('profile/', views.profile, name="profilepimpinan"),
    path('opd/', views.opd, name="opd"),
    
    path('profile-ppid/', views.profileppid, name="profileppid"),
    path('visimisi-ppid/', views.visimisippid, name="visimisippid"),
    path('structure-ppid/', views.structureppid, name="structureppid"),
    path('authority-ppid/', views.authorityppid, name="authorityppid"),
    path('notice-ppid/', views.noticeppid, name="noticeppid"),

    path('complaint/', views.complaint, name="complaint"),
    path('contact/', views.contact, name="contact"),

    path('DIP/', views.DIP, name="DIP"),
    path('DIP-detail/<int:pk>', views.DIPdetail.as_view(), name='DIP'),
    path('download/<int:pk>', views.DIPdownload.as_view(), name='Download'),

    path('request-data/', views.requestdata, name="requestdata"),
    path('mekanisme/', views.mekanisme, name=" mekanisme"),
    path('dispute-resolution/', views.disputeresolution, name=" disputeresolution"),

    path('search/', views.search, name="search"),
    path('data-opd/<int:pk>', views.data_opd, name="data_opd"),
    path('data-type/', views.data_type, name="data_type"),

    path('berkala/', views.berkala, name="berkala"),
    path('sertamerta/', views.sertamerta, name="sertamerta"),
    path('setiapsaat/', views.setiapsaat, name="setiapsaat"),
    
    path('rulespermohonan/', views.rulespermohonan, name="rulespermohonan"),
    path('standarharga/', views.standarharga, name="standarharga"),
    path('permintaandata/', views.permintaandata, name="permintaandata"),
    
    path('formregister/', views.form_register, name="formregister"),
    
    # path('error/', views.error_404_view, name="error"),
    

]
