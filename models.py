from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime

# ==================== СПРАВОЧНИКИ (ГОСТ 7.60-2003) ====================

class EditionType(SQLModel, table=True):
    """Типы изданий по ГОСТ 7.60-2003"""
    __tablename__ = "edition_types"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(max_length=20, unique=True)           # Код типа
    name: str = Field(max_length=100)                      # Название типа
    description: Optional[str] = Field(default=None)       # Описание
    gost_reference: Optional[str] = Field(default=None, max_length=50)  # Ссылка на ГОСТ

class Language(SQLModel, table=True):
    """Языки изданий"""
    __tablename__ = "languages"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    iso_code: str = Field(max_length=20, unique=True)      # ISO 639 код
    name: str = Field(max_length=50)                       # Название языка

class Country(SQLModel, table=True):
    """Страны (ISO 3166)"""
    __tablename__ = "countries"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    iso_code: str = Field(max_length=20, unique=True)      # ISO 3166 код
    name: str = Field(max_length=100)                      # Название страны

class City(SQLModel, table=True):
    """Города"""
    __tablename__ = "cities"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)                      # Название города
    country_id: int = Field(foreign_key="Ichetovkina.countries.id")  # ID страны

class Publisher(SQLModel, table=True):
    """Издательства"""
    __tablename__ = "publishers"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=200)                      # Название издательства
    city_id: Optional[int] = Field(foreign_key="Ichetovkina.cities.id", default=None)  # Город
    address: Optional[str] = Field(default=None)           # Адрес
    website: Optional[str] = Field(default=None, max_length=200)  # Веб-сайт

class ReaderCategory(SQLModel, table=True):
    """Категории читателей (ГОСТ Р 7.0.20-2014)"""
    __tablename__ = "reader_categories"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(max_length=20, unique=True)          # Код категории
    name: str = Field(max_length=100)                      # Название
    loan_limit: int = Field(default=5)                     # Макс. количество книг
    loan_period: int = Field(default=30)                   # Срок выдачи в днях
    has_remote_access: bool = Field(default=False)         # Доступ к удаленным ресурсам

class BookStatus(SQLModel, table=True):
    """Статусы экземпляров книг"""
    __tablename__ = "book_statuses"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(max_length=20, unique=True)          # Код статуса
    name: str = Field(max_length=50)                       # Название статуса

class LoanStatus(SQLModel, table=True):
    """Статусы выдачи книг"""
    __tablename__ = "loan_statuses"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(max_length=20, unique=True)          # Код статуса
    name: str = Field(max_length=50)                       # Название статуса

class OperationType(SQLModel, table=True):
    """Типы финансовых операций"""
    __tablename__ = "operation_types"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(max_length=20, unique=True)          # Код операции
    name: str = Field(max_length=100)                      # Название операции

# ==================== ОСНОВНЫЕ ТАБЛИЦЫ ====================

class Reader(SQLModel, table=True):
    """Читатели библиотеки"""
    __tablename__ = "readers"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    # ЛИЧНЫЕ ДАННЫЕ
    last_name: str = Field(max_length=100)                 # Фамилия
    first_name: str = Field(max_length=100)                # Имя
    middle_name: Optional[str] = Field(max_length=100, default=None)  # Отчество
    birth_date: Optional[date] = Field(default=None)       # Дата рождения
    
    # КАТЕГОРИЯ
    category_id: int = Field(foreign_key="Ichetovkina.reader_categories.id")  # Категория читателя
    
    # КОНТАКТЫ
    phone: Optional[str] = Field(max_length=20, default=None)  # Телефон
    email: Optional[str] = Field(max_length=100, default=None)  # Email
    address: Optional[str] = Field(default=None)           # Адрес
    
    # ДОКУМЕНТЫ
    document_type: Optional[str] = Field(max_length=50, default=None)  # Тип документа
    document_number: Optional[str] = Field(max_length=50, default=None)  # Номер документа
    document_issued_by: Optional[str] = Field(default=None)  # Кем выдан
    document_issued_date: Optional[date] = Field(default=None)  # Дата выдачи
    
    # СТАТУС
    registration_date: date = Field(default_factory=date.today)  # Дата регистрации
    card_expiry_date: Optional[date] = Field(default=None)  # Срок действия карты
    is_active: bool = Field(default=True)                  # Активен ли читатель
    notes: Optional[str] = Field(default=None)             # Примечания
    
    # СИСТЕМНЫЕ ПОЛЯ
    created_at: datetime = Field(default_factory=datetime.now)  # Дата создания
    updated_at: Optional[datetime] = Field(default=None)   # Дата обновления

