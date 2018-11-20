import re
from django.urls import path
from bwca import views
from bwca import forms
from django import forms
from django.views.generic import CreateView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('campers/', views.CamperListView.as_view(), name='campers'),
    path('campers/<str:slug>', views.CamperDetailView.as_view(), name='camperdetail'),
    # path('avaialble/', views.AvailableDateListView.as_view(), name='available')

    # path()
    # path('campers/', views.CamperListView, name = 'campers'),
    # path('campers/add', forms.CamperCreateView(), name = 'addcamper'),
    ]

urlpatterns += [
    path('camper/create/', views.CamperCreate.as_view(), name='camper_create'),
    path('campers/<str:slug>/update/', views.CamperUpdate.as_view(), name='camper_update'),
    path('campers/<str:slug>/delete/', views.CamperDelete.as_view(), name='camper_delete'),
]

urlpatterns += [
    path('available/', views.CamperAvailability, name='available')
]