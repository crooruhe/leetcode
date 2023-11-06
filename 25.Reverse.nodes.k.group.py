# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp_node = ListNode(-1)
        prev_node = ListNode(-1)
        counter_node = ListNode(-1)
        result = head
        k_nodes = []
        temp_node.next = head
        counter_node.next = head
        length_total = 0

        while(counter_node.next != None):
            counter_node.next = counter_node.next.next
            length_total += 1

        reverse_num = length_total // k

        for i in range(reverse_num):
            k_nodes = []
            for nodehops in range(k):
                k_nodes.append(temp_node.next)
                temp_node.next = temp_node.next.next

            if(head == k_nodes[0]):
                result = k_nodes[-1]

            for n in range(k):
                idx = k - 1 - n
                if(k_nodes[idx - 1] != None):
                    k_nodes[idx].next = k_nodes[idx - 1]
                    if (prev_node.next != None):
                        prev_node.next.next = k_nodes[idx]
                        prev_node.next = None

                if(idx == 0):
                    prev_node.next = k_nodes[idx]
                    k_nodes[idx].next = temp_node.next
        
        return result