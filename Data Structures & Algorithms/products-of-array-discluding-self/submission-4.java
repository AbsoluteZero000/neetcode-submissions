class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] postfix = nums.clone();
        int[] prefix = nums.clone();
        for(int i = 1; i <nums.length; i++){
            prefix[i] = prefix[i-1] * prefix[i];
            postfix[postfix.length - 1 - i] = postfix[postfix.length - 1 - i] * postfix[postfix.length - i];
        }
        nums[0] = postfix[1];
        nums[nums.length-1] = prefix[prefix.length-2];
        for(int i = 1; i< nums.length-1; i++){
            nums[i] = prefix[i-1] * postfix[i+1];
        }

        return nums;
        
    }
}  
