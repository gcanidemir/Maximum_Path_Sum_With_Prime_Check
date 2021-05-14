import math


# Created by Görkem Canıdemir 13.05.2021
# !! Important Note: Please name the input file as "input.txt". !!


# Create 2D Array from the given input.
def form2DArray(fileName):
    anInputArray = []
    try:
        with open(fileName) as inputFile:
            lines = inputFile.readlines()
            for line in lines:
                lineElements = line.split()
                # Convert strings to integers.
                lineElements = list(map(int, lineElements))
                anInputArray.append(lineElements)
    except FileNotFoundError:
        print("ERROR: Please re-check the name of the file.")
    except Exception as e:
        print("ERROR:", end=' ')
        print(e)
    finally:
        aColumnLength = len(anInputArray)
        return anInputArray, aColumnLength


# Checks whether input is triangle or not.
def isInputTriangle(array):
    formerRowLength = 0
    for row in array:
        if formerRowLength >= len(row):
            print("Input is not a triangle.")
            return False
        formerRowLength = len(row)
    return True


# Find whether the number is prime or not.
def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number > 2 and number % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(number))
    for i in range(3, 1 + max_div, 2):
        if number % i == 0:
            return False
    return True


# If prime number found, change it with -1.
def findPrimeNumbers(array):
    # Check every element of the array whether it is prime or not.
    for row in range(len(array)):
        for column in range(len(array[row])):
            if isPrime(array[row][column]):
                array[row][column] = -1


# Param stands for parameter.
def maxPathSum(array, columnLengthParam):
    try:
        # If first number is prime number.
        if array[0][0] == -1:
            return 0

        # To fit the index system ([0], [1], etc.)
        columnLengthParam -= 1

        # Loop for bottom-up calculation
        for i in range(columnLengthParam - 1, -1, -1):
            for j in range(i + 1):
                # For each element, check both elements just below the number
                # and below right to the number add the maximum of them to it.
                # Check if parent node is prime.
                if array[i][j] != -1:
                    # Check if children are prime.
                    # Both are not prime.
                    if array[i + 1][j] != -1 and array[i + 1][j + 1] != -1:
                        if array[i + 1][j] > array[i + 1][j + 1]:
                            array[i][j] += array[i + 1][j]
                        else:
                            array[i][j] += array[i + 1][j + 1]
                    # Left child is prime.
                    elif array[i + 1][j] == -1 and array[i + 1][j + 1] != -1:
                        array[i][j] += array[i + 1][j + 1]
                    # Right child is prime.
                    elif array[i + 1][j] != -1 and array[i + 1][j + 1] == -1:
                        array[i][j] += array[i + 1][j]
                    # Both are prime.
                    elif array[i + 1][j] == -1 and array[i + 1][j + 1] == -1:
                        array[i][j] = -1

        # Return the top element which stores the maximum sum.
        return array[0][0]
    except:
        print("Something Happened while creating the array.")


# Driver Code
inputArray, columnLength = form2DArray("input.txt")
if isInputTriangle(inputArray):
    findPrimeNumbers(inputArray)
    total = maxPathSum(inputArray, columnLength)
    print("Maximum sum of the numbers with prime check: " + str(total))
