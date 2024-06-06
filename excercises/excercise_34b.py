from memory_profiler import profile
#correct answer!!
@profile
def process_datab(raw_data):
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i])):
            return raw_data[i][j].replace("$", "dollar")