class Book(SQLModel, table=True):
    """Библиографические описания книг (ГОСТ 7.1-2003)"""
    __tablename__ = "books"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # БИБЛИОГРАФИЧЕСКОЕ ОПИСАНИЕ
    isbn: Optional[str] = Field(max_length=17, default=None)  # ISBN (ГОСТ 7.53-2001)
    udk: Optional[str] = Field(max_length=50, default=None)   # УДК
    bbk: Optional[str] = Field(max_length=50, default=None)   # ББК
    main_title: str = Field(max_length=500)                   # Основное заглавие
    parallel_title: Optional[str] = Field(max_length=500, default=None)  # Параллельное заглавие
    additional_title: Optional[str] = Field(max_length=500, default=None)  # Дополнительное заглавие
    
    # ИЗДАТЕЛЬСКАЯ ИНФОРМАЦИЯ
    publisher_id: Optional[int] = Field(foreign_key="Ichetovkina.publishers.id", default=None)  # Издательство
    publication_place: Optional[str] = Field(max_length=100, default=None)  # Место издания
    publication_year: Optional[int] = Field(default=None)     # Год издания
    
    # ФИЗИЧЕСКИЕ ХАРАКТЕРИСТИКИ
    edition_type_id: int = Field(foreign_key="Ichetovkina.edition_types.id")  # Тип издания
    language_id: Optional[int] = Field(foreign_key="Ichetovkina.languages.id", default=None)  # Язык
    volume_pages: Optional[int] = Field(default=None)         # Количество страниц
    volume_copies: int = Field(default=1)                     # Количество томов
    dimensions: Optional[str] = Field(max_length=50, default=None)  # Размеры
    weight: Optional[float] = Field(default=None)             # Вес
    
    # СОДЕРЖАНИЕ
    abstract: Optional[str] = Field(default=None)             # Аннотация
    keywords: Optional[str] = Field(default=None)             # Ключевые слова
    table_of_contents: Optional[str] = Field(default=None)    # Оглавление
    
    # ЭЛЕКТРОННЫЕ РЕСУРСЫ (ГОСТ 7.82-2001)
    is_electronic: bool = Field(default=False)                # Электронная версия
    electronic_format: Optional[str] = Field(max_length=50, default=None)  # Формат
    electronic_access_url: Optional[str] = Field(default=None)  # URL доступа
    electronic_file_size: Optional[int] = Field(default=None)  # Размер файла
    
    # СИСТЕМНЫЕ ПОЛЯ
    created_at: datetime = Field(default_factory=datetime.now)  # Дата создания
    updated_at: Optional[datetime] = Field(default=None)   # Дата обновления

class Author(SQLModel, table=True):
    """Авторы книг"""
    __tablename__ = "authors"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    last_name: str = Field(max_length=100)                 # Фамилия автора
    first_name: Optional[str] = Field(max_length=100, default=None)  # Имя автора
    middle_name: Optional[str] = Field(max_length=100, default=None)  # Отчество автора
    birth_year: Optional[int] = Field(default=None)        # Год рождения
    death_year: Optional[int] = Field(default=None)        # Год смерти
    biography: Optional[str] = Field(default=None)         # Биография

class BookAuthor(SQLModel, table=True):
    """Связь книг и авторов (многие-ко-многим)"""
    __tablename__ = "book_authors"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="Ichetovkina.books.id")        # ID книги
    author_id: int = Field(foreign_key="Ichetovkina.authors.id")    # ID автора
    author_role: str = Field(max_length=50, default="author")       # Роль (автор, редактор и т.д.)
    author_order: int = Field(default=1, ge=1)                      # Порядок авторов

