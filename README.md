# Data Science API

A flask application for accessing the recommender engine

## Usage

Details for accessing the API and expected responses

### Recommender

> URL: base_url/api/recommend/?

> Parameters: search=<string> (text to search by), qty=<int> (number of responses to return)

> Example: base_url/api/recommend/?search=some flowery blue bud&qty=10

*Responses* are in JSON format
