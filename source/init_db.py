import sqlite3

# Création de la base de données et des tables
def create_database():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    # Création de la table Account
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Account (
            id INTEGER PRIMARY KEY,
            solde_compte REAL
        )
    ''')

    # Création de la table Transaction (notez les guillemets doubles autour du nom de la table)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Transaction" (
            transaction_id INTEGER PRIMARY KEY,
            account_id INTEGER,
            amount REAL,
            type TEXT,
            timestamp TEXT,
            FOREIGN KEY(account_id) REFERENCES Account(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Base de données et tables créées avec succès.")
