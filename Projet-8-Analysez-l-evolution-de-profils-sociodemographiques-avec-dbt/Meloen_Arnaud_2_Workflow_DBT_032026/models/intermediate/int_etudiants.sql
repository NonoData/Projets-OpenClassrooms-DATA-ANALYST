WITH staging AS (

    SELECT * 
    FROM {{ ref('stg_etudiants') }}

),

transformed AS (

    SELECT
        year_path_started AS annee,

        -- Nettoyage des espaces sur la tranche d'âge
        TRIM(age_group) AS age,

        -- Harmonisation des noms de région pour la future jointure INSEE
        CASE 
            WHEN TRIM(region) = 'Centre-Val de Loire' THEN 'Centre-Val-de-Loire'
            WHEN TRIM(region) = 'DROM' THEN 'DOM'
            ELSE TRIM(region)
        END AS region,

        -- Traitement des valeurs manquantes ou vides pour le genre
        COALESCE(
            NULLIF(TRIM(gender), ''), 
            'Non renseigné'
        ) AS sexe

    FROM staging

)

SELECT * FROM transformed