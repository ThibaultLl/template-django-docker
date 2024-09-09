from django.contrib import admin
from django.urls import path, include, re_path
import authentication.views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from hello_django import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls'), name='home'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('', include('authentication.urls')),
    path('accounts/login/', include('authentication.urls'), name='login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
