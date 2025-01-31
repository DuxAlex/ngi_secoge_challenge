SELECT 
    COUNT(*) AS total_obitos,
    SUM(CASE WHEN VACINA_COV = '1' THEN 1 ELSE 0 END) AS obitos_com_vacina
FROM 
    dados_influd24
WHERE 
    EVOLUCAO = '2'; -- Óbito
