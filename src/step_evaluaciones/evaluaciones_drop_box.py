import time
from os import path
from pathlib import Path

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from src.step_evaluaciones import constantes_evaluaciones_claro_drive as const
from src.utils.utils_evaluaciones import UtilsEvaluaciones
from src.utils.utils_html import ValidacionesHtml
from src.utils.utils_temporizador import Temporizador
from src.webdriver_actions.html_actions import HtmlActions


class EvaluacionesDropBoxDriveSteps:

    def ingreso_pagina_principal_dropbox(self, webdriver_test_ux: WebDriver, json_eval, url_login):
        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        webdriver_test_ux.get(url_login)

        try:
            time.sleep(const.TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_INICIALIZACION_WEBDRIVER)

            # verifica que no estemos loggeados desde un inicio, en caso contrario, cerramos sesion
            if ValidacionesHtml.verificar_elemento_html_por_id('maestro-portal', webdriver_test_ux):

                boton_imagen_perfil = HtmlActions.webdriver_wait_element_to_be_clickable(
                    webdriver_test_ux,
                    const.TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_BOTON_IMG_PERFIL,
                    class_name='account-menu-v2__avatar')

                HtmlActions.click_html_element(boton_imagen_perfil, class_name='account-menu-v2__avatar')

                boton_salir_sesion = HtmlActions.webdriver_wait_element_to_be_clickable(
                    webdriver_test_ux, const.TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_BOTON_SALIR_SESION,
                    xpath='//div[@class="dig-Menu-row-title"][text()="Salir"]')

                HtmlActions.click_html_element(
                    boton_salir_sesion, xpath='//div[@class="dig-Menu-row-title"][text()="Salir')

            else:
                webdriver_test_ux.get(url_login)

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, const.TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_INPUT_LOGIN_EMAIL, name='login_email')

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, const.TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_INPUT_LOGIN_PASSWORD,
                name='login_password')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 0, 0, True, const.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = const.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = const.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = const.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = const.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        except WebDriverException as e:
            msg_output = const.MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 0, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 0, tiempo_step_inicio, fecha_inicio)

        return json_eval

    def inicio_sesion_dropbox(self, webdriver_test_ux: WebDriver, json_eval, json_args, url_login):
        tiempo_step_inicio = None
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_pagina_principal(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 1,
                const.MSG_INICIO_SESION_FALLIDA_POR_INGRESO_DE_PAGINA)

            return json_eval

        try:

            btn_inicio_sesion = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_INICIO_SESION_DROP_BOX_BOTON_INICIO_SESION_GMAIL,
                xpath='//button[@class="auth-google button-primary"]')

            HtmlActions.click_html_element(btn_inicio_sesion, xpath='//button[@class="auth-google button-primary"]')

            if ValidacionesHtml.se_encuentran_mas_ventanas_en_sesion(
                    webdriver_test_ux, const.TIMEOUT_STEP_INICIO_SESION_DROP_BOX_VENTANAS_EN_SESION):
                ventana_padre = webdriver_test_ux.window_handles[0]
                ventana_hija = webdriver_test_ux.window_handles[1]

                webdriver_test_ux.switch_to.window(ventana_hija)

            btn_usuario = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_INICIO_SESION_DROP_BOX_BOTON_INICIO_SESION_GMAIL,
                xpath='//div[@data-email="{}"]'.format(json_args['user']))

            time.sleep(const.TIMEOUT_STEP_INICIO_SESION_DROP_BOX_ESPERA_RENDER_BOTON_USUARIO_GMAIL)

            HtmlActions.click_html_element(btn_usuario, xpath='//div[@data-email="{}"]'.format(json_args['user']))

            ValidacionesHtml.espera_desaparicion_modal_acceso_de_google(webdriver_test_ux, 60)

            tiempo_step_inicio = Temporizador.obtener_tiempo_timer()

            webdriver_test_ux.switch_to.window(ventana_padre)

            HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_INICIO_SESION_DROP_BOX_PORTAL_PRINCIPAL,
                class_name='maestro-portal')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 1, 0, True, const.MSG_OUTPUT_INICIO_SESION_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = const.MSG_OUTPUT_INICIO_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = const.MSG_OUTPUT_INICIO_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = const.MSG_OUTPUT_INICIO_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = const.MSG_OUTPUT_INICIO_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 1, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 1, tiempo_step_inicio, fecha_inicio)

        return json_eval

    def cargar_archivo_dropbox(self, webdriver_test_ux: WebDriver, json_eval, json_args, nombre_archivo_sin_ext,
                               nombre_archivo_con_ext):
        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 2,
                const.MSG_CARGA_ARCHIVO_FALLIDA_POR_INICIO_DE_SESION)

            return json_eval

        try:
            ValidacionesHtml.verificar_remover_ventana_configuracion(webdriver_test_ux)
            ValidacionesHtml.verificar_archivo_ya_existente_en_portal(webdriver_test_ux, nombre_archivo_sin_ext)

            # seingresa a la pagina principal del portal
            webdriver_test_ux.get('https://www.dropbox.com/h?role=personal')

            ValidacionesHtml.cargar_archivo_en_portal_drop_box(
                webdriver_test_ux, json_args['pathImage'], const.TIMEOUT_STEP_CARGA_ARCHIVO_VALIDACION_DE_CARGA)

            footer = HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, const.TIMEOUT_STEP_CARGA_ARCHIVO_VALIDACION_ELEMENTO_FOOTER,
                class_name='dig-Modal-footer')

            btn_carga = HtmlActions.webdriver_wait_element_to_be_clickable(
                footer, const.TIMEOUT_STEP_CARGA_ARCHIVO_VALIDACION_BOTON_CARGA_DE_ARCHIVO,
                class_name='dig-Button--primary')

            HtmlActions.click_html_element(btn_carga, class_name='dig-Button--primary')

            ValidacionesHtml.verificar_mensaje_de_carga_exitosa_de_archivo(
                webdriver_test_ux, nombre_archivo_con_ext, const.TIMEOUT_STEP_CARGA_ARCHIVO_VERIFICACION_CARGA_EXITOSA)

            btn_cerrar_progreso_carga = HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, const.TIMEOUT_STEP_CARGA_ARCHIVO_BOTON_CIERRE_PROGRESO_CARGA,
                xpath='//button[@data-testid="rich-snackback-close-btn"]')

            HtmlActions.click_html_element(btn_cerrar_progreso_carga,
                                           xpath='//button[@data-testid="rich-snackback-close-btn"]')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 2, 0, True, const.MSG_OUTPUT_CARGA_ARCHIVO_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = const.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = const.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = const.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = const.MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 2, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 2, tiempo_step_inicio, fecha_inicio)

        return json_eval

    def descargar_archivo_dropbox(self, webdriver_test_ux: WebDriver, json_eval, nombre_archivo_con_ext):

        extension_del_archivo = path.splitext(nombre_archivo_con_ext)[1]
        nombre_del_archivo_sin_extension = Path(nombre_archivo_con_ext).stem

        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 3,
                const.MSG_DESCARGA_ARCHIVO_FALLIDA_POR_CARGA_ARCHIVO_FALLIDA)

            return json_eval

        try:
            ValidacionesHtml.verificar_remover_ventana_configuracion(webdriver_test_ux)

            search_bar = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_DESCARGA_ARCHIVO_BARRA_BUSQUEDA, class_name='search__input')

            HtmlActions.enviar_data_keys(search_bar, nombre_archivo_con_ext, class_name='search__input')

            HtmlActions.enviar_data_keys(search_bar, Keys.RETURN, class_name='search__input')

            archivo_por_descargar = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_DESCARGA_ARCHIVO_ELEM_HTML_ARCHIVO_POR_DESCARGAR,
                xpath='//tr[@data-filename="{}"]'.format(nombre_archivo_con_ext))

            checkbox = HtmlActions.webdriver_wait_element_to_be_clickable(
                archivo_por_descargar, const.TIMEOUT_STEP_DESCARGA_ARCHIVO_CHECKBOX_ARCHIVO_POR_DESCARGAR,
                class_name='brws-checkbox-cell')

            HtmlActions.click_html_element(checkbox, class_name='brws-checkbox-cell')

            btn_mas_acciones = HtmlActions.webdriver_wait_element_to_be_clickable(
                archivo_por_descargar, const.TIMEOUT_STEP_DESCARGA_ARCHIVO_BOTON_MAS_ACCIONES,
                xpath='//button[@data-testid="action-bar-overflow"]')

            HtmlActions.click_html_element(btn_mas_acciones, xpath='//button[@data-testid="action-bar-overflow"]')

            btn_descargar = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_DESCARGA_ARCHIVO_BOTON_DESCARGAR,
                xpath='//div[@class="dig-Menu-row-title"][text()="Descargar"]')

            HtmlActions.click_html_element(btn_descargar,
                                           xpath='//div[@class="dig-Menu-row-title"][text()="Descargar"]')

            UtilsEvaluaciones.verificar_descarga_en_ejecucion(
                nombre_del_archivo_sin_extension, extension_del_archivo,
                const.TIMEOUT_STEP_DESCARGA_ARCHIVO_VERIFICAR_TIEMPO_DESCARGA)

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 3, 0, True, const.MSG_OUTPUT_DESCARGA_ARCHIVO_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = const.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = const.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = const.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = const.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        except StaleElementReferenceException as e:
            msg_output = const.MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 3, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 3, tiempo_step_inicio, fecha_inicio)

        return json_eval

    def eliminar_archivo_dropbox(self, webdriver_test_ux: WebDriver, json_eval, nombre_archivo_con_ext):
        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 4,
                const.MSG_ELIMINACION_ARCHIVO_FALLIDA_POR_CARGA_ARCHIVO_FALLIDA)

            return json_eval

        try:

            archivo_por_eliminar = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_ELIMINACION_ARCHIVO_ELEM_ARCHIVO_POR_ELIMINAR,
                xpath='//tr[@data-filename="{}"]'.format(nombre_archivo_con_ext))

            btn_mas_acciones = HtmlActions.webdriver_wait_element_to_be_clickable(
                archivo_por_eliminar, const.TIMEOUT_STEP_ELIMINACION_ARCHIVO_BOTON_MAS_ACCIONES,
                xpath='//button[@data-testid="action-bar-overflow"]')

            HtmlActions.click_html_element(btn_mas_acciones, xpath='//button[@data-testid="action-bar-overflow"]')

            btn_eliminar = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_ELIMINACION_ARCHIVO_BOTON_ELIMINAR,
                xpath='//div[@class="dig-Menu-row-title"][text()="Eliminar"]')

            HtmlActions.click_html_element(
                btn_eliminar, xpath='//div[@class="dig-Menu-row-title"][text()="Eliminar"]')

            btn_eliminar_modal = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_ELIMINACION_ARCHIVO_BOTON_ELIMINAR_MODAL,
                xpath='//span[@class="dig-Button-content"][text()="Eliminar"]')

            HtmlActions.click_html_element(
                btn_eliminar_modal, xpath='//span[@class="dig-Button-content"][text()="Eliminar"]')

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, const.TIMEOUT_STEP_ELIMINACION_ARCHIVO_MENSAJE_ELIMINACION_ELEMENTO,
                xpath='//span[@class="dig-Snackbar-message "][text()="Se elimin\u00F3 1 elemento."]')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 4, 0, True, const.MSG_OUTPUT_BORRADO_ARCHIVO_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = const.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = const.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = const.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = const.MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 4, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 4, tiempo_step_inicio, fecha_inicio)

        return json_eval

    def cerrar_sesion_dropbox(self, webdriver_test_ux: WebDriver, json_eval):
        tiempo_step_inicio = Temporizador.obtener_tiempo_timer()
        fecha_inicio = Temporizador.obtener_fecha_tiempo_actual()

        if not UtilsEvaluaciones.se_ingreso_correctamente_a_la_sesion(json_eval):
            json_eval = UtilsEvaluaciones.generar_json_inicio_de_sesion_incorrecta(
                json_eval, tiempo_step_inicio, fecha_inicio, 5,
                const.MSG_CIERRE_SESION_FALLIDA_POR_INICIO_DE_SESION)

            return json_eval

        try:
            boton_imagen_perfil = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_CIERRE_DE_SESION_BOTON_IMAGEN_PERFIL,
                class_name='account-menu-v2__avatar')

            HtmlActions.click_html_element(boton_imagen_perfil, class_name='account-menu-v2__avatar')

            boton_salir_sesion = HtmlActions.webdriver_wait_element_to_be_clickable(
                webdriver_test_ux, const.TIMEOUT_STEP_CIERRE_DE_SESION_BOTON_SALIR_SESION,
                xpath='//div[@class="dig-Menu-row-title"][text()="Salir"]')

            HtmlActions.click_html_element(boton_salir_sesion, xpath='//div[@class="dig-Menu-row-title"][text()="Salir')

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, const.TIMEOUT_STEP_CIERRE_DE_SESION_INPUT_LOGIN_EMAIL, name='login_email')

            HtmlActions.webdriver_wait_presence_of_element_located(
                webdriver_test_ux, const.TIMEOUT_STEP_CIERRE_DE_SESION_INPUT_LOGIN_PASSWORD, name='login_password')

            json_eval = UtilsEvaluaciones.establecer_output_status_step(
                json_eval, 5, 0, True, const.MSG_OUTPUT_CIERRE_SESION_EXITOSO)

        except ElementNotInteractableException as e:
            msg_output = const.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        except NoSuchElementException as e:
            msg_output = const.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        except TimeoutException as e:
            msg_output = const.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        except ElementClickInterceptedException as e:
            msg_output = const.MSG_OUTPUT_CIERRE_SESION_SIN_EXITO.format(e.msg)
            json_eval = UtilsEvaluaciones.establecer_output_status_step(json_eval, 5, 0, False, msg_output)

        json_eval = UtilsEvaluaciones.finalizar_tiempos_en_step(json_eval, 5, tiempo_step_inicio, fecha_inicio)

        return json_eval
