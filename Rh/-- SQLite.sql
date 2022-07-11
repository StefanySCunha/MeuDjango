-- SQLite
-- SQL (Sctructured Query Language)
-- MDL (Manipulate Data Language)

-- Seleciona todos os dados da tabela
SELECT * FROM Rh_departamento;

-- Insere registro na tabela
INSERT INTO Rh_departamento (id,nome)
VALUES (4, 'Cloud');

INSERT INTO Rh_departamento (id,nome)
VALUES (5, 'Cloud2');

-- Apaga resgistros da tabela
DELETE FROM Rh_departamento WHERE id = 5;

-- ORM (Object Relational Mapping)
