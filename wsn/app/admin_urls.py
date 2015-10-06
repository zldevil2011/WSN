from django.conf.urls import url, patterns, include
import views.admin.admin_login
import views.admin.admin_news

urlpatterns = \
    patterns('',
             url('^index$', views.admin.admin_login.admin_index, name='admin_index'),
             url('^admin_login', views.admin.admin_login.admin_login, name='admin_login'),
             url('^admin_news', views.admin.admin_news.admin_news, name='admin_news'),
             url('^pub_news_page', views.admin.admin_news.pub_news_page, name='pub_news_page'),
             url('^sel_change', views.admin.admin_news.sel_change, name='sel_change'),
             url('^pub_news', views.admin.admin_news.pub_news, name='pub_news'),
             )

# urlpatterns = [
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
# ]