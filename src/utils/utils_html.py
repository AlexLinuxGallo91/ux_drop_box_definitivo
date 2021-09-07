from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from src.webdriver_actions.html_actions import webdriver_actions_constantes
import time
import re


class ValidacionesHtml():

    @staticmethod
    def verificar_elemento_html_por_id(id: str, web_driver: WebDriver):

        try:
            web_driver.find_element_by_id(id)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def verificar_elemento_html_por_class_name(class_name: str, web_driver: WebDriver):

        try:
            web_driver.find_element_by_class_name(class_name)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def verificar_elemento_html_por_xpath(xpath: str, web_driver: WebDriver):

        try:
            web_driver.find_element_by_xpath(xpath)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def se_encuentran_mas_ventanas_en_sesion(web_driver: WebDriver, tiempo_espera: int):
        count = 0
        while count < tiempo_espera:
            if len(web_driver.window_handles) > 1:
                return True
            else:
                count = count + 1

            time.sleep(1)

        driverExcep = WebDriverException('Han transcurrido mas de {} seg. sin obtener la nueva ventana de '
                                         'inicio de sesion mediante Gmail'.format(tiempo_espera))

        raise TimeoutException(driverExcep)

    @staticmethod
    def verificar_remover_ventana_configuracion(web_driver: WebDriver):

        try:
            btn_cierre_ventana_configuracion = WebDriverWait(web_driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'continuous-onboarding-collapse-btn')))
            btn_cierre_ventana_configuracion.click()
        except TimeoutException:
            pass

    @staticmethod
    def verificar_archivo_ya_existente_en_portal(web_driver: WebDriver, nombre_archivo_sin_ext: str):

        try:
            lista_archivos_actuales = web_driver.find_elements_by_xpath('//div[@data-item-id]')

            if len(lista_archivos_actuales) > 0:
                for div_archivo in lista_archivos_actuales:
                    div_recent_item_header = div_archivo.find_element_by_class_name('recents-item-header')
                    div_recent_item_header_content = div_recent_item_header.find_element_by_class_name(
                        'recents-item-header__content')
                    link_nombre_archivo = div_recent_item_header_content.find_element_by_tag_name('a')

                    if link_nombre_archivo.text.strip() == nombre_archivo_sin_ext.strip():
                        div_item_actions = WebDriverWait(web_driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, 'recents-item__actions')))

                        WebDriverWait(div_item_actions, 10).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, 'dig-IconButton-content')))

                        btn_mas = div_item_actions.find_element_by_class_name('dig-IconButton-content')
                        btn_mas.click()

                        sub_menu_acciones = WebDriverWait(web_driver, 10).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, 'dig-Layer')))

                        btn_eliminar = WebDriverWait(sub_menu_acciones, 10).until(
                            EC.element_to_be_clickable((By.XPATH, '//span[text()="Eliminar…"]')))

                        btn_eliminar.click()

                        modal_eliminacion = WebDriverWait(web_driver, 10).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, 'db-modal-box')))

                        btn_eliminacion_definitivo = WebDriverWait(modal_eliminacion, 10).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, '//button[@class="button-primary dbmodal-button"][text()="Eliminar"]')))

                        btn_eliminacion_definitivo.click()

                        WebDriverWait(web_driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//span[@id="notify-msg"]')))

        except ElementNotInteractableException as e:
            pass
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass
        except ElementClickInterceptedException:
            pass

    @staticmethod
    def verificar_mensaje_de_carga_exitosa_de_archivo(web_driver: WebDriver, nombre_archivo_a_cargar: str,
                                                      numero_de_seg_en_espera: int = 720):
        segundos_transcurridos = 0

        while segundos_transcurridos < numero_de_seg_en_espera:
            list_span_mensaje_carga_exitosa = web_driver.find_elements_by_class_name('dig-RichSnackbar-message')

            if len(list_span_mensaje_carga_exitosa) > 0:
                texto_mensaje_de_carga = list_span_mensaje_carga_exitosa[0].get_attribute('innerText')

                if re.search('^Se cargaron*', texto_mensaje_de_carga) or \
                        texto_mensaje_de_carga == 'Se carg\u00F3 {}.'.format(nombre_archivo_a_cargar):
                    break

            time.sleep(1)
            segundos_transcurridos += 1

        if segundos_transcurridos == numero_de_seg_en_espera:
            e = TimeoutException()
            e.msg = webdriver_actions_constantes.WEBDRIVER_WAIT_TIMEOUT_EXCEPTION.format(
                segundos_transcurridos,
                'span con el texto de finalizacion de carga de archivo dentro del portal drop box.',
                '')
            raise e

    @staticmethod
    def cargar_archivo_en_portal_drop_box(web_driver: WebDriver, path_archivo_por_cargar: str,
                                          tiempo_de_espera: int = 10):
        seg_transcurridos = 0

        while seg_transcurridos < tiempo_de_espera:

            lista_de_input_file = web_driver.find_elements_by_xpath('//input[@type="file"]')

            if ValidacionesHtml.verificar_elemento_html_por_class_name('dig-Modal-footer', web_driver):
                break

            if len(lista_de_input_file) > 0:
                input_file = lista_de_input_file[0]
                input_file.send_keys(path_archivo_por_cargar)

            seg_transcurridos += 1
            time.sleep(1)

    @staticmethod
    def espera_desaparicion_modal_acceso_de_google(web_driver: WebDriver, tiempo_de_espera: int = 60):

        tiempo_transcurrido = 0

        while tiempo_transcurrido < tiempo_de_espera:
            numero_ventanas_activas = len(web_driver.window_handles)

            if numero_ventanas_activas < 2:
                break

            time.sleep(1)
            tiempo_transcurrido += 1
