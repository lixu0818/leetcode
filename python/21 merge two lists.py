    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1==None:
            return l2
        if l2==None:
            return l1
        cap = ListNode(0)
        temp = cap
        
        while True: ######## not while ()
            if l1.val <= l2.val:
                temp.next =l1
                temp =l1
                if l1.next == None:
                    temp.next = l2
                    break
                else:
                    l1= l1.next
            else:
                temp.next =l2
                temp =l2
                if l2.next == None:
                    temp.next = l1
                    break
                else:
                    l2= l2.next
                    
        return cap.next

        