WITH insee AS (

    SELECT 
        annee,
        region,
        sexe,
        age,
        population
    FROM {{ ref('int_insee_2022_2025') }}

),

etudiants_agreges AS (

    SELECT 
        annee,
        region,
        sexe,
        age,
        COUNT(*) AS nb_etudiants_oc
    FROM {{ ref('int_etudiants') }}
    GROUP BY 
        annee,
        region,
        sexe,
        age

),

joined AS (

    SELECT 
        COALESCE(insee.annee, etudiants_agreges.annee)   AS annee,
        COALESCE(insee.region, etudiants_agreges.region) AS region,
        COALESCE(insee.sexe, etudiants_agreges.sexe)     AS sexe,
        COALESCE(insee.age, etudiants_agreges.age)       AS age,
        
        -- On garde NULL si la population INSEE n'existe pas pour cette ligne
        insee.population                                 AS population,
        
        -- On garde 0 pour le nombre d'étudiants s'il n'y en a pas sur un croisement INSEE
        COALESCE(etudiants_agreges.nb_etudiants_oc, 0)   AS nb_etudiants_oc

    FROM insee
    FULL JOIN etudiants_agreges
        ON  insee.annee  = etudiants_agreges.annee
        AND insee.region = etudiants_agreges.region
        AND insee.sexe   = etudiants_agreges.sexe
        AND insee.age    = etudiants_agreges.age

)

SELECT * FROM joined