SELECT Municipios_Brasileiros.Cidade, Municipios_Status.populacao_residente 
FROM Municipios_Brasileiros  
INNER JOIN Municipios_Status ON Municipios_Brasileiros.municipio_ID = Municipios_Status.municipio_ID;


SELECT Estado, COUNT(Cidade) 
FROM Municipios_Brasileiros  
GROUP BY Estado ORDER BY 2 DESC ;

-- Vamos somar o número de pessoas brancas e pretas/pardas:
SELECT SUM(pessoas_brancas), SUM(pessoas_pretas_pardas) FROM Gerencia_Regiao;


-- Acompanhe a região com mínimo ou máximo de pessoas pretas/pardas:
SELECT Regiao, MIN(pessoas_pretas_pardas) FROM Gerencia_Regiao;


-- Acompanhe as regiões em que gerencia branca é maior do que a gerencia preta/parda:
SELECT Regiao FROM Gerencia_Regiao WHERE gerencia_branca>gerencia_preta_parda;

-- Como seria a query para somar a população total de um estado e ordenar pelo estado com menor população?
SELECT Municipios_Brasileiros.Estado, SUM(Municipios_Status.populacao_residente ) AS populacao_total
FROM Municipios_Status
GROUP BY Estado
ORDER BY populacao_total ASC;