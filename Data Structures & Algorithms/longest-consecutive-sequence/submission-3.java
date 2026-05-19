class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for(int i: nums){
            set.add(i);
        }
        int mxSize =0;
        int size = 0;
        for(int i: nums){
            size = 0;
            var curr = i;
            while(set.contains(curr)){
                curr++; size++;
            }
            if(size > mxSize)
                mxSize = size;
        }
        return mxSize;
    }
}
