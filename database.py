from sqlmodel import create_engine, SQLModel, Session
from urllib.parse import quote_plus

# Данные подключения
password = "mis2025!"
encoded_password = quote_plus(password)
DATABASE_URL = f"postgresql://student:{encoded_password}@176.108.247.125:5432/mis2025"

print("🔗 Подключаемся к PostgreSQL...")
print(f"📊 База: mis2025, Схема: Ichetovkina")
print(f"👤 Пользователь: student")

# Создаем движок
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    """Создаем таблицы в базе данных"""
    print("🗃️ Создаем таблицы в схеме Ichetovkina...")
    SQLModel.metadata.create_all(engine)
    print("✅ Таблицы успешно созданы!")

def get_session():
    """Создаем сессию для работы с БД"""
    with Session(engine) as session:
        yield session