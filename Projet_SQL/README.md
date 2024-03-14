########################################################################################################################################
REALISE PAR : IFEGH MANAL
              ALPTEKIN EYLUL 
GROUPE :    INM2
########################################################################################################################################
1. MENU PRINCIPALE 
    il contient 5 options qui dépendent de la réponse de l'utilisateur , s'il veut bien afficher les informations des tables

    (option 1 : Affichage ) 
    Dans ce menu affichage on a 9 choix , et tous ces choix portent bien sur notre thème qui est (la diversification au sein de l'entreprise)
    comme on affiche le taux de femmes dans l'entreprise , pour bien savoir que ce taux est bien équilibré ou il faut bien le prendre
    en concidération pour créer un équilibre au niveau du sexe , on a fait de même pour l'origine , on affiche le taux par origine 
    comme ça si un origine n'existe pas ou existe avec un taux très faible on peut recruter plus des gens de cet origine , sans oublié 
    qu'on a aussi fait des options pour les gens en situation d'handicap , commme ça on peut aussi les intégrer au sein de 
    l'entreprise .
    Concernant les requettes qui nécessitent une interaction  avec l'utilisateur , on a fait deux :
        la première : qui affiche les numero des salariés qui ont suivis une formation donné par l'utilisteur (on affiche la liste 
        des formations pour qu'il choisis bien une qui existe ), le but de cette requette , c'est par exemple si le recruteur ou 
        le responsable veut bien s'assurer que les salariés ont suivis une formation qui semble utile pour leurs niveaux et pour évoluer
        leurs compétences , ou bien recruter un salarié qui a suivi une telle formation.
        la deuxième : qui affiche les salariés s'ils ont une telle situation d'handicap et c'est à l'utilisateur de taper le type 
        (on affiche bien tous les types existants ).
    Une requette qui utilise les opérations ensemblistes (EXCEPT dans notre cas) , cette requette affiche tous les salarié 
    qui n'ont suivi aucune formation .
    Deux view une dans la table salrié qui calcule l'âge de chaque salarié , et une deuxième qui calcule la durée de formation
    faite par chaque salarié .

    ou (option 2 : Insertion)
     insérer des nouveaux attributs dans la table de son choix , c'est pour cela dans notre code on  demande bien à l'utilisateur qu'il 
    tape le nom de la table dans la quelle il veut insérer , et pour éviter les erreurs on affiche bien avant tous les noms des tables 
    qu'ils existent et si comme même il a mal taper le nom de la table on affiche une erreur disant que cette table n'existe pas et 
    on lui redonne la main pour qu'il rentre une deuxième fois le nom de la table , lorsque cela est fait on lui demande qu'il saisis 
    un attribut suivant l'autre , et si les valeurs saisis ne vérifiaient pas nos contraintes (primarykey, foreignkey , check...), on 
    affiche bien une erreur sur la sortie standart et succès si on abien fait  , on a aussi bien fait attention dans nos code de faire une commit() à la fin du code
    de l'insertion pour bien enregistrer toutes les modifications .

     ou (option 3 : Supression)
        pour la Supression des attributs déja existants , on demande à l'utilisateur de taper la table voulue après avoir afficher ceux 
        qui existent , si les contraintes d'intégrité sont bien repectées , on fait (DELETE)sion une erreur est affichée .
    
     ou (option 4 : Update)
        l'utlisateur peut aussi mis à jour les information dans une tables , pour cela on demande la table qu'il veut en donnant 
        tous les noms qu'ils existent , et aussi le nom de l'attribut qui veut changer et par quoi , et nous dans notre code 
        on change les informations et on fait commit() , pour sauvegarder . 

    QUITTER (taper "r" ) ------------> on sort des menus fils , et on est redirigés directement au menu principale , pour rechoisir d'autre 
    options ou quitter tout en tappons "q".
    

                Merci D'avoir lu :)
    