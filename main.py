import requests


def get_api_response(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Помилка отримання відповіді. Код помилки - {response.status_code}")

    except Exception as e:
        print(f"Виникла помилка: {e}")


get_api_response('https://jsonplaceholder.typicode.com/todos/1')
