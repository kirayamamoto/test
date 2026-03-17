# event_ticketing/services/decorator.py

class QRDecorator:
    """
    Декоратор для билета: добавляет в объект свойство qr_png,
    генерируемое переданным функтором generator(data).
    """
    def __init__(self, ticket, generator):
        self._ticket   = ticket
        self._generator = generator

    def decorate(self):
        # Собираем минимальный payload
        payload = {
            'ticket_id': self._ticket.id,
            'event_id':  self._ticket.event_id,
            'user_id':   self._ticket.user_id
        }
        # Генерируем QR-код
        qr_base64 = self._generator(payload)
        # Записываем в объект билета
        self._ticket.qr_png = qr_base64
        return self._ticket
