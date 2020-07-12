# include <tuple>
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

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
private:
    std::tuple<int, int> summarize(int leftValue, int rightValue, int odd) {
        int sum = leftValue + rightValue + odd;
        return std::tuple<int, int>{sum % 10, sum / 10};
    }

    ListNode* allocateNew(ListNode* current) {
        ListNode* newNode = new ListNode();
        current->next = newNode;
        return newNode;
    }
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l1 && !l2) {
            return nullptr;
        }
        int odd = 0;
        ListNode* resultRoot = new ListNode();
        ListNode* current = resultRoot;
        while (l1 && l2) {
            auto summarization = summarize(l1->val, l2->val, odd);
            current->val = std::get<0>(summarization);
            odd = std::get<1>(summarization);
            l1 = l1->next;
            l2 = l2->next;
            if (l1 || l2) {
                current = allocateNew(current);
            }
        }
        ListNode* list = nullptr;
        if (l1) list = l1;
        if (l2) list = l2;
        while (list) {
            auto summarization = summarize(list->val, 0, odd);
            current->val = std::get<0>(summarization);
            odd = std::get<1>(summarization);
            list = list->next;
            if (list) {
                current = allocateNew(current);
            }
        }
        if (odd) {
            current = allocateNew(current);
            current->val = odd;
        }
        return resultRoot;
    }
};

int main(int argc, char** argv) {
}