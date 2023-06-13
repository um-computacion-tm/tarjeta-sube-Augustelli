class NoHaySaldoException(Exception):
    pass


class UsuarioDesactivadoException(Exception):
    pass


class EstadoNoExistenteException(Exception):
    pass


PRECIO_TICKET = 50
PRIMARIO = "primario"
ACTIVADO = "activado"
DESACTIVADO = "desactivado"


class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            return 35
        else:
            return PRECIO_TICKET

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("Usuario desactivado. No se puede pagar el pasaje.")

        precio_ticket = self.obtener_precio_ticket()
        if self.saldo < precio_ticket:
            raise NoHaySaldoException("Saldo insuficiente. No se puede pagar el pasaje.")

        self.saldo -= precio_ticket

    def cambiar_estado(self, estado):
        if estado not in [ACTIVADO, DESACTIVADO]:
            raise EstadoNoExistenteException("Estado no existente.")

        self.estado = estado

    def cambiar_grupo_beneficiario(self, grupo_beneficiario):
        self.grupo_beneficiario = grupo_beneficiario
