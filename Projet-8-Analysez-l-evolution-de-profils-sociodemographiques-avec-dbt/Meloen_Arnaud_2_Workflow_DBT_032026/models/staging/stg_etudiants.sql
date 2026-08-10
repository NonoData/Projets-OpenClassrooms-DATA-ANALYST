WITH source AS (

    SELECT * 
    FROM {{ source('raw_data', 'ETUDIANTS') }}

),

renamed AS (

    SELECT
        -- Conversion de type directe
        TRY_CAST(YEAR_PATH_STARTED AS INTEGER) AS year_path_started,
        CAST(AGE_GROUP AS VARCHAR)             AS age_group,
        CAST(REGION AS VARCHAR)                AS region,
        CAST(GENDER AS VARCHAR)                AS gender
        
        -- Exclusions RGPD / Inutiles :
        -- USER_ID est exclu pour conformité RGPD
        -- PATH_CATEGORY_NAME est exclu car contient uniquement 'DATA'

    FROM source

)

SELECT * FROM renamed