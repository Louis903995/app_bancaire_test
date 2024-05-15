# initialise la connexion à la BDD 
import sqlite3

# Établir une connexion à la base de données 
connexion = sqlite3.connect('BDD.db')

# curseur
curseur = connexion.cursor()

# Créer une table
curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY,
                    account_id INTEGER,
                    balance INTEGER
                  )''')

curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('234', 3000)")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('678', 25)")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('87','98')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('889','9678')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('8567','9856')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('8787','908')")


connexion.commit()
connexion.close()