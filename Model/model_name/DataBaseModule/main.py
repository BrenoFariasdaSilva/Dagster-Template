from extraction import Extraction
from Model.model_name.DataBaseModule.database import DataBaseModule

db = DataBaseModule()
db.connect()

# Criar um novo esquema

# Criar uma nova tabela no esquema
schema_name = "teste"
table_name = "animais"
columns = [
    "id INTEGER PRIMARY KEY",
    "nome VARCHAR(50)",
    "idade INTEGER"
]

# db.create_schema()

# db.create_table(schema_name, table_name, columns)
# db.create_table()

# data = {'id':3, "nome": "Zelda", "idade": 7}
# db.add_data_to_table(schema_name, table_name, data)

# view_name = "teste.minhaview"
# query = "SELECT * FROM teste.animais WHERE nome = 'Zelda'"
# db.create_view(view_name, query)
# db.drop_view(view_name)

# view_name = "teste.minhaviewmaterializada"
# query = "SELECT * FROM teste.animais WHERE nome = 'Zelda'"
# db.create_materialized_view(view_name, query)

# db.refresh_materialized_view('public', 'minhaviewmaterializada')

# condition = "id = 1"
# db.remove_data_from_table(schema_name, table_name, condition)


# db.truncate_table(schema_name, table_name)
# db.drop_table(schema_name, table_name)
# db.drop_schema("novoschema")

table_name = "teste.animais"

filters = {"nome": "Zelda"}

result = db.select_from_table(table_name, filters=filters, order_by='id ASC')

for row in result:
    print(row)

db.disconnect()

# ext = Extraction("01/01/2018", "31/12/2023"
# , "v1"
# )
# print(ext.get_info("pessoas", True))
# exercicios = ext.get_info("exercicios")
# print(exercicios)
# print(ext.get_iterated_info(exercicios,"elementosdegastosdoexercicio"))
# print(ext.get_iterated_info(exercicios,"orgaosdoexercicio"))
