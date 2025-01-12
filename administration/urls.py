from django.urls import path
from .views import send_verification_email
from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import simple_password_change, verify_account
from django.contrib.auth import views as auth_views

from academic.forms import MaterialCreateForm
from academic.views import MaterialUpdateView, MaterialDeleteView, MaterialDetailView
from .views import CourseView, MaterialView, MemberView, MemberCreateView, MemberUpdateView, MemberDeleteView, \
    MemberDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, CourseDetailView, MaterialCreateView, ModuleListView, \
    ModuleDetailView,ModuleCreateView,ModuleUpdateView,ModuleDeleteView

# from administration.views import member_profile
urlpatterns = [
    # path('member/', member_profile, name='member_profile'),
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
    path('course/detail/<str:pk>/', CourseDetailView.as_view(), name='view_course'),
    path('material/create', MaterialCreateView.as_view(), name='create_material'),
    path('material/update/<str:pk>/', MaterialUpdateView.as_view(), name='update_material'),
    path('material/delete/<str:pk>/', MaterialDeleteView.as_view(), name='delete_material'),
    path('material/detail/<str:pk>/', MaterialDetailView.as_view(), name='view_material'),
    path('verify-account/<int:member_id>/', verify_account, name='verify_account'),
    path('modules/', ModuleListView.as_view(), name='module'),
    path('modules/<int:pk>/', ModuleDetailView.as_view(), name='module_detail'),
    path('modules/add/', ModuleCreateView.as_view(), name='module_add'),
    path('modules/<int:pk>/edit/', ModuleUpdateView.as_view(), name='module_edit'),
    path('modules/<int:pk>/delete/', ModuleDeleteView.as_view(), name='module_delete'),
    path('password-change-direct/', simple_password_change, name='simple_password_change'),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset',
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done',
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm',
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete',
    ),

]

