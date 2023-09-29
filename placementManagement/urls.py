from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('account/', include('accounts.urls')),
    path('student/', include('students.urls')),
    path('faculty/', include('faculty.urls')),
    path('company/', include('companies.urls')),
    path('placement/', include('placement.urls')),
    path('university/', include('college.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
