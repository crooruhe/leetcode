class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> results;

        // need to keep track of which combination leads to which vector like a unique address
        // going to sort the letters alphabetically and then use that as a key to a map
        // each key should be unique except when the word is an anagram of a word already in the map
        // even if it has repeat letters the key will be different

        // this map represents a unique key (sorted string entry)
        // and the value is the array of strings that match that anagram group

        map<string, vector<string>> anagramGroups;
        for(string const & originalEntry : strs){

            string sortedEntry = originalEntry;
            sort(sortedEntry.begin(), sortedEntry.end());

            cout << "\"" << originalEntry << "\" has been sorted into \"" << sortedEntry << "\"" << endl;

            vector<string> singleEntry;
            singleEntry.push_back(originalEntry);

            pair<map<string,vector<string>>::iterator, bool> insertionResult = anagramGroups.try_emplace(sortedEntry, singleEntry);
            map<string,vector<string>>::iterator location = insertionResult.first;
            bool insertSucceeded = insertionResult.second;

            if(insertSucceeded) {
                cout << "No existing anagram found for \"" << originalEntry << "\". Creating new list..." << endl;
            }
            else {
                cout << "Found existing anagram for \"" << originalEntry << "\". Appending to list..." << endl;
                location->second.push_back(originalEntry);
            }
        }

        for (auto const & [sorted, entries] : anagramGroups) {
            cout << sorted << " => ";
            for (string const entry : entries) {
                cout << entry << " ";
            }
            cout << endl;
            results.push_back(entries);
        }

        return results;
    }
};