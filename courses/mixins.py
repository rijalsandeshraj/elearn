from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin():
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(LoginRequiredMixin, OwnerMixin):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    fields = '__all__'
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'
