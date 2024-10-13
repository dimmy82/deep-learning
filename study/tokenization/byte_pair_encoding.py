from collections import Counter
from collections.abc import Sequence


class Tokenizer:
    def __init__(self, words: Sequence[str]):
        self.vocab: dict[str, int] = {
            char: 0 for char in set(self.chars(words))}
        self.word_chars: dict[str, list[str]] = {
            word: self.chars([word]) for word in words}
        self.words = words

    def chars(self, strings: Sequence[str]) -> list[str]:
        chars = list()
        for string in strings:
            for char in string:
                chars.append(char)
        return chars

    def most_frequent_char_pair(self) -> tuple[tuple[str, str], int]:
        char_pair_frequence: Counter = Counter()
        for word in self.words:
            chars_in_word = self.word_chars[word]
            for i in range(len(chars_in_word) - 1):
                char_pair = (chars_in_word[i], chars_in_word[i + 1])
                char_pair_frequence[char_pair] += 1
        return char_pair_frequence.most_common(1)[0]

    def merge_char_pair(self, char_pair: tuple[str, str]) -> None:
        left_char, right_char = char_pair
        for word, chars_in_word in self.word_chars.items():
            i = 0
            while i < len(chars_in_word) - 1:
                if left_char == chars_in_word[i] and right_char == chars_in_word[i+1]:
                    chars_in_word = chars_in_word[:i] + \
                        [left_char + right_char] + chars_in_word[i+2:]
                i += 1
            self.word_chars[word] = chars_in_word

    def tokenize(self, round: int) -> None:
        for _ in range(round):
            (left_char, right_char), frequence = self.most_frequent_char_pair()
            self.merge_char_pair((left_char, right_char))
            self.vocab[f"({left_char},{right_char})"] = frequence


if __name__ == "__main__":
    words = ["たのしい", "たのしい", "たのしい", "たのしい", "たのしい", "たのしい",
             "たのしさ", "たのしさ",
             "うつくしい", "うつくしい", "うつくしい", "うつくしい",
             "うつくしさ",
             "いそがしい", "いそがしい", "いそがしい"]
    tokenizer = Tokenizer(words)
    tokenizer.tokenize(9)
    print(tokenizer.vocab)
