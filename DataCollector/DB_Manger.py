from django.db import connection


class DB_Manager:
    """
    A class to manage database operations for fine-tuning data.
    """

    @staticmethod
    def insert_data_to_finetune_database(prev_text, cur_text, mappings):
        """
        Insert data into the ChatGPT4o_Finetune_Data table.
        If a row with the same prev_text and cur_text exists, it updates the mappings instead.

        :param prev_text: The previous text (str)
        :param cur_text: The current text (str)
        :param mappings: A list of mappings (list of str)
        """
        # 将mappings列表转换为逗号分隔的字符串
        mapping_data = ','.join(mappings)

        # 查询是否存在相同的prev_text和cur_text
        select_query = """
        SELECT COUNT(*) FROM ChatGPT4o_Finetune_Data WHERE PREVIOUS_TEXT = %s AND CURRENT_TEXT = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(select_query, (prev_text, cur_text))
            result = cursor.fetchone()

            if result[0] > 0:  # 如果存在匹配的行
                # 如果存在，则更新映射数据
                DB_Manager.update_data_in_finetune_database(prev_text, cur_text, mappings)
            else:
                # 如果不存在，则插入新数据
                insert_query = """
                INSERT INTO ChatGPT4o_Finetune_Data (PREVIOUS_TEXT, CURRENT_TEXT, MAPPING_DATA)
                VALUES (%s, %s, %s)
                """
                try:
                    cursor.execute(insert_query, (prev_text, cur_text, mapping_data))
                    connection.commit()
                    print("Data inserted successfully.")
                except Exception as e:
                    connection.rollback()
                    print(f"Error inserting data: {e}")

    @staticmethod
    def update_data_in_finetune_database(prev_text, cur_text, new_mappings):
        """
        Update the mappings in the ChatGPT4o_Finetune_Data table for the specified prev_text and cur_text.

        :param prev_text: The previous text (str)
        :param cur_text: The current text (str)
        :param new_mappings: A new list of mappings (list of str)
        """
        # 将新的mappings列表转换为逗号分隔的字符串
        new_mapping_data = ','.join(new_mappings)

        # 更新SQL语句
        update_query = """
        UPDATE ChatGPT4o_Finetune_Data 
        SET MAPPING_DATA = %s 
        WHERE PREVIOUS_TEXT = %s AND CURRENT_TEXT = %s
        """

        with connection.cursor() as cursor:
            try:
                cursor.execute(update_query, (new_mapping_data, prev_text, cur_text))
                connection.commit()
                print("Data updated successfully.")
            except Exception as e:
                connection.rollback()
                print(f"Error updating data: {e}")
