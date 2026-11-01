class Solution {
  public int minMoves(int[] nums) {
    long sum = 0;
    int minVal = Integer.MAX_VALUE;
    for (int num : nums) {
      sum += num;
      minVal = Math.min(minVal, num);
    }
    return (int) (sum - (long) minVal * nums.length);
  }
}