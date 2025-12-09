from sqlmodel import select, Session
from typing import List, Optional
from datetime import date, datetime
from models import *

# ==================== КОНСТАНТЫ ДЛЯ РАСЧЕТА ШТРАФОВ ====================
FINE_PER_DAY = 10.0      # Штраф за день просрочки
MAX_FINE_DAYS = 30       # Максимальное количество дней для расчета
MAX_FINE = 300.0         # Максимальный штраф
GRACE_PERIOD_DAYS = 3    # Дни без штрафа после срока возврата

# Ограничения
MAX_BOOKS_PER_READER = 10
MAX_LOAN_DAYS = 60
DEFAULT_LOAN_DAYS = 30
# =======================================================================

# ==================== СПРАВОЧНИКИ (CRUD для всех) ====================

# 1. EditionType
def get_all_edition_types(session: Session) -> List[EditionType]:
    return session.exec(select(EditionType)).all()

def get_edition_type_by_id(session: Session, type_id: int) -> Optional[EditionType]:
    return session.exec(select(EditionType).where(EditionType.id == type_id)).first()

def create_edition_type(session: Session, edition_type: EditionType) -> EditionType:
    session.add(edition_type)
    session.commit()
    session.refresh(edition_type)
    return edition_type

def update_edition_type(session: Session, type_id: int, edition_type_data: dict) -> Optional[EditionType]:
    edition_type = get_edition_type_by_id(session, type_id)
    if not edition_type:
        return None
    
    for key, value in edition_type_data.items():
        setattr(edition_type, key, value)
    
    session.add(edition_type)
    session.commit()
    session.refresh(edition_type)
    return edition_type

def delete_edition_type(session: Session, type_id: int) -> bool:
    edition_type = get_edition_type_by_id(session, type_id)
    if not edition_type:
        return False
    
    session.delete(edition_type)
    session.commit()
    return True

# 2. Language
def get_all_languages(session: Session) -> List[Language]:
    return session.exec(select(Language)).all()

def get_language_by_id(session: Session, language_id: int) -> Optional[Language]:
    return session.exec(select(Language).where(Language.id == language_id)).first()

def create_language(session: Session, language: Language) -> Language:
    session.add(language)
    session.commit()
    session.refresh(language)
    return language

def update_language(session: Session, language_id: int, language_data: dict) -> Optional[Language]:
    language = get_language_by_id(session, language_id)
    if not language:
        return None
    
    for key, value in language_data.items():
        setattr(language, key, value)
    
    session.add(language)
    session.commit()
    session.refresh(language)
    return language

def delete_language(session: Session, language_id: int) -> bool:
    language = get_language_by_id(session, language_id)
    if not language:
        return False
    
    session.delete(language)
    session.commit()
    return True

# 3. Country
def get_all_countries(session: Session) -> List[Country]:
    return session.exec(select(Country)).all()

def get_country_by_id(session: Session, country_id: int) -> Optional[Country]:
    return session.exec(select(Country).where(Country.id == country_id)).first()

def create_country(session: Session, country: Country) -> Country:
    session.add(country)
    session.commit()
    session.refresh(country)
    return country

def update_country(session: Session, country_id: int, country_data: dict) -> Optional[Country]:
    country = get_country_by_id(session, country_id)
    if not country:
        return None
    
    for key, value in country_data.items():
        setattr(country, key, value)
    
    session.add(country)
    session.commit()
    session.refresh(country)
    return country

def delete_country(session: Session, country_id: int) -> bool:
    country = get_country_by_id(session, country_id)
    if not country:
        return False
    
    session.delete(country)
    session.commit()
    return True

# 4. City
def get_all_cities(session: Session) -> List[City]:
    return session.exec(select(City)).all()

def get_city_by_id(session: Session, city_id: int) -> Optional[City]:
    return session.exec(select(City).where(City.id == city_id)).first()

def create_city(session: Session, city: City) -> City:
    session.add(city)
    session.commit()
    session.refresh(city)
    return city

def update_city(session: Session, city_id: int, city_data: dict) -> Optional[City]:
    city = get_city_by_id(session, city_id)
    if not city:
        return None
    
    for key, value in city_data.items():
        setattr(city, key, value)
    
    session.add(city)
    session.commit()
    session.refresh(city)
    return city

