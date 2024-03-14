#!/usr/bin/python3

from utils import db

from prettytable import PrettyTable

#############################################################################################
# EN DESSOUS IL Y A LES DIFFERENTS TYPES DE MENUS DEPENDANT DE CE QUE L'UTILISATEUR CHOISIT #
#############################################################################################

def menu_afficher(conn):
    while True:
        print("""
             
                    Menu d'affichage: 
                    
        1) Afficher tous les salariés                       
        2) Afficher le taux de femmes dans l'entreprise  
        3) Afficher le nombre total de salariés dans l'entreprise    
        4) Afficher le nombre total de salariés par domaine de poste
        5) Afficher la liste des salariés ayant suivi une formation donnée
        6) Afficher le taux pour chaque origine
        7) Afficher l'origine le moins présent dans l'entreprise avec le nombre 
        de salariés qui conviennent
        8) Afficher le nombre de salariés ayant un tel handicap
        9)Afficher les salaries qui n'ont pas poursuivi une formation 
                
                    r) Retour au menu principal   
    
                    """)
            
        print("#####################################################")
        print()
        print("Sélectionner un choix ou taper r pour retourner au menu principal ")
        print()
        print("#####################################################")
        choix=input("Votre choix: ")
        print()

        
        if choix == "r":
            break
        elif choix=="1":  
            print("#####################################################")
            print()
            print("Voici la liste de tous les salariés de l'entreprise")
            print()
            print("#####################################################")
            print()
            select_tous_les_salaries(conn)
        elif choix=="2":  
            print("#####################################################")
            print()
            print("Voici le Taux de femmes dans l'entreprise")
            print()
            print("#####################################################")
            print()
            select_taux_femmes(conn)
        elif choix=="3":  
            print("#####################################################")
            print()
            print("Voici le nombre total de salariés dans l'entreprise  ")
            print()
            print("#####################################################")
            print()
            select_nb_salaries(conn)
            
        elif choix=="4":  
            print("#####################################################")
            print()
            print("Voici le nombre total de salariés par domaine de poste  ")
            print()
            print("#####################################################")
            print()
            select_nb_salaries_par_domaine(conn)
            
        elif choix=="5": 
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Veuillez  choisir une de ces Formations: ")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            select_nom_formation(conn) 

            print("#####################################################")
            print()
            nom_formation = input("Entrez le nom de la formation : ")
            print("Voici la liste des salariés ayant suivi la formation",nom_formation)
            print()
            print("#####################################################")
            print()
            select_salaries_suivant_formation(conn,nom_formation)
            
        elif choix=="6":
            print("#####################################################")
            print()
            print("Voici le taux pour chaque origine dans l'entreprise")
            print()
            print("#####################################################")
            print()
            select_taux_par_origine(conn)
            
        elif choix=="7":
            print("#####################################################")
            print()
            print("Voici l'origine le moins présent dans l'entreprise avec le nombre de salariés qui lui  convient")
            print()
            print("#####################################################")
            print()    
            select_moindre_origine(conn)
            
        elif choix=="8":
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Veuillez  choisir un type d'handicap: ")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            select_types_handicapes(conn)

            print("#####################################################")
            print()
            nom_handicap = input("Entrez le type d'handicap : ")
            print("Voici le nombre des salariés qui ont le type d'handicap suivant ",nom_handicap)
            print()
            print("#####################################################")
            print()            
            select_nb_salaries_handicapes(conn,nom_handicap)
            
        elif choix=="9":
            print("#####################################################")
            print()
            print("Voici les salaries qui n'ont suivi aucune une formation")
            print()
            print("#####################################################")
            print()  
            select_salarie_sans_formation(conn)


def menu_inserer(conn):
    while True:
        print("""
             
                    Menu d'insertion: 
                    
        1) Insérer                         
                    
        r) Retour au menu principal   
    
                    """)
            
        print("#####################################################")
        print()
        print("Sélectionner un choix ou taper r pour retourner au menu principal ")
        print()
        print("#####################################################")
        choix=input("Votre choix: ")
        print()

        
        if choix == "r":
            break
        elif choix=="1":  
            afficher_tables()
            inserer(conn)
        

def menu_update(conn):
    while True:
        print("""
             
                    Menu d'update: 
                    
        1) Update                        
                    
        r) Retour au menu principal   
    
                    """)
            
        print("#####################################################")
        print()
        print("Sélectionner un choix ou taper r pour retourner au menu principal ")
        print()
        print("#####################################################")
        choix=input("Votre choix: ")
        print()

        
        if choix == "r":
            break
        elif choix=="1":  
            afficher_tables()
            update(conn)
        
