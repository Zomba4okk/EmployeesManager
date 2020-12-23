from employee import views
from django.urls import path

urlpatterns = (
    path(r'', views.EmployeeListView.as_view(), name='employees_list'),
    path(r'create', views.EmployeeCreateView.as_view(), name='employees_create'),
    path(r'<int:pk>/delete', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path(r'<int:pk>/update', views.EmployeeUpdateView.as_view(), name='employee_update'),
)