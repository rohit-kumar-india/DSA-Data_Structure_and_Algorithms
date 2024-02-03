''' #Python
CF Link: https://www.codingninjas.com/studio/problems/data-type_8357232?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
Problem statement: Data type refers to the type of value a variable has and the way the computer interprets it.

Each data type has a different size. You’ve studied 5 different data types and the sizes of the data types:

Integer: 4 bytes
Long: 8 bytes
Float: 4 bytes
Double: 8 bytes
Character: 1 byte

You’re given a data type. Print its size in bytes.

Example :
Input: Long

Output: 8

Explanation: The size of a Long variable is given as 8 bytes.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
Long

Sample Output 1:
8

Explanation of sample input 1 :
The size of a Long variable is given as 8 bytes.

Sample Input 2:
Float

Sample Output 2:
4

Explanation of sample input 2 :
The size of a Float variable is given as 4 bytes.

Expected time complexity :
The expected time complexity is O(1).

Constraints :
type is one of the data types given above.

Time limit: 1 second'''


def dataTypes(type: str):
    if type == 'Integer' or type == "Float":
        return 4
    elif type == "Long" or type == "Double":
        return 8
    elif type == "Character":
        return 1
    
type=input()
print(dataTypes(type))