import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale


DSN = "postgresql://postgres:13425Wertg@localhost:5432/DriverBD"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind = engine)
session = Session()

id_publisher = int(input('Введите id автора: '))

sales = session.query(
        Book.title,
        Shop.name,
        Sale.price,
        Sale.data_sale
    ).select_from(Publisher)\
     .join(Book, Publisher.id == Book.id_publisher)\
     .join(Stock, Book.id == Stock.id_book)\
     .join(Shop, Stock.id_shop == Shop.id)\
     .join(Sale, Stock.id == Sale.id_stock)\
     .filter(Publisher.id == id_publisher)\
     .order_by(Sale.data_sale.desc())\
     .all()


for title, shop, price, date in sales:
        print(f"{title: <20} | {shop: <10} | {price: <4} | {date.strftime('%d-%m-%Y')}")
