# -*- coding: utf-8 -*-
import Pyro4
import MySQLdb

class PyroServer(object):
    def add_opinion(self, book_id,opinion,user_name):
        sql = "INSERT INTO books_opinion (book_id,opinion,user_name)" \
           "VALUES (%s,%s,%s)"
        try:
            db = MySQLdb.connect("db4free.net", "ksiegarnia", "tas_projekt", "tasksiegarnia")
            cursor = db.cursor()
            cursor.execute(sql,(book_id,opinion,user_name))
            db.commit()
            print "Dodano"
            return 1  
        except:
            print "Problem z dodaniem"
            return 0        
            db.rollback()
        finally:
            cursor.close()
            db.close()

    def delete_opinion(self,id):
        sql = "DELETE FROM books_opinion WHERE id=%s"
        try:
            db = MySQLdb.connect("db4free.net", "ksiegarnia", "tas_projekt", "tasksiegarnia")
            cursor = db.cursor()
            cursor.execute(sql,(id,))
            db.commit()
            print "Usunięto"
            return 1
        except:
            print "Problem z usunięciem"
            return 0
        finally:
            cursor.close()
            db.close()

p_server=PyroServer()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(p_server)   # register the object as a Pyro object
ns.register("pyro.server", uri)  # register the object with a name in the name server

print "Ready."
daemon.requestLoop() 