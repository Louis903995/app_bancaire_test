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

# Exemple d'insertion de données
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('234', 3000)")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('678', 25)")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('87','98')")

# Valider les modifications et fermer la connexion
connexion.commit()
connexion.close()