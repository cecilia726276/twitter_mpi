# load json file from bigTwitter with mpi

from mpi4py import MPI
import str_extract_json
import MelbGrid
# import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# This commented out code can be used to test the execution time of the program.
# However, using standard time library of linux will be more accurate.
# if rank == 0:
#    startTime = time.time()


# Define process 0 as the root process.
# Here the program processes the big data by module operation.
# Each process decides on which line to work on through
# seeing if the process id (rank) matches(=) the remainder.
# Remainder = n mod size  (n: the nth line, size: total number of process)

# First of all, each process scans melbGrid to initialize the grid.
gridList = MelbGrid.readMelbGrid("melbGrid.json")

# Start processing the data from twitter dataset:
# The cursor is used to indicate which line the process is reading.
cursor = 0
with open("bigTwitter.json", "rU") as whole_data:
    # read the file line by line
    for line in whole_data:
        cursor += 1
        # The process will work on the line where rank is equal to cursor % size.
        if rank == cursor % size:
            # If the line matches, extract the hashtags and coordinates.
            m_list = str_extract_json.regex(line[:-1])
            if m_list[0] and len(m_list[0]) > 1:
                # type of x & y: float
                x = m_list[0][1]
                y = m_list[0][0]
                for i in range(0, len(gridList)):
                    # Check which grid box this coordinate(x,y) belongs to
                    if gridList[i].checkInGrid(x, y):
                        gridList[i].addpostcount()
                        # If the point is in the gridbox, increase its count by 1.
                        if m_list[1] and len(m_list[1]) > 0:
                            # Collect hashtags into corresponding gridbox.
                            # rephashtags is used to remove duplicated hashtags in one twitter object
                            rephashtags = []
                            for j in range(0, len(m_list[1])):
                                hashstr = m_list[1][j].encode('utf-8').lower()
                                if hashstr in rephashtags:
                                    continue
                                gridList[i].addhashtags(hashstr)
                                rephashtags.append(hashstr)

                        break
# Gather the grid list to No. 0 process.
recv_objList = comm.gather(gridList, root=0)
if rank == 0:
    for i in range(1, len(recv_objList)):
        for j in range(0, len(gridList)):
            # Accumulate the post count and hashtags counts of each grid from every process.
            recv_objList[0][j].postCount += recv_objList[i][j].postCount

            # The hashtags and its count is stored in the form of dictionary.
            for key, value in recv_objList[i][j].hashtagsList.items():
                if key in recv_objList[0][j].hashtagsList:
                    recv_objList[0][j].hashtagsList[key] += value
                else:
                    recv_objList[0][j].hashtagsList[key] = value

    print "grid info from processor %d: " % rank

    # Sort the post count.
    sortedPosts = sorted(recv_objList[0], key=lambda grid: grid.postCount, reverse=True)

    # Sort the number of occurrences of those hashtag of each grid.
    for obj in recv_objList[0]:
        obj.sortedDict = sorted(obj.hashtagsList.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

    # Order (rank) the top 5 hashtags in each Grid and print the outcome out.
    for obj in sortedPosts:
        rank = 1
        print ''
        print obj.id + ': '+ str(obj.postCount) + ' posts  ',
        preValue = 0
        for hashTag in obj.sortedDict:
            if hashTag[1] != preValue:
                if rank == 6:
                    break
                print '#' + str(rank) + str(hashTag),
                preValue = hashTag[1]
                rank += 1
            else:
                print '#' + str(rank - 1) + str(hashTag),
    print ''
    # The commented out code can be used to test the execution time.
    # print 'Execution time: ' + str(time.time() - startTime) + ' seconds'
