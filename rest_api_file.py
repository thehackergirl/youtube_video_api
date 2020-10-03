from flask import Flask,request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


#create app within api
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)        #data base
db.create_all()

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)        #unique id, this id will be diffenets for each video
    name = db.Column(db.String(100), nullable=False)    #this field has to have some information(yt video always has name
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"


video_put_args = reqparse.RequestParser()       #creating reqparse object
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)         #adding to this object
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")         #adding to this object
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

#
# def abort_if_video_id_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, message="Video id is not valid...")
#
#
# def abort_if_video_exists(video_id):
#     if video_id in videos:
#         abort(409, message="Video already exists with that id...")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'like': fields.Integer

}

class Video(Resource):
    @marshal_with(resource_fields)      #take return value and serialize it in resource_field
    def get(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)
        result = VideoModel.query.filter_by(id=video_id).first()   #look for video with this id in videomodule, filter for it and return first one
        if not result:
            abort(404, message="Could not find video with this id")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken..")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)                               #temporarlt adding the video to data base
        db.session.commit()                                  #permanently putting the video to data base
        return video, 201                                   #return an object so i need to serialize it @marshal_with(inresource_field)

    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video doesn't exist, can not update")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()

        return result

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return "", 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)                 #it will start the server and the flask application



