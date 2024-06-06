from memory_profiler import profile

@profile
def process_dataa(raw_data):
    l = []
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i])):
            l.append(raw_data[i][j].replace("$", "dollar"))
    return l