import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Question, Category
from flask_cors import CORS
import random


questions_per_page = 10


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * questions_per_page
    end = start + questions_per_page
    formatted_questions = [question.format() for question in selection]
    current_questions = formatted_questions[start:end]
    return current_questions


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    def after_request(response):

        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization, true"
        )
        response.headers.add(
            "Acess-Control-Allow-Methods", "GET, POST, DELETE,PATCH, OPTIONS"
        )
        return response

    @app.route("/categories", methods=["GET"])
    def get_all_category():
        categories = Category.query.all()
        category_format = {
          category.id: category.type for category in categories
          }

        if len(category_format) == 0:
            abort(404)
        else:
            return jsonify(
                {
                    "success": True,
                    "categories": category_format,
                    "total": len(category_format),
                }
            )

    @app.route("/questions/<int:question_id>", methods=["GET"])
    def get_specific_question(question_id):
        question = Question.query\
          .filter(Question.id == question_id)\
          .one_or_none()
        if question is None:
            abort(404)
        else:
            return jsonify({"success": True, "question": question.format()})

    @app.route("/questions", methods=["GET"])
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
        categories = Category.query.order_by(Category.id).all()
        category_formatted = {
          category.id: category.type for category in categories
          }

        if len(current_questions) == 0:
            abort(404)
        else:
            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "total_questions": len(Question.query.all()),
                    "category": category_formatted,
                }
            )

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            question = Question.query\
                .filter(Question.id == question_id)\
                .one_or_none()
            if question is None:
                abort(404)
            else:
                question.delete()
                selection = Question.query\
                    .order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                # similar to GET request

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                }
            )
        except Exception:
            abort(422)

    @app.route("/questions", methods=["POST"])
    def create_questions():

        body = request.get_json()

        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_diffic = body.get("difficulty", None)
        new_category = body.get("category", None)

        try:

            question = Question(
                question=new_question,
                answer=new_answer,
                difficulty=new_diffic,
                category=new_category,
            )
            question.insert()

            selection = Question.query\
                .order_by(Question.id).all()
            current_question = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "created_id": question.id,
                    "question_new": question.question,
                    "question": current_question,
                    "total_questions": len(Question.query.all()),
                }
            )

        except Exception:
            abort(422)

    @app.route("/questions/search", methods=["POST"])
    def questions_search():
        data = request.get_json()
        searchTerm = data["searchTerm"]

        try:
            questions = Question.query\
              .filter(Question.question.ilike(f"%{searchTerm}%"))\
              .all()
            current_questions = paginate_questions(request, questions)

            if len(questions) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "totalQuestions": len(Question.query.all()),
                }
            )
        except Exception:
            abort(404)

    @app.route("/categories/<category_type_id>/questions", methods=["GET"])
    def get_questions_by_category_type(category_type_id):
        try:
            questions = Question.query\
              .filter_by(category=category_type_id)\
              .all()
            current_questions = paginate_questions(request, questions)

            if len(current_questions) == 0:
                abort(404)

            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "total_questions": len(questions),
                }
            )

        except Exception:
            abort(404)

    @app.route("/quizzes", methods=["POST"])
    def play_quizz():
        try:
            data = request.get_json()
            quiz_category = data.get("quiz_category")
            # returns dictionary id (str) and type (str)
            previous_questions = data.get("previous_questions")
            # returns a list of previous questions (int)

            if quiz_category["id"] is "":
                questions = Question.query.all()

            else:
                questions = Question.query\
                  .filter_by(category=quiz_category["id"])\
                  .all()

            def random_question(questions, previous_questions):
                rand_quest = random.choice(questions)\
                  .format()
                while random_quest["id"] in previous_questions:
                    rand_quest = random.choice(questions)\
                      .format()
                if random_quest["id"] not in previous_questions:
                    return random_quest

            question_random = random_question(questions, previous_questions)

            return jsonify({
              "success": True,
              "random_question": question_random
              })
        except Exception:
            abort(400)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          "success": False,
          "error": 404,
          "message": "Not found"}), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"}), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
          "success": False,
          "error": 400,
          "message": "bad request"}), 400

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
          "success": False,
          "error": 500,
          "message": "internal server error"}), 500
    return app
