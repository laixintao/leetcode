{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "按2个一组转换链表，简单的画个图就可以。\n",
    "\"\"\"\n",
    "# Definition for singly-linked list.\n",
    "# class ListNode:\n",
    "#     def __init__(self, x):\n",
    "#         self.val = x\n",
    "#         self.next = None\n",
    "\n",
    "class Solution:\n",
    "    def swapPairs(self, head: ListNode) -> ListNode:\n",
    "        head_last = ans = ListNode(0)\n",
    "        head_last.next = head\n",
    "        \n",
    "        while head:\n",
    "            head_next = head.next\n",
    "            \n",
    "            head.next = head_next.next\n",
    "            head_next.next = head\n",
    "            head_last.next = head_next\n",
    "            \n",
    "            head_last = head\n",
    "            head = head.next\n",
    "            \n",
    "        return ans.next"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definition for singly-linked list.\n",
    "class ListNode:\n",
    "    def __init__(self, x):\n",
    "        self.val = x\n",
    "        self.next = None\n",
    "\n",
    "def create(nums):\n",
    "    head = ListNode(nums[0])\n",
    "    tail = head\n",
    "    for num in nums[1:]:\n",
    "        tail.next = ListNode(num)\n",
    "        tail = tail.next\n",
    "    return head\n",
    "\n",
    "def print_list(head):\n",
    "    while head:\n",
    "        print(head.val, \"->\",end=\"\")\n",
    "        head = head.next"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 ->2 ->4 ->3 ->\n",
      "0 ->2 ->1 ->4 ->3 ->\n",
      "0 ->2 ->1 ->3 ->4 ->\n",
      "2 ->1 ->3 ->4 ->"
     ]
    }
   ],
   "source": [
    "a = create([1,2,4,3])\n",
    "print_list(a)\n",
    "r = Solution().swapPairs(a)\n",
    "print()\n",
    "print_list(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
