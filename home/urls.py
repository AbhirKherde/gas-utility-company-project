from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('subreq', views.subreq, name='subreq'),
    path('trackreq', views.trackreq, name='trackreq'),
    path('viewacc', views.viewacc, name='viewacc'),
    path('trackreq/', views.trackreq, name='trackreq'),
    path('reqlist/', views.reqlist, name='reqlist'),
    path('update_status/', views.updatestatus, name='update_status'),
    path('account/<str:account_number>/', views.account_info, name='account_info')
]


