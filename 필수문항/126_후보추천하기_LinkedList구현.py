import sys

input = sys.stdin.readline

N = int(input())

num = int(input())

recs = list(map(int, input().split()))


class Node:
    def __init__(self, person, order):
        self.person = person
        self.order = order
        self.count = 1
        self.next = None
        self.back = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.order = 1
        self.size = 0

    def plus(self, person):
        global N
        # 첫 입력인경우
        if self.head is None:
            self.head = Node(person, self.order)
            self.order += 1
            self.size += 1
            return

        curr_node = self.head
        while curr_node != None:
            # 기존 리스트에 있던 경우
            if curr_node.person == person:
                curr_node.count += 1

                # 움직일 필요가 있는경우
                if not (
                    curr_node.next == None
                    or curr_node.next.count > curr_node.count
                    or (
                        curr_node.next.count == curr_node.count
                        and curr_node.next.order > curr_node.order
                    )
                ):
                    # 현재 노드가 헤드인경우 다음노드로 헤드 바꾼다
                    if curr_node == self.head:
                        self.head = curr_node.next
                        self.head.back = None
                    else:
                        curr_node.back.next = curr_node.next
                    found_node = curr_node
                    curr_node = curr_node.next
                    found_node.back = None
                    found_node.next = None

                    # curr_node 다음으로 집어넣도록
                    while curr_node.next != None and (
                        curr_node.next.count < found_node.count
                        or (
                            curr_node.next.count == found_node.count
                            and curr_node.next.order > found_node.order
                        )
                    ):
                        curr_node = curr_node.next
                    if curr_node.next == None:
                        curr_node.next = found_node
                        found_node.back = curr_node
                    else:
                        next_node = curr_node.next
                        curr_node.next = found_node
                        found_node.back = curr_node
                        found_node.next = next_node
                        next_node.back = found_node
                return
            else:
                curr_node = curr_node.next

        new_node = Node(person, self.order)
        self.order += 1

        # 기존 리스트에 없는경우
        # 꽉찬경우는 head pop
        if self.size == N:
            pop_node = self.head
            self.head = pop_node.next
            self.head.back = None
            pop_node = None
            self.size -= 1

        curr_node = self.head

        # head count가 1 초과면 바로 head에
        if curr_node.count != 1:
            curr_node.back = new_node
            new_node.next = curr_node
            self.head = new_node
        # 1이면 curr_node 뒤에
        else:
            while curr_node.next != None and curr_node.next.count == 1:
                curr_node = curr_node.next
            if curr_node.next == None:
                curr_node.next = new_node
                new_node.back = curr_node
            else:
                next_node = curr_node.next
                curr_node.next = new_node
                new_node.back = curr_node
                new_node.next = next_node
                next_node.back = new_node
        self.size += 1


l_list = LinkedList()

for r in recs:
    l_list.plus(r)

curr_node = l_list.head
ans = []
while curr_node != None:
    ans.append(curr_node.person)
    curr_node = curr_node.next

ans.sort()
print(*ans, sep=" ")
