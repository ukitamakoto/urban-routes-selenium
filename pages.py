from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    # ==========================================
    # 1. LOCALIZADORES
    # ==========================================
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    comfort_plan_card = (By.XPATH, 'seletor_do_plano_comfort')
    phone_input = (By.ID, 'phone')
    cvv_input = (By.ID, 'code')  # Conforme a dica da imagem 1
    add_card_button = (By.XPATH, 'seletor_botao_adicionar_cartao')
    blanket_slider = (By.CLASS_NAME, 'slider')  # Exemplo do botão de ativar
    blanket_state = (By.XPATH, 'seletor_que_indica_estado_ativo')
    add_ice_cream_btn = (By.XPATH, 'seletor_adicionar_sorvete')

    def __init__(self, driver):
        self.driver = driver

    # ==========================================
    # 2. MÉTODOS DE INTERAÇÃO
    # ==========================================

    def set_route(self, from_address, to_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def select_comfort_plan(self):
        comfort_btn = self.driver.find_element(*self.comfort_plan_card)
        is_selected = "active" in comfort_btn.get_attribute("class")  # Exemplo de validação
        if not is_selected:
            comfort_btn.click()

    def fill_card_cvv(self, cvv):
        cvv_element = self.driver.find_element(*self.cvv_input)
        cvv_element.send_keys(cvv)
        cvv_element.send_keys(Keys.TAB)  # Simula a tecla TAB para tirar o foco do campo

        # Agora o botão pode ser clicado
        self.driver.find_element(*self.add_card_button).click()

    def order_ice_creams(self, amount):
        # DICA: O ciclo para pedir sorvetes deve ser movido para cá (Imagem 5)
        add_btn = self.driver.find_element(*self.add_ice_cream_btn)
        for _ in range(amount):
            add_btn.click()

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_slider).click()

    def is_blanket_selected(self):
        # Retorna True ou False
        return self.driver.find_element(*self.blanket_state).is_selected()