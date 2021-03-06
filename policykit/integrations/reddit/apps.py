from django.apps import AppConfig


class redditIntegrationConfig(AppConfig):
    name = 'integrations.reddit'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('RedditUser'))
