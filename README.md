# Autocomplete Service

## Introduction
This repository contains a simple autocomplete service implemented in Python using Flask and a trie data structure. The service is designed to provide query suggestions based on prefixes input by users, similar to the functionality seen in search engines like Google. 
The data can be downloaded from here: https://drive.google.com/file/d/17L5fLvdni029_M2dmV0BYxtfE6y0At8Y/view?usp=sharing

## Design Decisions

### Trie Data Structure
The core of the autocomplete functionality is based on a trie, chosen for its efficient prefix-based query retrieval. Each node in the trie represents a character of the alphabet, and nodes are linked in a way that represents the queries and their respective frequencies.

### Case Insensitivity
The queries are stored in a case-insensitive manner to ensure that the autocomplete suggestions are consistent regardless of the case of the input text.

### Scoring and Sorting
Each query is associated with a frequency score representing its popularity. The search function returns suggestions sorted by these scores in descending order to ensure that the most relevant suggestions are presented first.

## Testing

### Unit Testing
Unit tests have been written to test individual components of the service, such as trie insertion and query retrieval.

### Integration Testing
Integration tests involve sending HTTP requests to the Flask service and verifying the JSON response matches the expected autocomplete suggestions.

### Load Testing
Load testing was conducted to ensure the service can handle a high number of simultaneous requests without significant latency.

## Performance

### Response Time
The trie data structure provides quick lookup times, which helps maintain a low response time for the autocomplete suggestions.

### Scalability
While the current dataset is relatively small and directly included in the source code for simplicity, the service is designed to scale with a larger dataset that can be read from a file or a database.

### Optimization
To further optimize performance, a caching layer could be implemented to cache popular queries and reduce the time taken to retrieve these suggestions.

## Usage
To use the service, start the Flask application and send a GET request to the `/s` endpoint with a query parameter `q` representing the search prefix.

Example: `http://localhost:5000/s?q=how`

## Future Enhancements

### Caching
Implement caching for frequently requested queries to improve response times.

### Fuzzy Matching
Introduce fuzzy matching capabilities to handle typos and provide relevant suggestions despite input errors.

### Analytics
Integrate an analytics system to track query popularity and adjust suggestions based on real-time data.

## Conclusion
This autocomplete service is a basic implementation designed to showcase the functionality with a focus on data structures and algorithmic efficiency. It is not intended for production use without further development and optimization.
