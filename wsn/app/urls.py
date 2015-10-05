from django.conf.urls import url, patterns, include
import views.welcome
import views.index

urlpatterns = \
    patterns('',
             url('^welcome/$', views.welcome.welcome, name='welcome'),
             url('^index/$', views.index.index, name='index'),
             )

# urlpatterns = [
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
# ]