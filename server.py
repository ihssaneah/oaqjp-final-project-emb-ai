from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector 
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detect():
    textToAnalyze = request.args.get('textToAnalyze')
    response = emotion_detector(textToAnalyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return f"For the given statement, the system response is " \
       f"'anger': , 'disgust': , 'fear':, " \
       f"'joy': , and 'sadness': .\nThe dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

