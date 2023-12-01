
# # import mysql.connector
# from itemadapter import ItemAdapter
# import sqlite3

# class SqliteDemoPipeline:

#     def __init__(self):
#         pass

#     def process_item(self, item, spider):
#         return item
# # class MysqlDemoPipeline:
    
# #     def __init__(self):
# #         self.conn = mysql.connector.connect(
# #             host='localhost',
# #             user='root',
# #             password='Codmast3er13$',
# #             database='amazon'
# #         )
# #         # Create cursor, used to execute commands
# #         self.cur = self.conn.cursor()
    
# #         # Create quotes table if none exists
# #         self.cur.execute("""
# #             CREATE TABLE IF NOT EXISTS amazon(
# #                 id int NOT NULL auto_increment, 
# #                 content text,
# #                 tags text,
# #                 author VARCHAR(255),
# #                 PRIMARY KEY (id)
# #             )
# #         """)

# #     def process_item(self, item, spider):
# #         # Define insert statement
# #         self.cur.execute("""
# #             INSERT INTO amazon (name, author, num_reviews, description, reading_age, main_image, url)
# #             VALUES (%s, %s, %s, %s, %s, %s, %s)
# #         """, (
# #             item["name"],
# #             item["author"],
# #             item["num_reviews"],
# #             item["description"],
# #             item["reading_age"],
# #             item["main_image"],
# #             item["url"],
# #         ))

# #         # Execute insert of data into the database
# #         self.conn.commit()
        
# #     def close_spider(self, spider):
# #         # Close cursor & connection to the database 
# #         self.cur.close()
# #         self.conn.close()