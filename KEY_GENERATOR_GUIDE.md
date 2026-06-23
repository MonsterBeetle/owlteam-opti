# 🔑 OwlTeam Opti - License Key Generator

## Как работает генератор ключей

### Формат ключа
```
OWL-XXXXX-XXXXX-XXXXX-XXXXX
```

Пример:
```
OWL-A3K2M-7PQ9L-B8RC5-N2VD4
```

### Компоненты ключа
- **OWL** - Префикс (OwlTeam Opti)
- **5 + 5 + 5 + 5 символов** - Случайные буквы (A-Z) и цифры (0-9)
- **Всего 29 символов** включая дефисы

### Как использовать генератор

#### Вариант 1: Через CLI (Командная строка)

```bash
python key_generator_cli.py
```

Меню:
1. **Generate single key** - Создать один ключ
2. **Generate batch of keys** - Создать пакет ключей (например, 100 шт)
3. **Export keys to file** - Сохранить ключи в JSON файл
4. **View key formats** - Посмотреть примеры форматов
5. **Exit** - Выход

#### Вариант 2: Через Python код

```python
from tools.key_generator import KeyGenerator

# Создаём генератор
gen = KeyGenerator()

# Генерируем один ключ
key = gen.generate_key()
print(key)  # OWL-A3K2M-7PQ9L-B8RC5-N2VD4

# Генерируем пакет из 50 ключей на 30 дней
keys = gen.generate_batch(count=50, duration="30_days")
for key_info in keys:
    print(f"{key_info['key']} - {key_info['duration']}")

# Проверяем формат ключа
if gen.validate_key_format("OWL-A3K2M-7PQ9L-B8RC5-N2VD4"):
    print("✓ Ключ валидный")
```

### Доступные сроки действия

```python
LICENSE_DURATION_DAYS = {
    "7_days": 7,        # Неделя
    "30_days": 30,      # Месяц
    "90_days": 90,      # 3 месяца
    "365_days": 365,    # Год
    "lifetime": 99999   # На всегда
}
```

### Примеры использования

#### Пример 1: Генерация одного ключа
```bash
$ python key_generator_cli.py

[1] Single key
[2] Batch keys
...

Choice: 1

Duration options:
[1] 7_days
[2] 30_days
[3] 90_days
[4] 365_days
[5] lifetime

Choice: 2

✅ Generated!
Key: OWL-K9M2X-5WL7P-3R8Q1-4J6T2
Duration: 30_days
Days: 30
```

#### Пример 2: Генерация пакета
```bash
Choice: 2

Number of keys: 100

Duration: 2

⏳ Generating 100 keys...

✅ Generated 100 keys!

1. OWL-A3K2M-7PQ9L-B8RC5-N2VD4 (30_days)
2. OWL-K9M2X-5WL7P-3R8Q1-4J6T2 (30_days)
3. OWL-P5N1X-8QR3L-2M7C4-5K9V6 (30_days)
...
100. OWL-X2B4L-9M3P7-6K1W5-4R8T9 (30_days)

Save to file? (y/n): y

💾 Keys saved to: generated_keys/keys_30_days_20240623_221000.json
```

### Структура JSON файла с ключами

```json
{
  "generated_at": "2024-06-23T22:10:00.123456",
  "duration": "30_days",
  "days": 30,
  "count": 100,
  "keys": [
    {
      "key": "OWL-A3K2M-7PQ9L-B8RC5-N2VD4",
      "duration": "30_days",
      "created_at": "2024-06-23T22:10:00.123456"
    },
    ...
  ]
}
```

### Привязка к HWID

Когда пользователь вводит ключ в приложении:

1. Приложение получает HWID пользователя (уникальный для его ПК)
2. Сравнивает HWID с сохранённым в базе данных
3. Если HWID совпадает - ключ активируется
4. Если HWID не совпадает - ключ отклоняется (нельзя давать друзьям)

### Процесс активации в приложении

```
Узер заходит в License Manager
    ↓
Система генерирует HWID пользователя
    ↓
Узер вводит ключ (OWL-XXXXX-XXXXX-XXXXX-XXXXX)
    ↓
Приложение проверяет:
  - Ключ существует в БД?
  - HWID совпадает?
  - Ключ не истёк?
    ↓
Если ДА - Активация успешна ✅
Если НЕТ - Ошибка ❌
```

---

## Требования для запуска оптимизатора

### Python версия
**Python 3.8 или выше** (рекомендуется **3.10+**)

Проверить версию:
```bash
python --version
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Список зависимостей

```
PyQt6==6.7.0              # GUI фреймворк
PyQt6-sip==13.6.0         # PyQt6 зависимость
psutil==5.9.8             # Мониторинг системы
wmi==1.5.1                # Windows Management Info
gputil==1.4.0             # GPU информация
requests==2.31.0          # HTTP запросы
Pillow==10.1.0            # Работа с изображениями
numpy==1.24.3             # Численные вычисления
matplotlib==3.8.2         # Графики
sqlite3-python==1.0.0     # База данных
cryptography==41.0.7      # Шифрование
hwinfo==1.0.0             # Информация о железе
opencv-python==4.8.1.78   # Компьютерное зрение
pyinstaller==6.3.0        # Сборка в EXE
```

### Системные требования

- **ОС**: Windows 10 / Windows 11
- **RAM**: Минимум 2GB (рекомендуется 4GB+)
- **Место на диске**: 500MB свободного места
- **Internet**: Для первичной загрузки зависимостей

### Как запустить оптимизатор

#### Вариант 1: Через Python

```bash
# 1. Установить зависимости
pip install -r requirements.txt

# 2. Запустить приложение
python main.py
```

#### Вариант 2: Через batch файл

```bash
run.bat
```

#### Вариант 3: Собрать EXE

```bash
# Установить PyInstaller (если не установлен)
pip install pyinstaller

# Собрать приложение
python build.py

# Запустить из dist/
dist/OwlTeam-Opti.exe
```

#### Вариант 4: Использовать готовый batch файл для сборки

```bash
build.bat
```

### Проверка установки

```bash
# Проверить Python
python --version

# Проверить pip
pip --version

# Проверить установку PyQt6
python -c "from PyQt6.QtWidgets import QApplication; print('✓ PyQt6 installed')"

# Проверить psutil
python -c "import psutil; print(f'✓ psutil {psutil.__version__} installed')"
```

### Решение проблем

#### Ошибка: "ModuleNotFoundError: No module named 'PyQt6'"
```bash
pip install PyQt6 --upgrade
```

#### Ошибка: "wmi not found"
```bash
pip install wmi pypiwin32
```

#### Python не найден
- Переустановить Python с опцией "Add Python to PATH"
- Использовать полный путь: `C:\\Python310\\python.exe main.py`

#### Приложение медленно работает
- Закрыть ненужные программы
- Увеличить RAM
- Обновить видеодрайверы

---

**OwlTeam Opti © 2024** - Создано с ❤️ для геймеров
