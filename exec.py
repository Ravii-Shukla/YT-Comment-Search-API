from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def fetch_comments():

    api_url = "https://app.ylytic.com/ylytic/test"

    try:
        # Make a GET request to the our api URL
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response content as JSON
            data = response.json()

            # Extracting comments from the data
            comments = data.get("comments", [])

            # Getting query parameters
            search_author = request.args.get('search_author')
            at_from = request.args.get('at_from')
            at_to = request.args.get('at_to')
            like_from = request.args.get('like_from')
            like_to = request.args.get('like_to')
            reply_from = request.args.get('reply_from')
            reply_to = request.args.get('reply_to')
            search_text = request.args.get('search_text')

            # Applying filters
            filtered_comments = comments
            if search_author:
                filtered_comments = [comment for comment in filtered_comments if search_author.lower() in comment['author'].lower()]
            if at_from:
                filtered_comments = [comment for comment in filtered_comments if comment['at'] >= at_from]
            if at_to:
                filtered_comments = [comment for comment in filtered_comments if comment['at'] <= at_to]
            if like_from:
                filtered_comments = [comment for comment in filtered_comments if comment['like'] >= int(like_from)]
            if like_to:
                filtered_comments = [comment for comment in filtered_comments if comment['like'] <= int(like_to)]
            if reply_from:
                filtered_comments = [comment for comment in filtered_comments if comment['reply'] >= int(reply_from)]
            if reply_to:
                filtered_comments = [comment for comment in filtered_comments if comment['reply'] <= int(reply_to)]
            if search_text:
                filtered_comments = [comment for comment in filtered_comments if search_text.lower() in comment['text'].lower()]
        
            return jsonify(filtered_comments)

        # If the request was not successful, return an error response
        return jsonify(
            {"error": f"Failed to fetch comments. Status code: {response.status_code}"}
        )

    except Exception as e:
        # Handle exceptions (e.g. network errors, invalid JSON, etc.)
        return jsonify({"error": f"An error occurred: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)