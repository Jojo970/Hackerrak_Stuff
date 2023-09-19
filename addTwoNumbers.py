class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ''
        second = ''
        

        while l1.next:
            first = f"{l1.val}" + first
            l1 = l1.next
        first = int(f"{l1.val}" + first)
        
        while l2.next:
            second = f"{l2.val}" + second
            l2 = l2.next
        second = int(f"{l2.val}" + second)

        sum_num = str((first + second))
        new_lst = [int(x) for x in sum_num]
        

        list_to_return = ListNode(val=new_lst[0])
        count = 1

        while count < len(new_lst):
            temp_node = ListNode(val=new_lst[count], next=list_to_return)
            list_to_return = temp_node
            count+=1

        return list_to_return