class BookCopy(SQLModel, table=True):
    """Физические экземпляры книг"""
    __tablename__ = "book_copies"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="Ichetovkina.books.id")        # ID книги
    inventory_number: str = Field(max_length=50, unique=True)       # Инвентарный номер
    barcode: Optional[str] = Field(max_length=100, default=None)    # Штрих-код
    copy_number: int = Field(default=1, ge=1)                       # Номер экземпляра
    acquisition_date: date = Field(default_factory=date.today)      # Дата поступления
    acquisition_source: Optional[str] = Field(default=None, max_length=200)  # Источник поступления
    price: Optional[float] = Field(default=None)                    # Цена
    location: Optional[str] = Field(max_length=100, default=None)   # Место хранения
    current_status_id: int = Field(foreign_key="Ichetovkina.book_statuses.id", default=1)  # Текущий статус
    condition_notes: Optional[str] = Field(default=None)            # Заметки о состоянии
    write_off_date: Optional[date] = Field(default=None)            # Дата списания
    write_off_reason: Optional[str] = Field(default=None)           # Причина списания
    created_at: datetime = Field(default_factory=datetime.now)      # Дата создания

class Loan(SQLModel, table=True):
    """Выдачи книг читателям"""
    __tablename__ = "loans"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    # СВЯЗИ
    book_copy_id: int = Field(foreign_key="Ichetovkina.book_copies.id")  # ID экземпляра
    reader_id: int = Field(foreign_key="Ichetovkina.readers.id")         # ID читателя
    librarian_id: Optional[int] = Field(default=None)                    # ID библиотекаря
    
    # ДАТЫ
    loan_date: date = Field(default_factory=date.today)                  # Дата выдачи
    due_date: date                                                       # Плановая дата возврата
    return_date: Optional[date] = Field(default=None)                    # Фактическая дата возврата
    
    # СТАТУС
    status_id: int = Field(foreign_key="Ichetovkina.loan_statuses.id", default=1)  # Статус выдачи
    
    # ПРОДЛЕНИЯ
    renewal_count: int = Field(default=0, ge=0)                          # Количество продлений
    last_renewal_date: Optional[date] = Field(default=None)              # Дата последнего продления
    
    # ШТРАФЫ
    fine_amount: float = Field(default=0, ge=0)                          # Сумма штрафа
    fine_paid: bool = Field(default=False)                               # Штраф оплачен
    fine_payment_date: Optional[date] = Field(default=None)              # Дата оплаты штрафа
    
    # КОММЕНТАРИИ
    notes: Optional[str] = Field(default=None)                           # Примечания
    
    # СИСТЕМНЫЕ ПОЛЯ
    created_at: datetime = Field(default_factory=datetime.now)           # Дата создания
    updated_at: Optional[datetime] = Field(default=None)                 # Дата обновления

    def calculate_fine(self, fine_per_day: float = None, max_fine_days: int = None, max_fine: float = None) -> float:
        """Рассчитать штраф за просрочку"""
        from datetime import date
        
        # Параметры по умолчанию (можно переопределить)
        fine_per_day = fine_per_day or 10.0
        max_fine_days = max_fine_days or 30
        max_fine = max_fine or 300.0
        
        if self.return_date or not self.due_date:
            return 0.0
        
        today = date.today()
        if today <= self.due_date:
            return 0.0
        
        days_overdue = (today - self.due_date).days
        days_overdue = max(0, days_overdue - 3)  # Учитываем grace period
        days_overdue = min(days_overdue, max_fine_days)
        
        fine = days_overdue * fine_per_day
        return min(fine, max_fine)