def delete_city(session: Session, city_id: int) -> bool:
    city = get_city_by_id(session, city_id)
    if not city:
        return False
    
    session.delete(city)
    session.commit()
    return True

# 5. Publisher
def get_all_publishers(session: Session) -> List[Publisher]:
    return session.exec(select(Publisher)).all()

def get_publisher_by_id(session: Session, publisher_id: int) -> Optional[Publisher]:
    return session.exec(select(Publisher).where(Publisher.id == publisher_id)).first()

def create_publisher(session: Session, publisher: Publisher) -> Publisher:
    session.add(publisher)
    session.commit()
    session.refresh(publisher)
    return publisher

def update_publisher(session: Session, publisher_id: int, publisher_data: dict) -> Optional[Publisher]:
    publisher = get_publisher_by_id(session, publisher_id)
    if not publisher:
        return None
    
    for key, value in publisher_data.items():
        setattr(publisher, key, value)
    
    session.add(publisher)
    session.commit()
    session.refresh(publisher)
    return publisher

def delete_publisher(session: Session, publisher_id: int) -> bool:
    publisher = get_publisher_by_id(session, publisher_id)
    if not publisher:
        return False
    
    session.delete(publisher)
    session.commit()
    return True

# 6. ReaderCategory
def get_all_reader_categories(session: Session) -> List[ReaderCategory]:
    return session.exec(select(ReaderCategory)).all()

def get_reader_category_by_id(session: Session, category_id: int) -> Optional[ReaderCategory]:
    return session.exec(select(ReaderCategory).where(ReaderCategory.id == category_id)).first()

def create_reader_category(session: Session, reader_category: ReaderCategory) -> ReaderCategory:
    session.add(reader_category)
    session.commit()
    session.refresh(reader_category)
    return reader_category

def update_reader_category(session: Session, category_id: int, reader_category_data: dict) -> Optional[ReaderCategory]:
    reader_category = get_reader_category_by_id(session, category_id)
    if not reader_category:
        return None
    
    for key, value in reader_category_data.items():
        setattr(reader_category, key, value)
    
    session.add(reader_category)
    session.commit()
    session.refresh(reader_category)
    return reader_category

def delete_reader_category(session: Session, category_id: int) -> bool:
    reader_category = get_reader_category_by_id(session, category_id)
    if not reader_category:
        return False
    
    session.delete(reader_category)
    session.commit()
    return True

# 7. BookStatus
def get_all_book_statuses(session: Session) -> List[BookStatus]:
    return session.exec(select(BookStatus)).all()

def get_book_status_by_id(session: Session, status_id: int) -> Optional[BookStatus]:
    return session.exec(select(BookStatus).where(BookStatus.id == status_id)).first()

def create_book_status(session: Session, book_status: BookStatus) -> BookStatus:
    session.add(book_status)
    session.commit()
    session.refresh(book_status)
    return book_status

def update_book_status(session: Session, status_id: int, book_status_data: dict) -> Optional[BookStatus]:
    book_status = get_book_status_by_id(session, status_id)
    if not book_status:
        return None
    
    for key, value in book_status_data.items():
        setattr(book_status, key, value)
    
    session.add(book_status)
    session.commit()
    session.refresh(book_status)
    return book_status

def delete_book_status(session: Session, status_id: int) -> bool:
    book_status = get_book_status_by_id(session, status_id)
    if not book_status:
        return False
    
    session.delete(book_status)
    session.commit()
    return True

# 8. LoanStatus
def get_all_loan_statuses(session: Session) -> List[LoanStatus]:
    return session.exec(select(LoanStatus)).all()

def get_loan_status_by_id(session: Session, status_id: int) -> Optional[LoanStatus]:
    return session.exec(select(LoanStatus).where(LoanStatus.id == status_id)).first()

def create_loan_status(session: Session, loan_status: LoanStatus) -> LoanStatus:
    session.add(loan_status)
    session.commit()
    session.refresh(loan_status)
    return loan_status

def update_loan_status(session: Session, status_id: int, loan_status_data: dict) -> Optional[LoanStatus]:
    loan_status = get_loan_status_by_id(session, status_id)
    if not loan_status:
        return None
    
    for key, value in loan_status_data.items():
        setattr(loan_status, key, value)
    
    session.add(loan_status)
    session.commit()
    session.refresh(loan_status)
    return loan_status

