WITH staging AS (
    SELECT *
    FROM {{ ref('stg_insee_2022_2025') }}
),

unpivoted AS (
    SELECT
        annee,
        region,
        colonne,
        TRY_CAST(REPLACE(valeur_str, ' ', '') AS INT) AS valeur
    FROM staging
    UNPIVOT (
        valeur_str FOR colonne IN (
            -- Génération propre des colonnes C2 à C64 sans virgule finale en trop
            {{ "C" ~ range(2, 65) | join(", C") }}
        )
    )
),

transformed AS (
    SELECT
        annee,
        region,
       
        -- Population (Ensemble / Hommes / Femmes)
        CASE
            WHEN TRY_CAST(SUBSTRING(colonne, 2) AS INT) BETWEEN 2 AND 22 THEN 'Ensemble'
            WHEN TRY_CAST(SUBSTRING(colonne, 2) AS INT) BETWEEN 23 AND 43 THEN 'M'
            WHEN TRY_CAST(SUBSTRING(colonne, 2) AS INT) BETWEEN 44 AND 64 THEN 'F'
        END AS population,

        -- Tranches d'âge
        CASE TRY_CAST(SUBSTRING(colonne, 2) AS INT) % 21
            WHEN 2 THEN '0-4 ans'
            WHEN 3 THEN '5-9 ans'
            WHEN 4 THEN '10-14 ans'
            WHEN 5 THEN '15-19 ans'
            WHEN 6 THEN '20-24 ans'
            WHEN 7 THEN '25-29 ans'
            WHEN 8 THEN '30-34 ans'
            WHEN 9 THEN '35-39 ans'
            WHEN 10 THEN '40-44 ans'
            WHEN 11 THEN '45-49 ans'
            WHEN 12 THEN '50-54 ans'
            WHEN 13 THEN '55-59 ans'

-- Regroupement de 60 ans à 95 ans et plus :
            WHEN 14 THEN '60 ans ou plus'
            WHEN 15 THEN '60 ans ou plus'
            WHEN 16 THEN '60 ans ou plus'
            WHEN 17 THEN '60 ans ou plus'
            WHEN 18 THEN '60 ans ou plus'
            WHEN 19 THEN '60 ans ou plus'
            WHEN 20 THEN '60 ans ou plus'
            WHEN 0  THEN '60 ans ou plus'
           
            WHEN 1 THEN 'Total'
        END AS age,

        SUM(valeur) AS valeur

    FROM unpivoted
    GROUP BY 1, 2, 3, 4
)

SELECT
    annee,
    region,
    population AS sexe,
    age,
    valeur AS population
FROM transformed

-- Enlève les regions non voulues de la colonne 'region'
WHERE region NOT IN (
    'France métropolitaine et DOM',
    'France métropolitaine',
    'Guadeloupe',
    'Martinique',
    'Guyane',
    'La Réunion',
    'Mayotte'
)

-- Enlève les tranches d'âge non voulues de la colonne 'age'
AND age NOT IN (
    '0-4 ans',
    '5-9 ans',
    '10-14 ans',
    '15-19 ans',
    'Total'
)

-- Enlève les lignes associées à la valeur 'Ensemble' dans la colonne 'sexe'
AND sexe NOT IN ('Ensemble')
