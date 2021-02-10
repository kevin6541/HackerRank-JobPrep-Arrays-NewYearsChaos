import threading
import time
#import thread


def run(q,printThis,count,total):
    for i in range(len(q)-1,-1,-1):
        if i != q.index(i+1):
            if i - q.index(i+1) > 2:
                printThis = 'Too chaotic'
                break
            else:
                total += i - q.index(i+1) 
                q.insert(i, q.pop(q.index(i+1)))
                printThis = total
                #print(q)
    print(printThis)

def runA(qa,printThis,count,total):
    for i in range(len(qa)-1,-1,-1):
        if i != qa.index(i+1):
            moveIndex = qa.index(i+1)
            moveThis = qa[moveIndex]
            if i - moveIndex > 2:
                printThis = 'Too chaotic'
                break
            else:
                total += i - moveIndex
                sliceA = qa[:moveIndex]
                #print('A: ' + str(sliceA))
                sliceB = qa[moveIndex+1:i+1]
                #print('B: ' + str(sliceB))
                sliceB.append(moveThis)
                #print('B-app: ' + str(sliceB))
                if len(qa) - 1 == i:#at the end
                    qa = sliceA + sliceB
                    #print('q-Bend: ' + str(q))
                else:
                    sliceC = qa[i+1:]
                    #print('C: ' + str(sliceC))
                    qa = sliceA + sliceB + sliceC
                    #print('q-Cend: ' + str(q))
                #q.insert(i,q.pop(move))
                printThis = total
                #print(q)
                
    print(str(printThis) + '\n')
    #return True
    

def runB(qb,printThis,count,total):
    for i in range(len(qb)-1,-1,-1):
        if i != qb.index(i+1):
            moveIndex = qb.index(i+1)
            moveThis = qb[moveIndex]
            if i - moveIndex > 2:
                printThis = 'Too chaotic'
                break
            else:
                total += i - moveIndex
                sliceA = qb[:moveIndex]
                #print('A: ' + str(sliceA))
                sliceB = qb[moveIndex+1:i+1]
                #print('B: ' + str(sliceB))
                sliceB.append(moveThis)
                #print('B-app: ' + str(sliceB))
                if len(qb) - 1 == i:#at the end
                    qb = sliceA + sliceB
                    #print('q-Bend: ' + str(q))
                else:
                    sliceC = qb[i+1:]
                    #print('C: ' + str(sliceC))
                    qb = sliceA + sliceB + sliceC
                    #print('q-Cend: ' + str(q))
                #q.insert(i,q.pop(move))
                printThis = total
                #print(q)
                
    print(str(printThis) + '\n')
    #return True

def run1(q,printThis,count,total,p,t_1):
    for i in range(len(q)-1,-1,-1):
        if i != q.index(i+1):
            moveIndex = q.index(i+1)
            moveThis = q[moveIndex]
            if i - moveIndex > 2:
                printThis = 'Too chaotic'
                break
            else:
                total += i - moveIndex
                sliceA = q[:moveIndex]
                #print('A: ' + str(sliceA))
                sliceB = q[moveIndex+1:i+1]
                #print('B: ' + str(sliceB))
                sliceB.append(moveThis)
                #print('B-app: ' + str(sliceB))
                if len(q) - 1 == i:#at the end
                    q = sliceA + sliceB
                    #print('q-Bend: ' + str(q))
                else:
                    sliceC = q[i+1:]
                    #print('C: ' + str(sliceC))
                    q = sliceA + sliceB + sliceC
                    #print('q-Cend: ' + str(q))
                #q.insert(i,q.pop(move))
                printThis = total
                #print(q)
                
    print(str(p) + str(printThis) + str(t_1 - time.time()))
    #return True

def run2(q,printThis,count,total,p,t_1):
    for i in range(len(q)-1,-1,-1):
        if i != q.index(i+1):
            moveIndex = q.index(i+1)
            moveThis = q[moveIndex]
            if i - moveIndex > 2:
                printThis = 'Too chaotic'
                break
            else:
                total += i - moveIndex
                sliceA = q[:moveIndex]
                #print('A: ' + str(sliceA))
                sliceB = q[moveIndex+1:i+1]
                #print('B: ' + str(sliceB))
                sliceB.append(moveThis)
                #print('B-app: ' + str(sliceB))
                if len(q) - 1 == i:#at the end
                    q = sliceA + sliceB
                    #print('q-Bend: ' + str(q))
                else:
                    sliceC = q[i+1:]
                    #print('C: ' + str(sliceC))
                    q = sliceA + sliceB + sliceC
                    #print('q-Cend: ' + str(q))
                #q.insert(i,q.pop(move))
                printThis = total
                #print(q)
                
    print(str(p) + str(printThis) + str(t_1 - time.time()))
    #return True



def main():
    total = 0
    count = 0
    printThis = ''

    longQueue = ''
    
    #qa = [1,2,3,5,7,8,6,4]
    #qb = [1,2,3,5,4,6,8,7]

    readFile = open('chaosInput.txt','r')
    #printFile = open('printFile.txt','w')
    #inputQ = readFile.split()
    for line in readFile:
        longQueue += line
    #print(longQueue,file=printFile)
    #printFile.close()
    readFile.close()

 
    longQ = list(map(int, longQueue.rstrip().split()))
    longQcpy = longQ.copy()

    threadNames = ['1','2']
    threadQs = [longQ,longQcpy]

    threads = []
    
    #print(len(longQ))
    #print(longQ[-1])
    #t_1 = time.time()
    #t = threading.Thread(target=run1, args=(longQ,printThis,count,total,1,t_1))
    #t2 = threading.Thread(target=run2, args=(longQcpy,printThis,count,total,2,t_1))
    #t.start()
    #t2.start()
    run(longQ,printThis,count,total)
    #for i in range(2):
        #threadNames[i] = threading.Thread(target=run, args=(threadQs[i],printThis,count,total,i,t_1))
        #t = threading.Thread(target=run, args=(threadQs[i],printThis,count,total,i,t_1))
        #threads.append(t)
        #t.start()
        #threadNames[i].start()
    #threadNames[0].join()
    #threadNames[1].join()
    #t.join()

    #longQ.sort()
    #t_2 = time.time()
    
    #cpuTime = (t_2-t_1)/60
    #print(cpuTime)
    
    #print(longQ)
    

    #queues = [qa,qb]
    #threadNames = ['q1','q2']

    #for i in range(len(queues)):
    #    threadNames[i] = threading.Thread(target=run, args=(queues[i],printThis,count,total,))
    #    threadNames[i].start()

    #threadNames[0].join()

    #thread1 = threading.Thread(target=runA, args=(qa,printThis,count,total,))
    #thread2 = threading.Thread(target=runB, args=(qb,printThis,count,total))

    #thread1.start()
    #thread2.start()
    #thread1.join()
    #thread2.join()

    

    #thread.start_new_thread(run2(qa,printThis,count,total))
    #thread.start_new_thread(run2(qb,printThis,count,total))
    #run2(q,printThis,count,total)

main()
