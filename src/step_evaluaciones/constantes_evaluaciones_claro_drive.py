# ingreso_pagina_principal_claro_drive

MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_EXITOSO = 'Se ingresa correctamente a la pagina principal de Drop Box'
MSG_OUTPUT_INGRESO_PAGINA_PRINCIPAL_SIN_EXITO = 'No fue posible ingresar a la pagina principal de Drop Box: {}'

# inicio_sesion_claro_drive
MSG_OUTPUT_INICIO_SESION_EXITOSO = 'Se ingresa correctamente al portal Drop Box'
MSG_OUTPUT_INICIO_SESION_SIN_EXITO = 'No fue posible ingresar al portal Drop Box: {}'

# carga_archivo_claro_drive
MSG_OUTPUT_CARGA_ARCHIVO_EXITOSO = 'Se realiza correctamente la carga del archivo'
MSG_OUTPUT_CARGA_ARCHIVO_SIN_EXITO = 'No fue posible realizar la carga del archivo: {}'

# descarga_archivo_claro_drive
MSG_OUTPUT_DESCARGA_ARCHIVO_EXITOSO = 'Se realiza la descarga del archivo correctamente'
MSG_OUTPUT_DESCARGA_ARCHIVO_SIN_EXITO = 'No fue posible realizar la descarga del archivo correctamente: {}'

# borrar_archivo_claro_drive
MSG_OUTPUT_BORRADO_ARCHIVO_EXITOSO = 'Se realiza el borrado del archivo correctamente'
MSG_OUTPUT_BORRADO_ARCHIVO_SIN_EXITO = 'No fue posible realizar el borrado del archivo correctamente: {}'

# cerrar_sesion_claro_drive
MSG_OUTPUT_CIERRE_SESION_EXITOSO = 'Se cierra sesion correctamente'
MSG_OUTPUT_CIERRE_SESION_SIN_EXITO = 'No fue posible realizar el cierre de sesion: {}'

# ingreso a la pagina principal sin exito
MSG_INICIO_SESION_FALLIDA_POR_INGRESO_DE_PAGINA = 'No fue posible iniciar sesion dentro de la plataforma Drop Box. ' \
                                                  'Ingreso a la pagina principal de la plataforma Drop box sin exito.'

MSG_CARGA_ARCHIVO_FALLIDA_POR_INICIO_DE_SESION = 'No fue posible cargar el archivo dentro de la plataforma Drop ' \
                                                  'Box. Inicio de sesion dentro de la plataforma sin exito.'

MSG_DESCARGA_ARCHIVO_FALLIDA_POR_CARGA_ARCHIVO_FALLIDA = 'No fue posible descargar el archivo dentro de la ' \
    'plataforma Drop Box. Carga de archivo dentro de la plataforma sin exito.'

MSG_ELIMINACION_ARCHIVO_FALLIDA_POR_CARGA_ARCHIVO_FALLIDA = 'No fue posible eliminar el archivo dentro de la ' \
    'plataforma Drop Box. Carga de archivo dentro de la plataforma sin exito.'

MSG_CIERRE_SESION_FALLIDA_POR_INICIO_DE_SESION = 'No fue posible realizar el cierre de sesion dentro de la ' \
    'plataforma Drop Box. Inicio de sesion dentro de la plataforma sin exito.'

# identificadores html de cada elemento por localizar

# STEP INGRESO DE PAGINA PRINCIPAL
HTML_STEP_INGRESO_PAGINA_ID_PORTAL_PRINCIPAL = 'maestro-portal'
HTML_STEP_INGRESO_PAGINA_CLASS_NAME_BOTON_PERFIL_USUARIO = 'dig-Avatar'
HTML_STEP_INGRESO_PAGINA_XPATH_BOTON_CIERRE_DE_SESION = '//div[@class="dig-Menu-row-title"][text()="Salir"]'
HTML_STEP_INGRESO_PAGINA_NAME_INPUT_LOGIN_EMAIL = 'login_email'
HTML_STEP_INGRESO_PAGINA_NAME_INPUT_LOGIN_PASSWORD = 'login_password'