def menu_supprimer(conn):
    while True:
        print("""
             
                    Menu de supression: 
                    
        1) Supprimer                        
                    
        r) Retour au menu principal   
    
                    """)
            
        print("#####################################################")
        print()
        print("Sélectionner un choix ou taper r pour retourner au menu principal ")
        print()
        print("#####################################################")
        choix=input("Votre choix: ")
        print()

        
        if choix == "r":
            break
        elif choix=="1":  
            afficher_tables()
            supprimer(conn)


    
# ##############################################################################################
# EN DESSOUS IL Y A TOUTES LES FONCTIONS QUI PERMETTENT A L'UTILISATEUR D'INSERER DES DONNEES  #
################################################################################################

def afficher_tables():

    print("Salaries_base \n")
    print("""
        Les attributs: 
        * numero_salarie
        * date_naissance_salarie
        * sexe_salarie,
        * religion_salarie
        * origine_salarie
        * titre_poste
        * statut_situation_familiale
        * ancienneté_poste_salarie
        * nb_personnes_charges_situation_familiale
                    """)

    print("##########################################################################################")

    print("Participations_base \n")
    print(""" 
            Les attributs:
    
            * nom_formation
            * numero_salarie
            * nb_seances_formation_salarie
            
                    """)
    print("##########################################################################################")

    print("Difficultes \n")
    print(""" 
            Les attributs:
    
            * nom_formation
            * numero_salarie
            * nb_seances_formation_salarie
            
                    """)

    print("##########################################################################################")


    print("Postes \n")
    print(""" 
            Les attributs:
    
            * titre_poste
            * domaine_poste
            
                    """)
    
    print("##########################################################################################")

    print("Formations \n")
    print(""" 
            Les attributs:
    
            * nom_formation
            * numero_prestataire_formation
            * duree_seance_formation
            
                    """)
    
    print("##########################################################################################")

    print("SituationsFamiliales \n")
    print(""" 
            Les attributs:
    
            * statut_situation_familiale
            * nb_personnes_charges_situation_familiale
            
                    """)
    print("##########################################################################################")

    print("SituationsHandicap \n")
    print(""" 
            Les attributs:
    
            * type_situation_handicap
            * niveau_situation_handicap
            
                    """)
    
    
def inserer(conn):
    
    import sqlite3

    # Demander à l'utilisateur le nom de la table
    table_name = input("Entrez le nom de la table dans laquelle vous souhaitez insérer des données : ")

    # Vérifier si la table existe
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
    if not cursor.fetchone():
        print("La table {} n'existse pas.".format(table_name))
        conn.close()
        exit()

    # Demander à l'utilisateur de saisir les valeurs des attributs
    columns = []
    values = []
    for row in conn.execute("PRAGMA table_info({});".format(table_name)):
        column_name = row[1]
        if column_name != "id":
            columns.append(column_name)
            value = input("Entrez la valeur pour l'attribut '{}': ".format(column_name))
            values.append(value)

    # Insérer les données dans la table
    columns_str = ", ".join(columns)
    values_str = ", ".join(["'{}'".format(value) for value in values])

    try:
        conn.execute("INSERT INTO {} ({}) VALUES ({});".format(table_name, columns_str, values_str))
        print("Les données ont été insérées avec succès !")
    except sqlite3.IntegrityError as e:
        print("Erreur: ", e)
        print("Impossible d'insérer les données car une contrainte d'intégrité a été violée.")
        print("Veuillez vérifier que la clé primaire n'est pas déjà utilisée.")
    except sqlite3.Error as e:
        print("Erreur: ", e)
        print("Une erreur s'est produite lors de l'insertion des données.")
        print("Veuillez vérifier les types de données et réessayer.")

    # Enregistrer les modifications
    conn.commit()


#####################################################################################
#  EN DESSOUS IL Y A TOUTES LES FONCTIONS QU'ON UTILISE POUR FAIRE LES UPDATES      #
#####################################################################################

def update(conn):
    import sqlite3

    # Demander à l'utilisateur le nom de la table
    table_name = input("Entrez le nom de la table dans laquelle vous souhaitez insérer des données : ")

    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
    if not cursor.fetchone():
        print("La table {} n'existe pas.".format(table_name))
        conn.close()
        exit()

    # Demander à l'utilisateur le nom de l'attribut à modifier et sa nouvelle valeur
    attribute_name = input("Entrez le nom de l'attribut à modifier : ")
    new_value = input("Entrez la nouvelle valeur de l'attribut : ")

    # Modifier l'attribut dans la table
    query = "UPDATE {} SET {} = ?;".format(table_name, attribute_name)
    values = (new_value,)
    try:
        conn.execute(query, values)
        print("La valeur de l'attribut {} a été modifiée avec succès !".format(attribute_name))
    except sqlite3.Error as e:
        print("Erreur: ", e)
        print("Une erreur s'est produite lors de la modification des données.")

    # Enregistrer les modifications
    conn.commit()


