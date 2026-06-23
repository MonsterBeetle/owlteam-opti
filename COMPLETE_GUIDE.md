# 🦇 OwlTeam Opti - Полное руководство

## 📋 Содержание

1. [Генератор ключей](#генератор-ключей)
2. [Запуск оптимизатора](#запуск-оптимизатора)
3. [Требования Python](#требования-python)
4. [FAQ](#faq)

---

## 🔑 Генератор ключей

### Что это?

Генератор ключей - это утилита для создания лицензионных ключей доступа к OwlTeam Opti. Каждый ключ:
- **Уникален** - случайно сгенерирован
- **Привязан к HWID** - нельзя передать другому пользователю
- **Имеет срок действия** - от 7 дней до пожизненно
- **Защищён от копирования** - HWID проверяется при активации

### Формат ключа

```
OWL-XXXXX-XXXXX-XXXXX-XXXXX
```

**Пример:**
```
OWL-K9M2X-5WL7P-3R8Q1-4J6T2
```

**Компоненты:**
- `OWL` - префикс (OwlTeam Opti)
- 4 группы по 5 символов - случайные буквы (A-Z) и цифры (0-9)
- Всего 29 символов включая дефисы

### Как использовать генератор

#### Способ 1: CLI (Командная строка) - САМЫЙ ПРОСТОЙ

```bash
python key_generator_cli.py
```

**Откроется меню:**
```
============================================================
           🔑 OwlTeam Opti - License Key Generator
============================================================

[1] Generate single key
[2] Generate batch of keys
[3] Export keys to file
[4] View key formats
[5] Exit
```

**Пример генерации одного ключа на 30 дней:**
```
Choice: 1

Select duration:
[1] 7_days
[2] 30_days
[3] 90_days
[4] 365_days
[5] lifetime

Choice: 2

✅ Key Generated Successfully!

Key: OWL-A3K2M-7PQ9L-B8RC5-N2VD4
Duration: 30_days
Days: 30
Generated: 2024-06-23 22:10:00
```

**Пример генерации пакета из 100 ключей:**
```
Choice: 2

Number of keys to generate: 100

Select duration:
[1] 7_days
[2] 30_days
...

Choice: 2

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

#### Способ 2: Python API

Для интеграции в свой код:

```python
from tools.key_generator import KeyGenerator

# Инициализация
gen = KeyGenerator()

# Генерация одного ключа
key = gen.generate_key()
print(key)  # OWL-A3K2M-7PQ9L-B8RC5-N2VD4

# Генерация пакета из 50 ключей на 30 дней
keys = gen.generate_batch(count=50, duration="30_days")

for key_info in keys:
    print(f"{key_info['key']} - {key_info['duration']}")

# Проверка формата ключа
if gen.validate_key_format("OWL-A3K2M-7PQ9L-B8RC5-N2VD4"):
    print("✓ Ключ валидный")
else:
    print("✗ Ключ невалидный")
```

### Доступные сроки действия

```python
"7_days"      # 7 дней (неделя)
"30_days"     # 30 дней (месяц)
"90_days"     # 90 дней (3 месяца)
"365_days"    # 365 дней (год)
"lifetime"    # На всегда (99999 дней)
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
    {
      "key": "OWL-K9M2X-5WL7P-3R8Q1-4J6T2",
      "duration": "30_days",
      "created_at": "2024-06-23T22:10:00.123456"
    }
  ]
}
```

### Как это работает (Привязка к HWID)

**Процесс активации:**

```
1. Пользователь запускает OwlTeam Opti
   ↓
2. Система автоматически генерирует HWID ПК
   (на основе: CPU ID + Motherboard Serial + Disk Serial)
   ↓
3. Пользователь переходит в License Manager
   ↓
4. Вводит ключ (OWL-XXXXX-XXXXX-XXXXX-XXXXX)
   ↓
5. Приложение проверяет:
   ✓ Ключ существует в БД?
   ✓ HWID совпадает с сохранённым?
   ✓ Ключ не истёк?
   ✓ Ключ не отозван?
   ↓
6. Если ДА → Активация успешна ✅
   Если НЕТ → Ошибка активации ❌
```

**Защита от передачи:**
- Ключ привязан к конкретному HWID
- Если друг попытается использовать ключ на своём ПК - ошибка
- Нужен отдельный ключ для каждого ПК

---

## ▶️ Запуск оптимизатора

### Требования Python

**Минимум:** Python 3.8  
**Рекомендуется:** Python 3.10 или выше

**Проверить версию:**
```bash
python --version
```

**Если Python не установлен:**
1. Перейти на https://www.python.org/downloads/
2. Скачать Python 3.11 или выше
3. **ВАЖНО:** При установке отметить ✅ "Add Python to PATH"
4. Перезагрузить ПК

### Запуск через Python

**Шаг 1: Установить зависимости**

```bash
pip install -r requirements.txt
```

Это установит все необходимые библиотеки:
- PyQt6 - графический интерфейс
- psutil - мониторинг системы
- wmi - информация о железе
- И другие...

**Шаг 2: Запустить приложение**

```bash
python main.py
```

**Или через batch файл (Windows):**

```bash
run.bat
```

### Сборка в EXE (Standalone)

**Вариант 1: Автоматическая сборка**

```bash
build.bat
```

Этот файл автоматически:
1. Установит зависимости
2. Соберёт приложение
3. Создаст `dist/OwlTeam-Opti.exe`

**Вариант 2: Ручная сборка**

```bash
# Установить PyInstaller
pip install pyinstaller

# Собрать приложение
python build.py

# Запустить
dist/OwlTeam-Opti.exe
```

### Структура после сборки

```
папка_проекта/
├── dist/
│   └── OwlTeam-Opti.exe    ← Готовое приложение
├── build/
│   └── [временные файлы]
└── [исходный код]
```

**EXE файл можно передавать пользователям** - это полностью автономное приложение.

### Установка на систему (опционально)

```bash
# Создать ярлык на рабочий стол
create_shortcut.bat

# Или вручную:
# Правый клик на EXE → "Отправить" → "Рабочий стол (создать ярлык)"
```

---

## 🐍 Требования Python

### Минимальные требования

```
ОС: Windows 10, Windows 11
Python: 3.8+
RAM: 2GB (рекомендуется 4GB+)
Диск: 500MB свободного места
Internet: Для установки зависимостей
```

### Установленные компоненты

После `pip install -r requirements.txt` будут установлены:

```
✓ PyQt6              - Графический интерфейс
✓ psutil             - Мониторинг ПК (CPU, RAM, диск, сеть)
✓ wmi                - Информация о железе Windows
✓ gputil             - Информация о видеокарте
✓ requests           - HTTP запросы
✓ Pillow             - Работа с изображениями
✓ numpy              - Вычисления
✓ matplotlib         - Графики
✓ cryptography       - Шифрование
✓ opencv-python     - Компьютерное зрение
✓ pyinstaller        - Сборка в EXE
```

### Проверка установки

```bash
# Проверить Python
python --version

# Проверить pip
pip --version

# Проверить PyQt6
python -c "from PyQt6.QtWidgets import QApplication; print('✓ PyQt6 OK')"

# Проверить psutil
python -c "import psutil; print(f'✓ psutil {psutil.__version__} OK')"

# Проверить все зависимости
pip list | findstr PyQt6
pip list | findstr psutil
pip list | findstr wmi
```

### Решение проблем

**Ошибка: "ModuleNotFoundError: No module named 'PyQt6'"**
```bash
pip install PyQt6 --upgrade
```

**Ошибка: "wmi not found"**
```bash
pip install wmi pypiwin32
```

**Ошибка: "Python not found" или "python is not recognized"**
- Переустановить Python с опцией "Add Python to PATH"
- Или использовать полный путь: `C:\Python311\python.exe main.py`

**Приложение запускается медленно**
- Закрыть ненужные программы
- Обновить видеодрайверы
- Увеличить RAM

---

## ❓ FAQ

### Q: Какой Python нужен?
**A:** Python 3.10 или 3.11. Скачать с https://www.python.org/downloads/

### Q: Сколько место занимает приложение?
**A:** ~500MB с зависимостями. EXE файл после сборки ~300-400MB.

### Q: Можно ли запустить без Python?
**A:** Да! Используй скомпилированный `OwlTeam-Opti.exe` из папки `dist/`

### Q: Как распространять ключи пользователям?
**A:** 
1. Запусти `python key_generator_cli.py`
2. Выбери "Generate batch of keys"
3. Сохрани в JSON файл
4. Отправь ключи пользователям

### Q: Что такое HWID?
**A:** Hardware ID - уникальный ID ПК. Состоит из CPU ID + Motherboard Serial + Disk Serial. Каждый ПК имеет уникальный HWID.

### Q: Можно ли использовать один ключ на нескольких ПК?
**A:** Нет. Ключ привязан к HWID конкретного ПК. Для каждого ПК нужен отдельный ключ.

### Q: Ключ истёк - что делать?
**A:** 
1. Сгенерируй новый ключ
2. Дай его пользователю
3. Он введёт ключ в License Manager

### Q: Как отозвать ключ?
**A:** Ключ можно отозвать через базу данных `licenses.db` или добавить функцию отзыва в админ-панель.

### Q: Где хранятся ключи в приложении?
**A:** В файле `~/.owlteam_opti/licenses.db` (SQLite база данных)

### Q: Приложение требует админ-права?
**A:** Да, для изменения параметров системы (BOOST режим, tweaks, очистка). Запусти с правами администратора.

### Q: Какие игры поддерживаются?
**A:** Apex Legends, CS2, PUBG, Rust, GTA V (остальные можно добавить)

### Q: BOOST режим безопасен?
**A:** Да, но может увеличить температуру. Убедись в хорошем охлаждении ПК.

### Q: Можно ли использовать на ноутбуке?
**A:** Да, но следи за температурой и расходом батареи.

---

## 📦 Что входит в проект

```
owlteam-opti/
├── main.py                     # Точка входа приложения
├── key_generator_cli.py        # Генератор ключей (CLI)
├── build.py                    # Скрипт сборки в EXE
├── run.bat                     # Запуск приложения
├── build.bat                   # Сборка в EXE
├── requirements.txt            # Зависимости Python
├── README.md                   # Описание проекта
├── INSTALL.md                  # Инструкция установки
├── KEY_GENERATOR_GUIDE.md      # Это руководство
│
├── config/
│   ├── constants.py            # Константы и настройки
│   ├── settings.py             # Пользовательские настройки
│   └── license_config.py       # Конфиг лицензирования
│
├── core/
│   ├── hwid_manager.py         # Управление HWID
│   ├── license_manager.py      # Управление лицензиями
│   ├── optimizer.py            # Основной оптимизатор
│   ├── system_monitor.py       # Мониторинг системы
│   └── ai_assistant.py         # AI помощник для BIOS
│
├── tools/
│   ├── key_generator.py        # Генератор ключей (API)
│   └── network_optimizer.py    # Оптимизация сети
│
├── ui/
│   ├── main_window.py          # Главное окно
│   └── pages/
│       ├── dashboard.py        # Панель управления
│       ├── games.py            # Преsets для игр
│       ├── cleanup.py          # Очистка системы
│       ├── tweaks.py           # Твики производительности
│       ├── license_manager.py  # Менеджер лицензий
│       ├── bios_assistant.py   # AI BIOS помощник
│       ├── boost_mode.py       # BOOST режим
│       └── settings.py         # Настройки
│
├── generated_keys/             # Папка с сгенерированными ключами
│   └── keys_*.json             # JSON файлы с ключами
│
└── dist/
    └── OwlTeam-Opti.exe        # Скомпилированное приложение
```

---

## 🚀 Быстрый старт

### За 5 минут от нуля до работающего приложения

**Шаг 1:** Установить Python 3.10+
```bash
https://www.python.org/downloads/
```

**Шаг 2:** Клонировать репозиторий
```bash
git clone https://github.com/MonsterBeetle/owlteam-opti.git
cd owlteam-opti
```

**Шаг 3:** Установить зависимости
```bash
pip install -r requirements.txt
```

**Шаг 4:** Запустить приложение
```bash
python main.py
```

**Шаг 5:** Сгенерировать ключи
```bash
python key_generator_cli.py
```

**Шаг 6 (опционально):** Собрать EXE
```bash
build.bat
```

---

## 📧 Поддержка

Если возникли проблемы:
1. Проверь [GitHub Issues](https://github.com/MonsterBeetle/owlteam-opti/issues)
2. Прочитай это руководство
3. Создай новую issue с описанием проблемы

---

**OwlTeam Opti © 2024** - Сделано с ❤️ для геймеров
