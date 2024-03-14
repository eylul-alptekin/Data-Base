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



		



		
