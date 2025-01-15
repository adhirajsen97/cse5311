#include <iostream>
#include <vector>
#include <list>
#include <string>

using namespace std;

// HashTable class template
class HashTable {
private:
    // Bucket: A vector of lists (for chaining)
    vector<list<pair<string, int>>> table;
    int numBuckets;  // Number of buckets

    // Hash function to calculate the bucket index
    int hashFunction(const string& key) {
        int hash = 0;
        for (char ch : key) {
            hash = (hash + ch) % numBuckets;  // Simple hash formula
        }
        return hash;
    }

public:
    // Constructor
    HashTable(int size) : numBuckets(size) {
        table.resize(numBuckets);  // Resize the table to hold 'size' buckets
    }

    // Insert a key-value pair into the hash table
    void insert(const string& key, int value) {
        int index = hashFunction(key);  // Get the bucket index
        auto& chain = table[index];    // Reference to the bucket (chain)

        // Check if the key already exists, update the value if it does
        for (auto& pair : chain) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }

        // If key does not exist, insert a new key-value pair
        chain.push_back({key, value});
    }

    // Search for a value by key
    int search(const string& key) {
        int index = hashFunction(key);  // Get the bucket index
        auto& chain = table[index];    // Reference to the bucket (chain)

        // Search for the key in the chain
        for (auto& pair : chain) {
            if (pair.first == key) {
                return pair.second;  // Return the value if key is found
            }
        }

        // If key is not found, throw an exception
        throw runtime_error("Key not found!");
    }

    // Remove a key-value pair from the hash table
    void remove(const string& key) {
        int index = hashFunction(key);  // Get the bucket index
        auto& chain = table[index];    // Reference to the bucket (chain)

        // Iterate through the chain to find the key
        for (auto it = chain.begin(); it != chain.end(); ++it) {
            if (it->first == key) {
                chain.erase(it);  // Remove the key-value pair
                return;
            }
        }

        // If key is not found, throw an exception
        throw runtime_error("Key not found for removal!");
    }

    // Display the hash table
    void display() {
        for (int i = 0; i < numBuckets; i++) {
            cout << "Bucket " << i << ": ";
            for (auto& pair : table[i]) {
                cout << "(" << pair.first << ", " << pair.second << ") ";
            }
            cout << endl;
        }
    }
};

// Main function
int main() {
    // Create a hash table with 5 buckets
    HashTable ht(5);

    // Insert key-value pairs
    ht.insert("Alice", 30);
    ht.insert("Bob", 25);
    ht.insert("Charlie", 35);
    ht.insert("Diana", 40);

    // Display the hash table
    cout << "Hash Table:" << endl;
    ht.display();

    // Search for a key
    try {
        cout << "\nValue for key 'Bob': " << ht.search("Bob") << endl;
    } catch (const exception& e) {
        cout << e.what() << endl;
    }

    // Remove a key
    try {
        ht.remove("Alice");
        cout << "\nAfter removing 'Alice':" << endl;
        ht.display();
    } catch (const exception& e) {
        cout << e.what() << endl;
    }

    return 0;
}
