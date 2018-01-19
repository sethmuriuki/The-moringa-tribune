from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[   
    url(r'^$',views.news_today,name='newsToday'),
    url(r'^search/',views.search_results, name = 'search_results'),
    url(r'^article/(\d+)',views.article,name ='article'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)