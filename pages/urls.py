from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # www.site.com/pages/index
    # path('', views.index, name='index'),  # www.site.com/
    # www.site.com/demandeST/
    path('demandeST/', views.demandeST, name='demandeST'),
    path('demandeCED/', views.DCED, name='demandeCED'),
    path('demandelist/', views.listerdemande,
         name='demandelist/'),  # www.site.com/demandelist/
    path('register', views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    # path('logout/', views.Logout, name="logout")
    path('logout', auth_views.LogoutView.as_view(
        template_name='index.html'), name='logout'),
]
