from pyorientdb import OrientDB

class OrientCrud:
    def __init__(self) -> None:
        
        self.client = OrientDB("localhost", 2424)
        session_id = self.client.connect("root", "rootpwd")




    def create_database(self, db_name):
        if not self.client.db_exists(db_name):
            print("db exist")
            self.client.db_create(db_name)

    def delete_database(self, db_name):
        self.client.db_drop(db_name)


    def create_table(self, db_name, table_name):
        self.client.db_open(db_name, "root", "rootpwd")


        class_exists = self.client.query(f"SELECT FROM (SELECT expand(classes) FROM metadata:schema) WHERE name = '{table_name}'")
        
        if class_exists:
            print(f"Class 'Person' already exists in database '{db_name}'.")
        else:
            # ایجاد کلاس جدید در صورت عدم وجود
            cluster = self.client.command(f"CREATE CLASS {table_name} EXTENDS V")
            self.client.command(f"CREATE PROPERTY {table_name}.name STRING")
            self.client.command(f"CREATE PROPERTY {table_name}.price INTEGER")
            print(f"Class '{table_name}' created in database '{db_name}'.")


        # print(f"Table 'Person' created in database '{db_name}'.")

        # # client.command("CREATE CLASS Person EXTENDS V")
        # # print("class create")


    def post_table(self):
        self.client.db_open("javad", "root", "rootpwd")
        print(self.client.command("insert into product set name = 'samsung', price = '3000' "))


    def get_list_db(self):
        print(self.client.db_list())

    def get_row(self):

        self.client.db_open("javad", "root", "rootpwd")

        result = self.client.query("select * from product")
        for rec in result:
            print(rec.oRecordData)


a = OrientCrud()    
# a.create_database("javad")
# a.get_list_db()
# # # a.delete_database("javad1")
# a.create_table("javad", "product")
# a.post_table()
a.get_row()

# # # print(client.db_list())




            