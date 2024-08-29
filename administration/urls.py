from django.urls import path
from .views import CourseView, MaterialView, MemberView, MemberCreateView, MemberUpdateView, MemberDeleteView, MemberDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, CourseDetailView

urlpatterns = [
    path('course/', CourseView.as_view(), name='course'),
    path('material/', MaterialView.as_view(), name='material'),
    path('member/', MemberView.as_view(), name='member'),
    path('member/create', MemberCreateView.as_view(), name='create_member'),
    path('member/update/<str:pk>', MemberUpdateView.as_view(), name='update_member'),
    path('member/delete/<str:pk>', MemberDeleteView.as_view(), name='delete_member'),
    path('member/detail/<str:pk>', MemberDetailView.as_view(), name='view_member'),
    path('course/create', CourseCreateView.as_view(), name='create_course'),
    path('course/update/<str:pk>/', CourseUpdateView.as_view(), name='update_course'),
    path('course/delete/<str:pk>/', CourseDeleteView.as_view(), name='delete_course'),
    path('course/detail/<str:pk>/', CourseDetailView.as_view(), name='view_course')

]
