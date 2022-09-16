from models import User
from mixins import JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin

class CRUD(JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    _file_name = 'db.json'
    _model = User


crud = CRUD()
# crud.create()
# crud.list()
# crud.delete()
# crud.get_user_by_id()
# crud.get_db_content()
# crud.update()

