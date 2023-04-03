import heapq
# 用dijkstra找路径
class Map:
    def __init__(self,size=8):
        self.size=size
        self.map = []
        self.explored=[]
        self.setMap()

    def setMap(self):
        for y in range(self.size):
            row = []
            for x in range(self.size):
                row.append(0)
            self.map.append(row)
        self.map[0][3]=1
        self.map[1][3]=1
        self.map[2][3]=1
        self.map[3][3]=1

    def showMap(self):
        for i in range(self.size-1,-1,-1):
                print(self.map[i])

    def printExplored(self):
         for pos in self.explored:
              self.map[pos[1]][pos[0]]=6
         self.showMap()
         return 

class Node:
     def __init__(self) -> None:
          self.parent=None
          self.dis = 0

class Dijkstra:
     def __init__(self) -> None:
          self.tb = dict()
          self.pq = []
     
     def search(self,map:Map,start_pos=(0,0),end_pos=(1,1)):
          start_node = Node()
          self.tb[start_pos]=start_node
          index = 0
          map.explored.append(start_pos)
          heapq.heappush(self.pq,(0,index,start_pos))
          while self.pq:
               x,y,cur_node = heapq.heappop(self.pq)
               cur_x,cur_y = cur_node
               # # 到达终点提前退出
               if (cur_x,cur_y)==end_pos:
                    return
               for i in range(-1,2,1):
                    for j in range(-1,2,1):
                         nei_pos = (cur_x+i,cur_y+j)
                         # 跳过自己
                         if i==0 and j==0:
                              continue
                         # 超出边界的处理
                         if nei_pos[0]>=map.size or nei_pos[0]<0 or nei_pos[1]>=map.size or nei_pos[1]<0:
                              continue
                         # 障碍物处理
                         if map.map[nei_pos[1]][nei_pos[0]]==1:
                              continue
                         dis = self.tb[(cur_x,cur_y)].dis+(i*i+j*j)**0.5
                         if nei_pos not in self.tb or dis<self.tb[nei_pos].dis:
                              nei_node = Node()
                              nei_node.dis = dis
                              nei_node.parent=(cur_x,cur_y)
                              self.tb[nei_pos]=nei_node
                              index=index+1
                              map.explored.append(nei_pos)
                              heapq.heappush(self.pq,(dis,index,nei_pos))
          return 
     def printPath(self,map:Map,end_pos):
          path =[]
          pos = end_pos
          map.map[pos[1]][pos[0]]=8
          while self.tb[pos].parent:
               path.append(pos)
               pos = self.tb[pos].parent
               map.map[pos[1]][pos[0]]=8
          return path                    
               
     


     
if __name__=='__main__':
    map = Map()
    map.showMap()
    dijkstra = Dijkstra()
    start_pos = (1,1)
    end_pos = (6,1)
    dijkstra.search(map,start_pos,end_pos)
    dijkstra.printPath(map,end_pos)
    print('*************************')
    map.showMap()
    print('*************************')
    map.printExplored()
        