#####################################################################################
#  EN DESSOUS IL Y A TOUTES LES FONCTIONS QU'ON UTILISE POUR FAIRE LES SUPPRESSIONS #
#####################################################################################

def supprimer(conn):
    
    import sqlite3

    # Demander à l'utilisateur le nom de la table
    table_name = input("Entrez le nom de la table dans laquelle vous souhaitez supprimer des données : ")

    # Vérifier si la table existe
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
    if not cursor.fetchone():
        print("La table {} n'existe pas.".format(table_name))
        conn.close()
        exit()

    # Demander à l'utilisateur le nom de l'attribut et la valeur à supprimer
    attribute_name = input("Entrez le nom de l'attribut dans lequel vous souhaitez supprimer une valeur : ")
    attribute_value = input("Entrez la valeur de l'attribut à supprimer : ")

    # Vérifier si l'attribut existe dans la table
    cursor = conn.execute("PRAGMA table_info({});".format(table_name))
    attribute_names = [row[1] for row in cursor]
    if attribute_name not in attribute_names:
        print("L'attribut {} n'existe pas dans la table {}.".format(attribute_name, table_name))
        conn.close()
        exit()

    # Supprimer la valeur de l'attribut dans la table
    try:
        conn.execute("DELETE FROM {} WHERE {} = ?;".format(table_name, attribute_name), (attribute_value,))
        print("La valeur {} a été supprimée avec succès de l'attribut {} de la table {}.".format(attribute_value, attribute_name, table_name))
    except sqlite3.Error as e:
        print("Erreur: ", e)
        print("Une erreur s'est produite lors de la suppression de la valeur {} de l'attribut {} de la table {}.".format(attribute_value, attribute_name, table_name))

    # Enregistrer les modifications
    conn.commit()


#####################################################################################
#  EN DESSOUS IL Y A TOUTES LES FONCTIONS QU'ON UTILISE POUR AFFICHER LES REQUÊTES  #
#####################################################################################

def select_tous_les_salaries(conn):
    """
    Affiche la liste de tous les salaries.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Salaries
                """)

    rows = cur.fetchall()
    
    # Création de la table
    table = PrettyTable()
    table.field_names = ['Numéro salarié', 'Date de naissance', 'Sexe', 'Religion', 'Origine', 'Titre du poste', 'Statut de la situation familiale', 'Ancienneté du poste', 'Nombre de personnes à sa charge','Âge']
    
       
    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)
         
    # Affichage de la table
    print(table)


def select_nb_salaries(conn):       
    """
    Afficher le nombre total de salariés dans l'entreprise.
        :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
               SELECT COUNT(numero_salarie) AS nombre_salaries 
               FROM Salaries_base;

                """)

    rows = cur.fetchall()
    
    # Création de la table
    table = PrettyTable()
    table.field_names = ['Nombre salariés']
    
    # Ajout des lignes à la table
    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)
    
    # Affichage de la table
    print(table)

def select_nb_salaries_par_domaine(conn):       
    """
    Afficher le nombre total de salariés par domaine de poste.
        :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
               SELECT domaine_poste, COUNT(*) AS nb_salaries 
               FROM Salaries_base 
               JOIN Postes USING (titre_poste)
               GROUP BY domaine_poste;

                """)

    rows = cur.fetchall()

    # Création de la table
    table = PrettyTable()
    table.field_names = ['Domaine du poste','Nombre de salarié dans ce domaine']

    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data) 

    # Affichage de la table
    print(table)
        
        
def select_taux_femmes(conn):
    """
    Affiche le taux des femmes au sein de l'entreprise.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
        WITH nb_tot_salaries AS (
            SELECT COUNT(*) AS total_salaries
            FROM Salaries_base
        ),
        nb_tot_femmes AS (
            SELECT COUNT(*) AS total_femmes
            FROM Salaries_base
            WHERE sexe_salarie = 'F'
        )
        SELECT nb_tot_femmes.total_femmes * 100 / nb_tot_salaries.total_salaries AS taux_femmes
        FROM nb_tot_salaries, nb_tot_femmes;
                    """)

    rows = cur.fetchall()

    # Création de la table
    table = PrettyTable()
    table.field_names = ["Taux de femmes dans l'entreprise"]
                         
    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data) 

    # Affichage de la table
    print(table)
        
        
