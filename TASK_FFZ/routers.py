from rest_framework import routers
from api.viewsets import CartViewSet, CustomerViewset, PlacedOrderViewSet, ProductViewSet

router=routers.DefaultRouter()
router.register('allcustomers',CustomerViewset)
router.register('allproducts',ProductViewSet)
router.register('allcarts',CartViewSet)
router.register('allplacedorders',PlacedOrderViewSet)
# router.register('placedorder',PlacedOrderperticularViewSet)
# router.register('placedorder_user',PlacedOrderByIdViewSet)
# router.register('customer',CustomerPerticularViewSet)
