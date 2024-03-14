--Insertions des données dans la table Formations:

INSERT INTO Formations VALUES ('AI', 34, 1);
INSERT INTO Formations VALUES ('IT project management', 57, 2);
INSERT INTO Formations VALUES ('Cybersecurity', 89, 1);
INSERT INTO Formations VALUES ('Web Design', 34, 2);
INSERT INTO Formations VALUES ('Mobile application development', 45, 1);
INSERT INTO Formations VALUES ('Cloud computing', 100, 1);

--Insertions des données dans la table SituationsHandicap :

INSERT INTO SituationsHandicap VALUES ('Dwarfism', 'léger');
INSERT INTO SituationsHandicap VALUES ('Down Syndrome', 'modéré');
INSERT INTO SituationsHandicap VALUES ('Autism', 'modéré');
INSERT INTO SituationsHandicap VALUES ('Tourette Syndrome', 'profond');
INSERT INTO SituationsHandicap VALUES ('Dyslexie', 'léger');
INSERT INTO SituationsHandicap VALUES ('Color blind', 'sévère');

--Insertions des données dans la table SituationsFamiliales :

INSERT INTO SituationsFamiliales VALUES ('Marié(e)', 2);
INSERT INTO SituationsFamiliales VALUES ('Célibataire', 0);
INSERT INTO SituationsFamiliales VALUES ('Divorcé(e)', 1);
INSERT INTO SituationsFamiliales VALUES ('Célibataire', 1);
INSERT INTO SituationsFamiliales VALUES ('Marié(e)', 1);
INSERT INTO SituationsFamiliales VALUES ('Veuve', 2);


--Insertion des données dans la table Postes:

INSERT INTO Postes VALUES ('Ingénieur informatique', 'Informatique');
INSERT INTO Postes VALUES ( 'Chef de projet', 'Informatique');
INSERT INTO Postes VALUES ('Analyste financier', 'Finance');
INSERT INTO Postes VALUES ('Développeur web', 'Marketing');
INSERT INTO Postes VALUES ('Consultant RH', 'Finance');
INSERT INTO Postes VALUES ('Directeur des ventes', 'Finance');
	   	   	   
INSERT INTO Salaries_base VALUES (1, '1990-02-15', 'M', 'Musulman', 'Marocain', 'Ingénieur informatique', 'Marié(e)', 3, 2 );   
INSERT INTO Salaries_base VALUES (2, '1985-05-12', 'F', 'Chrétien', 'Français', 'Chef de projet', 'Célibataire', 1,0 );
INSERT INTO Salaries_base VALUES (3, '1992-11-23', 'M', 'Juif', 'Isralien', 'Analyste financier', 'Divorcé(e)', 2, 1 );
INSERT INTO Salaries_base VALUES (4, '1987-07-01', 'F', 'Atheist', 'Britannique', 'Développeur web', 'Célibataire', 4, 1 );
INSERT INTO Salaries_base VALUES (5, '1995-09-10', 'M', 'Hindou', 'Indien', 'Consultant RH', 'Marié(e)', 1, 1);
INSERT INTO Salaries_base VALUES (6, '1988-04-02', 'F', 'Bouddhiste', 'Thalandaise', 'Directeur des ventes', 'Veuve', 5, 2);
INSERT INTO Salaries_base VALUES (7, '1985-06-23', 'M', 'Chrétien', 'Français', 'Directeur des ventes', 'Marié(e)',7 ,2 );
INSERT INTO Salaries_base VALUES (8, '1995-02-20', 'M', 'Musulman', 'Algérien', 'Ingénieur informatique', 'Marié(e)', 4, 2); 
INSERT INTO Salaries_base VALUES (9, '1999-07-01', 'M', 'Atheist', 'Américain', 'Développeur web', 'Célibataire', 1, 0 ); 
INSERT INTO Salaries_base VALUES (10, '1998-02-15', 'M', 'Musulman', 'Marocain', 'Ingénieur informatique', 'Marié(e)', 3, 2 );   
INSERT INTO Salaries_base VALUES (11, '1993-02-15', 'F', 'Musulman', 'Marocain', 'Ingénieur informatique', 'Célibataire', 8, 0 );   
INSERT INTO Salaries_base VALUES (12, '1992-02-15', 'M', 'Musulman', 'Marocain', 'Ingénieur informatique', 'Marié(e)', 7, 2 );   
INSERT INTO Salaries_base VALUES (13, '1997-11-23', 'F', 'Juif', 'Isralien', 'Analyste financier', 'Célibataire', 0, 0);
INSERT INTO Salaries_base VALUES (14, '1996-09-20', 'M', 'Hindou', 'Indien', 'Consultant RH', 'Célibataire', 5, 1);

--Insertions des données dans la table Participations_base:
INSERT INTO Participations_base VALUES ('AI',1,5);
INSERT INTO Participations_base VALUES ('IT project management',2,3);
INSERT INTO Participations_base VALUES ('Cybersecurity',3,4);
INSERT INTO Participations_base VALUES ('AI',4,4);
INSERT INTO Participations_base VALUES ('AI',5,3);
INSERT INTO Participations_base VALUES ('Web Design',4,4);
INSERT INTO Participations_base VALUES ('Mobile application development',5,2);
INSERT INTO Participations_base VALUES ('Web Design',6,2);
INSERT INTO Participations_base VALUES ('Cloud computing',6,3);

--Insertions des données  dans la table Difficultes:
INSERT INTO Difficultes VALUES (1,'Autism');
INSERT INTO Difficultes VALUES (2, 'Down Syndrome');
INSERT INTO Difficultes VALUES (4,'Tourette Syndrome');
INSERT INTO Difficultes VALUES (12,'Color blind');
INSERT INTO Difficultes VALUES (6,'Autism');
INSERT INTO Difficultes VALUES (7, 'Dyslexie');
INSERT INTO Difficultes VALUES (10,'Tourette Syndrome');
INSERT INTO Difficultes VALUES (13,'Dwarfism');
INSERT INTO Difficultes VALUES (1,'Tourette Syndrome');
INSERT INTO Difficultes VALUES (13,'Dyslexie');




