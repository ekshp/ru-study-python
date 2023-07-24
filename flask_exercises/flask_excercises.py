from flask import Flask, request, jsonify


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.route('/user', methods=["POST"])
        def create_user():
            data = request.get_json()
            if 'name' not in data:
                response = {"errors": {"name": "This field is required"}}
                return jsonify(response), 422
            name = data['name']
            response = {"data": f"User {name} is created!"}
            return jsonify(response), 201

        @app.route('/user/<name>', methods=['GET'])
        def read_user(name):
            if name:
                response = {"data": f"My name is {name}"}
                return jsonify(response), 200
            else:
                return "", 404

        @app.route('/user/<name>', methods=['PATCH'])
        def update_user(name):
            data = request.get_json()
            response = {"data": f"My name is {data['name']}"}
            return jsonify(response), 200

        @app.route('/user/<name>', methods=['DELETE'])
        def delete_user(name):
            if name:
                response = {"errors": {"name": "This field is required"}}
                return jsonify(response), 204

