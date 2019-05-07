from django.urls import include, path
from django.contrib import admin
from aplicaciones.mascota import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tipo', views.TipoList)
router.register('mascota', views.MascotaList)
urlpatterns = [
    path('',views.base, name='base'),
    path('tipo/',views.tipo,name="tipo"),
    path('tipo/<int:tipo_id>/detail', views.tipo_detail, name="tipo-detail"),
    path('mascota/', views.MascotaListView.as_view(), name='mascota-list'),
    path('mascota/<int:pk>/detail', views.MascotaDetailView.as_view(), name='mascota-detail'),
    path('mascota/create/', views.MascotaCreate.as_view(), name='mascota-create'),
    path('mascota/<int:pk>/update/', views.MascotaUpdate.as_view(), name='mascota-update'),
    path('mascota/<int:pk>/delete/', views.MascotaDelete.as_view(), name='mascota-delete'),
    #path('', include(router.urls)),
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
]