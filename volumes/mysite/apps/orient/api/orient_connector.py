from pyorientdb import OrientDB
from ..models import OrientHost

class OrientCrud:
    def __init__(self, host) -> None:
        orient = OrientHost.objects.get(id=host)
        self.host = orient.host
        self.port = orient.port
        self.user = orient.user
        self.password = orient.password
        
        self.client = OrientDB(self.host, int(self.port))
        session_id = self.client.connect(self.user, self.password)


    def create_database(self, db_name):

        if not self.client.db_exists(db_name):
            self.client.db_create(db_name)
            return f"database {db_name} created."
        else:

            return "exist"

    def delete_database(self, db_name):
        self.client.db_drop(db_name)
        return f"delete database {db_name}."


    def create_table(self, db_name, table_name):
        self.client.db_open(db_name, self.user, self.password)


        class_exists = self.client.query(f"SELECT FROM (SELECT expand(classes) FROM metadata:schema) WHERE name = '{table_name}'")
        
        if class_exists:
            return f"Class 'Person' already exists in database '{db_name}'."
        else:
            # ایجاد کلاس جدید در صورت عدم وجود
            cluster = self.client.command(f"CREATE CLASS {table_name} EXTENDS V")
            self.client.command(f"CREATE PROPERTY {table_name}.name STRING")
            self.client.command(f"CREATE PROPERTY {table_name}.price INTEGER")
            return f"Class '{table_name}' created in database '{db_name}'."




    def insert_table(self, db_name,table_name ,name, price):
        self.client.db_open(db_name, "root", "rootpwd")
        self.client.command(f"insert into {table_name} set name = '{name}', price = {price} ")

        return f"insert into {table_name} set name = {name}, price = {price}"


    def get_row(self, db_name, table_name):
        # print(self.client.db_list())
        self.client.db_open(db_name, "root", "rootpwd")

        result = self.client.query(f"select * from {table_name}")
        rows = []
        for rec in result:
            rows.append(rec.oRecordData)
        return rows

    def table_list(self):
        print(self.client.db_list())



    def update(self, table_name, name, new_name, db_name):
        self.client.db_open(db_name, "root", "rootpwd")
        query = f"UPDATE {table_name} SET name = '{new_name}' WHERE name = '{name}'"
        self.client.command(query)
        return query
    

    def get_classes(self, db_name):
        # اجرای دستور SQL برای دریافت لیست کلاس‌ها
        self.client.db_open(db_name, "root", "rootpwd")
        query = "SELECT name FROM (SELECT expand(classes) FROM metadata:schema)"
        result = self.client.command(query)
        
        # چاپ یا برگرداندن لیست کلاس‌ها
        classes = [record.oRecordData['name'] for record in result]
        return classes



    def drop_table(self,db_name ,table_name):
        self.client.db_open(db_name, "root", "rootpwd")
        print("after opne db")
        query = f"DROP CLASS {table_name} UNSAFE"
        self.client.command(query)
        return f"Table '{table_name}' has been dropped."
    
# db_name = "salam1"
# if not client.db_exists(db_name):
#     print("db exist")
#     client.db_create( db_name)

# a = OrientCrud()    
# # a.create_database("shop")
# # # a.delete_database("javad1")
# a.create_table("javad", "product")
# a.post_table()
# a.get_row()

# # print(client.db_list())




            