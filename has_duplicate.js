class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let ans = new Set();
        for(let i=0;i<nums.length;i++) {
            if(ans.has(nums[i])) {
                return true
            } else {
                ans.add(nums[i])
            }
        }
        return false
    }
}
