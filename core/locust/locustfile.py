from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    host = "backend:8000"
    wait_time = between(1, 3)

    def on_start(self):
        response = self.client.post('/accounts/api/v2/jwt/create/', data={
            "email": "admin@admin.com",
            "password": "123"
        }).json()
        self.client.headers = {'Authorization': f'Bearer {response.get("access", None)}'}


    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")

    @task
    def category_list(self):
        self.client.get("/blog/api/v1/category/")