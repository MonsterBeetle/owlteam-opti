# 🦇 OwlTeam Opti - Professional PC Optimizer

**OwlTeam Opti** — премиальный оптимизатор для ПК с интегрированной системой лицензирования, AI BIOS ассистентом и расширенным функционалом для геймеров.

## 🎯 Основные функции

### 🎮 Геймерские возможности
- **Game Presets**: Готовые профили для Apex Legends, CS2, PUBG, Rust, GTA V
- **BOOST Mode**: Кастомный режим питания для максимального FPS
- **Performance Tweaks**: Оптимизация реестра и параметров системы
- **Network Optimizer**: Снижение пинга и оптимизация интернета

### 🤖 AI BIOS Assistant
- Интеллектуальный ассистент для оптимизации параметров BIOS
- Анализ характеристик вашего ПК
- Рекомендации по настройкам

### 🧹 Очистка системы
- Удаление временных файлов
- Очистка реестра
- Управление автозагрузкой
- Удаление дублей и мусора

### 🔐 Система лицензирования
- Генератор ключей активации
- HWID привязка (защита от передачи ключей)
- Управление подписками
- Статусы ключей (активный, истекший, отключённый)

### 📊 Dashboard
- Системная информация в реальном времени
- Графики использования CPU, RAM, GPU
- Температуры компонентов
- Скорость интернета

## 🚀 Быстрый старт

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
python main.py
```

## 📁 Структура проекта

```
owlteam-opti/
├── main.py                 # Точка входа
├── requirements.txt        # Зависимости
├── config/
│   ├── settings.py
│   ├── constants.py
│   └── license_config.py
├── ui/
│   ├── main_window.py
│   ├── dashboard.py
│   ├── pages/
│   │   ├── games.py
│   │   ├── cleanup.py
│   │   ├── tweaks.py
│   │   ├── bios_assistant.py
│   │   ├── license_manager.py
│   │   └── settings.py
│   ├── widgets/
│   │   ├── charts.py
│   │   ├── buttons.py
│   │   └── animations.py
│   └── styles/
│       └── style.qss
├── core/
│   ├── optimizer.py
│   ├── system_monitor.py
│   ├── game_profiles.py
│   ├── license_manager.py
│   ├── hwid_manager.py
│   └── ai_assistant.py
├── tools/
│   ├── key_generator.py
│   ├── registry_tweaks.py
│   └── network_optimizer.py
├── data/
│   ├── game_presets.json
│   ├── bios_profiles.json
│   └── licenses.db
└── assets/
    ├── logo.png
    └── icons/
```

## 💡 Технический стек

- **GUI**: PyQt6
- **Система мониторинга**: psutil, wmi, gputil
- **AI**: OpenAI/Gemini API
- **База данных**: SQLite
- **Лицензирование**: HWID + ключи активации

## 📝 Лицензия

OwlTeam © 2024 - All Rights Reserved

---

**Разработано с ❤️ для геймеров и оверклокеров**
