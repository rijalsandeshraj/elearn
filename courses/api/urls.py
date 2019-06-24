from django.urls import path
from rest_framework import routers
from . import views

app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),
    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),
    # View to below URL pattern is replaced by
    # 'enroll' method of 'CourseViewSet'.
    # path('courses/<pk>/enroll/',
    #      views.CourseEnrollView.as_view(),
    #      name='course_enroll')
]

urlpatterns += router.urls
