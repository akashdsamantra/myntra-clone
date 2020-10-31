import graphene
from graphene_django import DjangoObjectType

from myauth.schema import MyAuthQuery
from myproduct.schema import MyProductQuery

class Query(MyAuthQuery, MyProductQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
