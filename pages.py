import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    # ==========================================
    # 1. LOCALIZADORES
    # ==========================================
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    
    # Botão de pedir um táxi
    call_a_taxi_button = (By.XPATH, "//button[contains(text(), 'Call a taxi') or contains(text(), 'Pedir um táxi') or contains(text(), 'Chamar um táxi') or @class='button round']")
    
    # Seleção de tarifa
    comfort_tariff_option = (By.XPATH, "//*[@class='tcard-title' and (text()='Comfort' or text()='Comfort')]")
    current_tariff = (By.XPATH, "//div[contains(@class, 'tcard') and contains(@class, 'active')]")
    
    # Telefone
    add_phone_number_main_button = (By.CLASS_NAME, "np-text")
    phone_number_input_field = (By.ID, "phone")
    phone_number_next_button = (By.XPATH, "//button[contains(text(), 'Next') or contains(text(), 'Próximo')]")
    phone_code_field = (By.ID, "code")
    phone_number_confirm_button = (By.XPATH, "//button[contains(text(), 'Confirm') or contains(text(), 'Confirmar')]")
    registered_phone_number = (By.CLASS_NAME, "np-text")
    
    # Pagamento
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card_option_button = (By.CLASS_NAME, "pp-plus-container")
    card_number_input = (By.ID, "number")
    card_code_input = (By.XPATH, "//div[contains(@class, 'card-code-input')]//input[@id='code']")
    final_add_card_button = (By.XPATH, "//button[contains(text(), 'Link') or contains(text(), 'Adicionar') or contains(text(), 'Ligar')]")
    close_payment_method_modal_button = (By.CSS_SELECTOR, ".payment-picker .close-button")
    current_payment_method = (By.CLASS_NAME, "pp-value-text")
    
    # Requisitos da viagem
    message_for_driver_field = (By.ID, "comment")
    blanket_slider = (By.CSS_SELECTOR, ".r-sw-container .slider")
    blanket_state = (By.CSS_SELECTOR, ".r-sw-container .switch-input")
    add_ice_cream_btn = (By.CSS_SELECTOR, ".r-counter .counter-plus")
    ice_cream_count = (By.CSS_SELECTOR, ".r-counter .counter-value")
    
    # Botão de confirmar corrida e Modal de procura
    order_button = (By.CLASS_NAME, "smart-button")
    order_timer = (By.CLASS_NAME, "order-header-time")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ==========================================
    # 2. MÉTODOS UTILITÁRIOS
    # ==========================================
    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
        
    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    # ==========================================
    # 3. MÉTODOS DE NEGÓCIO
    # ==========================================
    def set_route_addresses(self, from_address, to_address):
        self._type(self.from_field, from_address)
        self._type(self.to_field, to_address)
        
    def get_from_field_text(self):
        return self._find(self.from_field).get_property('value')
        
    def get_to_field_text(self):
        return self._find(self.to_field).get_property('value')

    def click_call_a_taxi_button(self):
        self._click(self.call_a_taxi_button)

    def click_comfort_option(self):
        self._click(self.comfort_tariff_option)
        
    def get_selected_tariff_option(self):
        return self._find(self.current_tariff).get_attribute('class')

    # Fluxo unificado de telefone
    def set_phone(self, phone):
        self._click(self.add_phone_number_main_button)
        self._type(self.phone_number_input_field, phone)
        self._click(self.phone_number_next_button)
        code = helpers.retrieve_phone_code(self.driver)
        self._type(self.phone_code_field, code)
        self._click(self.phone_number_confirm_button)

    def get_inserted_phone_number(self):
        return self._find(self.registered_phone_number).text
        
    # Fluxo unificado de cartão
    def set_card(self, card_number, cvv):
        self._click(self.payment_method_button)
        self._click(self.add_card_option_button)
        self._type(self.card_number_input, card_number)
        element = self._find(self.card_code_input)
        element.send_keys(cvv)
        element.send_keys(Keys.TAB)
        self._click(self.final_add_card_button)
        self._click(self.close_payment_method_modal_button)
        
    def get_current_payment_method(self):
        return self._find(self.current_payment_method).text
        
    def set_message_for_driver(self, message):
        self._type(self.message_for_driver_field, message)
        
    def get_message_for_driver(self):
        return self._find(self.message_for_driver_field).get_property('value')
        
    def click_blanket_and_handkerchiefs_option(self):
        self._click(self.blanket_slider)
        
    def is_blanket_and_handkerchiefs_option_checked(self):
        return self._find(self.blanket_state).is_selected()
        
    def click_add_ice_cream_button(self, amount=2):
        for _ in range(amount):
            self._click(self.add_ice_cream_btn)
            
    def get_current_icecream_amount(self):
        return self._find(self.ice_cream_count).text
        
    def click_order_button(self):
        self._click(self.order_button)
        
    def is_order_taxi_popup_displayed(self):
        return self._find(self.order_timer).is_displayed()