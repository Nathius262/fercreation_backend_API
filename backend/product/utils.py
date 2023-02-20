import uuid
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class SetProductPaginationResult(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")[:12]
    return code