def delete_loan_status(session: Session, status_id: int) -> bool:
    loan_status = get_loan_status_by_id(session, status_id)
    if not loan_status:
        return False
    
    session.delete(loan_status)
    session.commit()
    return True

# 9. OperationType
def get_all_operation_types(session: Session) -> List[OperationType]:
    return session.exec(select(OperationType)).all()

def get_operation_type_by_id(session: Session, type_id: int) -> Optional[OperationType]:
    return session.exec(select(OperationType).where(OperationType.id == type_id)).first()

def create_operation_type(session: Session, operation_type: OperationType) -> OperationType:
    session.add(operation_type)
    session.commit()
    session.refresh(operation_type)
    return operation_type

def update_operation_type(session: Session, type_id: int, operation_type_data: dict) -> Optional[OperationType]:
    operation_type = get_operation_type_by_id(session, type_id)
    if not operation_type:
        return None
    
    for key, value in operation_type_data.items():
        setattr(operation_type, key, value)
    
    session.add(operation_type)
    session.commit()
    session.refresh(operation_type)
    return operation_type

def delete_operation_type(session: Session, type_id: int) -> bool:
    operation_type = get_operation_type_by_id(session, type_id)
    if not operation_type:
        return False
    
    session.delete(operation_type)
    session.commit()
    return True

# ==================== ОСНОВНЫЕ ТАБЛИЦЫ (CRUD для всех) ====================

# 10. Reader
def get_all_readers(session: Session) -> List[Reader]:
    return session.exec(select(Reader)).all()

def get_reader_by_id(session: Session, reader_id: int) -> Optional[Reader]:
    return session.exec(select(Reader).where(Reader.id == reader_id)).first()

def create_reader(session: Session, reader: ReaderCreate) -> Reader:
    db_reader = Reader(**reader.dict())
    session.add(db_reader)
    session.commit()
    session.refresh(db_reader)
    return db_reader

def update_reader(session: Session, reader_id: int, reader_data: ReaderUpdate) -> Optional[Reader]:
    db_reader = get_reader_by_id(session, reader_id)
    if not db_reader:
        return None
    
    update_data = reader_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_reader, key, value)
    
    session.add(db_reader)
    session.commit()
    session.refresh(db_reader)
    return db_reader

def delete_reader(session: Session, reader_id: int) -> bool:
    db_reader = get_reader_by_id(session, reader_id)
    if not db_reader:
        return False
    
    session.delete(db_reader)
    session.commit()
    return True

# 11. Book
def get_all_books(session: Session) -> List[Book]:
    return session.exec(select(Book)).all()

def get_book_by_id(session: Session, book_id: int) -> Optional[Book]:
    return session.exec(select(Book).where(Book.id == book_id)).first()

def create_book(session: Session, book: BookCreate) -> Book:
    db_book = Book(**book.dict())
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

def update_book(session: Session, book_id: int, book_data: BookUpdate) -> Optional[Book]:
    db_book = get_book_by_id(session, book_id)
    if not db_book:
        return None
    
    update_data = book_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

def delete_book(session: Session, book_id: int) -> bool:
    db_book = get_book_by_id(session, book_id)
    if not db_book:
        return False
    
    session.delete(db_book)
    session.commit()
    return True

# 12. Author
def get_all_authors(session: Session) -> List[Author]:
    return session.exec(select(Author)).all()

def get_author_by_id(session: Session, author_id: int) -> Optional[Author]:
    return session.exec(select(Author).where(Author.id == author_id)).first()

def create_author(session: Session, author: AuthorCreate) -> Author:
    db_author = Author(**author.dict())
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author

def update_author(session: Session, author_id: int, author_data: dict) -> Optional[Author]:
    db_author = get_author_by_id(session, author_id)
    if not db_author:
        return None
    
    for key, value in author_data.items():
        setattr(db_author, key, value)
    
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author

def delete_author(session: Session, author_id: int) -> bool:
    db_author = get_author_by_id(session, author_id)
    if not db_author:
        return False
    
    session.delete(db_author)
    session.commit()
    return True

