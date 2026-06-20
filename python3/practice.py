#!/usr/python3

import heapq
# from absl import app

heap = []
l = [2, 5, 14, 54, 8, 23, 31, 18]
for num in l:
  heapq.heappush(heap, num)

while heap:
  print(heapq.heappop(heap))

def main():
  print("hello world")

print("1 hello world")
if __name__ == '__main__':
  # app.run(main)
  main()
