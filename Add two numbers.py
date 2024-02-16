class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        buffer = 0

        result = ListNode()

        tail = result

        while l1 or l2:   

            i = l1.val + l2.val + buffer

            tail.next = ListNode(i%10)

            tail = tail.next

            buffer = i//10

            l1 = l1.next

            l2 = l2.next

            if l1 != None and l2 == None:

                l2 = ListNode()

            if l2 != None and l1 == None:

                l1 = ListNode()

        if buffer != 0:

            tail.next = ListNode(buffer)

        return  result.next
