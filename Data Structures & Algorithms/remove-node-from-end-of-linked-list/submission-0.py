class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # Step 1: Find the total length of the linked list
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
            
        # Step 2: Convert "Nth from end" into an exact index from the front
        target_index = length - n
        
        # Edge Case: If we need to remove the very first node (the head)
        if target_index == 0:
            return head.next
            
        # Step 3: Traverse to the node JUST BEFORE the target node
        cur = head
        c_index = 0
        while cur is not None and c_index < target_index - 1:
            cur = cur.next
            c_index += 1
            
        # Step 4: Disconnect the target node safely
        if cur is not None and cur.next is not None:
            cur.next = cur.next.next
            
        return head
