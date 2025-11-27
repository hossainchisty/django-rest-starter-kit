"""
Core Pagination

Custom pagination classes for consistent API responses.
"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard pagination class with customizable page size.
    
    Default page size: 50
    Max page size: 100
    """
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        """
        Return paginated response with metadata.
        
        Response format:
        {
            "count": total_count,
            "next": next_page_url,
            "previous": previous_page_url,
            "results": [...]
        }
        """
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )


class LargeResultsSetPagination(PageNumberPagination):
    """Pagination for large datasets"""
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class SmallResultsSetPagination(PageNumberPagination):
    """Pagination for small datasets"""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
