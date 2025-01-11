from typing import List, Dict
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Step 1: Convert each word into a dictionary of character counts
        word_counts = [Counter(word) for word in words]
        
        # Step 2: Create a dictionary of available letters and their counts
        letter_counts = Counter(letters)
        
        # Step 3: Function to calculate the score of a word
        def calculate_word_score(word_count: Counter) -> int:
            return sum(score[ord(char) - ord('a')] * count for char, count in word_count.items())
        
        # Step 4: Backtracking to find the maximum score
        def backtrack(index: int, available_letters: Counter) -> int:
            if index == len(words):  # Base case: no more words to process
                return 0
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1, available_letters)
            
            # Option 2: Use the current word if possible
            word_count = word_counts[index]
            if all(available_letters[char] >= count for char, count in word_count.items()):
                # Deduct the word's letters from available_letters
                new_available_letters = available_letters - word_count
                # Calculate score of this word
                current_score = calculate_word_score(word_count)
                # Include the current word and recurse
                max_score = max(max_score, current_score + backtrack(index + 1, new_available_letters))
            
            return max_score
        
        # Start backtracking from the first word
        return backtrack(0, letter_counts)
