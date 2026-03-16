import logging
import time

logger = logging.getLogger("api.requests")


class RequestLoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = (time.time() - start) * 1000

        msg = "%s %s %s %.2fms" % (
            request.method,
            request.get_full_path(),
            response.status_code,
            duration
        )

        if response.status_code >= 500:
            logger.error(msg)
        elif response.status_code >= 400:
            logger.warning(msg)
        else:
            logger.info(msg)

        return response
