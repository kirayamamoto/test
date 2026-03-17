# event_ticketing/services/strategy.py

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """Интерфейс для различных способов оплаты."""
    @abstractmethod
    def pay(self, ticket, card_info):
        """Пытается провести оплату. При успехе меняет состояние ticket,
        при неудаче кидает Exception."""
        pass

class SimplePaymentStrategy(PaymentStrategy):
    """Простейшая реализация: если card_info == "fail" — бросает ошибку,
    иначе помечает билет как оплаченный."""
    def pay(self, ticket, card_info):
        if card_info == "fail":
            raise Exception("Payment failed")
        ticket.paid = True
