from flask import Flask, request, jsonify, render_template
import base64

from controller.controller import AttendenceController

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    # Check if the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Extract base64 image data from JSON payload
    json_data = request.get_json()
    if 'image' not in json_data:
        return jsonify({"error": "No image data provided"}), 400
    
    base64_image_data = json_data['image']
  
    # Decode base64 image data
    try:
        image_data = base64.b64decode(base64_image_data)
        AttendenceController.detect_img(img=image_data)
        

    except Exception as e:
        return jsonify({"error": f"Failed to decode image: {str(e)}"}), 400
    
    # Here you can process the image (e.g., save to disk, analyze with ML model, etc.)
    # For demonstration, we just return a success message
    return jsonify({"message": "Image received and processed successfully"}), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
