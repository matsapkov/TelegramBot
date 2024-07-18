from pythonProject.config import host, user, password, db_name
import psycopg2
class DB:

    def __init__(self):
        pass

    def get_random_compliment(self):

        connection = None
        cursor = None

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()

            cursor.execute(
                'SELECT string from compliments_ order by RANDOM() LIMIT 1;'
            )

            compliment = cursor.fetchone()

            return compliment
            # print(f'{cursor.fetchone()}')

        except Exception as ex:
            print('[INFO] Error while working with PostgreSQL', ex)
        finally:
            if connection:
                connection.close()
                cursor.close()
                print('PostgreSQL connection closed')

    def put_user_in_db(self, ChatID, nickname, name):
        connection = None
        cursor = None

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()

            query = 'INSERT INTO users (chatid, nickname, name) VALUES (%s, %s, %s);'
            values = (ChatID, nickname, name)

            print(f'Executing query: {query} with values {values}')

            cursor.execute(query, values)

            connection.commit()
            print("User inserted successfully")
        except Exception as ex:
            print('[INFO] Error while working with PostgreSQL', ex)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print('PostgreSQL connection closed')

    def get_chatID(self):

        connection = None
        cursor = None

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()

            cursor.execute(
                'SELECT chatid from users;'
            )

            chat_id = cursor.fetchall()
            set_chat_id = set(chat_id)
            print(set_chat_id)
            return set_chat_id

        except Exception as ex:
            print('[INFO] Error while working with PostgreSQL', ex)
        finally:
            if connection:
                connection.close()
                cursor.close()
                print('PostgreSQL connection closed')