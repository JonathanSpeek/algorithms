def isPalindrome(s):
    """Determines whether or not a string is a palindrome using recursion.
    """
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c.isalpha():
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
