import requests


class PlaceholderClient:
    """Клиент для JSONPlaceholder API.

    Инкапсулирует HTTP-запросы и сессию. Тесты работают через методы
    клиента, а не через голый requests — тот же принцип, что Page Object
    для UI: если поменяется эндпоинт, правка в одном месте.
    """

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_posts(self, **params) -> requests.Response:
        return self.session.get(f"{self.base_url}/posts", params=params)

    def get_post(self, post_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/posts/{post_id}")

    def get_post_comments(self, post_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/posts/{post_id}/comments")

    def create_post(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/posts", json=payload)

    def update_post(self, post_id: int, payload: dict) -> requests.Response:
        return self.session.put(f"{self.base_url}/posts/{post_id}", json=payload)

    def patch_post(self, post_id: int, payload: dict) -> requests.Response:
        return self.session.patch(f"{self.base_url}/posts/{post_id}", json=payload)

    def delete_post(self, post_id: int) -> requests.Response:
        return self.session.delete(f"{self.base_url}/posts/{post_id}")
