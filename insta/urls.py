from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^search/', views.search, name='search'),
    url(r'^profile/(?P<username>[0-9]+)$', views.profile, name='users_page'),
    url(r'^mainprofile/$', views.mainprofile, name='mainprofile'),
    url(r'^edit/profile$', views.edit_user, name='edit_user'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)