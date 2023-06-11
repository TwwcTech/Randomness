from rdoclient import RandomOrgClient


class RDOProcessor(RandomOrgClient):
    def __init__(self, api_key, blocking_timeout=2.0, http_timeout=10.0, serialized=False):
        super().__init__(api_key, blocking_timeout, http_timeout, serialized)

    def generate_ints(self, index, minimum, maximum) -> list:
        self.generate_integers(n=index, min=minimum, max=maximum)
