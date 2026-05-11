class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> lst = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(lst.containsKey(target-nums[i])){
                return new int[]{lst.get(target-nums[i]), i};
            }
            lst.put(nums[i], i);
        }
        return new int[]{0, 0};
    }
}
