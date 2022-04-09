from rest_framework import mixins, viewsets


class FollowCreateListRetrieve(mixins.CreateModelMixin, mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    pass