# 13. BookAuthor
def get_all_book_authors(session: Session) -> List[BookAuthor]:
    return session.exec(select(BookAuthor)).all()

def get_book_author_by_id(session: Session, book_author_id: int) -> Optional[BookAuthor]:
    return session.exec(select(BookAuthor).where(BookAuthor.id == book_author_id)).first()

def create_book_author(session: Session, book_author: BookAuthor) -> BookAuthor:
    session.add(book_author)
    session.commit()
    session.refresh(book_author)
    return book_author

def update_book_author(session: Session, book_author_id: int, book_author_data: dict) -> Optional[BookAuthor]:
    book_author = get_book_author_by_id(session, book_author_id)
    if not book_author:
        return None
    
    for key, value in book_author_data.items():
        setattr(book_author, key, value)
    
    session.add(book_author)
    session.commit()
    session.refresh(book_author)
    return book_author

def delete_book_author(session: Session, book_author_id: int) -> bool:
    book_author = get_book_author_by_id(session, book_author_id)
    if not book_author:
        return False
    
    session.delete(book_author)
    session.commit()
    return True

# 14. BookCopy
def get_all_book_copies(session: Session) -> List[BookCopy]:
    return session.exec(select(BookCopy)).all()

def get_book_copy_by_id(session: Session, copy_id: int) -> Optional[BookCopy]:
    return session.exec(select(BookCopy).where(BookCopy.id == copy_id)).first()

def create_book_copy(session: Session, book_copy: BookCopyCreate) -> BookCopy:
    db_copy = BookCopy(**book_copy.dict())
    session.add(db_copy)
    session.commit()
    session.refresh(db_copy)
    return db_copy

def update_book_copy(session: Session, copy_id: int, book_copy_data: dict) -> Optional[BookCopy]:
    book_copy = get_book_copy_by_id(session, copy_id)
    if not book_copy:
        return None
    
    for key, value in book_copy_data.items():
        setattr(book_copy, key, value)
    
    session.add(book_copy)
    session.commit()
    session.refresh(book_copy)
    return book_copy

def delete_book_copy(session: Session, copy_id: int) -> bool:
    book_copy = get_book_copy_by_id(session, copy_id)
    if not book_copy:
        return False
    
    session.delete(book_copy)
    session.commit()
    return True

# 15. Loan
def get_all_loans(session: Session) -> List[Loan]:
    return session.exec(select(Loan)).all()

def get_loan_by_id(session: Session, loan_id: int) -> Optional[Loan]:
    return session.exec(select(Loan).where(Loan.id == loan_id)).first()

def create_loan(session: Session, loan: LoanCreate) -> Loan:
    db_loan = Loan(**loan.dict())
    session.add(db_loan)
    session.commit()
    session.refresh(db_loan)
    return db_loan

def update_loan(session: Session, loan_id: int, loan_data: LoanUpdate) -> Optional[Loan]:
    db_loan = get_loan_by_id(session, loan_id)
    if not db_loan:
        return None
    
    update_data = loan_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_loan, key, value)
    
    session.add(db_loan)
    session.commit()
    session.refresh(db_loan)
    return db_loan

def delete_loan(session: Session, loan_id: int) -> bool:
    db_loan = get_loan_by_id(session, loan_id)
    if not db_loan:
        return False
    
    session.delete(db_loan)
    session.commit()
    return True

# 16. Payment
def get_all_payments(session: Session) -> List[Payment]:
    return session.exec(select(Payment)).all()

def get_payment_by_id(session: Session, payment_id: int) -> Optional[Payment]:
    return session.exec(select(Payment).where(Payment.id == payment_id)).first()

def create_payment(session: Session, payment: PaymentCreate) -> Payment:
    db_payment = Payment(**payment.dict())
    session.add(db_payment)
    session.commit()
    session.refresh(db_payment)
    return db_payment

def update_payment(session: Session, payment_id: int, payment_data: dict) -> Optional[Payment]:
    payment = get_payment_by_id(session, payment_id)
    if not payment:
        return None
    
    for key, value in payment_data.items():
        setattr(payment, key, value)
    
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment

def delete_payment(session: Session, payment_id: int) -> bool:
    payment = get_payment_by_id(session, payment_id)
    if not payment:
        return False
    
    session.delete(payment)
    session.commit()
    return True

