from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from ctmis.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT, DEBUG
from administration.views import send_verification_email  # Import the view for sending emails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('auth/login/', permanent=False)),
    path('ctmis/', include([
        path('dashboard/', include('dashboard.urls')),
        path('academic/', include('academic.urls')),
        path('finance/', include('finance.urls')),
        path('administration/', include('administration.urls')),
    ])),
    # Add the route for sending emails
    path('send-email/<int:member_id>/', send_verification_email, name='send-email'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
