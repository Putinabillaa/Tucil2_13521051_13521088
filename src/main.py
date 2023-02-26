import time
import Helper
import ClosestPoint_BruteForce

def main(): 
    # Input
    # Input banyaknya dimensi
    nDim = int(input("Enter dimensions: "))
    while(nDim < 2):
        print("Dimensions must larger than 1")
        nDim = input("Enter dimensions: ")

    # set range koordinat titik
    if(nDim == 2 or nDim == 3): 
        maxRange = 1000000.00
        minRange = -1000000.00
    else:
        maxRange = 1000.00
        minRange = -1000.00
    
    # Input banyaknya titik
    n = int(input("Enter number of points: "))
    while(n < 2):
        print("Number of points must larger than 1")
        n = int(input("Enter number of points: "))
    # Menu input koordinat titik
    print("How do you want to input the points' coordinates?")
    print("1. Randomize")
    print("2. Input File")
    choice = input(">>> ")
    while(choice != '1' and choice != '2'):
        print("You've inputed wrong choice, please choose 1 or 2!")
        choice = input(">>> ")

    # Pemanggilan method randomizer
    if(choice == '1'):
        points = Helper.ListRandomizer(nDim, n, maxRange, minRange)

    # Pemanggilan method read file
    else:
        points = Helper.ReadFile(nDim, n, maxRange, minRange)
        while (points == -1):
            points = Helper.ReadFile(nDim, n, maxRange, minRange)

    # Pemanggilan method bruteforce
    start_time = time.process_time()
    BF_minDist, BF_closestIdx, BF_totalOps = ClosestPoint_BruteForce.ClosestPoint_Bf(nDim, points, maxRange, minRange)
    BF_execTime = '%.5f'%(time.process_time() - start_time)

    # Pemangginan method DnC
    DnC_execTime = 0
    DnC_totalOps = 0

    # Pemanggilan method visualiser & Output
    print(BF_closestIdx)
    print("The Minimum Distance is: ")
    print("Between points: ")
    if(nDim == 3):
        print("Pair(s) of closest points indicated by different color")
        Helper.Visualizer3D(n, points, BF_closestIdx)
    elif(nDim == 2):
        print("Pair(s) of closest points indicated by different color")
        Helper.Visualizer2D(n, points, BF_closestIdx)      
    tableHead = ["No", "Metrics", "Brute Force", "Divide and Conquer"]
    print('---------------------------------------------------------------------------------')
    print('| {:2} | {:^26} | {:^20} | {:^20} |'.format(*tableHead))
    print('---------------------------------------------------------------------------------')
    table = [["1.", "Execution Time", str(BF_execTime) + " sec", str(DnC_execTime) + " sec"], ["2.", "Total Euclidean Operations", BF_totalOps, DnC_totalOps]]
    for row in table:
        print('| {:2} | {:<26} | {:^20} | {:^20} |'.format(*row))
    print('---------------------------------------------------------------------------------')
main()