# 17. Reservation
def get_all_reservations(session: Session) -> List[Reservation]:
    return session.exec(select(Reservation)).all()

def get_reservation_by_id(session: Session, reservation_id: int) -> Optional[Reservation]:
    return session.exec(select(Reservation).where(Reservation.id == reservation_id)).first()

def create_reservation(session: Session, reservation: Reservation) -> Reservation:
    session.add(reservation)
    session.commit()
    session.refresh(reservation)
    return reservation

def update_reservation(session: Session, reservation_id: int, reservation_data: dict) -> Optional[Reservation]:
    reservation = get_reservation_by_id(session, reservation_id)
    if not reservation:
        return None
    
    for key, value in reservation_data.items():
        setattr(reservation, key, value)
    
    session.add(reservation)
    session.commit()
    session.refresh(reservation)
    return reservation

def delete_reservation(session: Session, reservation_id: int) -> bool:
    reservation = get_reservation_by_id(session, reservation_id)
    if not reservation:
        return False
    
    session.delete(reservation)
    session.commit()
    return True

# 18. Visit
def get_all_visits(session: Session) -> List[Visit]:
    return session.exec(select(Visit)).all()

def get_visit_by_id(session: Session, visit_id: int) -> Optional[Visit]:
    return session.exec(select(Visit).where(Visit.id == visit_id)).first()

def create_visit(session: Session, visit: Visit) -> Visit:
    session.add(visit)
    session.commit()
    session.refresh(visit)
    return visit

def update_visit(session: Session, visit_id: int, visit_data: dict) -> Optional[Visit]:
    visit = get_visit_by_id(session, visit_id)
    if not visit:
        return None
    
    for key, value in visit_data.items():
        setattr(visit, key, value)
    
    session.add(visit)
    session.commit()
    session.refresh(visit)
    return visit

def delete_visit(session: Session, visit_id: int) -> bool:
    visit = get_visit_by_id(session, visit_id)
    if not visit:
        return False
    
    session.delete(visit)
    session.commit()
    return True

# 19. ReferenceRequest
def get_all_reference_requests(session: Session) -> List[ReferenceRequest]:
    return session.exec(select(ReferenceRequest)).all()

def get_reference_request_by_id(session: Session, request_id: int) -> Optional[ReferenceRequest]:
    return session.exec(select(ReferenceRequest).where(ReferenceRequest.id == request_id)).first()

def create_reference_request(session: Session, reference_request: ReferenceRequest) -> ReferenceRequest:
    session.add(reference_request)
    session.commit()
    session.refresh(reference_request)
    return reference_request

def update_reference_request(session: Session, request_id: int, reference_request_data: dict) -> Optional[ReferenceRequest]:
    reference_request = get_reference_request_by_id(session, request_id)
    if not reference_request:
        return None
    
    for key, value in reference_request_data.items():
        setattr(reference_request, key, value)
    
    session.add(reference_request)
    session.commit()
    session.refresh(reference_request)
    return reference_request

def delete_reference_request(session: Session, request_id: int) -> bool:
    reference_request = get_reference_request_by_id(session, request_id)
    if not reference_request:
        return False
    
    session.delete(reference_request)
    session.commit()
    return True

# 20. DailyStatistic
def get_all_daily_statistics(session: Session) -> List[DailyStatistic]:
    return session.exec(select(DailyStatistic)).all()

def get_daily_statistic_by_id(session: Session, statistic_id: int) -> Optional[DailyStatistic]:
    return session.exec(select(DailyStatistic).where(DailyStatistic.id == statistic_id)).first()

def create_daily_statistic(session: Session, daily_statistic: DailyStatistic) -> DailyStatistic:
    session.add(daily_statistic)
    session.commit()
    session.refresh(daily_statistic)
    return daily_statistic

def update_daily_statistic(session: Session, statistic_id: int, daily_statistic_data: dict) -> Optional[DailyStatistic]:
    daily_statistic = get_daily_statistic_by_id(session, statistic_id)
    if not daily_statistic:
        return None
    
    for key, value in daily_statistic_data.items():
        setattr(daily_statistic, key, value)
    
    session.add(daily_statistic)
    session.commit()
    session.refresh(daily_statistic)
    return daily_statistic

