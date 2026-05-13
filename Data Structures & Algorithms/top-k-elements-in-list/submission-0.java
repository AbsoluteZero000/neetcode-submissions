class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> freq = new HashMap<>();
        
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        ArrayList<Integer>[] buckets = new ArrayList[nums.length + 1];

        for (Integer key : freq.keySet()) {
            int f = freq.get(key);
            if (buckets[f] == null) {
                buckets[f] = new ArrayList<>();
            }
            buckets[f].add(key);
        }

        int[] ans = new int[k];
        int idx = 0;

        for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
            if (buckets[i] != null) {
                for (int num : buckets[i]) {
                    ans[idx++] = num;
                    if (idx == k) {
                        break;
                    }
                }
            }
        }

        return ans;
    }
}