-- Ranks longetivity of bands, ordered by their style Glam rock.
SELECT band_name,
       (CASE
         WHEN formed IS NULL OR disbanded IS NULL THEN NULL
         ELSE  YEAR(CURDATE()) - GREATEST(formed, 0)
       END) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
