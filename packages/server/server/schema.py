import graphene
from graphene_django import DjangoObjectType

import myauth.schema
import myproduct.schema

class Query(myauth.schema.Query, myproduct.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
