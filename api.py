from flask_restful import Resource

class StudentAPI(Resource):
    def get(self,course_id):
        print("GET courese_id",course_id)
        return {'test':course_id}

    def put(self,course_id):
        print("PUT courese_id",course_id)
        return {"Course_id":course_id}

    def delete(self,course_id):
        print("DELETE courese_id",course_id)
        return {"Course_id":course_id}

    def post(self,course_id):
        print("POST courese_id",course_id)
        return {"Course_id":course_id}


