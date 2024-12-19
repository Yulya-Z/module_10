import requests

# Отправляем GET-запрос к URL
r = requests.get('http://api.github.com/events')
# передача параметров в URL адресах
data = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org//get', params=data)
print(r.url)
# проверяем код статус ответа
print(r.status_code)
# при создании неправильного запроса, т.к. у нас правильный, то None
print(r.raise_for_status())
# Отправляем POST-запрос к URL с данными
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org//get', data=data)
# выводим текст ответа
print(r.text)
# Отправляем DEL-запрос к URL с данными
r = requests.delete('https://httpbin.org//delet')
# выводим текст ответа
print(r.text)
