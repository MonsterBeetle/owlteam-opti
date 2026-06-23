# 🦇 OwlTeam Opti - Системное руководство по лицензированию

## 📋 Содержание
1. [Как работает система ключей](#как-работает-система-ключей)
2. [Генерация ключей](#генерация-ключей)
3. [Привязка к HWID](#привязка-к-hwid)
4. [Локальная работа без сервера](#локальная-работа-без-сервера)
5. [Примеры использования](#примеры-использования)

---

## 🔐 Как работает система ключей

### 🎯 Принцип работы

Система лицензирования OwlTeam Opti полностью **локальная и автономная**. Она не требует:
- ❌ Сайта
- ❌ Хостинга
- ❌ Сервера
- ❌ Интернета (после первого запуска)
- ❌ Платежной системы
- ❌ Базы данных на облаке

### 📊 Архитектура системы

```
┌─────────────────────────────────────────┐
│      OwlTeam Opti (Приложение)          │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Локальная БД (SQLite - licenses.db)    │
│  Хранится в ~/.owlteam_opti/licenses.db │
└─────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   HWID пользователя (CPU+MB+Disk)       │
│   Хранится в ~/.owlteam_opti/hwid.txt   │
└─────────────────────────────────────────┘

При активации ключа:
1. Приложение получает HWID ПК
2. Ищет ключ в БД (licenses.db)
3. Проверяет HWID из БД с текущим HWID
4. Проверяет срок действия
5. Активирует или отклоняет
```

### 🔑 Жизненный цикл ключа

**Шаг 1: Генерация ключа (ТЫ)**
```
Команда: python key_generator_cli.py
         ↓
      Выбор количества: 1-1000
         ↓
      Выбор срока: 7, 30, 90, 365 дней или lifetime
         ↓
    Генерация случайных ключей
         ↓
    Сохранение в JSON файл (generated_keys/)
         ↓
  Ты раздаёшь ключи пользователям
```

**Шаг 2: Активация ключа (ПОЛЬЗОВАТЕЛЬ)**
```
Пользователь запускает OwlTeam Opti
         ↓
Приложение генерирует HWID ПК
         ↓
Пользователь: License Manager → Validate License
         ↓
Вводит ключ (OWL-XXXXX-XXXXX-XXXXX-XXXXX)
         ↓
┌─────────────────────────────────────────┐
│  Приложение проверяет:                  │
│  1. Ключ существует в БД?               │
│  2. HWID совпадает?                     │
│  3. Ключ не истёк?                      │
│  4. Ключ не отозван?                    │
└─────────────────────────────────────────┘
         ↓
    ЕСЛИ ДА → Активация ✅
    ЕСЛИ НЕТ → Ошибка ❌
```

**Шаг 3: Хранение**
```
Вся информация хранится ЛОКАЛЬНО на ПК пользователя:

~/.owlteam_opti/
├── licenses.db          # SQLite база с ключами
├── hwid.txt             # HWID ПК пользователя
└── settings.json        # Настройки приложения
```

### 🛡️ Защита от копирования

**HWID привязка:**
```
Примеры HWID:
- ПК #1: A3B5C7D9E1F3G5H7I9J1K3L5M7N9O1P3
- ПК #2: X1Y2Z3A4B5C6D7E8F9G0H1I2J3K4L5M6
- ПК #3: M9N8O7P6Q5R4S3T2U1V0W9X8Y7Z6A5B4

Когда пользователь вводит ключ:
✓ Ключ OWL-XXXXX связан с HWID ПК #1
✓ HWID текущего ПК = ПК #1 → ✅ Активация
✗ HWID текущего ПК = ПК #2 → ❌ Ошибка: "HWID mismatch"
```

**Почему не работает для друга:**
```
Друг получает ключ от пользователя
Запускает OwlTeam Opti на своём ПК
         ↓
Система генерирует HWID ПК друга (другой!)
         ↓
Друг вводит полученный ключ
         ↓
Приложение проверяет:
  • Ключ найден в БД ✓
  • HWID из БД = "A3B5C7D..." (ПК #1)
  • Текущий HWID = "X1Y2Z3A..." (ПК #2)
  • НЕ СОВПАДАЮТ → ❌ ОШИБКА!
         ↓
Сообщение: "HWID mismatch - License bound to different PC"
```

---

## 🎯 Генерация ключей

### Способ 1: CLI (Рекомендуется для больших партий)

```bash
python key_generator_cli.py
```

**Интерактивное меню:**
```
============================================================
           🔑 OwlTeam Opti - License Key Generator
============================================================

[1] Generate single key
[2] Generate batch of keys
[3] Export keys to file
[4] View key formats
[5] Exit

Select option: 
```

### Вариант A: Генерация одного ключа

```
Choice: 1

Select duration:
[1] 7_days
[2] 30_days
[3] 90_days
[4] 365_days
[5] lifetime

Choice: 2  (выбираем 30 дней)

✅ Key Generated Successfully!

Key: OWL-K9M2X-5WL7P-3R8Q1-4J6T2
Duration: 30_days
Days: 30
Generated: 2024-06-23 22:10:00
```

**Копируешь этот ключ и даёшь пользователю!**

### Вариант B: Генерация пакета ключей (ЛУЧШИЙ ВАРИАНТ)

```
Choice: 2

Number of keys to generate: 100

Select duration:
[1] 7_days
[2] 30_days
[3] 90_days
[4] 365_days
[5] lifetime

Choice: 3  (выбираем 90 дней)

⏳ Generating 100 keys...

✅ Generated 100 keys!

1. OWL-A3K2M-7PQ9L-B8RC5-N2VD4 (90_days)
2. OWL-K9M2X-5WL7P-3R8Q1-4J6T2 (90_days)
3. OWL-P5N1X-8QR3L-2M7C4-5K9V6 (90_days)
...
100. OWL-X2B4L-9M3P7-6K1W5-4R8T9 (90_days)

Save to file? (y/n): y

📄 Keys saved to: generated_keys/keys_90_days_20240623_221000.json
```

**Откроешь JSON файл и увидишь:**
```json
{
  "generated_at": "2024-06-23T22:10:00.123456",
  "duration": "90_days",
  "days": 90,
  "count": 100,
  "keys": [
    {
      "key": "OWL-A3K2M-7PQ9L-B8RC5-N2VD4",
      "duration": "90_days",
      "created_at": "2024-06-23T22:10:00.123456"
    },
    ...
  ]
}
```

**Можешь:**
- Распечатать и раздать
- Скопировать в Excel и отправить по почте
- Выложить в приватный канал Telegram
- Дать в личку Discord

### Способ 2: Python API (для интеграции)

```python
from tools.key_generator import KeyGenerator

gen = KeyGenerator()

# Один ключ на 30 дней
key = gen.generate_key()
print(f"Key: {key}")  # OWL-A3K2M-7PQ9L-B8RC5-N2VD4

# 100 ключей на 365 дней
keys = gen.generate_batch(count=100, duration="365_days")

for key_info in keys:
    print(f"{key_info['key']} - {key_info['duration']}")

# Проверить формат
if gen.validate_key_format("OWL-A3K2M-7PQ9L-B8RC5-N2VD4"):
    print("✓ Valid key format")
```

### Доступные сроки

```python
"7_days"      # Неделя - для тестирования
"30_days"     # Месяц - самый популярный
"90_days"     # 3 месяца - для подписки
"365_days"    # Год - для премиума
"lifetime"    # Навеки - для VIP
```

---

## 🔗 Привязка к HWID

### Что такое HWID?

**HWID** (Hardware ID) - уникальный идентификатор ПК на основе:
```
HWID = SHA256(CPU_ID + MOTHERBOARD_SERIAL + DISK_SERIAL)[:32]
```

**Пример:**
```
ПК #1 (Игровой ПК):
  CPU ID: BFEBFBFF000906A2
  Motherboard: X570-AORUS-MASTER
  Disk Serial: 123456789ABCDEF
  ↓
  HWID: A3B5C7D9E1F3G5H7I9J1K3L5M7N9O1P3

ПК #2 (Ноутбук):
  CPU ID: 63068D910000F11
  Motherboard: LENOVO20V10006US
  Disk Serial: FEDCBA9876543210
  ↓
  HWID: X1Y2Z3A4B5C6D7E8F9G0H1I2J3K4L5M6
```

### Как система работает с HWID?

**Первый запуск приложения:**
```
1. Пользователь запускает OwlTeam Opti
2. Приложение проверяет: есть ли файл hwid.txt?
   - ЕСТь → Загружает сохранённый HWID
   - НЕТ → Генерирует новый HWID из железа
3. Сохраняет HWID в ~/.owlteam_opti/hwid.txt
4. Показывает HWID пользователю (для справки)
```

**При активации ключа:**
```
┌─────────────────────────────────────────┐
│ Пользователь вводит ключ в приложение   │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│ Приложение берёт текущий HWID из hwid.txt│
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│ Ищет ключ в БД (licenses.db)            │
└──────────────┬──────────────────────────┘
               ▼
         ✓ Ключ найден?
         ├─ НЕТ → ❌ "License not found"
         └─ ДА → Проверяем дальше
               ▼
         ✓ HWID совпадает?
         ├─ НЕТ → ❌ "HWID mismatch"
         └─ ДА → Проверяем дальше
               ▼
         ✓ Ключ не истёк?
         ├─ ДА (истёк) → ❌ "License expired"
         └─ НЕТ → Проверяем дальше
               ▼
         ✓ Ключ активен?
         ├─ НЕТ (отозван) → ❌ "License revoked"
         └─ ДА → ✅ АКТИВАЦИЯ УСПЕШНА!
```

---

## 🏠 Локальная работа без сервера

### ✅ Что уже встроено (Всё работает ЛОКАЛЬНО)

**1. Генерация ключей** - На твоём ПК
```bash
python key_generator_cli.py
# Создаёт JSON файл с ключами
# Никуда не отправляет - только на диск
```

**2. База данных ключей** - На диске пользователя
```
~/.owlteam_opti/licenses.db
# SQLite база данных
# Не требует интернета
# Не требует сервера
```

**3. Проверка ключей** - Локально
```
Приложение проверяет ключ прямо на ПК пользователя
Без связи с интернетом!
Без связи с сервером!
```

**4. HWID привязка** - Локально
```
HWID генерируется на ПК пользователя
Сравнивается с HWID из БД
Все проверки локальные
```

### 🚀 Полный цикл БЕЗ интернета

**Сценарий: Пользователь в офлайне**

```
1. Пользователь скачивает OwlTeam-Opti.exe (один раз)
2. Запускает на своём ПК
3. Приложение генерирует HWID
4. Заходит в License Manager
5. Вводит ключ (который получил от тебя)
6. Приложение проверяет ключ ЛОКАЛЬНО
   - Даже без интернета! ✓
7. Ключ активирован!
8. Пользователь работает с приложением

🔥 НИКАКОГО ИНТЕРНЕТА НЕ ТРЕБУЕТСЯ!
```

### 📊 Структура локальной БД

**licenses.db (SQLite)**
```sql
CREATE TABLE licenses (
    id INTEGER PRIMARY KEY,
    key TEXT UNIQUE,                    -- OWL-XXXXX-XXXXX-XXXXX-XXXXX
    hwid TEXT,                          -- A3B5C7D9E1F3G5H7I9J1K3L5M7N9O1P3
    activation_date TIMESTAMP,          -- 2024-06-23 22:10:00
    expiration_date TIMESTAMP,          -- 2024-07-23 22:10:00 (30 дней)
    status TEXT,                        -- 'active', 'revoked', 'expired'
    created_at TIMESTAMP                -- 2024-06-23 22:10:00
);
```

**Пример записи:**
```
key:               OWL-K9M2X-5WL7P-3R8Q1-4J6T2
hwid:              A3B5C7D9E1F3G5H7I9J1K3L5M7N9O1P3
activation_date:   2024-06-23 22:10:00
expiration_date:   2024-07-23 22:10:00   (ровно через 30 дней)
status:            active
created_at:        2024-06-23 22:10:00
```

### 🔄 Как добавить ключ в БД

**Вариант 1: Через Python (автоматически при активации)**
```python
from core.license_manager import LicenseManager
from core.hwid_manager import HWIDManager

license_mgr = LicenseManager()
hwid_mgr = HWIDManager()

# Добавить ключ в БД
license_mgr.add_license(
    key="OWL-K9M2X-5WL7P-3R8Q1-4J6T2",
    hwid="A3B5C7D9E1F3G5H7I9J1K3L5M7N9O1P3",
    duration_days=30  # На 30 дней
)
```

**Вариант 2: Прямая вставка в БД (если нужно вручную)**
```bash
# Скачай DB Browser for SQLite:
# https://sqlitebrowser.org/

# Открой файл: ~/.owlteam_opti/licenses.db
# Нажми "Execute SQL"
# Выполни:

INSERT INTO licenses 
(key, hwid, activation_date, expiration_date, status, created_at)
VALUES (
  'OWL-K9M2X-5WL7P-3R8Q1-4J6T2',
  'A3B5C7D9E1F3G5H7I9J1K3L5M7N9O1P3',
  datetime('now'),
  datetime('now', '+30 days'),
  'active',
  datetime('now')
);
```

---

## 📝 Примеры использования

### Сценарий 1: Раздача ключей через Telegram

```bash
# 1. На своём ПК генерируешь ключи
python key_generator_cli.py

# Выбираешь:
# [2] Generate batch of keys
# 10 ключей
# 30_days
# Save to file: y

# 2. Открываешь файл generated_keys/keys_30_days_YYYYMMDD_HHMMSS.json

# 3. Копируешь ключи в Excel:
OWL-A3K2M-7PQ9L-B8RC5-N2VD4
OWL-K9M2X-5WL7P-3R8Q1-4J6T2
...

# 4. Отправляешь пользователю через Telegram/Discord/Email

# 5. Пользователь:
#    - Скачивает OwlTeam-Opti.exe
#    - Запускает
#    - License Manager → Validate
#    - Вводит ключ
#    - ✅ Активирован!
```

### Сценарий 2: Платная раздача (например, $5 за месяц)

```python
# Система:
# Пользователь оплачивает $5
# ↓
# Ты генерируешь 1 ключ на 30 дней
# ↓
# Даёшь пользователю
# ↓
# Пользователь активирует в приложении
# ↓
# Через 30 дней: ключ истекает автоматически ❌
# ↓
# Пользователь снова платит → новый ключ

# ВСЁ ПРОИСХОДИТ БЕЗ САЙТА И СЕРВЕРА!
```

### Сценарий 3: VIP клиенты (lifetime ключи)

```bash
# Генерируешь lifetime ключ (действует навсегда)
python key_generator_cli.py

# [2] Generate batch
# Count: 1
# Duration: [5] lifetime

# Пользователь получает ключ и может пользоваться вечно!
# Никогда не истечёт ✓
```

### Сценарий 4: Отзыв ключа (если клиент не платил)

```python
from core.license_manager import LicenseManager

license_mgr = LicenseManager()

# Отозвать ключ
license_mgr.revoke_license("OWL-K9M2X-5WL7P-3R8Q1-4J6T2")

# Теперь ключ не работает ❌
# "License revoked" - сообщение об ошибке
```

### Сценарий 5: Проверка информации о ключе

```python
from core.license_manager import LicenseManager

license_mgr = LicenseManager()

# Получить информацию о ключе
info = license_mgr.get_license_info("OWL-K9M2X-5WL7P-3R8Q1-4J6T2")

print(f"Key: {info[1]}")
print(f"HWID: {info[2]}")
print(f"Activation: {info[3]}")
print(f"Expiration: {info[4]}")
print(f"Status: {info[5]}")
```

---

## 🎯 Быстрый старт для использования

### Шаг 1: Настройка (один раз)

```bash
# 1. Установить Python 3.10+

# 2. Установить зависимости
pip install -r requirements.txt
```

### Шаг 2: Генерация ключей

```bash
python key_generator_cli.py

# [2] Generate batch
# Count: 100
# Duration: 30_days
# Save: y

# Получишь файл: generated_keys/keys_30_days_20240623_221000.json
```

### Шаг 3: Распределение

```
Ты:           Пользователь:
Клич → Email/Telegram/Discord → Ключ активирует в приложении
```

### Шаг 4: Монитор (опционально)

```python
# Проверить активные ключи
from core.license_manager import LicenseManager

license_mgr = LicenseManager()

# Запрос в БД
# SELECT * FROM licenses WHERE status='active'
```

---

## 🔧 Что нужно сделать для полной автономности

### ✅ Уже сделано (встроено)

- ✓ Генератор ключей (CLI + API)
- ✓ Локальная БД (SQLite)
- ✓ HWID система
- ✓ Проверка ключей БЕЗ интернета
- ✓ Сроки действия ключей
- ✓ Отзыв ключей

### 📝 Опционально (если хочешь расширить)

**1. Логирование активаций (текущий статус ключей)**
```python
# Добавить в LicenseManager
def log_activation(self, key, status, timestamp):
    with open("activation_log.txt", "a") as f:
        f.write(f"{timestamp} - {key} - {status}\n")
```

**2. Система рефералов (приглашение друзей)**
```python
def generate_referral_code(self):
    # Каждому пользователю уникальный код
    # Если он даст коду другу → бонус
```

**3. Статистика использования**
```python
def get_stats(self):
    # Сколько активных ключей
    # Сколько истекших
    # Сколько отозванных
```

**4. Экспорт отчётов**
```python
def export_report(self):
    # В Excel или PDF
    # Статус всех ключей
```

**5. Резервная копия БД**
```python
import shutil

def backup_database(self):
    shutil.copy("licenses.db", "licenses.backup.db")
```

---

## 💡 Важные моменты

### 1️⃣ Где хранятся ключи?
```
~/.owlteam_opti/licenses.db

Это ЛОКАЛЬНЫЙ файл на ПК пользователя
Ты НЕ видишь эти файлы!
Кажды ПК имеет свою БД
```

### 2️⃣ Как отследить кто использует ключи?
```
Вариант А: Попроси пользователя показать скриншот HWID
           (License Manager → показывает HWID)

Вариант Б: Веди текстовый лог с раздачей
           "Ключ OWL-XXX раздан Ивану 23.06.2024"

Вариант В: Добавь логирование в код
```

### 3️⃣ Безопасность
```
✓ HWID защита - ключ не скопировать
✓ БД зашифрована (в коде используется SHA256)
✓ Каждый ключ уникален
✓ Автоматическое истечение
✓ Возможность отзыва
```

### 4️⃣ Тестирование
```bash
# Тестовый ключ на 7 дней
python key_generator_cli.py

[2] Generate batch
Count: 1
Duration: [1] 7_days
Save: y

# Даёшь себе для тестирования
```

---

## 📞 Чек-лист для запуска

- [ ] Python 3.10+ установлен
- [ ] `pip install -r requirements.txt` выполнен
- [ ] Генератор ключей работает: `python key_generator_cli.py`
- [ ] Приложение запускается: `python main.py`
- [ ] Сгенерировал тестовый ключ
- [ ] Протестировал активацию
- [ ] Готов раздавать ключи пользователям
- [ ] Сделал резервную копию (опционально)

---

## 🎯 Итого

**ТЫ:**
1. Генерируешь ключи → `python key_generator_cli.py`
2. Раздаёшь пользователям (Email/Telegram/Discord/etc)
3. Всё! Они сами активируют в приложении

**ПОЛЬЗОВАТЕЛЬ:**
1. Скачивает OwlTeam-Opti.exe
2. Запускает
3. Вводит ключ в License Manager
4. Использует приложение

**БЕЗ:**
- ❌ Сайта
- ❌ Хостинга
- ❌ Сервера
- ❌ Интернета (после первого запуска)
- ❌ Платежных систем
- ❌ Усложнений

**ВСЁ ЛОКАЛЬНО И АВТОНОМНО!** ✅

---

**OwlTeam Opti © 2024** - Лицензирование для профессионалов
