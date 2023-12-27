from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns =[
    path('',views.index,name='index'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('emplogin', views.emplogin, name='emplogin'),
    path('acclogin', views.acclogin, name='acclogin'),
    path('regemp', views.regemp, name='regemp'),
    path('regacc', views.regacc, name='regacc'),
    path('about', views.about, name='about'),
    path('pricing', views.pricing, name='pricing'),
    path('employee', views.employee, name='employee'),
    path('contact', views.contact, name='contact'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('accdashboard', views.accdashboard, name='accdashboard'),
    path('empdashboard', views.empdashboard, name='empdashboard'),
    path('brandsandpriceadmin', views.brandsandpriceadmin, name='brandsandpriceadmin'),
    path('brandsandpriceemp', views.brandsandpriceemp, name='brandsandpriceemp'),
    path('dailysheetadmin', views.dailysheetadmin, name='dailysheetadmin'),
    path('dailysheetemp', views.dailysheetemp, name='dailysheetemp'),
    path('dailysheetacc', views.dailysheetacc, name='dailysheetacc'),
    path('challanandbills', views.challanandbills, name='challanandbills'),
    path('challanandbillsacc', views.challanandbillsacc, name='challanandbillsacc'),
    path('stockmanagementadmin', views.stockmanagementadmin, name='stockmanagementadmin'),
    path('stockmanagementemp', views.stockmanagementemp, name='stockmanagementemp'),
    path('members', views.members, name='members'),
    path('others', views.others, name='others'),
    path('load', views.load, name='load'),
    path('addstock', views.addstock, name='addstock'),
    path('addsheet', views.addsheet, name='addsheet'),
    path('addbrands', views.addbrands, name='addbrands'),
    path('addfiles', views.addfiles, name='addfiles'),   
    path('editstock/<str:w_id>/', views.editstock, name='editstock'),   
    path('editbrands/<str:id>/', views.editbrands, name='editbrands'),   
    path('deletestock/<str:brand_no>/', views.deletestock, name='deletestock'),
    path('deletebrands/<str:id>/delete/', views.deletebrands, name='deletebrands'),
    path('deletesheet/<str:brand_name>/', views.deletesheet, name='deletesheet'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('emplogout', views.emplogout, name='emplogout'),
    path('acclogout', views.acclogout, name='acclogout'),
    path('password_recovery', views.password_recovery, name='password_recovery'),
    path('password', views.password, name='password'),
    path('editsheet/<str:d_id>', views.editsheet, name='editsheet'),
    #path('delete', views.delete, name='delete'),
    path('removeemp/<str:emp_id>/', views.removeemp, name='removeemp'),
    path('removeacc/<str:acc_id>/', views.removeacc, name='removeacc'),
    path('editemp/<str:emp_id>/', views.editemp, name='editemp'),
    path('editacc/<str:acc_id>/', views.editacc, name='editacc'),
   
   
   
  
     
   
 
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)