SELECT 
    EXTRACT(YEAR FROM AGE(DATE '2024-01-01', DT_NASC)) AS idade,
    COUNT(*) AS total_criancas_afetadas,
    SUM(CASE WHEN EVOLUCAO = '2' THEN 1 ELSE 0 END) AS total_obitos,
    SUM(CASE WHEN EVOLUCAO = '2' AND VACINA_COV = '1' THEN 1 ELSE 0 END) AS obitos_vacinados,
    SUM(CASE WHEN EVOLUCAO = '2' AND VACINA_COV = '2' THEN 1 ELSE 0 END) AS obitos_nao_vacinados
FROM 
    dados_influd24
WHERE 
    EXTRACT(YEAR FROM AGE(DATE '2024-01-01', DT_NASC)) <= 12
    AND EVOLUCAO = '2'
GROUP BY 
    idade

UNION ALL

SELECT 
    NULL AS idade,
    COUNT(*) AS total_criancas_afetadas,
    SUM(CASE WHEN EVOLUCAO = '2' THEN 1 ELSE 0 END) AS total_obitos,
    SUM(CASE WHEN EVOLUCAO = '2' AND VACINA_COV = '1' THEN 1 ELSE 0 END) AS obitos_vacinados,
    SUM(CASE WHEN EVOLUCAO = '2' AND VACINA_COV = '2' THEN 1 ELSE 0 END) AS obitos_nao_vacinados
FROM 
    dados_influd24
WHERE 
    EXTRACT(YEAR FROM AGE(DATE '2024-01-01', DT_NASC)) <= 12
    AND EVOLUCAO = '2'
ORDER BY 
    idade NULLS LAST LIMIT 100