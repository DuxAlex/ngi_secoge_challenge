SELECT 
    CS_SEXO, 
    COUNT(*) AS num_obitos
FROM 
    dados_influd24
WHERE 
    EVOLUCAO = '2' -- Óbito
GROUP BY 
    CS_SEXO
ORDER BY 
    num_obitos DESC LIMIT 100