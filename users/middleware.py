from django.utils import timezone

from users.models import CustomUser


class UpdateLastActivityMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), \
            'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
        if request.user.is_authenticated:
            CustomUser.objects.filter(uuid=request.user.uuid).update(last_activity=timezone.now())
