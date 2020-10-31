import graphene
from graphene_django import DjangoObjectType

from .models import User, OTP

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'otps', 'mobile', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'dob', 'is_mobile_verified', 'is_email_verified')

class OTPType(DjangoObjectType):
    class Meta:
        model = OTP
        fields = ('id', 'user', 'email', 'mobile', 'code', 'kind')

class MyAuthQuery(graphene.ObjectType):
    otps = graphene.List(OTPType)
    users = graphene.Field(UserType, email=graphene.String(required=True))

    def resolve_otps(root, info):
        return OTP.objects.select_related("user").all()

    def resolve_users_by_email(root, info, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
