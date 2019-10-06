from django.conf import settings
from django.db import connection
import logging
import time
import six
from django.utils.deprecation import MiddlewareMixin

log = logging.getLogger(__name__)


class RequestLoggingMiddleware(MiddlewareMixin):
    """
    Logs the start and the end of a request, with optional timing stats.
    The log message in `process_request` usefully logs when the request truly starts, rather than
    the confusing way Django server logs are (IMO) - telling us when the request finishes,
    meaning that all our personal logging that occurs during the processing of the request
    appears out of sequence, 'before' the official endpoint GET/POST log entry that triggered it.
    This middleware fixes that 'problem' and logs the true beginning of the request.
    Originally from https://djangosnippets.org/snippets/2624/
    Modified by abulka@gmail.com to be Django 2 compatible, added a log message to the
    request as well as response.
    """

    def process_request(self, request):
        self.start_time = time.time()
        log.info(f"Endpoint {request.get_full_path()} request {request.META.get('REMOTE_ADDR')}")

    def process_response(self, request, response):
        try:
            remote_addr = request.META.get("REMOTE_ADDR")
            if remote_addr in getattr(settings, "INTERNAL_IPS", []):
                remote_addr = request.META.get("HTTP_X_FORWARDED_FOR") or remote_addr
            user_email = "-"
            extra_log = ""
            if hasattr(request, "user"):
                user_email = getattr(request.user, "email", "-")
            req_time = time.time() - self.start_time
            content_len = len(response.content)
            if settings.DEBUG:
                sql_time = sum(float(q["time"]) for q in connection.queries) * 1000
                extra_log += " (%s SQL queries, %s ms)" % (len(connection.queries), sql_time)
            log.info(
                "Endpoint completed, %s %s %s %s %s %s (%.02f seconds)%s"
                % (
                    remote_addr,
                    user_email,
                    request.method,
                    request.get_full_path(),
                    response.status_code,
                    content_len,
                    req_time,
                    extra_log,
                )
            )
        except Exception as e:
            log.error("LoggingMiddleware Error: %s" % e)
        return response