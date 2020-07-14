package leetcodetask

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	root := ListNode{}
	current := &root
	for (l1 != nil) || (l2 != nil) {
		var val int
		if l1 == nil {
			val = l2.Val
			l2 = l2.Next
		} else if l2 == nil {
			val = l1.Val
			l1 = l1.Next
		} else {
			if l1.Val < l2.Val {
				val = l1.Val
				l1 = l1.Next
			} else {
				val = l2.Val
				l2 = l2.Next
			}
		}
		newNode := ListNode{Val: val, Next: nil}
		current.Next = &newNode
		current = current.Next
	}
	return root.Next
}