def select_salaries_suivant_formation(conn,nom_formation):    
    """
    Afficher la liste des salariés ayant suivi une formation donnée.
        :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                   SELECT Salaries_base.numero_salarie, Salaries_base.titre_poste, Participations_base.nom_formation, Participations_base.nb_seances_formation_salarie 
                   FROM Salaries_base 
                   JOIN Participations_base ON Salaries_base.numero_salarie = Participations_base.numero_salarie 
                   WHERE Participations_base.nom_formation = ?;
                """, (nom_formation,))

    rows = cur.fetchall()

    # Création de la table
    table = PrettyTable()
    table.field_names = ['Numéro salarié','Titre du poste',nom_formation,'Nombre de séance par formation']
                         

    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data) 

    # Affichage de la table
    print(table)
        
        
def select_nom_formation(conn):     
    """
    Afficher la liste de toutes les formations qui existent.
        :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                   SELECT nom_formation 
                   FROM Formations

                """)

    rows = cur.fetchall()

    # Création de la table
    table = PrettyTable()
    table.field_names = ['Nom de toutes les formations']

    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)    

    # Affichage de la table
    print(table)

def select_taux_par_origine(conn):
    """
    Afficher le taux pour chaque origine.
        :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                  WITH nb_tot_salaries AS (
                      SELECT COUNT(*) AS total_salaries
                      FROM Salaries_base
                  ),
                  nb_tot_origine AS (
                      SELECT origine_salarie, COUNT(*) AS total_origine
                      FROM Salaries_base
                      GROUP BY origine_salarie
                  )
                  SELECT nb_tot_origine.origine_salarie, nb_tot_origine.total_origine * 100 / nb_tot_salaries.total_salaries AS taux_par_origine
                  FROM nb_tot_salaries, nb_tot_origine
                  ORDER BY taux_par_origine DESC;
    
                """)
    
    rows = cur.fetchall()
    
    # Création de la table
    table = PrettyTable()
    table.field_names = ['Origine', 'Taux par origine']
                         

    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)

    # Affichage de la table
    print(table)
            
        
def select_moindre_origine(conn):
    """
    Afficher l'origine le moins présent dans l'entreprise avec le nombre de salariés qui conviennent
        :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
        SELECT s.origine_salarie, COUNT(*) as nb_salarie
        FROM Salaries_base s
        GROUP BY s.origine_salarie
        HAVING COUNT(*) = (
            SELECT MIN(nb_salarie)
            FROM (
                SELECT COUNT(*) as nb_salarie
                FROM Salaries_base
                GROUP BY origine_salarie
            )
        )

        """)
        
    rows = cur.fetchall()


    # Création de la table
    table = PrettyTable()
    table.field_names = ['Origine le moins présent', 'Nombre de salarié correspondant']
                         
    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)

    # Affichage de la table
    print(table)
               
        
def select_nb_salaries_handicapes(conn,nom_handicap):
    """
    Afficher le nombre de salariés ayant un tel handicap.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT COUNT(type_situation_handicap)
                FROM Difficultes
                WHERE type_situation_handicap= ?;
             """, (nom_handicap,))

    rows = cur.fetchall()

    # Création de la table
    table = PrettyTable()
    table.field_names = ['Nombre de salarié(s) ayant '+nom_handicap]
                         
    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)

    # Affichage de la table
    print(table)
               
        
def select_types_handicapes(conn):
    """
    Afficher la liste de tous les types d'handicap.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT type_situation_handicap
                FROM SituationsHandicap
             """)

    rows = cur.fetchall()

     # Création de la table
    table = PrettyTable()
    table.field_names = ["Tous les types d'handicap"]
                         
    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)


    # Affichage de la table
    print(table)
        
      
def select_salarie_sans_formation(conn):
    """
     Afficher le numéro des salariés qui n'ont suivi aucune formation.

     :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
        SELECT numero_salarie
        FROM Salaries_base
        EXCEPT
        SELECT numero_salarie
        FROM Participations_base;

              """)

    rows = cur.fetchall()

    # Création de la table
    table = PrettyTable()
    table.field_names = ["Numéro des salariés qui n'ont suivi aucune formation"]
                            
    for row in rows:
        row_data = []
        for col in row:
            row_data.append(col)
        table.add_row(row_data)

    # Affichage de la table
    print(table) 
        
                               
def main():
    # Nom de la BD à créer
    db_file = "data/entreprise.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, "data/entreprise_creation.sql")
    db.mise_a_jour_bd(conn, "data/entreprise_insertion_ok.sql")
    

    # Lire la BD
    while True:
        print("""
              
              Menu principal: 
              
        ****************************
              
        1) Insérer     2)Afficher
        3) Supprimer   4) Update
                
                q)Quitter
        ****************************
        """)
        
        choix=input("Votre choix: ")
        
        if choix == "q":
            break
        elif choix=="1":  
            menu_inserer(conn)
        elif choix=="2":  
            menu_afficher(conn)     
        elif choix=="3":
            menu_supprimer(conn)    
        elif choix=="4":  
            menu_update(conn)

           
        
                                       
if __name__ == "__main__":
    main()
