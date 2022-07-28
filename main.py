import json
from flask import request
from models import User, Order, Offer
from config import app
from service import init_db, get_all, get_by_id, insert_data_user, update_data, insert_data_order, insert_data_offer, \
    delete_data


@app.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print("Данные введены некорректно")
    return app.response_class(
        response=json.dumps(request.json, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order([request.json])
        else:
            print("Данные введены некорректно")
    return app.response_class(
        response=json.dumps(request.json, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])
        else:
            print("Данные введены некорректно")
    return app.response_class(
        response=json.dumps(request.json, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        user_by_id = get_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(user_by_id, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(User, user_id)
        return app.response_class(
            response=json.dumps(["Данные удалены"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(user_id):
    if request.method == 'GET':
        order_by_id = get_by_id(Order, user_id)
        return app.response_class(
            response=json.dumps(order_by_id, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(Order, user_id)
        return app.response_class(
            response=json.dumps(["Данные удалены"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(user_id):
    if request.method == 'GET':
        offer_by_id = get_by_id(Offer, user_id)
        return app.response_class(
            response=json.dumps(offer_by_id, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(Offer, user_id)
        return app.response_class(
            response=json.dumps(["Данные удалены"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
