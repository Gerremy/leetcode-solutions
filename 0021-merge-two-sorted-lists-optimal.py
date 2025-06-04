# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # So basically you create a list with a faux head so you don't have to worry about how to insert the first node. You're always just attaching. 
        # Then you "line up" both lists and whichever node is smaller gets added to the list first. And keep doing so until one list runs out of nodes. 
        # Then push the last valid list since it's already sorted and belongs at the end. And then you just return the next of the faux head.

        head = ListNode(-1)                     # Step 1: placeholder head node
        current = head                          # Step 2: current points to head

        while list1 and list2:                  # Keep going while both lists have nodes
            if list1.val < list2.val:           # Choose the smaller node
                current.next = list1            # Point current's next to the smaller one
                list1 = list1.next              # Move list1 ahead
            else:
                current.next = list2            # Same logic for list2
                list2 = list2.next
            current = current.next              # Advance current to build the new list
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return head.next
