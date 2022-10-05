from django.urls import path
from .views import articles, article_detail, author,reaction,comment,login_view,log_out,registration

urlpatterns = [
    path('', articles, name='articles'),
    path('article/<int:id>', article_detail, name='article_detail'),
    path('reaction/<int:id>/<str:react>', reaction, name='reaction'),
    path('author/<int:id>', author, name='author'),
    path('comment/<int:id>',comment,name='comment'),
    path('login/',login_view,name='login'),
    path('logout/',log_out,name='logout'),
    path('registration/',registration,name='registration')

]
