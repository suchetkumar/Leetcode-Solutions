/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head) return head;
        if (!head->next) return head;
        ListNode* curr = head->next->next;
        ListNode* second = head->next;
        if (curr) {
            curr = swapPairs(curr);
        }
        head->next = curr;
        second->next = head;
        return second;
    }
};