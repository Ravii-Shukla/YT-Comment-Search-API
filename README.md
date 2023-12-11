# Flask Comment Search API

This Flask application provides an API endpoint to search comments from a YouTube video fetched from [https://app.ylytic.com/ylytic/test](https://app.ylytic.com/ylytic/test).

## API Endpoint

### `/search`

- **Method:** GET
- **Parameters:**
  - `search_author`: Search comments by author name.
  - `at_from` and `at_to`: Search comments within a date range.
  - `like_from` and `like_to`: Search comments based on the number of likes.
  - `reply_from` and `reply_to`: Search comments based on the number of replies.
  - `search_text`: Search comments by text content.

### Example

```bash
 "http://localhost:5000/search?search_author=fedrick"
