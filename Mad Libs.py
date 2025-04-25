def mad_libs():
    print("📝 Welcome to the Mad Libs Generator!")
    print("Please provide the following words:\n")

    # Ask user for words
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb (present tense): ")
    adverb = input("Adverb: ")
    place = input("Place: ")
    animal = input("Animal: ")

    # Template story
    story = f"""
    One day, a {adjective} {animal} appeared in the middle of {place}.
    It looked right at the {noun} and started to {verb} {adverb}.
    Everyone around was shocked, but it was the best day ever!
    """

    print("\n🎉 Here's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
