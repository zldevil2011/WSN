from django.conf.urls import url, patterns, include
import views.admin.admin_login
import views.admin.admin_news
import views.admin.admin_drafts
import views.admin.admin_data

urlpatterns = \
    patterns('',
             url('^index/$', views.admin.admin_login.admin_index, name='admin_index'),
             url('^admin_login/$', views.admin.admin_login.admin_login, name='admin_login'),
             url('^admin_news/$', views.admin.admin_news.admin_news, name='admin_news'),
             url('^pub_news_page/$', views.admin.admin_news.pub_news_page, name='pub_news_page'),
             url('^sel_change/$', views.admin.admin_news.sel_change, name='sel_change'),
             url('^pub_news/$', views.admin.admin_news.pub_news, name='pub_news'),
             url('^edit_draft/$', views.admin.admin_drafts.edit_draft_view, name='edit_draft_view'),
             url('^data/$', views.admin.admin_data.admin_data, name='admin_data'),
             url('^data/upload/$', views.admin.admin_data.admin_data_upload, name='admin_data_upload'),
             )

# urlpatterns = [
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
# ]