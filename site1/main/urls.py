from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('article1/', views.article1, name='article1'),
    path('article2/', views.article2, name='article2'),
    path('article3/', views.article3, name='article3'),
    path('article4/', views.article4, name='article4'),
    path('article5/', views.article5, name='article5'),
    path('article6/', views.article6, name='article6'),
    path('article7/', views.article7, name='article7'),
    path('article8/', views.article8, name='article8'),
    path('article9/', views.article9, name='article9'),
    path('article10/', views.article10, name='article10'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('appointment/submit/', views.appointment_submit, name='appointment_submit'),
    path('admin/services/', views.ServiceListView.as_view(), name='admin_service_list'),
    path('admin/services/add/', views.ServiceCreateView.as_view(), name='admin_service_add'),
    path('admin/services/<int:pk>/', views.ServiceUpdateView.as_view(), name='admin_service_change'),
    path('admin/services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='admin_service_delete'),
]



