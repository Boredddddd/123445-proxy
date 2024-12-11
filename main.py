from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def proxy():
    # Get target URL from the request
    target_url = request.args.get("url")
    if not target_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    try:
        # Forward the request
        if request.method == "GET":
            response = requests.get(target_url, params=request.args)
        elif request.method == "POST":
            response = requests.post(target_url, data=request.form)

        # Return the response content
        return (response.content, response.status_code, response.headers.items())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
