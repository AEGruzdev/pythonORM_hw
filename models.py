import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


class Publisher(Base):
    tablename = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)



class Book(Base):
    tablename = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable = False)

    publisher = relationship(Publisher, backref="book")



class Shop(Base):
    tablename = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)



class Stock(Base):
    tablename = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable = False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable = False)
    count = sq.Column(sq.Integer, nullable = False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")



class Sale(Base):
    tablename = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable = False)
    data_sale = sq.Column(sq.Date, nullable = False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable = False)
    count = sq.Column(sq.Integer, nullable = False)

    stock = relationship(Stock, backref="sale")



def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
