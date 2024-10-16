-- Script para criar o banco de dados
CREATE DATABASE adivinha_o_numero;

-- Selecionar o banco de dados
USE adivinha_o_numero;

-- Tabela de usuários
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de tentativas
CREATE TABLE attempts (
    attempt_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    guess INT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Tabela de consequências
CREATE TABLE consequences (
    consequence_id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL
);

-- Inserir algumas consequências iniciais
INSERT INTO consequences (description) VALUES 
('Você dançou!'),
('Você terá que cantar uma música!'),
('Agora faça 10 flexões!'),
('Hora de imitar um gato!');

-- Dados de exemplo para usuário
INSERT INTO users (username, email) VALUES ('Jogador1', 'jogador1@exemplo.com');
