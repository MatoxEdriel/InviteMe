import os
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)


frames_folder = os.path.join(os.path.dirname(__file__), "static", "videos", "FramesSaludos")

print("Buscando en:", frames_folder)

frames = [Image.open(os.path.join(frames_folder, f"frame{i}.png")) for i in range(1, 7)]


gif_output = os.path.join(os.path.dirname(__file__), "static", "videos", "saludo_animado.gif")
if not os.path.exists(gif_output):
    frames[0].save(
        gif_output,
        save_all=True,
        append_images=frames[1:],
        duration=200,
        loop=0
    )


@app.route("/", methods=["GET", "POST"])
def home():
    nombre = ""
    if request.method == "POST":
        nombre = request.form.get("nombre")
    return render_template("index.html", nombre=nombre)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)