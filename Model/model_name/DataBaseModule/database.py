import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import traceback
from typing import Optional, List, Dict, Any, Tuple


load_dotenv(dotenv_path=r".env")


class DataBaseModule:
    def __init__(self):
        """
        Método de inicialização da classe.
        """
        self.sql_alchemy = os.environ.get("SQLALCHEMY")
        self.connection = ""
        self.engine = ""

    def connect(self):
        """
        Método de conexão com o banco de dados.
        """
        try:
            self.engine = create_engine(self.sql_alchemy)
            self.connection = self.engine.connect()
            print("Conexão com banco de dados estabelecida com sucesso!")
        except:
            print("Falha ao criar conexão com banco de dados.")

    def disconnect(self):
        """
        Método de desconexão com o banco de dados.
        """
        if self.connection != '':
            try:
                self.connection.close()
                self.connection = ''
                print('Conexão com o banco de dados encerrada com sucesso!')
            except:
                print('Falha ao encerrar a conexão com o banco de dados.')
        else:
            print('Conexão não estabelecida, não é necessário desconectar.')

    def create_schema(self, name: str):
        """
        Cria um esquema no banco de dados.

        Args:
            name: Nome do esquema.
        """
        if self.connection != "":
            try:
                self.connection.execute(f"CREATE SCHEMA IF NOT EXISTS {name}")
                print("Esquema criado com sucesso!")
            except:
                print("Falha ao criar o esquema.")
        else:
            print("Conexão não estabelecida, conecte-se ao banco de dados.")

    def drop_schema(self, name: str):
        """
        Remove um esquema do banco de dados.

        Args:
            name: Nome do esquema.
        """
        if self.connection != "":
            try:
                self.connection.execute(f"DROP SCHEMA IF EXISTS {name} CASCADE")
                print("Esquema removido com sucesso!")
            except:
                print("Falha ao remover o esquema.")
        else:
            print("Conexão não estabelecida, conecte-se ao banco de dados.")

    def create_table(self, schema_name: str, table_name: str, columns: list):
        """
        Cria uma nova tabela no esquema especificado.

        Args:
            schema_name: Nome do esquema.
            table_name: Nome da tabela.
            columns: Lista de colunas da tabela, adicionando os tipos das colunas. 
                Exemplos:   "id INTEGER PRIMARY KEY",
                            "nome VARCHAR(50)",
                            "idade INTEGER"
        """
        if self.connection != "":
            try:
                column_str = ", ".join(columns)
                query = f"CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} ({column_str})"
                self.connection.execute(query)
                print(f"Tabela {schema_name}.{table_name} criada com sucesso!")
            except:
                print(f"Falha ao criar a tabela {schema_name}.{table_name}.")
        else:
            print("Conexão não estabelecida, conecte-se ao banco de dados.")

    def drop_table(self, schema_name: str, table_name: str):
        """
        Remove uma tabela do esquema especificado.

        Args:
            schema_name: Nome do esquema.
            table_name: Nome da tabela.
        """
        if self.connection != "":
            try:
                query = f"DROP TABLE IF EXISTS {schema_name}.{table_name}"
                self.connection.execute(query)
                print(f"Tabela {schema_name}.{table_name} removida com sucesso!")
            except:
                print(f"Falha ao remover a tabela {schema_name}.{table_name}.")
        else:
            print("Conexão não estabelecida, conecte-se ao banco de dados.")

    def truncate_table(self, schema_name: str, table_name: str):
        """
        Exclui todas as linhas de uma tabela.

        Args:
            schema_name: Nome do esquema.
            table_name: Nome da tabela.
        """
        if self.connection != '':
            try:
                query = f"TRUNCATE TABLE {schema_name}.{table_name}"
                self.connection.execute(query)
                print(f'Tabela {schema_name}.{table_name} truncada com sucesso!')
            except:
                print(f'Falha ao truncar a tabela {schema_name}.{table_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def create_view(self, view_name: str, query: str):
        """
        Cria uma view.

        Args:
            view_name: Nome da view.
            query: Consulta SQL da view.
        """
        if self.connection != '':
            try:
                self.connection.execute(f"CREATE VIEW {view_name} AS {query}")
                print(f'View {view_name} criada com sucesso!')
            except:
                print(f'Falha ao criar a view {view_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def drop_view(self, view_name: str):
        """
        Remove uma view.

        Args:
            view_name: Nome da view.
        """
        if self.connection != '':
            try:
                self.connection.execute(f"DROP VIEW IF EXISTS {view_name}")
                print(f'View {view_name} removida com sucesso!')
            except:
                print(f'Falha ao remover a view {view_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def create_materialized_view(self, view_name: str, query: str):
        """
        Cria uma view materializada.

        Args:
            view_name: Nome da view materializada.
            query: Consulta SQL da view materializada.
        """
        if self.connection != '':
            try:
                self.connection.execute(f"CREATE MATERIALIZED VIEW {view_name} AS {query}")
                print(f'View materializada {view_name} criada com sucesso!')
            except Exception as e:
                traceback.print_exc()
                print(f'Falha ao criar a view materializada {view_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def refresh_materialized_view(self, schema_name: str, table_name: str):
        """
        Atualiza uma view materializada.

        Args:
            schema_name: Nome do esquema.
            table_name: Nome da tabela (view materializada).
        """
        if self.connection != '':
            try:
                query = f"REFRESH MATERIALIZED VIEW {schema_name}.{table_name}"
                self.connection.execute(query)
                print(f'Tabela {schema_name}.{table_name} atualizada com sucesso!')
            except:
                print(f'Falha ao atualizar a tabela {schema_name}.{table_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def drop_materialized_view(self, schema_name: str, table_name: str):
        """
        Remove uma view materializada.

        Args:
            schema_name: Nome do esquema.
            table_name: Nome da tabela (view materializada).
        """
        if self.connection != '':
            try:
                self.connection.execute(f"DROP MATERIALIZED VIEW IF EXISTS {schema_name}.{table_name}")
                print(f'View materializada {schema_name}.{table_name} removida com sucesso!')
            except:
                print(f'Falha ao remover a view materializada {schema_name}.{table_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def add_data_to_table(self, schema_name: str, table_name: str, data: dict):
        """
        Adiciona dados a uma tabela.

        Args:
            schema_name: Nome do esquema.
            table_name: Nome da tabela.
            data: Dicionário contendo os dados a serem inseridos na tabela.
        """
        if self.connection != '':
            try:
                columns = ', '.join(data.keys())
                values = ', '.join([f"'{value}'" for value in data.values()])
                query = f"INSERT INTO {schema_name}.{table_name} ({columns}) VALUES ({values})"
                self.connection.execute(query)
                print(f'Dados adicionados à tabela {schema_name}.{table_name} com sucesso!')
            except:
                print(f'Falha ao adicionar dados à tabela {schema_name}.{table_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def remove_data_from_table(self, schema_name: str, table_name: str, condition: str):
        """
        Remove dados de uma tabela.

        Args:
            schema_name: Nome do esquema.
            table_name: Nome da tabela.
            condition: Condição para filtrar os dados a serem removidos.
        """
        if self.connection != '':
            try:
                query = f"DELETE FROM {schema_name}.{table_name} WHERE {condition}"
                self.connection.execute(query)
                print(f'Dados removidos da tabela {schema_name}.{table_name} com sucesso!')
            except:
                print(f'Falha ao remover dados da tabela {schema_name}.{table_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def update_data_in_table(self, table_name: str, filters: dict, new_data: dict):
        """
        Atualiza um dado na tabela.

        Args:
            table_name: Nome da tabela.
            filters: Dicionário contendo os filtros para a cláusula WHERE.
            new_data: Dicionário contendo os novos dados a serem atualizados.
        """
        if self.connection != '':
            try:
                # Constrói a cláusula WHERE com base nos filtros
                where_clause = ' AND '.join([f"{key} = '{value}'" for key, value in filters.items()])
                # Constrói a cláusula SET com base nos novos dados
                set_clause = ', '.join([f"{key} = '{value}'" for key, value in new_data.items()])
                query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
                self.connection.execute(query)
                print(f'Dados atualizados na tabela {table_name} com sucesso!')
            except:
                print(f'Falha ao atualizar dados na tabela {table_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

    def select_from_table(self, table_name: str, columns: Optional[List[str]] = None, filters: Optional[Dict[str, Any]] = None, order_by: Optional[str] = None) -> List[Tuple]:
        """
        Seleciona dados de uma tabela.

        Args:
            table_name: Nome da tabela.
            columns: Lista de colunas a serem selecionadas. Se não especificado, serão selecionadas todas as colunas.
            filters: Dicionário contendo os filtros para a cláusula WHERE. Cada chave representa o nome da coluna e o valor representa o valor a ser filtrado.
            order_by: String contendo o campo e a classificação para ordenação. Exemplo: 'id ASC'
        Returns:
            Uma lista de tuplas contendo os dados selecionados.
        """
        if self.connection != '':
            try:
                select_columns = '*' if columns is None else ', '.join(columns)
                where_clause = '' if filters is None else 'WHERE ' + ' AND '.join([f"{key} = '{value}'" for key, value in filters.items()])
                query = f"SELECT {select_columns} FROM {table_name} {where_clause} ORDER BY {order_by}"
                result = self.connection.execute(query)
                return result.fetchall()
            except:
                print(f'Falha ao buscar dados na tabela {table_name}.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')
            
    def execute_query(self, query: str):
        """
        Executa uma consulta SQL.

        Args:
            query: Consulta SQL a ser executada.
        """
        if self.connection != '':
            try:
                self.connection.execute(query)
                print('Consulta executada com sucesso!')
            except:
                print('Falha ao executar a consulta.')
        else:
            print('Conexão não estabelecida, conecte-se ao banco de dados.')

