from flask import Flask, request, jsonify
from flask_cors import CORS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"])

from aws_s3 import upload_file_to_s3
import tempfile

@app.route('/api/generate-avatar', methods=['POST'])
def generate_avatar():
    data = request.json
    text = data.get('text')
    avatar_params = data.get('avatarParams', {})

    # Placeholder simulated generation process
    # Generate temporary files locally (simulation)
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    temp_video.write(b'Simulated video content')
    temp_audio.write(b'Simulated audio content')
    temp_video.close()
    temp_audio.close()

    # Upload to AWS S3
    video_s3_url = upload_file_to_s3(temp_video.name, 'avatars/generated_avatar_video.mp4')
    audio_s3_url = upload_file_to_s3(temp_audio.name, 'avatars/generated_audio.mp3')

    response = {
        "message": "Avatar generated and uploaded",
        "text_received": text,
        "avatar_params_received": avatar_params,
        "video_url": video_s3_url or "",
        "audio_url": audio_s3_url or ""
    }
    return jsonify(response)

@app.route('/api/get-upload-url', methods=['POST'])
def get_upload_url():
    data = request.json
    file_name = data.get('fileName')
    file_type = data.get('fileType')

    if not file_name or not file_type:
        return jsonify({"error": "fileName and fileType are required"}), 400

    s3_key = f"uploads/{file_name}"
    presigned_url = generate_presigned_url(s3_key)

    if presigned_url:
        return jsonify({"uploadUrl": presigned_url, "s3Key": s3_key})
    else:
        return jsonify({"error": "Failed to generate upload URL"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
