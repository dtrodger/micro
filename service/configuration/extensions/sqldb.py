import re
from flask_sqlalchemy import SQLAlchemy


class SQLDB(SQLAlchemy):

    def drop_everything(self):
        from sqlalchemy.engine import reflection
        from sqlalchemy.schema import (
            MetaData,
            Table,
            DropTable,
            ForeignKeyConstraint,
            DropConstraint,
            )

        conn = self.engine.connect()
        trans = conn.begin()
        inspector = reflection.Inspector.from_engine(self.engine)
        metadata = MetaData()

        tbs = []
        all_fks = []

        for table_name in inspector.get_table_names():
            fks = []
            for fk in inspector.get_foreign_keys(table_name):
                if not fk['name']:
                    continue
                fks.append(
                    ForeignKeyConstraint((), (), name=fk['name'])
                    )

            pattern = re.compile('sqlite')
            match = pattern.search(table_name)
            if not match:
                t = Table(table_name,metadata,*fks)
                tbs.append(t)
                all_fks.extend(fks)

        for fkc in all_fks:
            conn.execute(DropConstraint(fkc))

        for table in tbs:
            conn.execute(DropTable(table))

        trans.commit()

sqldb = SQLDB()
