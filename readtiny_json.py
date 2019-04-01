# load json file from tiny Twitter with mpi

from mpi4py import MPI
import str_extract2
import MelbGrid

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:  # define as root node, calculate the total number of lines given the json file, then divide the tasks into several processors.
    count = -1
    for count, line in enumerate(open("file-0.json", "rU")):
        pass
    count += 1
    print "count = %d from processor %d" % (count, rank)

# The master process broadcasts the total number of the lines.
count = comm.bcast(count if rank == 0 else None, root=0)
tasks = count / size
print "tasks = %d from processor %d" % (tasks, rank)

start_line = rank * tasks
print "start_line = %d from processor %d" % (start_line, rank)
end_line = 0
if rank != size - 1 or (count % size == 0):
    end_line = start_line + tasks
else:
    rest = count % size
    print "rest = %d from processor %d" % (rest, rank)
    end_line = start_line + rest + tasks
print "end_line = %d from processor %d" % (end_line, rank)

# each processor scan melbGrid to initial grid object first
gridList = MelbGrid.readMelbGrid("melbGrid.json")

# now start to process data from twitter dataset
cursor = 0
with open("file-0.json", "rU") as whole_data:
    line = whole_data.readline()
    # could resolve multiple cores issues, what if multiple nodes (scatter?)
    while line:
        cursor += 1
        if cursor > start_line and cursor <= end_line:
            m_list = str_extract2.regex(line[:-2])
            if m_list[0] and len(m_list[0]) > 1:
                x = m_list[0][1]
                y = m_list[0][0]
                print('x: ' + str(x) + ' y: ' + str(y))
                for i in range(0, len(gridList)):
                    if(gridList[i].checkInGrid(x, y)): # check the coordinates in which region
                        gridList[i].addpostcount()
                        if m_list[1] and len(m_list[1]) > 0:
                            for j in range(0, len(m_list[1])):
                                gridList[i].addhashtags((m_list[1][j]['text'].encode('utf-8')))
                        break
        # print "line from processor %d: " % rank
        # print line
        line = whole_data.readline()

    print "grid info from processor %d: " % rank
    for obj in gridList:
	print obj.id
	print obj.postCount
	print obj.hashtagsList
