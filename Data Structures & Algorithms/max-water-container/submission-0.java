class Solution {
    public int maxArea(int[] heights) {
        int l = 0, r =heights.length-1;
        int maxArea = 0;
        while(r > l){
            maxArea = Math.max(maxArea, Math.min(heights[r], heights[l])* (r-l));
            if(heights[l] > heights[r]) r--;
            else l++;
        }

        return maxArea;
    }
}
