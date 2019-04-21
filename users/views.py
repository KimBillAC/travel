from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

# Create your views here.
from django.views.generic import RedirectView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.models import UserProfile


class UserViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):

    pass


class WeiboLoginView(RedirectView):

    pass


class WeiboCodeView(RedirectView):

    pass


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = UserProfile.objects.get(Q(name=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:

            return None
