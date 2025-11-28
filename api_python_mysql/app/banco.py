from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

usuario_banco = "root"
senha_banco = "root"
nome_banco = "fastapi_db"
porta_banco = "3307"
host_banco = "localhost"


URL_BD = f"mysql+pymysql://{usuario_banco}:{senha_banco}@{host_banco}:{porta_banco}/{nome_banco}"


ENGINE = create_engine(
    URL_BD,
    echo=True, # exibi os comando sql no terminal se for true
    pool_pre_ping=True
)


session = sessionmaker(autoflush=False, autocommit=False, bind=ENGINE)

BASE = declarative_base() #(pai de todos os modelos)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()