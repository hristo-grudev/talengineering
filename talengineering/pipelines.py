import sqlite3


class TalengineeringPipeline:
    conn = sqlite3.connect('talengineering.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `talengineering` (
                                                    title varchar(100),
                                                    description text,
                                                    lang text
                                                    )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        language = item['language'][0]

        self.cursor.execute(f"""select * from talengineering where title = '{title}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `talengineering`
                                                (`title`, `description`, `lang`)
                                                values (?, ?, ?)""", (title, description, language))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
