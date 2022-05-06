
# 4.	Implement a simple priority queue.

# Assume an incoming stream of dictionaries containing two keys;
# command to be executed and priority.

# Priority is an integer value [0, 10],
# where work items of the same priority are processed in the order they are received.

import heapq

#Two keys command(str) and priority(int) with vaue of work item (str)
jobs_dict = {(1 ,'command_1'): "work item 1", (2 , 'command_2'): "work item 2",
             (3, 'command_3'): "work item 3", (2, 'command_4'): "work item 4",
             (5, 'command_5'): "work item 5", (1, 'command_6'): "work item 6",
             (10, 'command_7'): "work item 7", (1, 'command_8'): "work item 8"}

def sort_jobs(dict):
    """Sort a given dictionary"""
    dict_items = dict.items()
    sorted_items = sorted(dict_items)

    return sorted_items

def priority_queue(dict):
    """Add add items from a dictionary to heap by priority"""

    jobs_sorted = sort_jobs(dict)

    prioritized_list = []

    for items in jobs_sorted:
        heapq.heappush(prioritized_list, items[0])

    return [heapq.heappop(prioritized_list) for i in range(len(prioritized_list))]

def run():
    queued_jobs = priority_queue(jobs_dict)

    while queued_jobs:
        print(heapq.heappop(queued_jobs))


if __name__ == '__main__':
    run()
    
    
