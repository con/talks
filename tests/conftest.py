def pytest_configure(config):
    config.addinivalue_line("markers", "ai_generated: test written by an AI assistant")
