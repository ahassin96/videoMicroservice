from flask import Flask, render_template, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from urllib.parse import quote
import logging


app = Flask(__name__, template_folder='Templates')
app.logger.setLevel(logging.DEBUG)
CORS(app)

@app.route('/api/video/<video_id>')
def get_video_details(video_id):
    app.logger.info(f'Received API request for video ID: {video_id}')
    try:
        client = MongoClient("mongodb://ec2-54-221-90-30.compute-1.amazonaws.com:27017")
        db = client.admin
        video_details = db.movies.find_one({'_id': ObjectId(video_id)})

        if video_details:
            app.logger.info(f'Video details: {video_details}')


            video_details['_id'] = str(video_details['_id'])

            return jsonify({'success': True, 'video_details': video_details})
        else:
            app.logger.warning("Video not found.")
            return jsonify({'success': False, 'error': 'Video not found.'})

    except Exception as e:
        app.logger.exception("An error occurred:")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/watch.php/<video_id>')
def watch(video_id):


    mongo_uri = "mongodb://ec2-54-221-90-30.compute-1.amazonaws.com:27017"
    client = MongoClient(mongo_uri)
    db = client.admin

    app.logger.info(f'Received request for video ID: {video_id}')


    try:
        video_details = db.movies.find_one({'_id': ObjectId(video_id)})

        if video_details:
            app.logger.info(f'Video details: {video_details}')

            return render_template('watch.php', video_details=video_details)
        else:
         app.logger.warning("Video not found.")
         return "Video not found."

    except Exception as e:

        app.logger.exception("An error occurred:")
        print(f"An error occurred: {str(e)}")
        return "Error: " + str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
