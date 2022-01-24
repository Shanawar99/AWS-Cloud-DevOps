class Solution:
    def removeNthFromEnd(self, head, n):
        if not head.next :
            return 
        prev = ListNode(None)
        prev.next = head 
        self.removeNthFromEndHelepr(prev,head,n)
        return prev.next
    
        
    def removeNthFromEndHelepr(self,prev,head,n):
        if not head:
            return n-1
            
        idx =  self.removeNthFromEndHelepr(head,head.next,n)
        if idx == 0:
            prev.next = head.next
        idx = idx - 1
        return idx