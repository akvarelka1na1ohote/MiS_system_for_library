from sqlmodel import create_engine, text
from urllib.parse import quote_plus

# Данные подключения
password = "mis2025!"
encoded_password = quote_plus(password)
DATABASE_URL = f"postgresql://student:{encoded_password}@176.108.247.125:5432/mis2025"

print("🗑️ Удаляем старые таблицы в схеме Ichetovkina...")

# Создаем движок (ВНИМАНИЕ: правильное название DATABASE_URL!)
engine = create_engine(DATABASE_URL)

# Список таблиц для удаления
tables = [
    "daily_statistics", "reference_requests", "visits", "reservations",
    "payments", "loans", "book_copies", "book_authors", "authors", "books",
    "readers", "operation_types", "loan_statuses", "book_statuses",
    "reader_categories", "publishers", "cities", "countries", "languages",
    "edition_types"
]

with engine.connect() as conn:
    for table in tables:
        try:
            conn.execute(text(f'DROP TABLE IF EXISTS "Ichetovkina"."{table}" CASCADE;'))
            print(f"✅ Таблица {table} удалена")
        except Exception as e:
            print(f"⚠️ {table}: {e}")
    
    conn.commit()

print("🎉 Все старые таблицы удалены!")
print("📝 Теперь можно создавать новые таблицы:")
print("   python create_tables.py")