from address import Address
from mailing import Mailing

from_addr = Address("123456", "Москва", "Тверская", "10", "5")
to_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "12", "67")

from_addr = Address("индекс", "город", "улица", "дом", "квартира")
mail = Mailing(to_address=to_addr, from_address=from_addr,
               cost=250.0, track="RC123456789RU")

track_info = f"Отправление {mail.track} из "
from_info = from_addr.formatted()
to_info = f" в {mail.to_address.formatted()}"
cost_info = f". Стоимость {mail.cost} рублей."
print(track_info + from_info + to_info + cost_info)
