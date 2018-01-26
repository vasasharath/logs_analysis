#! /usr/bin/env python3

import psycopg2

DBNAME = "news"


def get_popular_articles():
    # Connecting to news database
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # executing the query on database
    c.execute("""
	           SELECT articles.title,COUNT(*) as num
               FROM articles,log
               WHERE log.path like concat('%article%',articles.slug)
               GROUP BY 1
               ORDER BY 2 DESC
               LIMIT 3;
               """)
    rows = c.fetchall()
    # closing database connection
    db.close()
    print('\nThe 3 most popular articles of all time are\n')
    # loop through the result and display each row
    for article in rows:
        print(article[0] + ' — ' + str(article[1]) + ' views')


def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
                SELECT authors.name, COUNT(*) AS num
                FROM authors,articles,log
                WHERE authors.id = articles.author
                AND log.path like concat('/article/%', articles.slug)
                GROUP BY 1
                ORDER BY 2 DESC
                LIMIT 3;
              """)
    rows = c.fetchall()
    db.close()
    print('\n\nThe most popular article authors of all time are\n')
    for author in rows:
        print(author[0] + ' — ' + str(author[1]) + ' views')


def get_error_day():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
               SELECT *
               FROM error_log
               WHERE Error_percentage > 1;
              """)
    rows = c.fetchall()
    db.close()
    print('\n\nDays with more than 1% of request that lead to an error\n')
    for result in rows:
        print(str(result[0]) + ' — ' + str(result[1]) + ' % ')


get_popular_articles()
get_popular_authors()
get_error_day()
