from django.conf.urls import url, patterns, include
import views.welcome


urlpatterns = \
    patterns('',
             url('^welcome/', views.welcome.welcome, name='welcome')
             )

# urlpatterns = [
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
# ]