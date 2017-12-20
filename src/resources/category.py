from flask_restful import Resource, reqparse
from models.category import Category

class CategoryResource(Resource):
    def get(self,id):
        '''Get Category by ID'''
        category = Category.find_by_id(id)
        if category:
            return category.json()
        return {'message' : 'category NOT found'}, 404

    def put(self,id):
        '''Update the Category by ID'''
        self._validate()
        data = CategoryResource.parser.parse_args()
        category = Category.find_by_id(id)
        if not category:
            return {'message' : 'Category with the ID: {} does not exist. To update please create the Category first'.format(id)}
        else:
            category.name = data['name']
            category.save_to_db()
            return category.json()

    def _validate(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            required=True,
                            help="This field cannot be blank")


class CategoryListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="This field cannot be blank")

    def get(self):
        '''Get all the Categories in database'''
        return list(map(lambda category: category.json(), Category.query.all()))

    def post(self):
        '''Create a new Category instance in the database'''
        data = CategoryListResource.parser.parse_args()
        category = Category(data['name'])
        category.save_to_db()
        return {'message' : 'Success'}, 200