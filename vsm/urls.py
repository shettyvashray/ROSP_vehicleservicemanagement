"""vsm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vehicle import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('customerclick', views.customerclick_view),
    path('mechanicsclick', views.mechanicsclick_view),

    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('mechanicsignup', views.mechanic_signup_view,name='mechanicsignup'),

    path('customerlogin', LoginView.as_view(template_name='vehicle/customerlogin.html'),name='customerlogin'),
    path('mechaniclogin', LoginView.as_view(template_name='vehicle/mechaniclogin.html'),name='mechaniclogin'),
    path('adminlogin', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='adminlogin'),



    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-customer', views.admin_customer_view,name='admin-customer'),
    path('admin-view-customer',views.admin_view_customer_view,name='admin-view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('admin-add-customer', views.admin_add_customer_view,name='admin-add-customer'),
    path('admin-view-customer-enquiry', views.admin_view_customer_enquiry_view,name='admin-view-customer-enquiry'),
    path('admin-view-customer-invoice', views.admin_view_customer_invoice_view,name='admin-view-customer-invoice'),


    path('admin-request', views.admin_request_view,name='admin-request'),
    path('admin-view-request',views.admin_view_request_view,name='admin-view-request'),
    path('change-status/<int:pk>', views.change_status_view,name='change-status'),
    path('admin-delete-request/<int:pk>', views.admin_delete_request_view,name='admin-delete-request'),
    path('admin-add-request',views.admin_add_request_view,name='admin-add-request'),
    path('admin-approve-request',views.admin_approve_request_view,name='admin-approve-request'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    
    path('admin-view-service-cost',views.admin_view_service_cost_view,name='admin-view-service-cost'),
    path('update-cost/<int:pk>', views.update_cost_view,name='update-cost'),

    path('admin-mechanic', views.admin_mechanic_view,name='admin-mechanic'),
    path('admin-view-mechanic',views.admin_view_mechanic_view,name='admin-view-mechanic'),
]
