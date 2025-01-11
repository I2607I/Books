from books.endpoints.health_check import api_router as health_check_router
from books.endpoints.product import api_router as product_router


list_of_routes = [
    health_check_router,
    product_router,
]


__all__ = [
    "list_of_routes",
]