def delete_daily_statistic(session: Session, statistic_id: int) -> bool:
    daily_statistic = get_daily_statistic_by_id(session, statistic_id)
    if not daily_statistic:
        return False
    
    session.delete(daily_statistic)
    session.commit()
    return True


# ==================== ПОИСК ====================

def search_readers(
    session: Session,
    last_name: Optional[str] = None,
    first_name: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    is_active: Optional[bool] = None
) -> List[Reader]:
    """Поиск читателей по параметрам"""
    query = select(Reader)
    
    if last_name:
        query = query.where(Reader.last_name.ilike(f"%{last_name}%"))
    if first_name:
        query = query.where(Reader.first_name.ilike(f"%{first_name}%"))
    if phone:
        query = query.where(Reader.phone.ilike(f"%{phone}%"))
    if email:
        query = query.where(Reader.email.ilike(f"%{email}%"))
    if is_active is not None:
        query = query.where(Reader.is_active == is_active)
    
    return session.exec(query.order_by(Reader.last_name, Reader.first_name)).all()

def search_books(
    session: Session,
    title: Optional[str] = None,
    author_name: Optional[str] = None,
    isbn: Optional[str] = None,
    publication_year: Optional[int] = None,
    is_electronic: Optional[bool] = None,
    language_id: Optional[int] = None
) -> List[Book]:
    """Поиск книг по параметрам"""
    query = select(Book)
    
    if title:
        query = query.where(
            (Book.main_title.ilike(f"%{title}%")) |
            (Book.parallel_title.ilike(f"%{title}%")) |
            (Book.additional_title.ilike(f"%{title}%"))
        )
    
    if author_name:
        # Подзапрос для поиска по авторам
        author_subquery = select(BookAuthor.book_id).join(Author).where(
            (Author.last_name.ilike(f"%{author_name}%")) |
            (Author.first_name.ilike(f"%{author_name}%"))
        )
        query = query.where(Book.id.in_(author_subquery))
    
    if isbn:
        query = query.where(Book.isbn.ilike(f"%{isbn}%"))
    if publication_year:
        query = query.where(Book.publication_year == publication_year)
    if is_electronic is not None:
        query = query.where(Book.is_electronic == is_electronic)
    if language_id:
        query = query.where(Book.language_id == language_id)
    
    return session.exec(query.order_by(Book.main_title)).all()


def get_author_books_with_counts(session: Session, author_id: int) -> dict:
    """Получить все книги автора с количеством экземпляров"""
    from sqlmodel import select, func, case
    
    # Получаем автора
    author = get_author_by_id(session, author_id)
    if not author:
        return {"error": "Автор не найден"}
    
    # Получаем все книги автора с количеством экземпляров
    query = (
        select(
            Book.id,
            Book.main_title,
            Book.isbn,
            Book.publication_year,
            func.count(BookCopy.id).label("copies_count"),
            func.sum(
                case((BookCopy.current_status_id == 1, 1), else_=0)
            ).label("available_copies")
        )
        .join(BookAuthor, Book.id == BookAuthor.book_id)
        .join(BookCopy, Book.id == BookCopy.book_id, isouter=True)
        .where(BookAuthor.author_id == author_id)
        .group_by(Book.id, Book.main_title, Book.isbn, Book.publication_year)
        .order_by(Book.main_title)
    )
    
    books_with_counts = session.exec(query).all()
    
    # Преобразуем результат
    books = []
    for book in books_with_counts:
        books.append({
            "book_id": book.id,
            "title": book.main_title,
            "isbn": book.isbn,
            "publication_year": book.publication_year,
            "total_copies": book.copies_count or 0,
            "available_copies": book.available_copies or 0,
            "loaned_copies": (book.copies_count or 0) - (book.available_copies or 0)
        })
    
    # Общая статистика
    total_copies = sum(b["total_copies"] for b in books)
    available_copies = sum(b["available_copies"] for b in books)
    
    return {
        "author": {
            "id": author.id,
            "name": f"{author.last_name} {author.first_name or ''} {author.middle_name or ''}".strip(),
            "birth_year": author.birth_year,
            "death_year": author.death_year
        },
        "books_count": len(books),
        "total_copies": total_copies,
        "available_copies": available_copies,
        "books": books
    }