# STEP INICIO SESION DROPBOX
HTML_STEP_INICIO_SESION_XPATH_BTN_INICIO_SESION = '//button[@class="auth-google button-primary"]'
HTML_STEP_INICIO_SESION_ID_HEADING_TEXT = 'headingText'
HTML_STEP_INICIO_SESION_ID_VIEW_CONTAINER = 'view_container'
HTML_STEP_INICIO_SESION_XPATH_BTN_USUARIO = '//div[@data-email="{}"]'
HTML_STEP_INICIO_SESION_ID_DIV_PASSWORD_GMAIL = 'password'
HTML_STEP_INICIO_SESION_NAME_INPUT_PASSWORD_GMAIL = 'password'
HTML_STEP_INICIO_SESION_ID_BTN_INICIO_DE_SESION = 'passwordNext'
HTML_STEP_INICIO_SESION_CLASS_NAME_DIV_MAESTRO_PORTAL = 'maestro-portal'

# STEP CARGAR ARCHIVO DROPBOX
HTML_STEP_CARGAR_ARCHIVO_URL_ROLE_PERSONAL = 'https://www.dropbox.com/h?role=personal'
HTML_STEP_CARGAR_ARCHIVO_CLASS_NAME_FOOTER = 'dig-Modal-footer'
HTML_STEP_CARGAR_ARCHIVO_CLASS_NAME_BTN_CARGA = 'dig-Button--primary'
HTML_STEP_CARGAR_ARCHIVO_XPATH_BTN_CERRAR_PROGRESO_CARGA = '//button[@data-testid="rich-snackbar-close-btn"]'

# STEP DESCARGA ARCHIVO DROPBOX
HTML_STEP_DESCARGA_ARCHIVO_CLASS_NAME_SEARCH_BAR = 'dig-GlobalHeader-Search__input'
HTML_STEP_DESCARGA_ARCHIVO_XPATH_ARCHIVO_POR_DESCARGAR = '//tr[@data-filename="{}"]'
HTML_STEP_DESCARGA_ARCHIVO_CLASS_NAME_CHECKBOX = 'brws-checkbox-cell'
HTML_STEP_DESCARGA_ARCHIVO_XPATH_BTN_MAS_ACCIONES = '//button[@data-testid="action-bar-overflow"]'
HTML_STEP_DESCARGA_ARCHIVO_XPATH_BTN_DESCARGAR = '//div[@class="dig-Menu-row-title"][text()="Descargar"]'

# STEP ELIMINAR ARCHIVO DROPBOX
HTML_STEP_ELIMINAR_ARCHIVO_XPATH_ARCHIVO_POR_ELIMINAR = '//tr[@data-filename="{}"]'
HTML_STEP_ELIMINAR_ARCHIVO_XPATH_BTN_MAS_ACCIONES = '//button[@data-testid="action-bar-overflow"]'
HTML_STEP_ELIMINAR_ARCHIVO_XPATH_BTN_ELIMINAR = '//div[@class="dig-Menu-row-title"][text()="Eliminar"]'
HTML_STEP_ELIMINAR_ARCHIVO_XPATH_BTN_ELIMINAR_MODAL = '//span[@class="dig-Button-content"][text()="Eliminar"]'
HTML_STEP_ELIMINAR_ARCHIVO_XPATH_MSG_ELIMINACION_EXITOSA = '//span[@class="dig-Snackbar-message "][text()="Se ' \
                                                           'elimin\u00F3 1 elemento."]'

# STEP CERRAR SESION DROPBOX
HTML_STEP_CERRAR_SESION_CLASS_NAME_BTN_IMAGEN_PERFIL = 'dig-Avatar'
HTML_STEP_CERRAR_SESION_XPATH_BTN_CERRAR_SESION = '//div[@class="dig-Menu-row-title"][text()="Salir"]'
HTML_STEP_CERRAR_SESION_NAME_INPUT_LOGIN_EMAIL = 'login_email'
HTML_STEP_CERRAR_SESION_NAME_INPUT_LOGIN_PASSWORD = 'login_password'

# TIEMPOS DE CADA EJECUCION DE STEP

