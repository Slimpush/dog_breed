[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

# Dog API

API для управления собаками и породами. Вы можете создавать, просматривать, редактировать и удалять записи о собаках и их породах.

## Модели

### Dog (Собака)
- **name**: Имя собаки (строка)
- **age**: Возраст собаки (целое число)
- **breed**: Порода (ссылка на модель Breed)
- **gender**: Пол собаки (строка)
- **color**: Окрас собаки (строка)
- **favorite_food**: Любимая еда (строка)
- **favorite_toy**: Любимая игрушка (строка)

### Breed (Порода)
- **name**: Название породы (строка)
- **size**: Размер (Tiny, Small, Medium, Large)
- **friendliness**: Дружелюбность (от 1 до 5)
- **trainability**: Обучаемость (от 1 до 5)
- **shedding_amount**: Количество шерсти при линьке (от 1 до 5)
- **exercise_needs**: Потребности в активности (от 1 до 5)

## API Эндпоинты

### Управление собаками
- **GET /api/dogs/** — Получить список всех собак  
  ![Список собак](docs/postman_screenshots/GET_api_dogs.jpg)

- **POST /api/dogs/** — Добавить новую собаку  
  ![Добавить собаку](docs/postman_screenshots/POST_api_dogs.jpg)

- **GET /api/dogs/<id>/** — Получить информацию о собаке по ID  
  ![Получить собаку по ID](docs/postman_screenshots/GET_api_dogs_id.jpg)

- **PUT /api/dogs/<id>/** — Обновить информацию о собаке по ID  
  ![Обновить собаку](docs/postman_screenshots/PUT_api_dogs_id.jpg)

- **DELETE /api/dogs/<id>/** — Удалить собаку по ID  
  ![Удалить собаку](docs/postman_screenshots/DELETE_api_dogs_id.jpg)

### Управление породами
- **GET /api/breeds/** — Получить список всех пород  
  ![Список пород](docs/postman_screenshots/GET_api_breeds.jpg)

- **POST /api/breeds/** — Добавить новую породу  
  ![Добавить породу](docs/postman_screenshots/POST_api_breeds.jpg)

- **GET /api/breeds/<id>/** — Получить информацию о породе по ID  
  ![Получить породу по ID](docs/postman_screenshots/GET_api_dogs_id.jpg)

- **PUT /api/breeds/<id>/** — Обновить информацию о породе по ID  
  ![Обновить породу](docs/postman_screenshots/PUT_api_dogs_id.jpg)

- **DELETE /api/breeds/<id>/** — Удалить породу по ID  
  ![Удалить породу](docs/postman_screenshots/DELETE_api_dogs_id.jpg)

---

Каждый скриншот отображает выполнение запросов к соответствующим эндпоинтам через Postman.
