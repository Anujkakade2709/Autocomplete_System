from flask import Flask, jsonify, request

app = Flask(__name__)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.score = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, query, score):
        node = self.root
        for char in query:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        node.score = score

    def _search(self, node, prefix):
        results = []
        if node.end_of_word:
            results.append((prefix, node.score))

        for char, next_node in node.children.items():
            results.extend(self._search(next_node, prefix + char))
        return results

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._search(node, prefix)

trie = Trie()

# Function to read queries from a file and insert into the Trie
def load_queries_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            query, score = line.rsplit(None, 1)
            trie.insert(query.lower(), int(score))

# Replace 'queries.txt' with the path to your file containing the queries and scores
load_queries_from_file('medical-questions')

@app.route('/s')
def autocomplete():
    q = request.args.get('q', '').lower()
    results = trie.search(q)
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    suggestions = [query for query, score in sorted_results]
    return jsonify({"q": q, "d": suggestions[:4]})  # Return top 4 results

if __name__ == '__main__':
    app.run(debug=True)
