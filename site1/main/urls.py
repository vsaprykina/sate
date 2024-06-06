from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointment/submit/', views.appointment_submit, name='appointment_submit'),
    path('admin/services/', views.ServiceListView.as_view(), name='admin_service_list'),
    path('admin/services/add/', views.ServiceCreateView.as_view(), name='admin_service_add'),
    path('admin/services/<int:pk>/', views.ServiceUpdateView.as_view(), name='admin_service_change'),
    path('admin/services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='admin_service_delete'),
    path('appointment/available-times/<str:appointment_date>/', views.appointment_available_times, name='appointment_available_times'),
    path('contacts/', views.contact_page, name='contacts'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('index-question/', views.index_question_view, name='index_question'),
    path('success/', views.success, name='success')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)