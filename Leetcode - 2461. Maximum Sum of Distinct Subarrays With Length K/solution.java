class Solution {
    
    public long maximumSubarraySum(int[] nums, int k) {
        long max_sum = 0l;
        long cur_sum = 0l;
        HashMap<Integer, Integer> visited = new HashMap();

        for(int end_i = 0, begin_i = 0; end_i < nums.length; end_i++){
            int cur_val = nums[end_i];

            // Add current value to the sum and the map
            cur_sum += cur_val;
            visited.put(cur_val, visited.getOrDefault(cur_val, 0) + 1);

            if(end_i - begin_i + 1 > k){ //sliding window. Need  to remove start value
                int begin_val = nums[begin_i];
                cur_sum -= begin_val;
                //remove from hashmap
                int begin_val_occur = visited.get(begin_val);

                if (begin_val_occur == 1) {
                    visited.remove(begin_val);
                }else{
                    visited.put(begin_val, begin_val_occur - 1);
                }
                begin_i++;
            }

            if(visited.size() == k){ // if SIZE is the same then all values are unique
                max_sum = Math.max(max_sum, cur_sum);
            }
        }

        return max_sum;
    }

    
}
