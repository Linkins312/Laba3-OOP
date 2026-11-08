# Лабораторная 3 ООП - про машинки(вариант 4)

### Описание
Класс моделирует автомобиль с инкапсуляцией данных и вычислением расхода топлива.

### Атрибуты
- `brand` (public) — марка
- `model` (public) — модель
- `year` (public) — год выпуска
- `color` (public) — цвет
- `__speed` (private) — скорость
- `__fuel` (private) — уровень топлива

### Инварианты
- `speed >= 0`
- `fuel` от 0 до 100

### Формулы
- Расход топлива: 8 л на 100 км
- Макс. дистанция = (топливо / 8) * 100

### Запуск
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python car.py