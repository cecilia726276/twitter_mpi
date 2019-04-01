# load json file from tiny Twitter with mpi

from mpi4py import MPI
import str_extract
import MelbGrid

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:  # define as root node, calculate the total number of lines given the json file, then divide the tasks into several processors.
    count = -1
    for count, line in enumerate(open("tinyTwitter(updated).json", "rU")):
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
with open("tinyTwitter(updated).json", "rU") as whole_data:
    line = whole_data.readline()
    # could resolve multiple cores issues, what if multiple nodes (scatter?)
    while line:
        cursor += 1
        if cursor > start_line and cursor <= end_line:
            coorstr_list = str_extract.regex(line, 1)
            if coorstr_list:
                coordList = coorstr_list[0].split(',')
                coord = [float(x) for x in coordList]
                x = coord[0]
                y = coord[1]
                hashtags_list = str_extract.regex(line, 2)
		if hashtags_list != None and len(hashtags_list) > 0:
                    mstr = "{" + hashtags_list[0] + "}"
                    try:
                        hash_dict = eval(mstr)
                    except Exception:
                        hash_dict = None
                else:
                    hash_dict = None

                a = 0  ###
                for i in range(0, len(gridList)):
                    if(gridList[i].checkInGrid(x, y)): # check the coordinates in which region
                        a = 1 ###
                        gridList[i].addpostcount()
                        if hash_dict != None:
                            for j in range(0, len(hash_dict["hashtags"])):
                                gridList[i].addhashtags(hash_dict["hashtags"][j]['text'])
                        break
                if a == 0:
                    print("not on the map:" + '[' + str(x) + ',' + str(y) + ']')
        # print "line from processor %d: " % rank
        # print line
        line = whole_data.readline()
for obj in gridList:
    print 'subprocess ' + str(rank) + ' ' + obj.id + ': ' + str(obj.postCount)

recv_objList = comm.gather(gridList, root = 0) # gather the grid list to No. 1 process.
if rank == 0:
    for i in range(1, len(recv_objList)):
        for j in range(0, len(gridList)):
			recv_objList[0][j].postCount += recv_objList[i][j].postCount
			# for key,value in recv_objList[i][j].hashtagsList.items():
			# 	if key in recv_objList[0][j].hashtagsList:
			# 		recv_objList[0][j].hashtagsList[key] += value
			# 	else:
			# 		recv_objList[0][j].hashtagsList[key] = value

	print "grid info from processor %d: " % rank
	for obj in recv_objList[0]:
		print obj.id + ': ' + str(obj.postCount)
		# print obj.hashtagsList

