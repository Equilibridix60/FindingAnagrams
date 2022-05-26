def is_anagram(s1, s2):
    print(sorted(s1), sorted(s2))
    if (sorted(s1) == sorted(s2)):
        print(sorted(s1), sorted(s2))
        return True
    return False

print(is_anagram("armed", "dream"))        