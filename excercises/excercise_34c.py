from memory_profiler import profile

@profile
def process_datac(raw_data):
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i])):
            yield raw_data[i][j].replace("$", "dollar")