from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from employee.models import Employee


class EmployeeListView(ListView):
    template_name = 'employees_table.html'
    queryset = Employee.objects.select_related('department', 'room', 'computer').all()
    context_object_name = 'employees'


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employees_list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ('first_name', 'last_name', 'room', 'department', 'computer')
    template_name = 'employee_create_update_form.html'
    success_url = reverse_lazy('employees_list')


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ('first_name', 'last_name', 'room', 'department', 'computer')
    template_name = 'employee_create_update_form.html'
    success_url = reverse_lazy('employees_list')