class Payment(SQLModel, table=True):
    """Финансовые операции (платежи)"""
    __tablename__ = "payments"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    reader_id: int = Field(foreign_key="Ichetovkina.readers.id")         # ID читателя
    operation_type_id: int = Field(foreign_key="Ichetovkina.operation_types.id")  # Тип операции
    amount: float = Field(gt=0)                                          # Сумма
    payment_date: date = Field(default_factory=date.today)               # Дата платежа
    payment_method: Optional[str] = Field(max_length=50, default=None)   # Способ оплаты
    transaction_id: Optional[str] = Field(max_length=100, default=None)  # Номер транзакции
    description: Optional[str] = Field(default=None)                     # Описание
    related_loan_id: Optional[int] = Field(foreign_key="Ichetovkina.loans.id", default=None)  # Связанная выдача
    created_at: datetime = Field(default_factory=datetime.now)           # Дата создания

class Reservation(SQLModel, table=True):
    """Бронирования книг"""
    __tablename__ = "reservations"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="Ichetovkina.books.id")             # ID книги
    reader_id: int = Field(foreign_key="Ichetovkina.readers.id")         # ID читателя
    reservation_date: datetime = Field(default_factory=datetime.now)     # Дата бронирования
    expiration_date: Optional[datetime] = Field(default=None)            # Срок действия брони
    status: str = Field(max_length=20, default="active")                 # Статус брони
    priority: Optional[int] = Field(default=None)                        # Приоритет в очереди
    notes: Optional[str] = Field(default=None)                           # Примечания

# ==================== СТАТИСТИЧЕСКИЕ ТАБЛИЦЫ ====================

class Visit(SQLModel, table=True):
    """Статистика посещений"""
    __tablename__ = "visits"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    reader_id: Optional[int] = Field(foreign_key="Ichetovkina.readers.id", default=None)  # ID читателя
    visit_date: date = Field(default_factory=date.today)               # Дата посещения
    visit_time: datetime = Field(default_factory=datetime.now)         # Время посещения
    is_remote: bool = Field(default=False)                             # Удаленное посещение
    purpose: Optional[str] = Field(max_length=100, default=None)       # Цель посещения
    duration_minutes: Optional[int] = Field(default=None)              # Продолжительность в минутах
    created_at: datetime = Field(default_factory=datetime.now)         # Дата создания

class ReferenceRequest(SQLModel, table=True):
    """Статистика запросов"""
    __tablename__ = "reference_requests"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    reader_id: Optional[int] = Field(foreign_key="Ichetovkina.readers.id", default=None)  # ID читателя
    request_date: datetime = Field(default_factory=datetime.now)       # Дата запроса
    request_type: Optional[str] = Field(max_length=100, default=None)  # Тип запроса
    subject: Optional[str] = Field(max_length=500, default=None)       # Тема запроса
    complexity_level: Optional[str] = Field(max_length=50, default=None)  # Уровень сложности
    completion_time_minutes: Optional[int] = Field(default=None)       # Время выполнения
    is_completed: bool = Field(default=False)                          # Завершен ли запрос
    librarian_notes: Optional[str] = Field(default=None)               # Примечания библиотекаря

class DailyStatistic(SQLModel, table=True):
    """Ежедневная статистика (ГОСТ Р 7.0.20-2014)"""
    __tablename__ = "daily_statistics"
    __table_args__ = {'schema': 'Ichetovkina'}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    statistic_date: date = Field(unique=True)                          # Дата статистики
    
    # ПОСЕЩЕНИЯ
    total_visits: int = Field(default=0)                               # Всего посещений
    physical_visits: int = Field(default=0)                            # Физических посещений
    remote_visits: int = Field(default=0)                              # Удаленных посещений
    
    # ЧИТАТЕЛИ
    new_readers: int = Field(default=0)                                # Новых читателей
    active_readers: int = Field(default=0)                             # Активных читателей
    
    # ВЫДАЧИ
    total_loans: int = Field(default=0)                                # Всего выдач
    book_loans: int = Field(default=0)                                 # Выдач книг
    electronic_loans: int = Field(default=0)                           # Выдач электронных ресурсов
    overdue_loans: int = Field(default=0)                              # Просроченных выдач
    
    # ФОНД
    total_copies: int = Field(default=0)                               # Всего экземпляров
    new_copies: int = Field(default=0)                                 # Новых экземпляров
    written_off_copies: int = Field(default=0)                         # Списано экземпляров
    
    # ЗАПРОСЫ
    reference_requests: int = Field(default=0)                         # Справочных запросов
    complex_requests: int = Field(default=0)                           # Сложных запросов
    
    # СИСТЕМНЫЕ ПОЛЯ
    calculated_at: datetime = Field(default_factory=datetime.now)      # Дата расчета

