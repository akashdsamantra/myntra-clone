import graphene
from graphene_django import DjangoObjectType

from .models import Seller, Product

class SellerType(DjangoObjectType):
    class Meta:
        model = Seller
        fields = ('id', 'name', 'location', 'address', 'country_of_origin', 'email', 'phone_number', 'alternate_phone_number')

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'code', 'name', 'description', 'price', 'currency', 'discount', 'seller')

class Query(graphene.ObjectType):
    sellers = graphene.List(SellerType)
    products = graphene.List(ProductType)

    def resolve_sellers(root, info):
        return Seller.objects.all()

    def resolve_products(root, info):
        return Product.objects.all()
