import graphene
from graphene_django import DjangoObjectType

from .myauth.models import User, OTP

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'otps', 'mobile', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'dob', 'is_mobile_verified', 'is_email_verified')

class OTPType(DjangoObjectType):
    class Meta:
        model = OTP
        fields = ('id', 'user', 'email', 'mobile', 'code', 'type')

class Query(graphene.ObjectType):
    otps = graphene.List(OTPType)
    users = graphene.Field(UserType, email=graphene.String(required=True))

    def resolve_otps(root, info):
        return OTP.objects.select_related("user").all()

schema = graphene.Schema(query=Query)
