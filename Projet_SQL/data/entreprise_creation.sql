
DROP TABLE IF EXISTS Difficultes;
DROP TABLE IF EXISTS Participations_base;
DROP TABLE IF EXISTS Salaries_base;
DROP TABLE IF EXISTS Postes;
DROP TABLE IF EXISTS SituationsFamiliales;
DROP TABLE IF EXISTS SituationsHandicap;
DROP TABLE IF EXISTS Formations;

DROP VIEW IF EXISTS Salaries;
DROP VIEW IF EXISTS Participations;


-- Pour activer les FKs
PRAGMA FOREIGN_KEYS=ON;

CREATE TABLE Salaries_base (

    numero_salarie INTEGER,
    date_naissance_salarie DATE NOT NULL,
    sexe_salarie TEXT NOT NULL,
    religion_salarie TEXT NOT NULL,
    origine_salarie TEXT NOT NULL,
    titre_poste TEXT NOT NULL,
    statut_situation_familiale TEXT NOT NULL,
    anciennete_poste_salarie INTEGER NOT NULL, 
	nb_personnes_charge_situation_familiale INTEGER NOT NULL,


    CONSTRAINT pk_salaries_base PRIMARY KEY(numero_salarie),

    CONSTRAINT ch0_salaries_base CHECK (statut_situation_familiale in ('Célibataire','Divorcé(e)','Marié(e)','Veuf','Veuve')),
	
	CONSTRAINT ch1_salaries_base CHECK (sexe_salarie in ('F','M')),

    CONSTRAINT fk1_salaries FOREIGN KEY (titre_poste)
    REFERENCES Postes(titre_poste),
	
	CONSTRAINT fk3_salaries FOREIGN KEY (statut_situation_familiale,nb_personnes_charge_situation_familiale)
    REFERENCES SituationsFamiliales(statut_situation_familiale,nb_personnes_charge_situation_familiale)

);

CREATE TABLE Postes (

    titre_poste TEXT,
    domaine_poste TEXT NOT NULL,

    CONSTRAINT pk_postes PRIMARY KEY(titre_poste)

    --CONSTRAINT fk1_postes FOREIGN KEY (titre_poste)
    --REFERENCES Salaries_base(titre_poste)

 
);


CREATE TABLE SituationsFamiliales (

    statut_situation_familiale TEXT,
    nb_personnes_charge_situation_familiale INTEGER,

    CONSTRAINT pk_situationsfamiliales PRIMARY KEY(statut_situation_familiale, nb_personnes_charge_situation_familiale),

    CONSTRAINT ch_situationsfamiliales CHECK (statut_situation_familiale in ('Célibataire','Divorcé(e)','Marié(e)','Veuf','Veuve'))

);



CREATE TABLE SituationsHandicap (

    type_situation_handicap TEXT,
    niveau_situation_handicap TEXT NOT NULL,
	
    CONSTRAINT ch_situationshandicap CHECK (niveau_situation_handicap in ('léger','modéré','profond','sévère')),
    CONSTRAINT pk_situationshandicap PRIMARY KEY(type_situation_handicap)

);



CREATE TABLE Formations (

    nom_formation TEXT,
    numero_prestataire_formation INTEGER NOT NULL,
	duree_seance_formation INTEGER NOT NULL,
	

    CONSTRAINT pk_formations PRIMARY KEY(nom_formation)

);



CREATE TABLE IF NOT EXISTS Difficultes (

    numero_salarie INTEGER,
    type_situation_handicap TEXT NOT NULL,

    CONSTRAINT pk_difficultes PRIMARY KEY(numero_salarie,type_situation_handicap),

    CONSTRAINT fk1_difficultes FOREIGN KEY (numero_salarie)
    REFERENCES Salaries_base(numero_salarie),

    CONSTRAINT fk2_difficultes FOREIGN KEY (type_situation_handicap)
    REFERENCES SituationsHandicap(type_situation_handicap)

);



CREATE TABLE Participations_base(

    nom_formation TEXT,
    numero_salarie INTEGER,
	nb_seances_formation_salarie INTEGER NOT NULL,

    CONSTRAINT pk_participations PRIMARY KEY(nom_formation,numero_salarie),

	CONSTRAINT fk1_particiations_base FOREIGN KEY (numero_salarie)
    REFERENCES Salaries_base(numero_salarie),

	CONSTRAINT fk2_participations_base FOREIGN KEY (nom_formation)
    REFERENCES Formations(nom_formation)


);
	
--Requête pour calculer un attribut "age" : 
CREATE VIEW Salaries AS
SELECT numero_salarie,
       date_naissance_salarie,
       sexe_salarie,
       religion_salarie,
       origine_salarie,
       titre_poste,
       statut_situation_familiale,
       anciennete_poste_salarie,
	   nb_personnes_charge_situation_familiale,
       strftime('%Y', 'now') - strftime('%Y', date_naissance_salarie) AS age
FROM Salaries_base; 


--Requête pour calculer un attribut "duree_participation": 
CREATE VIEW Participations AS
SELECT	nom_formation,
        numero_salarie, 
      	(nb_seances_formation_salarie*duree_seance_formation) AS duree_participation
FROM Participations_base
JOIN Formations USING (nom_formation)
GROUP BY numero_salarie, nom_formation;
		



 


	
