import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage
import data


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
        cls.driver.get(data.URBAN_ROUTES_URL)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route("Endereço A", "Endereço B")

        # Exemplo de assert (ajuste conforme os métodos que criar na page):
        # assert routes_page.get_from_value() == "Endereço A"

    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)

        # Passo 1: Abrir modal de telefone e digitar o número (crie esses métodos na page)
        # routes_page.click_add_phone()
        # routes_page.fill_phone_number("+1234567890") # Use o padrão exigido pelo app

        # Passo 2: Recuperar o código do sistema usando o helper
        phone_code = helpers.retrieve_phone_code(self.driver)

        # Passo 3: Confirmar o código recebido (crie este método na page)
        # routes_page.fill_sms_code(phone_code)

    def test_order_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_ice_creams(2)

        # Exemplo de assert (ajuste conforme os métodos que criar na page):
        # assert routes_page.get_ice_cream_count() == "2"