from flask import Flask, jsonify,request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource




from models import db, Newsletter


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['JSONIFY_PRETTYPRINT_REGULAR']=True



migrate  = Migrate(app,db)
# nitializes the Flask-Migrate extension with your Flask application and the SQLAlchemy database object, 
# enabling you to perform database migrations as your application's database schema evolve

api = Api(app)
#an object called api that initialise the  used api in our app
class Index(Resource):
    # method to get data of newsletters
    def get(self):
        response_dict ={
            
            "index":"Welcome to the Newsletter ResTful Api",
        }  
        response = make_response(
            
            jsonify(response_dict),
            200,
        
        )
        return response
    

api.add_resource(Index, '/')

class Newsletters(Resource):
    # 
    def get(self):
        response_dict_list = [n.to_dict() for n in Newsletter.query.all()]       
        
        response  = make_response(
            
            jsonify(response_dict_list),
            200,
             
             
         )
        
        return response
    
    #method to post
    
    def  post(self):
        new_record = Newsletters(
            
            
            title=request.form['title'],
            body=request.form['body'],
        )
        
        db.session.add(new_record)
        db.session.commit()
        
        
        response_dict  = new_record.to_dict()
        
        response = make_response(
            
            jsonify(response_dict),
            200,
        )
        
        return response
    
api.add_resource(NewslettersByID, '/newsletters/<int:id>') 


if __name__  == 'main':
    app.run(port=5555)   