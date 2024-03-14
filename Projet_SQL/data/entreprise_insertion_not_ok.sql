"""Problème de Primary key Absense du ID"""
INSERT INTO Salaries_base VALUES (, '1990-02-15', 'M', 'Musulman', 'Marocain', 'Ingénieur informatique', 'Marié(e)', 3, 2 ); 

"""Problème de foreign Key Poste qui n'existe pas dans la table Postes  """
INSERT INTO Salaries_base VALUES (133, '1990-02-15', 'M', 'Musulman', 'Marocain', 'Vendeur', 'Marié(e)', 3, 2 );   

"""problème de check pour célib """
INSERT INTO Salaries_base VALUES (5, '1995-09-10', 'M', 'Hindou', 'Indien', 'Consultant RH', 'célib', 1, 1);

""" Problème de Foreign key (le nom de la formation n'appartient pas à la table Formations"""
INSERT INTO Participations_base VALUES ('ANGLAIS',5,3);

"""FOREIGN Key problem car le nom de l'handicap n'appartient pas à la liste des types dans la atble SituationsHandicap"""
INSERT INTO Difficultes VALUES (2, 'Aucune');

"""Problème de Foreign Key car le salarié 102 n'existe pas dans l table Salaries_base"""
INSERT INTO Difficultes VALUES (102,'Autism');

"""Problème de check car le niveau de de lhandicap n'appartient pas à la liste de check qu'on a fait """
INSERT INTO SituationsHandicap VALUES ('Color blind', 'sévère');

"""Problème de check car le sexe femme n'appartient pas à la liste de check qu'on a effectué """""""
INSERT INTO Salaries_base VALUES (8, '1995-02-20', 'Femme', 'Musulman', 'Algérien', 'Ingénieur informatique', 'Marié(e)', 4, 2); 

"""""Problème de primary key non post égal à NULL ici """""
INSERT INTO Postes VALUES ( , 'Informatique');

"""Problème de Foreign Key car le num salarié (Num 1023) n'appartient pas à la table Salaries_base"""
INSERT INTO Participations_base VALUES ('AI',1023,5);


