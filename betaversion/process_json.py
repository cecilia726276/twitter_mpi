# load json file from tiny Twitter with mpi

from mpi4py import MPI
import str_extract_json
import MelbGrid
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    startTime = time.time()
# # We define process 0 as the root process,
# # calculate the total number of lines given the json file,
# # and distribute the tasks into several processors.
# if rank == 0:
#     startTime = time.time()
#     count = -1
#     for count, line in enumerate(open("file-0.json", "rU")):
#         pass
#     count += 1
#     # print "count = %d from processor %d" % (count, rank)
#
# # The master process broadcasts the total number of the lines.
# count = comm.bcast(count if rank == 0 else None, root=0)
# tasks = count / size
# # print "tasks = %d from processor %d" % (tasks, rank)
#
# # Each process decides on which line to start/end reading.
# start_line = rank * tasks
# # print "start_line = %d from processor %d" % (start_line, rank)
# end_line = 0
# if rank != size - 1 or (count % size == 0):
#     end_line = start_line + tasks
# else:
#     rest = count % size
#     # print "rest = %d from processor %d" % (rest, rank)
#     end_line = start_line + rest + tasks
# # print "end_line = %d from processor %d" % (end_line, rank)
#
# # Each processor scans melbGrid to initialize the grid.
gridList = MelbGrid.readMelbGrid("melbGrid.json")

# Start processing the data from twitter dataset
cursor = 0
with open("bigTwitter.json", "rU") as whole_data:
    for line in whole_data:
        cursor += 1
        if rank == cursor % size:
            m_list = str_extract_json.regex(line[:-1])
            if m_list[0] and len(m_list[0]) > 1:
                x = m_list[0][1]
                y = m_list[0][0]
                for i in range(0, len(gridList)):
                    # Get the grid box according to its coordinates
                    if gridList[i].checkInGrid(x, y):
                        gridList[i].addpostcount()
                        if m_list[1] and len(m_list[1]) > 0:
                            rephashtags = []
                            for j in range(0, len(m_list[1])):
                                hashstr = m_list[1][j]['text'].encode('utf-8').lower()
                                if hashstr in rephashtags:
                                    continue
                                gridList[i].addhashtags(hashstr)
                                rephashtags.append(hashstr)
                        break

recv_objList = comm.gather(gridList, root=0)  # gather the grid list to No. 1 process.
if rank == 0:
    for i in range(1, len(recv_objList)):
        for j in range(0, len(gridList)):
            recv_objList[0][j].postCount += recv_objList[i][j].postCount

            for key, value in recv_objList[i][j].hashtagsList.items():
                if key in recv_objList[0][j].hashtagsList:
                    recv_objList[0][j].hashtagsList[key] += value
                else:
                    recv_objList[0][j].hashtagsList[key] = value

    print "grid info from processor %d: " % rank

    sortedPosts = sorted(recv_objList[0], key=lambda grid: grid.postCount, reverse=True)
    for obj in sortedPosts:
        print obj.id + ': ' + str(obj.postCount) + ' posts'

    for obj in recv_objList[0]:
        obj.sortedDict = sorted(obj.hashtagsList.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
        # print obj.id + ': ' + str(obj.sortedDict)

        if obj.sortedDict:
            obj.topPost = obj.sortedDict[0]
        else:
            obj.topPost = ('null', 0)
    sortedHashTags = sorted(recv_objList[0], key=lambda grid: grid.topPost[1], reverse=True)

    for obj in sortedHashTags:
        rank = 1
        print ''
        print obj.id + ': ',
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
    print 'Execution time: ' + str(time.time() - startTime) + ' seconds'
