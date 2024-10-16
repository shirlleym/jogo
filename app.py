from flask import Flask, request, jsonify
import mysql.connector
import random

app = Flask(__name__)

# Função para conectar ao banco de dados
def connect_to_db():
    connection = mysql.connector.connect(
        host='localhost',
        database='adivinha_o_numero',
        user='root',
        password='senha_do_mysql'
    )
    return connection

# Função para registrar tentativas
def register_attempt(user_id, guess, is_correct):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "INSERT INTO attempts (user_id, guess, is_correct) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, guess, is_correct))
    connection.commit()
    cursor.close()
    connection.close()

# Função para pegar uma consequência aleatória
def get_random_consequence():
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "SELECT description FROM consequences ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    consequence = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return consequence

# Função principal do jogo
def guess_number(user_id, guess):
    correct_number = random.randint(1, 10)  # Gera o número aleatório
    is_correct = (int(guess) == correct_number)
    
    # Registrar a tentativa no banco de dados
    register_attempt(user_id, guess, is_correct)
    
    if is_correct:
        return "Parabéns! Você acertou o número."
    else:
        consequence = get_random_consequence()
        return f"Você errou! {consequence}"

# Rota para receber as tentativas do jogador via JavaScript
@app.route('/guess', methods=['POST'])
def process_guess():
    data = request.get_json()
    guess = data['guess']
    
    # Usuário exemplo (ajuste isso conforme seu sistema de usuários)
    user_id = 1
    
    # Chama a função que processa a tentativa
    result_message = guess_number(user_id, guess)
    
    # Retorna o resultado ao front-end
    return jsonify({"message": result_message})

if __name__ == '__main__':
    app.run(debug=True)
