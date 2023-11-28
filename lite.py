from sqlalchemy import create_engine
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)

engine = create_engine("sqlite+pysqlite:///sample.db", echo=False)
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'Aniket'"))
    print(result.all())