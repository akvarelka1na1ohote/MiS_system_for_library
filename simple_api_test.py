import json
import urllib.request
import sys

BASE_URL = "http://localhost:8000"

def get_json(url):
    """Получить JSON данные по URL"""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as e:
        print(f"❌ Ошибка при запросе {url}: {e}")
        return None

def print_section(title, data, max_items=3):
    """Вывести секцию с данными"""
    print(f"\n{title}")
    print("=" * 60)
    
    if isinstance(data, list):
        print(f"Всего записей: {len(data)}")
        for i, item in enumerate(data[:max_items], 1):
            print(f"\n📌 Пример записи #{i}:")
            # Выводим только ключевые поля для наглядности
            if 'last_name' in item:  # Для читателей
                print(f"   Читатель: {item.get('last_name')} {item.get('first_name')}")
                print(f"   Email: {item.get('email')}, Телефон: {item.get('phone')}")
            elif 'main_title' in item:  # Для книг
                print(f"   Книга: {item.get('main_title')}")
                print(f"   ISBN: {item.get('isbn')}, Год: {item.get('publication_year')}")
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))

def main():
    print("🧪 ТЕСТИРОВАНИЕ API БИБЛИОТЕЧНОЙ СИСТЕМЫ")
    print("=" * 60)
    
    # Проверка доступности API
    try:
        with urllib.request.urlopen(f"{BASE_URL}/health", timeout=5):
            print("✅ API доступен (health check passed)")
    except:
        print("❌ API не доступен!")
        print("Запустите: python -m uvicorn main:app --reload")
        return
    
    # 1. Корневой endpoint
    root = get_json(f"{BASE_URL}/")
    if root:
        print(f"\n🏠 Корневой endpoint:")
        print(f"   Версия: {root.get('version')}")
        print(f"   Таблиц: {root.get('tables_count')}")
        print(f"   Описание: {root.get('description')}")
    
    # 2. Читатели
    readers = get_json(f"{BASE_URL}/readers")
    if readers:
        print_section("👥 ЧИТАТЕЛИ", readers)
    
    # 3. Книги
    books = get_json(f"{BASE_URL}/books")
    if books:
        print_section("📚 КНИГИ (библиографические записи)", books)
    
    # 4. Авторы
    authors = get_json(f"{BASE_URL}/authors")
    if authors:
        print_section("✍️ АВТОРЫ", authors)
    
    # 5. Выдачи
    loans = get_json(f"{BASE_URL}/loans")
    if loans:
        print_section("📅 ВЫДАЧИ КНИГ", loans)
    
    # 6. Поиск книг
    search_result = get_json(f"{BASE_URL}/search/books?title=Граф")
    if search_result:
        print_section("🔍 ПОИСК КНИГ (по названию 'Граф')", search_result.get('books', []))
    
    # 7. Статистика библиотеки
    stats = get_json(f"{BASE_URL}/statistics/library")
    if stats:
        print("\n📊 СТАТИСТИКА БИБЛИОТЕКИ")
        print("=" * 60)
        stats_data = stats.get('library', {})
        print(f"   Библиотека: {stats_data.get('name')}")
        print(f"   Последнее обновление: {stats_data.get('last_updated')[:16]}")
        
        readers = stats.get('readers', {})
        print(f"\n   👥 Читатели: {readers.get('total')} всего, {readers.get('active')} активных")
        
        books = stats.get('books', {})
        print(f"   📚 Книги: {books.get('bibliographic_records')} записей, {books.get('physical_copies')} экземпляров")
        
        loans = stats.get('loans', {})
        print(f"   📅 Выдачи: {loans.get('total')} всего, {loans.get('active')} активных, {loans.get('overdue')} просроченных")
    
    # 8. Проверка основных endpoints
    print("\n🔧 ПРОВЕРКА ОСНОВНЫХ ENDPOINTS")
    print("=" * 60)
    
    endpoints_to_check = [
        ("/edition-types", "Типы изданий"),
        ("/reader-categories", "Категории читателей"),
        ("/book-statuses", "Статусы книг"),
        ("/book-copies", "Экземпляры книг"),
        ("/payments", "Платежи"),
        ("/visits", "Посещения"),
        ("/api/summary", "Сводка API")
    ]
    
    for endpoint, description in endpoints_to_check:
        data = get_json(f"{BASE_URL}{endpoint}")
        if data:
            if isinstance(data, list):
                print(f"✅ {description}: {len(data)} записей")
            else:
                print(f"✅ {description}: работает")
        else:
            print(f"❌ {description}: недоступен")
    
    print("\n🎉 Тестирование завершено!")
    print(f"📚 Документация: {BASE_URL}/docs")

if __name__ == "__main__":
    main()