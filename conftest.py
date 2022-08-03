import pytest
from application import Application

fixture = None


@pytest.fixture()
def app():
    global fixture
    if fixture is None or not fixture.session_is_valid():
        fixture = Application()
        # search_engine = "google"
        if not fixture.search_engine.is_opened:
            fixture.search_engine.open_search_engine()
        fixture.search_engine.request_execution("Совкомбанк")
        print(fixture.search_engine.number_of_found_results())
        fixture.search_engine.open_website()
        fixture.search_engine.close_search_engine()
        fixture.search_engine.switch_to_website()
    yield fixture


@pytest.fixture(scope="session", autouse=True)
def fixture_destroy(request):
    def fin():
        fixture.session_destroy()
    request.addfinalizer(fin)
