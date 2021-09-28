from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'heroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_hero'),
    path('edit/<hero_id>/', views.edit, name='edit_hero'),
    path('delete/<hero_id>/', views.delete, name='delete_hero')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)