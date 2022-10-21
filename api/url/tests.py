from rest_framework import status
from rest_framework.test import APIClient

def test_admin_page_return_status():
    client = APIClient()
    response = client.get("/admin/login/?next=/admin/")
    assert response.status_code == status.HTTP_200_OK