# ==================== МОДЕЛИ ДЛЯ СОЗДАНИЯ ====================

class ReaderCreate(SQLModel):
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    birth_date: Optional[date] = None
    category_id: int
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    document_type: Optional[str] = None
    document_number: Optional[str] = None
    document_issued_by: Optional[str] = None
    document_issued_date: Optional[date] = None
    card_expiry_date: Optional[date] = None
    notes: Optional[str] = None

class BookCreate(SQLModel):
    main_title: str
    edition_type_id: int
    isbn: Optional[str] = None
    udk: Optional[str] = None
    bbk: Optional[str] = None
    parallel_title: Optional[str] = None
    additional_title: Optional[str] = None
    publisher_id: Optional[int] = None
    publication_place: Optional[str] = None
    publication_year: Optional[int] = None
    language_id: Optional[int] = None
    volume_pages: Optional[int] = None
    volume_copies: int = 1
    dimensions: Optional[str] = None
    weight: Optional[float] = None
    abstract: Optional[str] = None
    keywords: Optional[str] = None
    table_of_contents: Optional[str] = None
    is_electronic: bool = False
    electronic_format: Optional[str] = None
    electronic_access_url: Optional[str] = None
    electronic_file_size: Optional[int] = None

class AuthorCreate(SQLModel):
    last_name: str
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    biography: Optional[str] = None

class BookCopyCreate(SQLModel):
    book_id: int
    inventory_number: str
    barcode: Optional[str] = None
    copy_number: int = 1
    acquisition_date: date = Field(default_factory=date.today)
    acquisition_source: Optional[str] = None
    price: Optional[float] = None
    location: Optional[str] = None
    current_status_id: int = 1
    condition_notes: Optional[str] = None

class LoanCreate(SQLModel):
    book_copy_id: int
    reader_id: int
    librarian_id: Optional[int] = None
    loan_date: date = Field(default_factory=date.today)
    due_date: date
    notes: Optional[str] = None

class PaymentCreate(SQLModel):
    reader_id: int
    operation_type_id: int
    amount: float
    payment_date: date = Field(default_factory=date.today)
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None
    description: Optional[str] = None
    related_loan_id: Optional[int] = None

# ==================== МОДЕЛИ ДЛЯ ОБНОВЛЕНИЯ ====================

class ReaderUpdate(SQLModel):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_date: Optional[date] = None
    category_id: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    document_type: Optional[str] = None
    document_number: Optional[str] = None
    document_issued_by: Optional[str] = None
    document_issued_date: Optional[date] = None
    card_expiry_date: Optional[date] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None

class BookUpdate(SQLModel):
    main_title: Optional[str] = None
    edition_type_id: Optional[int] = None
    isbn: Optional[str] = None
    udk: Optional[str] = None
    bbk: Optional[str] = None
    parallel_title: Optional[str] = None
    additional_title: Optional[str] = None
    publisher_id: Optional[int] = None
    publication_place: Optional[str] = None
    publication_year: Optional[int] = None
    language_id: Optional[int] = None
    volume_pages: Optional[int] = None
    volume_copies: Optional[int] = None
    dimensions: Optional[str] = None
    weight: Optional[float] = None
    abstract: Optional[str] = None
    keywords: Optional[str] = None
    table_of_contents: Optional[str] = None
    is_electronic: Optional[bool] = None
    electronic_format: Optional[str] = None
    electronic_access_url: Optional[str] = None
    electronic_file_size: Optional[int] = None

class LoanUpdate(SQLModel):
    return_date: Optional[date] = None
    status_id: Optional[int] = None
    renewal_count: Optional[int] = None
    last_renewal_date: Optional[date] = None
    fine_amount: Optional[float] = None
    fine_paid: Optional[bool] = None
    fine_payment_date: Optional[date] = None
    notes: Optional[str] = None