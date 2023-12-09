# from .models import get_unread_notification_count
from main.models import Znajomi


class UnreadNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            unread_notification_count = Znajomi.objects.filter(idZapraszanego=request.user.id, status='Wysłano').count()
            request.unread_notification_count = unread_notification_count

        response = self.get_response(request)
        return response