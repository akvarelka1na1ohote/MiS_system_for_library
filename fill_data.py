from sqlmodel import Session, select
from database import engine
from models import *
from datetime import date, datetime, timedelta
import random

def fill_test_data():
    """Заполнение базы тестовыми данными"""
    
    with Session(engine) as session:
        print("🗃️ Начинаем заполнение базы данных (ГОСТ версия)...")
        print("=" * 60)
        
        # ==================== 2. СПРАВОЧНИКИ ====================
        print("📋 Заполняем справочники...")
        
        # 2.1. Типы изданий (ГОСТ 7.60-2003)
        print("  📚 Типы изданий...")
        edition_types = [
            EditionType(code="01", name="Книга", gost_reference="ГОСТ 7.60-2003", description="Однотомное или многотомное издание"),
            EditionType(code="02", name="Журнал", gost_reference="ГОСТ 7.60-2003", description="Периодическое издание"),
            EditionType(code="03", name="Газета", gost_reference="ГОСТ 7.60-2003", description="Ежедневное или еженедельное издание"),
            EditionType(code="04", name="Ноты", gost_reference="ГОСТ 7.60-2003", description="Нотное издание"),
            EditionType(code="05", name="Карта", gost_reference="ГОСТ 7.60-2003", description="Картографическое издание"),
            EditionType(code="06", name="Электронный ресурс", gost_reference="ГОСТ 7.82-2001", description="Электронное издание"),
        ]
        
        for et in edition_types:
            session.add(et)
        session.commit()
        print(f"    ✅ Создано {len(edition_types)} типов изданий")
        
        # 2.2. Языки
        print("  🌐 Языки...")
        languages = [
            Language(iso_code="ru", name="Русский"),
            Language(iso_code="en", name="Английский"),
            Language(iso_code="de", name="Немецкий"),
            Language(iso_code="fr", name="Французский"),
            Language(iso_code="es", name="Испанский"),
        ]
        
        for lang in languages:
            session.add(lang)
        session.commit()
        print(f"    ✅ Создано {len(languages)} языков")
        
        # 2.3. Страны
        print("  🗺️ Страны...")
        countries = [
            Country(iso_code="RU", name="Россия"),
            Country(iso_code="US", name="США"),
            Country(iso_code="DE", name="Германия"),
            Country(iso_code="FR", name="Франция"),
            Country(iso_code="GB", name="Великобритания"),
        ]
        
        for country in countries:
            session.add(country)
        session.commit()
        print(f"    ✅ Создано {len(countries)} стран")
        
        # 2.4. Города
        print("  🏙️ Города...")
        cities = [
            City(name="Москва", country_id=countries[0].id),
            City(name="Санкт-Петербург", country_id=countries[0].id),
            City(name="Новосибирск", country_id=countries[0].id),
            City(name="Нью-Йорк", country_id=countries[1].id),
            City(name="Берлин", country_id=countries[2].id),
            City(name="Париж", country_id=countries[3].id),
            City(name="Лондон", country_id=countries[4].id),
        ]
        
        for city in cities:
            session.add(city)
        session.commit()
        print(f"    ✅ Создано {len(cities)} городов")
        
        # 2.5. Издательства
        print("  🏢 Издательства...")
        publishers = [
            Publisher(name="Издательство «Просвещение»", city_id=cities[0].id, address="ул. Тверская, 12", website="https://prosv.ru"),
            Publisher(name="АСТ", city_id=cities[0].id, address="ул. Правды, 24", website="https://ast.ru"),
            Publisher(name="Эксмо", city_id=cities[0].id, address="ул. Зорге, 1", website="https://eksmo.ru"),
            Publisher(name="Penguin Random House", city_id=cities[3].id, address="1745 Broadway, New York", website="https://penguinrandomhouse.com"),
            Publisher(name="Gallimard", city_id=cities[5].id, address="5 rue Sébastien Bottin, Paris", website="https://gallimard.fr"),
        ]
        
        for pub in publishers:
            session.add(pub)
        session.commit()
        print(f"    ✅ Создано {len(publishers)} издательств")
        
        # 2.6. Категории читателей (ГОСТ Р 7.0.20-2014)
        print("  👥 Категории читателей...")
        reader_categories = [
            ReaderCategory(code="ADULT", name="Взрослый", loan_limit=10, loan_period=30, has_remote_access=True),
            ReaderCategory(code="CHILD", name="Ребенок", loan_limit=5, loan_period=14, has_remote_access=False),
            ReaderCategory(code="STUDENT", name="Студент", loan_limit=8, loan_period=60, has_remote_access=True),
            ReaderCategory(code="PENSIONER", name="Пенсионер", loan_limit=5, loan_period=30, has_remote_access=False),
            ReaderCategory(code="RESEARCHER", name="Исследователь", loan_limit=15, loan_period=90, has_remote_access=True),
        ]
        
        for rc in reader_categories:
            session.add(rc)
        session.commit()
        print(f"    ✅ Создано {len(reader_categories)} категорий читателей")
        
        # 2.7. Статусы книг
        print("  🏷️ Статусы книг...")
        book_statuses = [
            BookStatus(code="AVAILABLE", name="Доступна"),
            BookStatus(code="LOANED", name="Выдана"),
            BookStatus(code="RESERVED", name="Зарезервирована"),
            BookStatus(code="LOST", name="Утеряна"),
            BookStatus(code="DAMAGED", name="Повреждена"),
            BookStatus(code="WRITTEN_OFF", name="Списана"),
        ]
        
        for bs in book_statuses:
            session.add(bs)
        session.commit()
        print(f"    ✅ Создано {len(book_statuses)} статусов книг")
        
        # 2.8. Статусы выдач
        print("  📅 Статусы выдач...")
        loan_statuses = [
            LoanStatus(code="ACTIVE", name="Активна"),
            LoanStatus(code="RETURNED", name="Возвращена"),
            LoanStatus(code="OVERDUE", name="Просрочена"),
            LoanStatus(code="LOST", name="Утеряна"),
        ]
        
        for ls in loan_statuses:
            session.add(ls)
        session.commit()
        print(f"    ✅ Создано {len(loan_statuses)} статусов выдач")
        
        # 2.9. Типы операций
        print("  💳 Типы операций...")
        operation_types = [
            OperationType(code="MEMBERSHIP", name="Членский взнос"),
            OperationType(code="FINE", name="Штраф за просрочку"),
            OperationType(code="DAMAGE", name="Компенсация ущерба"),
            OperationType(code="COPY", name="Ксерокопирование"),
            OperationType(code="RESERVATION", name="Плата за бронь"),
        ]
        
        for ot in operation_types:
            session.add(ot)
        session.commit()
        print(f"    ✅ Создано {len(operation_types)} типов операций")
        
        print("✅ Все справочники заполнены!")
        print("=" * 60)
        
        # Перезагружаем объекты после коммита
        edition_types = session.exec(select(EditionType)).all()
        languages = session.exec(select(Language)).all()
        countries = session.exec(select(Country)).all()
        cities = session.exec(select(City)).all()
        publishers = session.exec(select(Publisher)).all()
        reader_categories = session.exec(select(ReaderCategory)).all()
        book_statuses = session.exec(select(BookStatus)).all()
        loan_statuses = session.exec(select(LoanStatus)).all()
        operation_types = session.exec(select(OperationType)).all()
        
        # ==================== 3. ЧИТАТЕЛИ ====================
        print("👥 Создаем читателей...")
        
        readers = [
            Reader(
                last_name="Ичетовкина",
                first_name="Анна",
                middle_name="Евгеньевна",
                birth_date=date(2000, 5, 15),
                category_id=reader_categories[2].id,  # Студент
                phone="+79161234567",
                email="anna.ichetovkina@example.com",
                address="г. Москва, ул. Ленина, 10, кв. 25",
                document_type="Паспорт",
                document_number="4510 123456",
                document_issued_by="ОУФМС России по г. Москве",
                document_issued_date=date(2014, 4, 20),
                registration_date=date(2024, 9, 1),
                card_expiry_date=date(2025, 9, 1),
                is_active=True,
                notes="Отличный читатель, всегда возвращает книги вовремя"
            ),
            Reader(
                last_name="Петров",
                first_name="Иван",
                middle_name="Сергеевич",
                birth_date=date(1995, 3, 22),
                category_id=reader_categories[0].id,  # Взрослый
                phone="+79219876543",
                email="ivan.petrov@example.com",
                address="г. Санкт-Петербург, Невский пр., 45, кв. 12",
                document_type="Паспорт",
                document_number="4012 654321",
                document_issued_by="ОУФМС России по СПб",
                document_issued_date=date(2010, 11, 15),
                registration_date=date(2023, 8, 15),
                card_expiry_date=date(2024, 8, 15),
                is_active=True,
                notes="Часто берет техническую литературу"
            ),
            Reader(
                last_name="Сидорова",
                first_name="Мария",
                middle_name="Александровна",
                birth_date=date(1988, 7, 30),
                category_id=reader_categories[0].id,  # Взрослый
                phone="+79155556677",
                email="maria.sidorova@example.com",
                address="г. Новосибирск, ул. Кирова, 33, кв. 8",
                registration_date=date(2024, 1, 10),
                card_expiry_date=date(2025, 1, 10),
                is_active=True
            ),
            Reader(
                last_name="Кузнецов",
                first_name="Алексей",
                middle_name="Викторович",
                birth_date=date(1975, 11, 5),
                category_id=reader_categories[3].id,  # Пенсионер
                phone="+79187778899",
                email="alex.kuznetsov@example.com",
                address="г. Москва, ул. Мира, 15, кв. 42",
                registration_date=date(2022, 5, 20),
                card_expiry_date=date(2023, 5, 20),
                is_active=False,
                notes="Карта просрочена, не продлевал"
            ),
            Reader(
                last_name="Васильева",
                first_name="Екатерина",
                middle_name="Игоревна",
                birth_date=date(2012, 2, 14),
                category_id=reader_categories[1].id,  # Ребенок
                phone="+79190001122",
                email="ekaterina.vasilyeva@example.com",
                address="г. Москва, ул. Пушкина, 7, кв. 3",
                document_type="Свидетельство о рождении",
                document_number="VIII-АБ 123456",
                document_issued_by="ЗАГС Центрального района г. Москвы",
                document_issued_date=date(2012, 3, 1),
                registration_date=date(2023, 12, 5),
                card_expiry_date=date(2024, 12, 5),
                is_active=True,
                notes="Любит детские книги и комиксы"
            ),
        ]
        
        for reader in readers:
            session.add(reader)
        session.commit()
        print(f"✅ Создано {len(readers)} читателей")
        print("=" * 60)
        
        # Перезагружаем читателей
        readers = session.exec(select(Reader)).all()
        
        # ==================== 4. АВТОРЫ ====================
        print("✍️ Создаем авторы...")
        
        authors = [
            Author(
                last_name="Дюма",
                first_name="Александр",
                middle_name=None,
                birth_year=1802,
                death_year=1870,
                biography="Французский писатель, драматург и журналист. Один из самых читаемых французских авторов."
            ),
            Author(
                last_name="Леванова",
                first_name="Татьяна",
                middle_name="Александровна",
                birth_year=1978,
                death_year=None,
                biography="Современная российская писательница, автор романов в жанре современной прозы."
            ),
            Author(
                last_name="Булгаков",
                first_name="Михаил",
                middle_name="Афанасьевич",
                birth_year=1891,
                death_year=1940,
                biography="Русский писатель, драматург, театральный режиссёр и актёр."
            ),
            Author(
                last_name="Толстой",
                first_name="Лев",
                middle_name="Николаевич",
                birth_year=1828,
                death_year=1910,
                biography="Один из наиболее известных русских писателей и мыслителей, один из величайших писателей мира."
            ),
            Author(
                last_name="Достоевский",
                first_name="Фёдор",
                middle_name="Михайлович",
                birth_year=1821,
                death_year=1881,
                biography="Русский писатель, мыслитель, философ и публицист."
            ),
            Author(
                last_name="Роулинг",
                first_name="Джоан",
                middle_name=None,
                birth_year=1965,
                death_year=None,
                biography="Британская писательница, автор серии романов о Гарри Поттере."
            ),
        ]
        
        for author in authors:
            session.add(author)
        session.commit()
        print(f"✅ Создано {len(authors)} авторов")
        print("=" * 60)
        
        # Перезагружаем авторов
        authors = session.exec(select(Author)).all()
        
        # ==================== 5. КНИГИ ====================
        print("📚 Создаем книги (библиографические описания)...")
        
        books = [
            Book(
                isbn="978-5-699-12345-6",
                udk="821.133.1",
                bbk="84(4Фра)",
                main_title="Граф Монте-Кристо",
                parallel_title="Le Comte de Monte-Cristo",
                additional_title="Роман",
                publisher_id=publishers[1].id if publishers else None,  # АСТ
                publication_place="Москва",
                publication_year=1989,
                edition_type_id=edition_types[0].id if edition_types else 1,  # Книга
                language_id=languages[0].id if languages else 1,  # Русский
                volume_pages=928,
                volume_copies=2,
                dimensions="210x148 мм",
                weight=850.5,
                abstract="Классический роман Александра Дюма о мести и справедливости. История Эдмона Дантеса, несправедливо осуждённого и сбежавшего из тюрьмы.",
                keywords="приключения, месть, Франция, XIX век, тюрьма, сокровища",
                table_of_contents="Часть 1. Марсель... Часть 2. Париж...",
                is_electronic=False,
            ),
            Book(
                isbn="978-5-17-098765-4",
                main_title="Сквозняки",
                publisher_id=publishers[2].id if len(publishers) > 2 else None,  # Эксмо
                publication_year=2014,
                edition_type_id=edition_types[0].id if edition_types else 1,  # Книга
                language_id=languages[0].id if languages else 1,  # Русский
                volume_pages=320,
                abstract="Современный роман о жизни в большом городе, о любви и одиночестве.",
                keywords="современная проза, любовь, город, одиночество",
                is_electronic=False,
            ),
            Book(
                isbn="978-5-389-01234-5",
                main_title="Мастер и Маргарита",
                publisher_id=publishers[0].id if publishers else None,  # Просвещение
                publication_year=2003,
                edition_type_id=edition_types[0].id if edition_types else 1,  # Книга
                language_id=languages[0].id if languages else 1,  # Русский
                volume_pages=480,
                is_electronic=True,
                electronic_format="PDF",
                electronic_access_url="https://library.example.com/books/master-i-margarita.pdf",
                electronic_file_size=2048576,
            ),
            Book(
                isbn="978-5-17-134567-8",
                main_title="Война и мир",
                publication_year=2019,
                edition_type_id=edition_types[0].id if edition_types else 1,  # Книга
                language_id=languages[0].id if languages else 1,  # Русский
                volume_pages=1225,
                volume_copies=4,
                abstract="Роман-эпопея Льва Толстого, описывающий русское общество в эпоху войн против Наполеона.",
                keywords="эпопея, война, мир, Наполеон, Россия, XIX век",
            ),
            Book(
                isbn="978-5-04-112233-4",
                main_title="Преступление и наказание",
                publication_year=2020,
                edition_type_id=edition_types[0].id if edition_types else 1,  # Книга
                language_id=languages[0].id if languages else 1,  # Русский
                volume_pages=672,
                abstract="Роман Фёдора Достоевского о нравственных последствиях преступления.",
                is_electronic=True,
                electronic_format="EPUB",
                electronic_access_url="https://library.example.com/books/prestuplenie-i-nakazanie.epub",
                electronic_file_size=1536000,
            ),
            Book(
                isbn="978-5-353-04567-1",
                main_title="Гарри Поттер и философский камень",
                parallel_title="Harry Potter and the Philosopher's Stone",
                publication_year=2001,
                edition_type_id=edition_types[0].id if edition_types else 1,  # Книга
                language_id=languages[0].id if languages else 1,  # Русский
                volume_pages=432,
                abstract="Первая книга серии о юном волшебнике Гарри Поттере.",
                keywords="фэнтези, волшебство, школа, дружба",
                is_electronic=False,
            ),
        ]
        
        for book in books:
            session.add(book)
        session.commit()
        print(f"✅ Создано {len(books)} книг")
        print("=" * 60)
        
        # Перезагружаем книги
        books = session.exec(select(Book)).all()
        
        # ==================== 6. СВЯЗИ КНИГ-АВТОРЫ ====================
        print("🔗 Связываем книги с авторами...")
        
        book_authors = [
            BookAuthor(book_id=books[0].id, author_id=authors[0].id, author_role="author", author_order=1),
            BookAuthor(book_id=books[1].id, author_id=authors[1].id, author_role="author", author_order=1),
            BookAuthor(book_id=books[2].id, author_id=authors[2].id, author_role="author", author_order=1),
            BookAuthor(book_id=books[3].id, author_id=authors[3].id, author_role="author", author_order=1),
            BookAuthor(book_id=books[4].id, author_id=authors[4].id, author_role="author", author_order=1),
            BookAuthor(book_id=books[5].id, author_id=authors[5].id, author_role="author", author_order=1),
        ]
        
        for ba in book_authors:
            session.add(ba)
        session.commit()
        print(f"✅ Создано {len(book_authors)} связей книга-автор")
        print("=" * 60)
        
        # ==================== 7. ЭКЗЕМПЛЯРЫ КНИГ ====================
        print("📖 Создаем экземпляры книг...")
        
        book_copies = []
        
        # Для каждой книги создаем несколько экземпляров
        for i, book in enumerate(books):
            copies_count = book.volume_copies or 1
            for j in range(copies_count):
                copy_number = j + 1
                book_copies.append(
                    BookCopy(
                        book_id=book.id,
                        inventory_number=f"INV-{book.id:03d}-{copy_number:03d}",
                        barcode=f"978{book.id:010d}{copy_number:03d}" if book.isbn else None,
                        copy_number=copy_number,
                        acquisition_date=date(2023, random.randint(1, 12), random.randint(1, 28)),
                        acquisition_source="Закупка" if random.choice([True, False]) else "Дар",
                        price=random.uniform(300, 1500),
                        location=f"Стеллаж {random.randint(1, 10)}, Полка {random.randint(1, 5)}",
                        current_status_id=book_statuses[0].id if book_statuses else 1,  # Доступна
                        condition_notes="Отличное состояние" if random.choice([True, False]) else "Незначительные повреждения",
                    )
                )
        
        # Делаем некоторые экземпляры выданными или поврежденными
        if len(book_copies) >= 3 and book_statuses:
            book_copies[2].current_status_id = book_statuses[1].id  # Выдана
            book_copies[5].current_status_id = book_statuses[4].id  # Повреждена
            book_copies[8].current_status_id = book_statuses[5].id  # Списана
            book_copies[8].write_off_date = date(2024, 1, 15)
            book_copies[8].write_off_reason = "Утеряна читателем"
        
        for copy in book_copies:
            session.add(copy)
        session.commit()
        print(f"✅ Создано {len(book_copies)} экземпляров книг")
        print("=" * 60)
        
        # Перезагружаем экземпляры
        book_copies = session.exec(select(BookCopy)).all()
        
        # ==================== 8. ВЫДАЧИ КНИГ ====================
        print("📅 Создаем выдачи книг...")
        
        loans = []
        
        # Создаем несколько исторических выдач
        for i in range(10):
            reader = random.choice(readers)
            copy = random.choice(book_copies)
            
            # Проверяем, доступен ли экземпляр
            if copy.current_status_id == book_statuses[1].id if book_statuses else 2:  # Уже выдан
                continue
            
            loan_date = date(2024, random.randint(1, 8), random.randint(1, 28))
            due_date = loan_date + timedelta(days=30)
            return_date = loan_date + timedelta(days=random.randint(15, 40)) if random.choice([True, False]) else None
            
            loan = Loan(
                book_copy_id=copy.id,
                reader_id=reader.id,
                loan_date=loan_date,
                due_date=due_date,
                return_date=return_date,
                status_id=loan_statuses[0].id if loan_statuses and not return_date else (loan_statuses[1].id if loan_statuses else 2),
                renewal_count=random.randint(0, 2),
                fine_amount=random.uniform(0, 500) if return_date and return_date > due_date else 0,
                fine_paid=random.choice([True, False]) if return_date and return_date > due_date else True,
                notes="Обычная выдача" if random.choice([True, False]) else "По предварительному заказу"
            )
            
            # Обновляем статус экземпляра
            if not return_date and book_statuses:
                copy.current_status_id = book_statuses[1].id  # Выдана
            
            loans.append(loan)
            session.add(loan)
        
        session.commit()
        print(f"✅ Создано {len(loans)} выдач")
        print("=" * 60)
        
        # Перезагружаем выдачи
        loans = session.exec(select(Loan)).all()
        
        # ==================== 9. ПЛАТЕЖИ ====================
        print("💰 Создаем платежи...")
        
        payments = []
        
        for reader in readers[:3]:  # Только первые три читателя
            for _ in range(random.randint(1, 3)):
                payment = Payment(
                    reader_id=reader.id,
                    operation_type_id=operation_types[0].id if operation_types else 1,  # Членский взнос
                    amount=500.00,
                    payment_date=date(2024, random.randint(1, 8), random.randint(1, 28)),
                    payment_method=random.choice(["карта", "наличные", "онлайн"]),
                    transaction_id=f"TRX-{random.randint(10000, 99999)}",
                    description="Ежегодный членский взнос"
                )
                payments.append(payment)
                session.add(payment)
        
        # Добавляем несколько штрафов
        for loan in loans:
            if loan.fine_amount > 0 and loan.fine_paid:
                payment = Payment(
                    reader_id=loan.reader_id,
                    operation_type_id=operation_types[1].id if operation_types else 2,  # Штраф
                    amount=loan.fine_amount,
                    payment_date=loan.return_date or date.today(),
                    payment_method="наличные",
                    description=f"Штраф за просрочку выдачи #{loan.id}",
                    related_loan_id=loan.id
                )
                payments.append(payment)
                session.add(payment)
        
        session.commit()
        print(f"✅ Создано {len(payments)} платежей")
        print("=" * 60)
        
        # Перезагружаем платежи
        payments = session.exec(select(Payment)).all()
        
        # ==================== 10. БРОНИРОВАНИЯ ====================
        print("🔖 Создаем бронирования...")
        
        reservations = []
        
        for i in range(3):
            reader = random.choice(readers)
            book = random.choice(books)
            
            reservation = Reservation(
                book_id=book.id,
                reader_id=reader.id,
                reservation_date=datetime.now() - timedelta(days=random.randint(1, 10)),
                expiration_date=datetime.now() + timedelta(days=random.randint(1, 7)),
                status=random.choice(["active", "cancelled", "fulfilled"]),
                priority=random.randint(1, 5),
                notes="Обычное бронирование"
            )
            reservations.append(reservation)
            session.add(reservation)
        
        session.commit()
        print(f"✅ Создано {len(reservations)} бронирований")
        print("=" * 60)
        
        # ==================== 11. ПОСЕЩЕНИЯ ====================
        print("🚶 Создаем записи о посещениях...")
        
        visits = []
        
        for i in range(20):
            reader = random.choice(readers + [None])  # Некоторые посещения могут быть без читателя
            
            visit = Visit(
                reader_id=reader.id if reader else None,
                visit_date=date(2024, random.randint(1, 8), random.randint(1, 28)),
                visit_time=datetime.now().replace(hour=random.randint(9, 18), minute=random.randint(0, 59)),
                is_remote=random.choice([True, False]),
                purpose=random.choice(["взять книги", "вернуть книги", "поработать", "посещение мероприятия", "консультация"]),
                duration_minutes=random.randint(15, 180)
            )
            visits.append(visit)
            session.add(visit)
        
        session.commit()
        print(f"✅ Создано {len(visits)} записей о посещениях")
        print("=" * 60)
        
        # Перезагружаем посещения
        visits = session.exec(select(Visit)).all()
        
        # ==================== 12. СПРАВОЧНЫЕ ЗАПРОСЫ ====================
        print("❓ Создаем справочные запросы...")
        
        reference_requests = []
        
        for i in range(8):
            reader = random.choice(readers[:3])  # Только активные читатели
            
            request = ReferenceRequest(
                reader_id=reader.id,
                request_date=datetime.now() - timedelta(days=random.randint(1, 30)),
                request_type=random.choice(["библиографический", "тематический", "фактографический", "адресный"]),
                subject=random.choice(["история России", "программирование", "литература", "искусство", "наука"]),
                complexity_level=random.choice(["простой", "средний", "сложный"]),
                completion_time_minutes=random.randint(5, 60) if random.choice([True, False]) else None,
                is_completed=random.choice([True, False]),
                librarian_notes="Выполнен" if random.choice([True, False]) else "В процессе"
            )
            reference_requests.append(request)
            session.add(request)
        
        session.commit()
        print(f"✅ Создано {len(reference_requests)} справочных запросов")
        print("=" * 60)
        
        # Перезагружаем запросы
        reference_requests = session.exec(select(ReferenceRequest)).all()
        
        # ==================== 13. ЕЖЕДНЕВНАЯ СТАТИСТИКА ====================
        print("📊 Создаем ежедневную статистику...")
        
        daily_stats = []
        
        # Создаем статистику за последние 7 дней
        for i in range(7):
            stat_date = date.today() - timedelta(days=i)
            
            # Подсчитываем статистику для этой даты
            daily_visits = len([v for v in visits if v.visit_date == stat_date])
            physical_visits = len([v for v in visits if v.visit_date == stat_date and not v.is_remote])
            
            daily_stat = DailyStatistic(
                statistic_date=stat_date,
                total_visits=daily_visits,
                physical_visits=physical_visits,
                remote_visits=daily_visits - physical_visits,
                new_readers=1 if i == 0 else 0,  # Предположим, что новый читатель был только сегодня
                active_readers=len([r for r in readers if r.is_active]),
                total_loans=len([l for l in loans if l.loan_date == stat_date]),
                book_loans=len([l for l in loans if l.loan_date == stat_date]),
                electronic_loans=0,  # Упрощенно
                overdue_loans=len([l for l in loans if l.due_date < stat_date and not l.return_date]),
                total_copies=len(book_copies),
                new_copies=1 if i == 2 else 0,  # Предположим, что новые книги поступили 2 дня назад
                written_off_copies=1 if i == 4 else 0,  # Предположим, что списание было 4 дня назад
                reference_requests=len([r for r in reference_requests if r.request_date.date() == stat_date]),
                complex_requests=len([r for r in reference_requests if r.request_date.date() == stat_date and r.complexity_level == "сложный"])
            )
            daily_stats.append(daily_stat)
            session.add(daily_stat)
        
        session.commit()
        print(f"✅ Создано {len(daily_stats)} записей ежедневной статистики")
        print("=" * 60)
        
        # ==================== ФИНАЛЬНЫЙ ОТЧЕТ ====================
        print("🎉 БАЗА ДАННЫХ УСПЕШНО ЗАПОЛНЕНА!")
        print("=" * 60)
        print("📊 ИТОГОВАЯ СТАТИСТИКА:")
        
        # Перезагружаем все данные для отчета
        all_readers = session.exec(select(Reader)).all()
        all_books = session.exec(select(Book)).all()
        all_authors = session.exec(select(Author)).all()
        all_book_authors = session.exec(select(BookAuthor)).all()
        all_book_copies = session.exec(select(BookCopy)).all()
        all_loans = session.exec(select(Loan)).all()
        all_payments = session.exec(select(Payment)).all()
        all_reservations = session.exec(select(Reservation)).all()
        all_visits = session.exec(select(Visit)).all()
        all_reference_requests = session.exec(select(ReferenceRequest)).all()
        all_daily_stats = session.exec(select(DailyStatistic)).all()
        
        print(f"  📚 Книги: {len(all_books)} библиографических записей")
        print(f"  📖 Экземпляры: {len(all_book_copies)} физических экземпляров")
        print(f"  👥 Читатели: {len(all_readers)} человек")
        print(f"  ✍️ Авторы: {len(all_authors)} человек")
        print(f"  🔗 Связи: {len(all_book_authors)} связей книга-автор")
        print(f"  📅 Выдачи: {len(all_loans)} записей о выдаче")
        print(f"  💳 Платежи: {len(all_payments)} финансовых операций")
        print(f"  🔖 Бронирования: {len(all_reservations)} записей")
        print(f"  🚶 Посещения: {len(all_visits)} визитов")
        print(f"  ❓ Запросы: {len(all_reference_requests)} справочных запросов")
        print(f"  📊 Статистика: {len(all_daily_stats)} ежедневных отчетов")
        print("=" * 60)
        print("✅ Все данные успешно загружены в схему 'Ichetovkina'")
        print("🌐 API доступен по адресу: http://localhost:8000")
        print("📚 Документация API: http://localhost:8000/docs")

if __name__ == "__main__":
    try:
        fill_test_data()
    except Exception as e:
        print(f"❌ Ошибка при заполнении базы данных: {e}")
        import traceback
        traceback.print_exc()