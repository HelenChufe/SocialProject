from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('editar/', views.editar, name='editar'),
    path('delete/<int:post_id>',views.delete, name='delete'),
    path('follow/<str:username>/', views.follow, name='follow'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)