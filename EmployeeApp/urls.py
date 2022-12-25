from django.urls import path
from EmployeeApp import views
# from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('department/',views.departmentApi),
    path('employee/',views.employeeApi),
    path('employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url(r'^department$',views.departmentApi),
#     url(r'^depatment/([0-9]+)$',views.departmentApi),
    
#     url(r'^employee$',views.employeeApi),
#     url(r'^employee/([0-9]+)$',views.employeeApi),
    
#     url(r'^employee/savefile',views.SaveFile)
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
