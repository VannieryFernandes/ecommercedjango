
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url,include
from core import views
from catalog import views as views_catalog

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
	url(r'^contato/$', views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^entrar/$',auth_views.LoginView.as_view(template_name='login.html') , name='login'),
    url(r'^conta/',include('accounts.urls' , namespace='accounts')),
    url(r'^sair/$',auth_views.LogoutView.as_view(next_page='index') , name='logout'),

]
