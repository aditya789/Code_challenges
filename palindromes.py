'''Challenge 2

In the block of text below, find the longest substring that is the same in reverse (palindrome). As an example, if the input was "Ilikeracecarsthatgofast" the answer would be "racecar".

Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceiv
edinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedi
nagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo
ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionoft
hatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto
getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotco
nsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco
nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongre
memberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobed
edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedI
tisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore
ddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevoti
onthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod
shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh
allnotperishfromtheearth


Python Version :: Python 3.11.3'''

def longestPalindrome(texts):

    def inner_wrapper(text, left, right):
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return text[left + 1:right]

    longest_palindrome = ""
    for i in range(len(texts)):
        palindrome_odd = inner_wrapper(texts, i, i)
        palindrome_even = inner_wrapper(texts, i, i + 1)
        longest_palindrome = max(longest_palindrome, palindrome_odd, palindrome_even, key=len)
    return longest_palindrome


# calling the function
print(longestPalindrome('Ilikeracecarsthatgofast'))
print(longestPalindrome('Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceiv'
'edinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedi'
'nagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo'
'ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionoft'
'hatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto'
'getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotco'
'nsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco'
'nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongre'
'memberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobed'
'edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedI'
'tisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore'
'ddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevoti'
'onthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod'
'shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh'
'allnotperishfromtheearth'
))
