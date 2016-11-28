from camera import Camera
from flask import * 
def gen(camera): 
    while True: 
        frame = camera.get_frame() 
        yield (b"--frame\r\n" 
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b'\r\n') 
 
app = Flask(__name__) 
 
@app.route("/video_feed") 
def video(): 
    return Response(gen(Camera()), mimetype="multipart/x-mixed-replace; boundary=frame") 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
