from django.urls import path,include
from .views import mymodelviewset, brandViewSet,categoryViewSet,modelViewSet, variantViewSet,FeatureMasterViewSet, FeatureVariantViewSet, ItemViewSet,SalesViewSet


from rest_framework .routers import DefaultRouter
router = DefaultRouter()
router.register("product", mymodelviewset)
router.register("brand", brandViewSet)
router.register("cat", categoryViewSet)
router.register("models",modelViewSet)
router.register("variant",variantViewSet)
router.register("variant",FeatureMasterViewSet)
router.register("i_variant",FeatureVariantViewSet)
router.register("items",ItemViewSet)
router.register("sales",SalesViewSet)





urlpatterns = [
    path('', include(router.urls)),

    # url(r'login/$', views.login, name='login'),
]
