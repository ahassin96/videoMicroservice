from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import logging

app = Flask(__name__)
CORS(app)


@app.route('/test')
def test_route():
    return 'Hello, this is a test route!'


@app.route('/watch/<video_id>', methods=['GET'])
def get_video(video_id):
    mongo_uri = "mongodb://ec2-54-221-90-30.compute-1.amazonaws.com:27017"
    client = MongoClient(mongo_uri)
    db = client.admin

    app.logger.info(f'Received request for video ID: {video_id}')

    try:
        video_details = db.movies.find_one({'_id': ObjectId(video_id)})

        if video_details:
            video_details['_id'] = str(video_details['_id'])
            app.logger.info(f'Video details: {video_details}')
            return jsonify({"video_details": video_details}), 200
        else:
            app.logger.warning("Video not found.")
            return jsonify({"error": "Video not found."}), 404

    except Exception as e:
        app.logger.exception("An error occurred:")
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
