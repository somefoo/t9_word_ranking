# t9_word_ranking

A quick & dirty collection of scripts that were used to rank words for T9 keyboard input. When entering a T9 key-combination, the word that is most frequent should be suggested by the auto-completer. This script tries to sort all words with a common T9 key combination based on word frequencies.

What is the idea?
1. Place all words with the same T9 encoding in the same list.
2. Sort each list by the frequency of the actual words.
3. Rank the words according to their position in the sorted lists.

The ranking information is based on word frequencies as obtained from books. For example from the Gutenberg [project](https://www.gutenberg.org/).

Can be with the Android application [TraditionalT9](https://github.com/Clam-/TraditionalT9). The ranked dictionaries in gutenberg/updated_files/*/ present a vast improvement over the default dictionary used by TraditionalT9!
