def checkio(text: str) -> str:
    letters_freq = {}

    for l in text.lower():
        if l.isalpha():
            letters_freq[l] =  letters_freq.get(l, 0) + 1

    sorted_lettes_freq = sorted(letters_freq.items(), key=lambda v: (-v[1], v[0]))

    return sorted_lettes_freq[0][0]

# Better implementation
import string

def checkio(text: str) -> str:
    text = text.lower() = text.lower()
    return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
