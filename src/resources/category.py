from flask_restful import Resource, reqparse
# from flask_jwt import jwt_require

from models.category import Category

class CategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required = True,
                        help = "This field cannot be blank")

    def get(self,id):
        category = Category.find_by_id(id)
        if category:
            return category.json()
        return {'message' : 'category NOT found'}

    def post(self,id):
        data = CategoryResource.parser.parse_args()
        category = Category(data['name'])
        category.save_to_db()
        return {'message' : 'Success'}, 200

    def put(self,id):
        data = CategoryResource.parser.parse_args()
        category =  Category.find_by_id(id)
        if not category:
            return {'message' : 'Category with the ID: {} does not exist. To update please create the Category first'.format(id)}
        else:
            category.name = data['name']
            category.save_to_db()
            return category.json()


class CategoryListResource(Resource):
    def get(self):
        return {'category' :  list(map(lambda category: category.json(), Category.query.all()))}