class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> output = new ArrayList<>();
        Set<Integer> set1= new HashSet<>();
        Set<Integer> set2= new HashSet<>();
        List<Integer> diff1= new ArrayList<>();
        List<Integer> diff2= new ArrayList<>();
        for (int num : nums1) {
            set1.add(num);
        }
        
        
        for (int num : nums2) {
            set2.add(num);
        }
       for (int num : set1) {
            if (!set2.contains(num)) {
                diff1.add(num);
            }
        }
        
        for (int num : set2) {
            if (!set1.contains(num)) {
                diff2.add(num);
            }
        }
        
        output.add(diff1);
        output.add(diff2);
        
        return output;
        
    }
}