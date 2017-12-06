from project.configuration.extensions import sqldb


class BasicCRUD(object):

    @classmethod
    def commit(cls):
        try:
            sqldb.session.commit()
        except Exception as e:
            sqldb.session.rollback()
            raise e

    def update(self, obj):
        sqldb.session.add(obj)
        self.commit()

    def get(self, **kwargs):
        return self.get_all(**kwargs).first()

    def get_or_404(self, **kwargs):
        return self.get_all(**kwargs).first_or_404()

    def get_all(self, **kwargs):
        return self.current_table.query.filter_by(**kwargs)

    def get_all_order_by(self, order_by, **kwargs):
        return self.current_table.query.filter_by(**kwargs).order_by(order_by)

    def exists(self, **kwargs):
        return self.get(**kwargs) is not None

    def delete(self, **kwargs):
        self.current_table.query.filter_by(**kwargs).delete()
        self.commit()
