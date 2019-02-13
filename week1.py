def path_finder(matrix):
    def bfs(maze, node):
    #queue needs to be a list in a list and needs to be FIFO
        queue = [[node]]
    #we need an empty list to add to
        explored = []
        #a way to start at the last edge of the maze
        goal = [len(maze)+1, len(maze)+1]
    #cycle queue until its done
        while queue:
        #first in first out because its a queue
        #path pops out the starting
            way = queue.pop(0)
            node = way[:-1]
        #now want to check if we have searched path before because we want it to search the path
            if node not in explored:
                explored.append(node)
            #layer one connections to node
            #prints out list of possible places
                edges = path_finder(matrix)
                for edge in edges:
                #new_list is an array that
                    new_list = list(way)
                    new_list.append(edge)
                    queue.append(new_list)
                    if edge == goal:
                        return False
                    #because new_list are cordinates so need x,y
                        for x,y in new_list:
                            if maze[x][y] == "w":
                                return True
                            else:
                                return False
                                #because when  while queue is empty it cant return a true so has to be false
        return False

        return False
