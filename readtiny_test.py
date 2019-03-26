# load json file from tiny Twitter with mpi

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:  # define as root node, calculate the total number of lines given the json file, then divide the tasks into several processors.
    count = -1
    for count, line in enumerate(open("tinyTwitter.json", "rU")):
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
    end_line = start_line + rest
print "end_line = %d from processor %d" % (end_line, rank)

cursor = 0
with open("tinyTwitter.json", "rU") as whole_data:
    line = whole_data.readline()
    # could resolve multiple cores issues, what if multiple nodes (scatter?)
    while line:
        cursor += 1
        if cursor > start_line and cursor <= end_line:
            print "line from processor %d: " % rank
            print line
        line = whole_data.readline()
