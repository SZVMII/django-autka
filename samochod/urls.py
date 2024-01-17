from django.urls import path
from .views import CreateView, PartList, FavoriteListCreateView, CommentListVeiw,CreateComment,FavoriteAdd, RatingAdd, RatingList, RatingSoloList,CommentSoloList

urlpatterns = [
    path('create/',  CreateView.as_view(), name='adding new elements'),
    path('show/', PartList.as_view(), name='displaying elements'),
    path('favoritesshow/', FavoriteListCreateView.as_view(), name='favorite-list'),
    path('favoritescreate', FavoriteAdd.as_view(),name='add to favorites'),
    path('commentscreate/', CreateComment.as_view(), name='comments'),
    path('commentsshow/', CommentListVeiw.as_view(), name='comments'),
    path('ratingAdd/', RatingAdd.as_view(), name='add ratting'),
    path('ratingList/', RatingList.as_view(), name='show rating'),
    path('<int:pk>/rating', RatingSoloList.as_view(), name='show rating for one'),
    path('<int:pk>/comment', CommentSoloList.as_view(), name='show comment for one')
]
