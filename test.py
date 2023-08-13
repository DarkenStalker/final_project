# Илья Синелев, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_get_order():
    order_response = sender_stand_request.get_order()
    assert order_response.status_code == 201


