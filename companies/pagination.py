from rest_framework.pagination import PageNumberPagination

class CustomCompanyPagination(PageNumberPagination):
    default_page_size = 5

    def get_page_size(self, request):
        page_size = request.query_params.get('pagesize', self.page_size)
        if page_size is not None:
            return int(page_size)
        return self.default_page_size