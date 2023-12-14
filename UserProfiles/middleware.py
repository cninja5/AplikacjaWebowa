from django.template.response import TemplateResponse

from main.models import Znajomi


# class InviteCountMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         invite_count = Znajomi.objects.filter(idZapraszanego=request.user.id, status='Wysłano').count()
#         request.invite_count = invite_count
#
#         response = self.get_response(request)
#
#         if hasattr(response, 'context_data'):
#             response.context_data['invite_count'] = request.invite_count
#
#         return response
#
#     def process_template_response(self, request, response):
#         if hasattr(response, 'context_data'):
#             response.context_data['invite_count'] = request.invite_count
#
#         return response

class NotificationsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not ('notification_count' in getattr(response, 'context_data', {})):
            # Sprawdź, czy response jest instancją TemplateResponse
            if not isinstance(response, TemplateResponse):
                # Jeśli nie jest, przekształć go na TemplateResponse
                response = TemplateResponse(request, response.content)

            response.context_data = response.context_data or {}

            # Teraz możemy dodać context_data do TemplateResponse
            response.context_data['notification_count'] = 2

        return response
