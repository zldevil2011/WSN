from django.conf.urls import url, patterns, include
import views.welcome
import views.index
import views.news
import views.data

urlpatterns = \
    patterns('',
             url('^welcome/$', views.welcome.welcome, name='welcome'),
             url('^$', views.index.index, name='index'),
             url('^index/$', views.index.index, name='index'),
             url('^news/(?P<news_id>\d+)$', views.news.news_detail, name='news_detail'),
             url('^news_list/$', views.news.news_list, name='news_list'),
             url('^air/$', views.data.air, name='data_air'),
             url('^water/$', views.data.water, name='data_water'),
             )

# urlpatterns = [
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
# ]