from django.conf.urls import url
import views

#  'blog/' removed from each of the below to allow import into another project
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^/$', views.post_list, name="post_list"),
    url(r'^/stuff/$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^post/$', views.new_post, name='new_post'),
]