from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import *
from requests import *
from datetime import date, datetime

app = FastAPI(
    title="Library Management System API (ГОСТ)",
    version="4.0.0",
    description="Полнофункциональная система управления библиотекой с полным CRUD для всех таблиц",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ==================== КОРЕНЬ ====================

@app.get("/")
def read_root():
    return {
        "message": "Библиотечная система управления (ГОСТ-версия)",
        "version": "4.0.0",
        "schema": "Ichetovkina",
        "description": "Полный CRUD для всех 20 таблиц",
        "tables_count": 20,
        "endpoints": "/docs для полной документации"
    }

# ==================== СПРАВОЧНИКИ (CRUD) ====================

# 1. EditionType
@app.get("/edition-types", response_model=list[EditionType])
def get_all_edition_types_endpoint(session: Session = Depends(get_session)):
    """Получить все типы изданий"""
    return get_all_edition_types(session)

@app.get("/edition-types/{type_id}", response_model=EditionType)
def get_edition_type_by_id_endpoint(type_id: int, session: Session = Depends(get_session)):
    """Получить тип издания по ID"""
    edition_type = get_edition_type_by_id(session, type_id)
    if not edition_type:
        raise HTTPException(status_code=404, detail="Тип издания не найден")
    return edition_type

@app.post("/edition-types", response_model=EditionType)
def create_edition_type_endpoint(edition_type: EditionType, session: Session = Depends(get_session)):
    """Создать новый тип издания"""
    return create_edition_type(session, edition_type)

@app.put("/edition-types/{type_id}", response_model=EditionType)
def update_edition_type_endpoint(type_id: int, edition_type_data: dict, session: Session = Depends(get_session)):
    """Обновить тип издания"""
    edition_type = update_edition_type(session, type_id, edition_type_data)
    if not edition_type:
        raise HTTPException(status_code=404, detail="Тип издания не найден")
    return edition_type

@app.delete("/edition-types/{type_id}")
def delete_edition_type_endpoint(type_id: int, session: Session = Depends(get_session)):
    """Удалить тип издания"""
    success = delete_edition_type(session, type_id)
    if not success:
        raise HTTPException(status_code=404, detail="Тип издания не найден")
    return {"message": f"Тип издания {type_id} удален"}

# 2. Language
@app.get("/languages", response_model=list[Language])
def get_all_languages_endpoint(session: Session = Depends(get_session)):
    """Получить все языки"""
    return get_all_languages(session)

@app.get("/languages/{language_id}", response_model=Language)
def get_language_by_id_endpoint(language_id: int, session: Session = Depends(get_session)):
    """Получить язык по ID"""
    language = get_language_by_id(session, language_id)
    if not language:
        raise HTTPException(status_code=404, detail="Язык не найден")
    return language

@app.post("/languages", response_model=Language)
def create_language_endpoint(language: Language, session: Session = Depends(get_session)):
    """Создать новый язык"""
    return create_language(session, language)

@app.put("/languages/{language_id}", response_model=Language)
def update_language_endpoint(language_id: int, language_data: dict, session: Session = Depends(get_session)):
    """Обновить язык"""
    language = update_language(session, language_id, language_data)
    if not language:
        raise HTTPException(status_code=404, detail="Язык не найден")
    return language

@app.delete("/languages/{language_id}")
def delete_language_endpoint(language_id: int, session: Session = Depends(get_session)):
    """Удалить язык"""
    success = delete_language(session, language_id)
    if not success:
        raise HTTPException(status_code=404, detail="Язык не найден")
    return {"message": f"Язык {language_id} удален"}

# 3. Country
@app.get("/countries", response_model=list[Country])
def get_all_countries_endpoint(session: Session = Depends(get_session)):
    """Получить все страны"""
    return get_all_countries(session)

@app.get("/countries/{country_id}", response_model=Country)
def get_country_by_id_endpoint(country_id: int, session: Session = Depends(get_session)):
    """Получить страну по ID"""
    country = get_country_by_id(session, country_id)
    if not country:
        raise HTTPException(status_code=404, detail="Страна не найдена")
    return country

@app.post("/countries", response_model=Country)
def create_country_endpoint(country: Country, session: Session = Depends(get_session)):
    """Создать новую страну"""
    return create_country(session, country)

@app.put("/countries/{country_id}", response_model=Country)
def update_country_endpoint(country_id: int, country_data: dict, session: Session = Depends(get_session)):
    """Обновить страну"""
    country = update_country(session, country_id, country_data)
    if not country:
        raise HTTPException(status_code=404, detail="Страна не найдена")
    return country

@app.delete("/countries/{country_id}")
def delete_country_endpoint(country_id: int, session: Session = Depends(get_session)):
    """Удалить страну"""
    success = delete_country(session, country_id)
    if not success:
        raise HTTPException(status_code=404, detail="Страна не найдена")
    return {"message": f"Страна {country_id} удалена"}

# 4. City
@app.get("/cities", response_model=list[City])
def get_all_cities_endpoint(session: Session = Depends(get_session)):
    """Получить все города"""
    return get_all_cities(session)

@app.get("/cities/{city_id}", response_model=City)
def get_city_by_id_endpoint(city_id: int, session: Session = Depends(get_session)):
    """Получить город по ID"""
    city = get_city_by_id(session, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="Город не найден")
    return city

@app.post("/cities", response_model=City)
def create_city_endpoint(city: City, session: Session = Depends(get_session)):
    """Создать новый город"""
    return create_city(session, city)

@app.put("/cities/{city_id}", response_model=City)
def update_city_endpoint(city_id: int, city_data: dict, session: Session = Depends(get_session)):
    """Обновить город"""
    city = update_city(session, city_id, city_data)
    if not city:
        raise HTTPException(status_code=404, detail="Город не найден")
    return city

@app.delete("/cities/{city_id}")
def delete_city_endpoint(city_id: int, session: Session = Depends(get_session)):
    """Удалить город"""
    success = delete_city(session, city_id)
    if not success:
        raise HTTPException(status_code=404, detail="Город не найден")
    return {"message": f"Город {city_id} удален"}

# 5. Publisher
@app.get("/publishers", response_model=list[Publisher])
def get_all_publishers_endpoint(session: Session = Depends(get_session)):
    """Получить все издательства"""
    return get_all_publishers(session)

@app.get("/publishers/{publisher_id}", response_model=Publisher)
def get_publisher_by_id_endpoint(publisher_id: int, session: Session = Depends(get_session)):
    """Получить издательство по ID"""
    publisher = get_publisher_by_id(session, publisher_id)
    if not publisher:
        raise HTTPException(status_code=404, detail="Издательство не найдено")
    return publisher

@app.post("/publishers", response_model=Publisher)
def create_publisher_endpoint(publisher: Publisher, session: Session = Depends(get_session)):
    """Создать новое издательство"""
    return create_publisher(session, publisher)

@app.put("/publishers/{publisher_id}", response_model=Publisher)
def update_publisher_endpoint(publisher_id: int, publisher_data: dict, session: Session = Depends(get_session)):
    """Обновить издательство"""
    publisher = update_publisher(session, publisher_id, publisher_data)
    if not publisher:
        raise HTTPException(status_code=404, detail="Издательство не найдено")
    return publisher

@app.delete("/publishers/{publisher_id}")
def delete_publisher_endpoint(publisher_id: int, session: Session = Depends(get_session)):
    """Удалить издательство"""
    success = delete_publisher(session, publisher_id)
    if not success:
        raise HTTPException(status_code=404, detail="Издательство не найдено")
    return {"message": f"Издательство {publisher_id} удалено"}

# 6. ReaderCategory
@app.get("/reader-categories", response_model=list[ReaderCategory])
def get_all_reader_categories_endpoint(session: Session = Depends(get_session)):
    """Получить все категории читателей"""
    return get_all_reader_categories(session)

@app.get("/reader-categories/{category_id}", response_model=ReaderCategory)
def get_reader_category_by_id_endpoint(category_id: int, session: Session = Depends(get_session)):
    """Получить категорию читателя по ID"""
    reader_category = get_reader_category_by_id(session, category_id)
    if not reader_category:
        raise HTTPException(status_code=404, detail="Категория читателя не найдена")
    return reader_category

@app.post("/reader-categories", response_model=ReaderCategory)
def create_reader_category_endpoint(reader_category: ReaderCategory, session: Session = Depends(get_session)):
    """Создать новую категорию читателя"""
    return create_reader_category(session, reader_category)

@app.put("/reader-categories/{category_id}", response_model=ReaderCategory)
def update_reader_category_endpoint(category_id: int, reader_category_data: dict, session: Session = Depends(get_session)):
    """Обновить категорию читателя"""
    reader_category = update_reader_category(session, category_id, reader_category_data)
    if not reader_category:
        raise HTTPException(status_code=404, detail="Категория читателя не найдена")
    return reader_category

@app.delete("/reader-categories/{category_id}")
def delete_reader_category_endpoint(category_id: int, session: Session = Depends(get_session)):
    """Удалить категорию читателя"""
    success = delete_reader_category(session, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Категория читателя не найдена")
    return {"message": f"Категория читателя {category_id} удалена"}

# 7. BookStatus
@app.get("/book-statuses", response_model=list[BookStatus])
def get_all_book_statuses_endpoint(session: Session = Depends(get_session)):
    """Получить все статусы книг"""
    return get_all_book_statuses(session)

@app.get("/book-statuses/{status_id}", response_model=BookStatus)
def get_book_status_by_id_endpoint(status_id: int, session: Session = Depends(get_session)):
    """Получить статус книги по ID"""
    book_status = get_book_status_by_id(session, status_id)
    if not book_status:
        raise HTTPException(status_code=404, detail="Статус книги не найден")
    return book_status

@app.post("/book-statuses", response_model=BookStatus)
def create_book_status_endpoint(book_status: BookStatus, session: Session = Depends(get_session)):
    """Создать новый статус книги"""
    return create_book_status(session, book_status)

@app.put("/book-statuses/{status_id}", response_model=BookStatus)
def update_book_status_endpoint(status_id: int, book_status_data: dict, session: Session = Depends(get_session)):
    """Обновить статус книги"""
    book_status = update_book_status(session, status_id, book_status_data)
    if not book_status:
        raise HTTPException(status_code=404, detail="Статус книги не найден")
    return book_status

@app.delete("/book-statuses/{status_id}")
def delete_book_status_endpoint(status_id: int, session: Session = Depends(get_session)):
    """Удалить статус книги"""
    success = delete_book_status(session, status_id)
    if not success:
        raise HTTPException(status_code=404, detail="Статус книги не найден")
    return {"message": f"Статус книги {status_id} удален"}

# 8. LoanStatus
@app.get("/loan-statuses", response_model=list[LoanStatus])
def get_all_loan_statuses_endpoint(session: Session = Depends(get_session)):
    """Получить все статусы выдач"""
    return get_all_loan_statuses(session)

@app.get("/loan-statuses/{status_id}", response_model=LoanStatus)
def get_loan_status_by_id_endpoint(status_id: int, session: Session = Depends(get_session)):
    """Получить статус выдачи по ID"""
    loan_status = get_loan_status_by_id(session, status_id)
    if not loan_status:
        raise HTTPException(status_code=404, detail="Статус выдачи не найден")
    return loan_status

@app.post("/loan-statuses", response_model=LoanStatus)
def create_loan_status_endpoint(loan_status: LoanStatus, session: Session = Depends(get_session)):
    """Создать новый статус выдачи"""
    return create_loan_status(session, loan_status)

@app.put("/loan-statuses/{status_id}", response_model=LoanStatus)
def update_loan_status_endpoint(status_id: int, loan_status_data: dict, session: Session = Depends(get_session)):
    """Обновить статус выдачи"""
    loan_status = update_loan_status(session, status_id, loan_status_data)
    if not loan_status:
        raise HTTPException(status_code=404, detail="Статус выдачи не найден")
    return loan_status

@app.delete("/loan-statuses/{status_id}")
def delete_loan_status_endpoint(status_id: int, session: Session = Depends(get_session)):
    """Удалить статус выдачи"""
    success = delete_loan_status(session, status_id)
    if not success:
        raise HTTPException(status_code=404, detail="Статус выдачи не найден")
    return {"message": f"Статус выдачи {status_id} удален"}

# 9. OperationType
@app.get("/operation-types", response_model=list[OperationType])
def get_all_operation_types_endpoint(session: Session = Depends(get_session)):
    """Получить все типы операций"""
    return get_all_operation_types(session)

@app.get("/operation-types/{type_id}", response_model=OperationType)
def get_operation_type_by_id_endpoint(type_id: int, session: Session = Depends(get_session)):
    """Получить тип операции по ID"""
    operation_type = get_operation_type_by_id(session, type_id)
    if not operation_type:
        raise HTTPException(status_code=404, detail="Тип операции не найден")
    return operation_type

@app.post("/operation-types", response_model=OperationType)
def create_operation_type_endpoint(operation_type: OperationType, session: Session = Depends(get_session)):
    """Создать новый тип операции"""
    return create_operation_type(session, operation_type)

@app.put("/operation-types/{type_id}", response_model=OperationType)
def update_operation_type_endpoint(type_id: int, operation_type_data: dict, session: Session = Depends(get_session)):
    """Обновить тип операции"""
    operation_type = update_operation_type(session, type_id, operation_type_data)
    if not operation_type:
        raise HTTPException(status_code=404, detail="Тип операции не найден")
    return operation_type

@app.delete("/operation-types/{type_id}")
def delete_operation_type_endpoint(type_id: int, session: Session = Depends(get_session)):
    """Удалить тип операции"""
    success = delete_operation_type(session, type_id)
    if not success:
        raise HTTPException(status_code=404, detail="Тип операции не найден")
    return {"message": f"Тип операции {type_id} удален"}

# ==================== ОСНОВНЫЕ ТАБЛИЦЫ (CRUD) ====================

# 10. Reader
@app.get("/readers", response_model=list[Reader])
def get_all_readers_endpoint(session: Session = Depends(get_session)):
    """Получить всех читателей"""
    return get_all_readers(session)

@app.get("/readers/{reader_id}", response_model=Reader)
def get_reader_by_id_endpoint(reader_id: int, session: Session = Depends(get_session)):
    """Получить читателя по ID"""
    reader = get_reader_by_id(session, reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Читатель не найден")
    return reader

@app.post("/readers", response_model=Reader)
def create_reader_endpoint(reader: ReaderCreate, session: Session = Depends(get_session)):
    """Создать нового читателя"""
    return create_reader(session, reader)

@app.put("/readers/{reader_id}", response_model=Reader)
def update_reader_endpoint(reader_id: int, reader_data: ReaderUpdate, session: Session = Depends(get_session)):
    """Обновить данные читателя"""
    reader = update_reader(session, reader_id, reader_data)
    if not reader:
        raise HTTPException(status_code=404, detail="Читатель не найден")
    return reader

@app.delete("/readers/{reader_id}")
def delete_reader_endpoint(reader_id: int, session: Session = Depends(get_session)):
    """Удалить читателя"""
    success = delete_reader(session, reader_id)
    if not success:
        raise HTTPException(status_code=404, detail="Читатель не найден")
    return {"message": f"Читатель {reader_id} удален"}

# 11. Book
@app.get("/books", response_model=list[Book])
def get_all_books_endpoint(session: Session = Depends(get_session)):
    """Получить все книги"""
    return get_all_books(session)

@app.get("/books/{book_id}", response_model=Book)
def get_book_by_id_endpoint(book_id: int, session: Session = Depends(get_session)):
    """Получить книгу по ID"""
    book = get_book_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@app.post("/books", response_model=Book)
def create_book_endpoint(book: BookCreate, session: Session = Depends(get_session)):
    """Создать новую книгу"""
    return create_book(session, book)

@app.put("/books/{book_id}", response_model=Book)
def update_book_endpoint(book_id: int, book_data: BookUpdate, session: Session = Depends(get_session)):
    """Обновить данные книги"""
    book = update_book(session, book_id, book_data)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@app.delete("/books/{book_id}")
def delete_book_endpoint(book_id: int, session: Session = Depends(get_session)):
    """Удалить книгу"""
    success = delete_book(session, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"message": f"Книга {book_id} удалена"}

# 12. Author
@app.get("/authors", response_model=list[Author])
def get_all_authors_endpoint(session: Session = Depends(get_session)):
    """Получить всех авторов"""
    return get_all_authors(session)

@app.get("/authors/{author_id}", response_model=Author)
def get_author_by_id_endpoint(author_id: int, session: Session = Depends(get_session)):
    """Получить автора по ID"""
    author = get_author_by_id(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    return author

@app.post("/authors", response_model=Author)
def create_author_endpoint(author: AuthorCreate, session: Session = Depends(get_session)):
    """Создать нового автора"""
    return create_author(session, author)

@app.put("/authors/{author_id}", response_model=Author)
def update_author_endpoint(author_id: int, author_data: dict, session: Session = Depends(get_session)):
    """Обновить данные автора"""
    author = update_author(session, author_id, author_data)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    return author

@app.delete("/authors/{author_id}")
def delete_author_endpoint(author_id: int, session: Session = Depends(get_session)):
    """Удалить автора"""
    success = delete_author(session, author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Автор не найден")
    return {"message": f"Автор {author_id} удален"}

# 13. BookAuthor
@app.get("/book-authors", response_model=list[BookAuthor])
def get_all_book_authors_endpoint(session: Session = Depends(get_session)):
    """Получить все связи книга-автор"""
    return get_all_book_authors(session)

@app.get("/book-authors/{book_author_id}", response_model=BookAuthor)
def get_book_author_by_id_endpoint(book_author_id: int, session: Session = Depends(get_session)):
    """Получить связь книга-автор по ID"""
    book_author = get_book_author_by_id(session, book_author_id)
    if not book_author:
        raise HTTPException(status_code=404, detail="Связь книга-автор не найдена")
    return book_author

@app.post("/book-authors", response_model=BookAuthor)
def create_book_author_endpoint(book_author: BookAuthor, session: Session = Depends(get_session)):
    """Создать новую связь книга-автор"""
    return create_book_author(session, book_author)

@app.put("/book-authors/{book_author_id}", response_model=BookAuthor)
def update_book_author_endpoint(book_author_id: int, book_author_data: dict, session: Session = Depends(get_session)):
    """Обновить связь книга-автор"""
    book_author = update_book_author(session, book_author_id, book_author_data)
    if not book_author:
        raise HTTPException(status_code=404, detail="Связь книга-автор не найдена")
    return book_author

@app.delete("/book-authors/{book_author_id}")
def delete_book_author_endpoint(book_author_id: int, session: Session = Depends(get_session)):
    """Удалить связь книга-автор"""
    success = delete_book_author(session, book_author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Связь книга-автор не найдена")
    return {"message": f"Связь книга-автор {book_author_id} удалена"}

# 14. BookCopy
@app.get("/book-copies", response_model=list[BookCopy])
def get_all_book_copies_endpoint(session: Session = Depends(get_session)):
    """Получить все экземпляры книг"""
    return get_all_book_copies(session)

@app.get("/book-copies/{copy_id}", response_model=BookCopy)
def get_book_copy_by_id_endpoint(copy_id: int, session: Session = Depends(get_session)):
    """Получить экземпляр по ID"""
    book_copy = get_book_copy_by_id(session, copy_id)
    if not book_copy:
        raise HTTPException(status_code=404, detail="Экземпляр не найден")
    return book_copy

@app.post("/book-copies", response_model=BookCopy)
def create_book_copy_endpoint(book_copy: BookCopyCreate, session: Session = Depends(get_session)):
    """Создать новый экземпляр книги"""
    return create_book_copy(session, book_copy)

@app.put("/book-copies/{copy_id}", response_model=BookCopy)
def update_book_copy_endpoint(copy_id: int, book_copy_data: dict, session: Session = Depends(get_session)):
    """Обновить данные экземпляра"""
    book_copy = update_book_copy(session, copy_id, book_copy_data)
    if not book_copy:
        raise HTTPException(status_code=404, detail="Экземпляр не найден")
    return book_copy

@app.delete("/book-copies/{copy_id}")
def delete_book_copy_endpoint(copy_id: int, session: Session = Depends(get_session)):
    """Удалить экземпляр"""
    success = delete_book_copy(session, copy_id)
    if not success:
        raise HTTPException(status_code=404, detail="Экземпляр не найден")
    return {"message": f"Экземпляр {copy_id} удален"}

# 15. Loan
@app.get("/loans", response_model=list[Loan])
def get_all_loans_endpoint(session: Session = Depends(get_session)):
    """Получить все выдачи"""
    return get_all_loans(session)

@app.get("/loans/{loan_id}", response_model=Loan)
def get_loan_by_id_endpoint(loan_id: int, session: Session = Depends(get_session)):
    """Получить выдачу по ID"""
    loan = get_loan_by_id(session, loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Выдача не найдена")
    return loan

@app.post("/loans", response_model=Loan)
def create_loan_endpoint(loan: LoanCreate, session: Session = Depends(get_session)):
    """Создать новую выдачу"""
    return create_loan(session, loan)

@app.put("/loans/{loan_id}", response_model=Loan)
def update_loan_endpoint(loan_id: int, loan_data: LoanUpdate, session: Session = Depends(get_session)):
    """Обновить данные выдачи"""
    loan = update_loan(session, loan_id, loan_data)
    if not loan:
        raise HTTPException(status_code=404, detail="Выдача не найдена")
    return loan

@app.delete("/loans/{loan_id}")
def delete_loan_endpoint(loan_id: int, session: Session = Depends(get_session)):
    """Удалить выдачу"""
    success = delete_loan(session, loan_id)
    if not success:
        raise HTTPException(status_code=404, detail="Выдача не найдена")
    return {"message": f"Выдача {loan_id} удалена"}

# 16. Payment
@app.get("/payments", response_model=list[Payment])
def get_all_payments_endpoint(session: Session = Depends(get_session)):
    """Получить все платежи"""
    return get_all_payments(session)

@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment_by_id_endpoint(payment_id: int, session: Session = Depends(get_session)):
    """Получить платеж по ID"""
    payment = get_payment_by_id(session, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Платеж не найден")
    return payment

@app.post("/payments", response_model=Payment)
def create_payment_endpoint(payment: PaymentCreate, session: Session = Depends(get_session)):
    """Создать новый платеж"""
    return create_payment(session, payment)

@app.put("/payments/{payment_id}", response_model=Payment)
def update_payment_endpoint(payment_id: int, payment_data: dict, session: Session = Depends(get_session)):
    """Обновить платеж"""
    payment = update_payment(session, payment_id, payment_data)
    if not payment:
        raise HTTPException(status_code=404, detail="Платеж не найден")
    return payment

@app.delete("/payments/{payment_id}")
def delete_payment_endpoint(payment_id: int, session: Session = Depends(get_session)):
    """Удалить платеж"""
    success = delete_payment(session, payment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Платеж не найден")
    return {"message": f"Платеж {payment_id} удален"}

# 17. Reservation
@app.get("/reservations", response_model=list[Reservation])
def get_all_reservations_endpoint(session: Session = Depends(get_session)):
    """Получить все бронирования"""
    return get_all_reservations(session)

@app.get("/reservations/{reservation_id}", response_model=Reservation)
def get_reservation_by_id_endpoint(reservation_id: int, session: Session = Depends(get_session)):
    """Получить бронирование по ID"""
    reservation = get_reservation_by_id(session, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return reservation

@app.post("/reservations", response_model=Reservation)
def create_reservation_endpoint(reservation: Reservation, session: Session = Depends(get_session)):
    """Создать новое бронирование"""
    return create_reservation(session, reservation)

@app.put("/reservations/{reservation_id}", response_model=Reservation)
def update_reservation_endpoint(reservation_id: int, reservation_data: dict, session: Session = Depends(get_session)):
    """Обновить бронирование"""
    reservation = update_reservation(session, reservation_id, reservation_data)
    if not reservation:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return reservation

@app.delete("/reservations/{reservation_id}")
def delete_reservation_endpoint(reservation_id: int, session: Session = Depends(get_session)):
    """Удалить бронирование"""
    success = delete_reservation(session, reservation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return {"message": f"Бронирование {reservation_id} удалено"}

# 18. Visit
@app.get("/visits", response_model=list[Visit])
def get_all_visits_endpoint(session: Session = Depends(get_session)):
    """Получить все посещения"""
    return get_all_visits(session)

@app.get("/visits/{visit_id}", response_model=Visit)
def get_visit_by_id_endpoint(visit_id: int, session: Session = Depends(get_session)):
    """Получить посещение по ID"""
    visit = get_visit_by_id(session, visit_id)
    if not visit:
        raise HTTPException(status_code=404, detail="Посещение не найдено")
    return visit

@app.post("/visits", response_model=Visit)
def create_visit_endpoint(visit: Visit, session: Session = Depends(get_session)):
    """Создать новое посещение"""
    return create_visit(session, visit)

@app.put("/visits/{visit_id}", response_model=Visit)
def update_visit_endpoint(visit_id: int, visit_data: dict, session: Session = Depends(get_session)):
    """Обновить посещение"""
    visit = update_visit(session, visit_id, visit_data)
    if not visit:
        raise HTTPException(status_code=404, detail="Посещение не найдено")
    return visit

@app.delete("/visits/{visit_id}")
def delete_visit_endpoint(visit_id: int, session: Session = Depends(get_session)):
    """Удалить посещение"""
    success = delete_visit(session, visit_id)
    if not success:
        raise HTTPException(status_code=404, detail="Посещение не найдено")
    return {"message": f"Посещение {visit_id} удалено"}

# 19. ReferenceRequest
@app.get("/reference-requests", response_model=list[ReferenceRequest])
def get_all_reference_requests_endpoint(session: Session = Depends(get_session)):
    """Получить все справочные запросы"""
    return get_all_reference_requests(session)

@app.get("/reference-requests/{request_id}", response_model=ReferenceRequest)
def get_reference_request_by_id_endpoint(request_id: int, session: Session = Depends(get_session)):
    """Получить справочный запрос по ID"""
    reference_request = get_reference_request_by_id(session, request_id)
    if not reference_request:
        raise HTTPException(status_code=404, detail="Справочный запрос не найден")
    return reference_request

@app.post("/reference-requests", response_model=ReferenceRequest)
def create_reference_request_endpoint(reference_request: ReferenceRequest, session: Session = Depends(get_session)):
    """Создать новый справочный запрос"""
    return create_reference_request(session, reference_request)

@app.put("/reference-requests/{request_id}", response_model=ReferenceRequest)
def update_reference_request_endpoint(request_id: int, reference_request_data: dict, session: Session = Depends(get_session)):
    """Обновить справочный запрос"""
    reference_request = update_reference_request(session, request_id, reference_request_data)
    if not reference_request:
        raise HTTPException(status_code=404, detail="Справочный запрос не найден")
    return reference_request

@app.delete("/reference-requests/{request_id}")
def delete_reference_request_endpoint(request_id: int, session: Session = Depends(get_session)):
    """Удалить справочный запрос"""
    success = delete_reference_request(session, request_id)
    if not success:
        raise HTTPException(status_code=404, detail="Справочный запрос не найден")
    return {"message": f"Справочный запрос {request_id} удален"}


# 20. DailyStatistic
@app.get("/daily-statistics", response_model=list[DailyStatistic])
def get_all_daily_statistics_endpoint(session: Session = Depends(get_session)):
    """Получить всю ежедневную статистику"""
    return get_all_daily_statistics(session)

@app.get("/daily-statistics/{statistic_id}", response_model=DailyStatistic)
def get_daily_statistic_by_id_endpoint(statistic_id: int, session: Session = Depends(get_session)):
    """Получить ежедневную статистику по ID"""
    daily_statistic = get_daily_statistic_by_id(session, statistic_id)
    if not daily_statistic:
        raise HTTPException(status_code=404, detail="Ежедневная статистика не найдена")
    return daily_statistic

@app.post("/daily-statistics", response_model=DailyStatistic)
def create_daily_statistic_endpoint(daily_statistic: DailyStatistic, session: Session = Depends(get_session)):
    """Создать новую ежедневную статистику"""
    return create_daily_statistic(session, daily_statistic)

@app.put("/daily-statistics/{statistic_id}", response_model=DailyStatistic)
def update_daily_statistic_endpoint(statistic_id: int, daily_statistic_data: dict, session: Session = Depends(get_session)):
    """Обновить ежедневную статистику"""
    daily_statistic = update_daily_statistic(session, statistic_id, daily_statistic_data)
    if not daily_statistic:
        raise HTTPException(status_code=404, detail="Ежедневная статистика не найдена")
    return daily_statistic

@app.delete("/daily-statistics/{statistic_id}")
def delete_daily_statistic_endpoint(statistic_id: int, session: Session = Depends(get_session)):
    """Удалить ежедневную статистику"""
    success = delete_daily_statistic(session, statistic_id)
    if not success:
        raise HTTPException(status_code=404, detail="Ежедневная статистика не найдена")
    return {"message": f"Ежедневная статистика {statistic_id} удалена"}


# ==================== ПОИСК ====================

@app.get("/search/readers")
def search_readers_endpoint(
    last_name: Optional[str] = None,
    first_name: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    is_active: Optional[bool] = None,
    session: Session = Depends(get_session)
):
    """Поиск читателей"""
    from requests import search_readers
    readers = search_readers(
        session=session,
        last_name=last_name,
        first_name=first_name,
        phone=phone,
        email=email,
        is_active=is_active
    )
    
    return {
        "search_criteria": {
            "last_name": last_name,
            "first_name": first_name,
            "phone": phone,
            "email": email,
            "is_active": is_active
        },
        "found": len(readers),
        "readers": readers
    }

@app.get("/search/books")
def search_books_endpoint(
    title: Optional[str] = None,
    author: Optional[str] = None,
    isbn: Optional[str] = None,
    year: Optional[int] = None,
    electronic: Optional[bool] = None,
    language_id: Optional[int] = None,
    session: Session = Depends(get_session)
):
    """Поиск книг"""
    from requests import search_books
    books = search_books(
        session=session,
        title=title,
        author_name=author,
        isbn=isbn,
        publication_year=year,
        is_electronic=electronic,
        language_id=language_id
    )
    
    return {
        "search_criteria": {
            "title": title,
            "author": author,
            "isbn": isbn,
            "year": year,
            "electronic": electronic,
            "language_id": language_id
        },
        "found": len(books),
        "books": books
    }


@app.get("/authors/{author_id}/books-with-counts")
def get_author_books_with_counts_endpoint(author_id: int, session: Session = Depends(get_session)):
    """Получить все книги автора с количеством экземпляров"""
    from requests import get_author_books_with_counts
    result = get_author_books_with_counts(session, author_id)
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    return result

# ==================== ДОПОЛНИТЕЛЬНЫЕ ЭНДПОИНТЫ ====================

@app.get("/health")
def health_check(session: Session = Depends(get_session)):
    """Проверка здоровья системы"""
    try:
        session.execute("SELECT 1")
        return {
            "status": "healthy",
            "timestamp": datetime.now(),
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/api/summary")
def api_summary():
    """Сводка по API"""
    return {
        "api_name": "Library Management System (ГОСТ)",
        "version": "4.0.0",
        "tables": 20,
        "endpoints": "Все CRUD операции для каждой таблицы",
        "documentation": "/docs или /redoc"
    }


# ==================== СТАТИСТИЧЕСКИЕ ЭНДПОИНТЫ ====================

@app.get("/statistics/library")
def get_library_statistics(session: Session = Depends(get_session)):
    """Получить сводную статистику библиотеки"""
    try:
        # Читатели
        total_readers = len(get_all_readers(session))
        active_readers = len([r for r in get_all_readers(session) if r.is_active])
        
        # Книги
        total_books = len(get_all_books(session))
        electronic_books = len([b for b in get_all_books(session) if b.is_electronic])
        
        # Экземпляры
        total_copies = len(get_all_book_copies(session))
        
        # Выдачи
        total_loans = len(get_all_loans(session))
        active_loans = len([l for l in get_all_loans(session) if not l.return_date])
        overdue_loans = len([l for l in get_all_loans(session) if l.due_date < date.today() and not l.return_date])
        
        # Авторы
        total_authors = len(get_all_authors(session))
        
        # Посещения за сегодня
        today = date.today()
        today_visits = len([v for v in get_all_visits(session) if v.visit_date == today])
        
        # Справочные запросы
        total_requests = len(get_all_reference_requests(session))
        completed_requests = len([r for r in get_all_reference_requests(session) if r.is_completed])
        
        return {
            "library": {
                "name": "Библиотечная система Ичетовкиной (ГОСТ)",
                "schema": "Ichetovkina",
                "last_updated": datetime.now().isoformat()
            },
            "readers": {
                "total": total_readers,
                "active": active_readers,
                "inactive": total_readers - active_readers
            },
            "books": {
                "bibliographic_records": total_books,
                "physical_copies": total_copies,
                "electronic_books": electronic_books,
                "physical_books": total_books - electronic_books
            },
            "authors": {
                "total": total_authors
            },
            "loans": {
                "total": total_loans,
                "active": active_loans,
                "returned": total_loans - active_loans,
                "overdue": overdue_loans
            },
            "activity": {
                "visits_today": today_visits,
                "reference_requests_total": total_requests,
                "reference_requests_completed": completed_requests
            },
            "calculated_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при расчете статистики: {str(e)}")

@app.get("/statistics/daily")
def get_daily_statistics_summary(session: Session = Depends(get_session)):
    """Получить последние 7 дней статистики"""
    all_stats = get_all_daily_statistics(session)
    all_stats.sort(key=lambda x: x.statistic_date, reverse=True)
    
    return {
        "daily_statistics": all_stats[:7],  # Последние 7 дней
        "total_days": len(all_stats),
        "calculated_at": datetime.now().isoformat()
    }

@app.get("/api/statistics/library")
def get_library_statistics_alias(session: Session = Depends(get_session)):
    """Алиас для /statistics/library"""
    return get_library_statistics(session)

@app.get("/api/statistics")
def get_all_statistics(session: Session = Depends(get_session)):
    """Все статистические эндпоинты"""
    return {
        "endpoints": {
            "library_summary": "/statistics/library",
            "daily_statistics": "/statistics/daily",
            "all_daily_stats": "/daily-statistics",
            "visits": "/visits",
            "reference_requests": "/reference-requests"
        },
        "description": "Статистические данные библиотеки"
    }

@app.get("/test/stats")
def test_stats():
    """Простой тест-эндпоинт для проверки"""
    return {
        "message": "Статистика доступна!",
        "endpoints": {
            "library_summary": "/statistics/library",
            "daily_stats": "/daily-statistics",
            "test": "/test/stats"
        },
        "timestamp": datetime.now().isoformat()
    }

@app.get("/statistics/simple")
def get_simple_statistics(session: Session = Depends(get_session)):
    """Простая сводка по библиотеке"""
    return {
        "readers_count": len(get_all_readers(session)),
        "books_count": len(get_all_books(session)),
        "loans_count": len(get_all_loans(session)),
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)