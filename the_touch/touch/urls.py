from django.urls import path
from .views import home, post_detail, tagged, about, contact

app_name = 'touch'

urlpatterns = [
    path('', home, name='home'),
    # path('tag/<slug:tag_slug>/', home, name='post_list_by_tag'),
    path('tag/<slug:slug>/', tagged, name="tagged"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
    # path('post/new', PostCreateView.as_view(), name='post-create')

    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]
