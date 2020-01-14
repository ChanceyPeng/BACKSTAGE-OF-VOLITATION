"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet, CategoryViewSet, HotSearchsViewSet, BannerViewSet, IndexCategoryViewSet
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OderViewSet

# 注册路由
router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

# 配置codes的url
router.register(r'codes', SmsCodeViewSet, base_name="codes")

# 配置hotsearch的url
router.register(r'hotsearchs', HotSearchsViewSet, base_name="hotsearchs")

# 配置users的url
router.register(r'users', UserViewSet, base_name="users")

# 配置收藏url
router.register(r'userfavs', UserFavViewSet, base_name="userfavs")

# 配置留言url
router.register(r'messages', LeavingMessageViewSet, base_name="messages")

# 配置地址url
router.register(r'address', AddressViewSet, base_name="address")

# 配置购物车url
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")

# 配置订单相关url
router.register(r'orders', OderViewSet, base_name="orders")

# 配置轮播图相关url
router.register(r'banners', BannerViewSet, base_name="banners")

# 配置首页商品系列数据url
router.register(r'indexgoods', IndexCategoryViewSet, base_name="indexgoods")

good_list = GoodsListViewSet.as_view({
    'get': 'list'
})

from trade.views import AliPayViewSet

# from django.views.generic import TemplateView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 商品列表页
    # url(r'goods/$', good_list, name="goods-list"),

    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title="千寻生鲜")),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),


    # jwt的认证接口
    url(r'^login/$', obtain_jwt_token),

    # 支付宝认证接口
    url(r'^alipay/return/', AliPayViewSet.as_view(), name="alipay"),

    # url(r'^index', TemplateView.as_view(template_name="index.html"), name="index"),

    # 第三方登录url
    # url('', include('social_django.urls', namespace='social'))
]
