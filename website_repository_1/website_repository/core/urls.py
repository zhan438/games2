from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", views.index, name = "index"),
    # path('random/', views.as_view(), name='random'),
    # path('box_model_demo/', views.as_view(), name='box_model_demo'),
    # path('flexbox/', views.as_view(), name='flexbox'),
    # path('secret/', views.as_view(), name='secret'),
    path('geometry_dash/', views.geometry_dash_view, name='geometry_dash'),
    path('minecraft/', views.minecraft_view , name='minecraft'),
    path('polygon/', views.polygon_view, name='polygon'),
    path('get-time/', views.get_time, name='get_time'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
