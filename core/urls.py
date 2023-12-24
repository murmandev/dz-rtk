from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
from .views import Index, DetailArticleView, LikeArticle, Featured, CreateArticleView, DeleteArticleView, Moderated, Search, UpdateArticleView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('create/', CreateArticleView.as_view(), name='create'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete'),
    path('<int:pk>/moderated', Moderated.as_view(), name='moderated'),
    path('search/', Search.as_view(), name='search'),
    path('article/update/<int:pk>', UpdateArticleView.as_view(), name='article_update'),
]