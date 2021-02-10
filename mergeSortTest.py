import time
import sys

def merge(left, right, count,qu,printThis,moveCounts):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    print('l ' + str(left))
    print('r ' + str(right))
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            try:
                moveCounts[left[index_left]] += 1
                if moveCounts[left[index_left]] > 2:
                    printThis[0] = 'Too chaotic'
            except:
                moveCounts[left[index_left]] = 1
            if left[index_left]>right[-1] and len(right) > 2:
                printThis[0] = 'Too chaotic'
            result.append(right[index_right])
            index_right += 1
            count[0] += len(left) - index_left
            
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    print(result)
    return result

def merge_sort(array,count,qu,printThis,moveCounts):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    #print('L ' + str(array[:midpoint]))
    #print('R ' + str(array[midpoint:]))
    return merge(left=merge_sort(array[:midpoint],count,qu,printThis,moveCounts),right=merge_sort(array[midpoint:],count,qu,printThis,moveCounts),count=count,qu=qu,printThis=printThis,moveCounts=moveCounts)



def main():
    count = [0]
    printThis = ['']
    longQueue = ''
    moveCounts = {}
    
    #qa = [1,2,3,5,7,8,6,4]
    #qb = [1,2,3,5,4,6,8,7]
    #qc = [1,2,4,5,3]
    #merged = merge_sort(qc,count,qc,printThis)
    #print(count[0])

    readFile = open('chaosInput.txt','r')
    #printFile = open('printFile.txt','w')
    #inputQ = readFile.split()
    for line in readFile:
        longQueue += line
    #print(longQueue,file=printFile)
    #printFile.close()
    readFile.close()

    #readFile = open('chaosInput.txt','r')
    #printFile = open('printFile.txt','w')
    #inputQ = readFile.split()
    #for line in readFile:
    #    longQueue += line
    #print(longQueue,file=printFile)
    #printFile.close()
    #readFile.close()

    #longQ = list(map(int, longQueue.rstrip().split()))
    longQ = [2,5,1,3,4]
    #longQcpy = longQ.copy()
    t1Merge = time.time()
    
    merged = merge_sort(longQ,count,longQ,printThis,moveCounts)
    if printThis[0] == '':
        print(count[0])
    else:
        print(printThis)
    t2Merge = time.time()

    print(str(t2Merge - t1Merge))
    
    #t1Merge = time.time()
    #merged = merge_sort(longQ)
    #t2Merge = time.time()
    #t1Sort = time.time()
    #sor = longQcpy.sort(reverse=False)
    #t2Sort = time.time()

    #print(sys.getsizeof(merged))
    #print(sys.getsizeof(sor))

    #print(str(len(longQ)) + str(t2Merge - t1Merge))
    #print(str(len(longQcpy)) + str(t2Sort - t1Sort))

main()
