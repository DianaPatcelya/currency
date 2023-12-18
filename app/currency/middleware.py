from time import time
from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('BEFORE IN MIDDLEWARE')  # noqa: T201
        start = time()

        response = self.get_response(request)

        end = time()
        print(f'AFTER IN MIDDLEWARE {end - start}')  # noqa: T201

        log_entry = RequestResponseLog(
            path=request.path,
            request_method=request.method,
            time=end - start
        )
        log_entry.save()

        return response
