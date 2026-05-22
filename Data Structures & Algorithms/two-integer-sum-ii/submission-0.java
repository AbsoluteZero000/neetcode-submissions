class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length-1;
        while(j > i){
            System.out.println("i = "+ Integer.toString(i) +  " j = " + Integer.toString(j));
            if(numbers[i] + numbers[j] > target)
                j--;
            else if(numbers[i] + numbers[j] < target)
                i++;
            else return new int[]{i+1,j+1};

        }
        return new int[]{0,0};
        
    }
}
