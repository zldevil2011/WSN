from django.conf.urls import url, patterns, include
import views.welcome
import views.index
import views.news

urlpatterns = \
    patterns('',
             url('^welcome/$', views.welcome.welcome, name='welcome'),
             url('^index/$', views.index.index, name='index'),
             url('^news/(?P<news_id>\d+)$', views.news.news_detail, name='news_detail'),
             url('^news_list/$', views.news.news_list, name='news_list'),
             )

# urlpatterns = [
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
# ]