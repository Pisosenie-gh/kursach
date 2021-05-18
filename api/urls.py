from rest_framework import routers
from .views import BlogPostViewSet, BlogCategoryViewSet, ZayavkaViewSet
from django.urls import path


urlpatterns = [

]


router = routers.SimpleRouter()
router.register('category', BlogCategoryViewSet ,basename = 'category')
urlpatterns += router.urls


router = routers.SimpleRouter()
router.register('zayavka', ZayavkaViewSet ,basename = 'zayavka')
urlpatterns += router.urls



router = routers.SimpleRouter()
router.register('blog', BlogPostViewSet ,basename = 'blog')
urlpatterns += router.urls