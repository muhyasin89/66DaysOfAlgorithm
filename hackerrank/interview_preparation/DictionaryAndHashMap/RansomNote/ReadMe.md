Reference:
<https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps>

===========================
what the problem? |||
===========================
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.

The words in his note are case-sensitive and he must use only whole words available in the magazine.

He cannot use substrings or concatenation to create the words he needs.

===========================
Can you Elaborate? |||
===========================
magazine= "attack at dawn" note= "Attack at dawn"

===========================
This Question Consist of? |||
===========================

The magazine has all the right words, but there is a case mismatch. The answer is NO

string: either Yes or No, no return value is expected

#### Input Format

The first line contains two space-separated integers, m and n, the numbers of words in the magazine and the note, respectively.
The second line contains m space-separated strings, each magazine[i].
The third line contains n space-separated strings, each note[i].
========================================
what the example? |
========================================
Sample Input 0

```
6 4
give me one grand today night
give one grand today
```

Sample Output 0

Yes
Sample Input 1

```
6 5
two times three is not four
two times two is four
```

Sample Output 1

No
Explanation 1

'two' only occurs once in the magazine.

Sample Input 2

```
7 4
ive got a lovely bunch of coconuts
ive got some coconuts
```

Sample Output 2

No
Explanation 2

Harold's magazine is missing the word some.

    ===================
    Information so far|
    ===================
    what is first 2 number used for?
    the first number is number of original world
    the second number is expected word

    ========================================
    unclear use?|
    ========================================
    how you decide which word to eliminate?

    ========================================
    how to solve problem?|
    ========================================


    ========================================
    how many step for solving this problem?|
    ========================================

    =====================================
    how many ways to solve this problem?|
    =====================================

    ===========================
    how long it takes? ||
    ===========================