# STEP INGRESO DE PAGINA PRINCIPAL
TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_INICIALIZACION_WEBDRIVER = 4
TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_BOTON_IMG_PERFIL = 12
TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_BOTON_SALIR_SESION = 12
TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_INPUT_LOGIN_EMAIL = 10
TIMEOUT_STEP_INGRESO_PAGINA_PRINCIPAL_INPUT_LOGIN_PASSWORD = 10

# STEP INICIO DE SESION DROP BOX
TIMEOUT_STEP_INICIO_SESION_DROP_BOX_BOTON_INICIO_SESION_GMAIL = 12#6
TIMEOUT_STEP_INICIO_SESION_DROP_BOX_VENTANAS_EN_SESION = 12#6
TIMEOUT_STEP_INICIO_SESION_DROP_BOX_HEADING_TEXT = 10
TIMEOUT_STEP_INICIO_SESION_DROP_BOX_VIEW_CONTAINER = 10
TIMEOUT_STEP_INICIO_SESION_DROP_BOX_BOTON_USUARIO_GMAIL = 18
TIMEOUT_STEP_INICIO_SESION_DROP_BOX_ESPERA_RENDER_BOTON_USUARIO_GMAIL = 2
TIMEOUT_STEP_INICIO_SESION_DROP_BOX_PORTAL_PRINCIPAL = 48 #18

# STEP CARGA DE ARCHIVO EN PORTAL DROP BOX
TIMEOUT_STEP_CARGA_ARCHIVO_VALIDACION_DE_CARGA = 20
TIMEOUT_STEP_CARGA_ARCHIVO_VALIDACION_ELEMENTO_FOOTER = 5
TIMEOUT_STEP_CARGA_ARCHIVO_VALIDACION_BOTON_CARGA_DE_ARCHIVO = 5
TIMEOUT_STEP_CARGA_ARCHIVO_VERIFICACION_CARGA_EXITOSA = 720
TIMEOUT_STEP_CARGA_ARCHIVO_BOTON_CIERRE_PROGRESO_CARGA = 10

# STEP DESCARGA DE ARCHIVO EN PORTAL DROP BOX
TIMEOUT_STEP_DESCARGA_ARCHIVO_BARRA_BUSQUEDA = 20
TIMEOUT_STEP_DESCARGA_ARCHIVO_ELEM_HTML_ARCHIVO_POR_DESCARGAR = 20
TIMEOUT_STEP_DESCARGA_ARCHIVO_CHECKBOX_ARCHIVO_POR_DESCARGAR = 10
TIMEOUT_STEP_DESCARGA_ARCHIVO_BOTON_MAS_ACCIONES = 20
TIMEOUT_STEP_DESCARGA_ARCHIVO_BOTON_DESCARGAR = 20
TIMEOUT_STEP_DESCARGA_ARCHIVO_VERIFICAR_TIEMPO_DESCARGA = 180

# STEP ELIMINACION DE ARCHIVO EN PORTAL DROP BOX
TIMEOUT_STEP_ELIMINACION_ARCHIVO_ELEM_ARCHIVO_POR_ELIMINAR = 20
TIMEOUT_STEP_ELIMINACION_ARCHIVO_BOTON_MAS_ACCIONES = 20
TIMEOUT_STEP_ELIMINACION_ARCHIVO_BOTON_ELIMINAR = 20
TIMEOUT_STEP_ELIMINACION_ARCHIVO_BOTON_ELIMINAR_MODAL = 20
TIMEOUT_STEP_ELIMINACION_ARCHIVO_MENSAJE_ELIMINACION_ELEMENTO = 30

# STEP CIERRE DE SESION EN PORTAL DROP BOX
TIMEOUT_STEP_CIERRE_DE_SESION_BOTON_IMAGEN_PERFIL = 12
TIMEOUT_STEP_CIERRE_DE_SESION_BOTON_SALIR_SESION = 12
TIMEOUT_STEP_CIERRE_DE_SESION_INPUT_LOGIN_EMAIL = 10
TIMEOUT_STEP_CIERRE_DE_SESION_INPUT_LOGIN_PASSWORD = 10
