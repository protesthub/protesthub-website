from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_view.as_view(),name='search'),
    path('users/', include('main.users.urls'))
]
