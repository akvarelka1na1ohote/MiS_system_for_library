from sqlmodel import create_engine, text
from urllib.parse import quote_plus

password = "mis2025!"
encoded_password = quote_plus(password)
DATABASE_URL = f"postgresql://student:{encoded_password}@176.108.247.125:5432/mis2025"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        # Простой тест подключения
        result = conn.execute(text("SELECT 1 as test"))
        print("✅ Подключение к БД работает!")
        
        # Проверяем таблицы в схеме Ichetovkina
        tables = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'Ichetovkina'
            ORDER BY table_name
        """)).fetchall()
        
        print(f"\n📊 Таблицы в схеме Ichetovkina ({len(tables)} шт):")
        
        # Ожидаемые таблицы (20 штук)
        expected_tables = [
            'authors', 'book_authors', 'book_copies', 'book_statuses',
            'books', 'cities', 'countries', 'daily_statistics',
            'edition_types', 'languages', 'loan_statuses', 'loans',
            'operation_types', 'payments', 'publishers', 'reader_categories',
            'readers', 'reference_requests', 'reservations', 'visits'
        ]
        
        for expected in expected_tables:
            found = any(expected == table[0] for table in tables)
            status = "✅" if found else "❌"
            print(f"  {status} {expected}")
        
        print(f"\n📈 Статистика по таблицам:")
        for table in tables:
            try:
                count = conn.execute(
                    text(f'SELECT COUNT(*) FROM "Ichetovkina"."{table[0]}"')
                ).scalar()
                print(f"  - {table[0]}: {count} записей")
            except Exception as e:
                print(f"  - {table[0]}: ошибка ({e})")
        
        # Проверяем, все ли ожидаемые таблицы созданы
        missing = [t for t in expected_tables if t not in [table[0] for table in tables]]
        if missing:
            print(f"\n⚠️  Отсутствуют таблицы: {missing}")
            print("   Запустите: python create_tables.py")
        else:
            print(f"\n🎉 Все 20 таблиц созданы успешно!")
            
except Exception as e:
    print(f"❌ Ошибка: {e}")